import os
from random import paretovariate
from typing import OrderedDict
import pandas as pd
import LMIPy as lmi
import json
import requests
import re

# The content on the OceanWatch pages are configured using a json file managed by Vizzuality
ow_json_url = "https://raw.githubusercontent.com/resource-watch/resource-watch/develop/public/static/data/ocean-watch.json"

# read the content as a string, so we can search for assets ids (dataset, widget, and layer) ids
res = requests.get(ow_json_url).text

#ow_json = json.loads(res.text)
json_string = json.dumps(res)

# create a regex pattern that matches RW dataset, widget, and layer ids
pattern = re.compile('[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}')

# find all matches in the OW json
ids = pattern.findall(json_string)

# create empty dataframes to store information about each asset
widgets = pd.DataFrame()
layers = pd.DataFrame()
datasets = pd.DataFrame()

# fuction to get dataset information from an id
def get_dataset_info(id):
    object = lmi.Dataset(id)
    wri_id = object.attributes['name'].split(' ')[0]
    name = object.attributes['name'].replace(wri_id,"").lstrip(" ")
    if object.attributes['published'] == True:
        status = "Published"
    else: 
        status = "Unpublished"
    return id, wri_id, name, status

# fuction to get widget information from an id
def get_widget_info(id):
    object = lmi.Widget(id)
    name = object.attributes['name']
    parent_dataset_id= object.attributes['dataset']
    return id, name, parent_dataset_id

# fuction to get layer information from an id
def get_layer_info(id):
    object = lmi.Layer(id)
    name = object.attributes['name']
    parent_dataset_id= object.attributes['dataset']
    return id, name, parent_dataset_id

# function to get layers from a widget
def get_layers_from_widget(id):
    layer_df = pd.DataFrame()
    object = lmi.Widget(id)
    if 'paramsConfig' in object.attributes['widgetConfig']:
        layers = pattern.findall(json.dumps(object.attributes['widgetConfig']['paramsConfig']))
        for layer in layers:
            layer_object = lmi.Layer(layer)
            parent_dataset_id= layer_object.attributes['dataset']
            layer_df= layer_df.append({'layer_id': layer, 'widget_id': id, 'parent_dataset_id': parent_dataset_id}, ignore_index=True)
    return layer_df

# iterate through the ids in the json
for id in ids:
    # try to get dataset information
    try:
        id, wri_id, name, status = get_dataset_info(id)
        datasets = datasets.append({'API_ID': id, 'wri_id': wri_id, 'name': name, "status": status}, ignore_index=True)
    # if unsucesful, try to get widget information
    except: 
        try: 
            id, name, parent_dataset_id = get_widget_info(id)
            widgets = widgets.append({'id': id, 'name': name, 'parent_dataset_id': parent_dataset_id}, ignore_index=True)
            # try to get layer information from widget
            try: 
                layer_df= get_layers_from_widget(id)
                layers = layers.append(layer_df, ignore_index=True)
            except:
                pass
        # if the id is not a widget or a dataset, then it is a layer in the mini-explore. Get layer information. 
        except:
            try:
                id, name, parent_dataset_id = get_layer_info(id)
                layers = layers.append({'layer_id': id, 'widget_id': 'mini-explore', 'parent_dataset_id': parent_dataset_id}, ignore_index=True)
            except: 
                pass

# drop any duplicates
widgets = widgets.drop_duplicates(subset=['id'])
layers = layers.drop_duplicates(subset=['layer_id','widget_id'])


# Add datasets from any layers that are not in the dataset list
for id in layers['parent_dataset_id']:
    if id not in datasets['API_ID']:
        id, wri_id, name, status = get_dataset_info(id)
        datasets = datasets.append({'API_ID': id, 'wri_id': wri_id, 'name': name, "status": status}, ignore_index=True)

# Add any datasets from the widgets that are not in the dataset list
for id in widgets['parent_dataset_id']:
    if id not in datasets['API_ID']:
        id, wri_id, name, status = get_dataset_info(id)
        datasets = datasets.append({'API_ID': id, 'wri_id': wri_id, 'name': name, "status": status}, ignore_index=True)

# drop any duplicates
datasets = datasets.drop_duplicates(subset=['API_ID'])

# join the dataset information with information from the Resource Watch Data Tracking Sheet
METADATA_SHEET = "https://docs.google.com/spreadsheets/d/1A3RbymgsB5bwljFsL20Brj-M29as0m2yPCAoAK25N6k/export?format=csv&gid=0" 

# Read in RW metadata tracking sheet
mdata = pd.read_csv(METADATA_SHEET, header=0)

# Merge df with columns from RW metadata sheet
df = pd.merge(datasets,mdata[['API_ID','Github Link', 'table/asset_name on server', 'Server Location', 'Expected Date of Update', 'Last Update', 'Latest Check', 'Required Action']], on='API_ID', how='left')

# sort by the WRI id
df= df.sort_values(by=['wri_id'])

# reorder columns
df = df[['wri_id', 'name', 'status','API_ID', 'table/asset_name on server', 'Server Location',  'Github Link', 'Expected Date of Update', 'Last Update', 'Latest Check', 'Required Action']]

# path to processed table
processed_table = os.path.join(os.getenv('OCEANWATCH_DATA_DIR'), 'generated_tracking_sheets/ow_dataset_tracking_sheet.xlsx')

# save processed table to the Ocean Watch Data Directory
df.to_excel(processed_table, index= False)

    