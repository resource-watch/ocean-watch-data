import os
from random import paretovariate
from typing import OrderedDict
from unittest import TestCase
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
id_pattern = re.compile('[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}')

# find all matches in the OW json
ids = id_pattern.findall(json_string)

# create empty dataframes to store information about each asset
widgets = pd.DataFrame()
layer_datasets = []

# fuction to get dataset information from an id
def get_dataset_info(id):
    object = lmi.Dataset(id)
    wri_id = object.attributes['name'].split(' ')[0]
    name = object.attributes['name'].replace(wri_id,"").lstrip(" ")
    if object.attributes['published'] == True:
        status = "Published"
    else: 
        status = "Unpublished"
    return wri_id, name 

# fuction to get widget information from an id
def get_widget_info(id):
    object = lmi.Widget(id)
    name = object.attributes['name']
    parent_dataset_id= object.attributes['dataset']
    parent_wri_id, parent_dataset_name = get_dataset_info(parent_dataset_id)
    try:
        type = object.attributes['widgetConfig']['paramsConfig']['visualizationType']
    except: 
        type = 'chart'
    return id, name, parent_dataset_id, parent_dataset_name, parent_wri_id, type

# function to get layers from a widget
def get_datasets_from_widget(id):
    dataset_list = []
    object = lmi.Widget(id)
    if 'paramsConfig' in object.attributes['widgetConfig']:
        layers = id_pattern.findall(json.dumps(object.attributes['widgetConfig']['paramsConfig']))
        for layer in layers:
            layer_object = lmi.Layer(layer)
            parent_dataset_id= layer_object.attributes['dataset']
            parent_wri_id, parent_dataset_name = get_dataset_info(parent_dataset_id)
            dataset_list.append(parent_wri_id)
    dictionary = dict.fromkeys(dataset_list)
    datasets = list(dictionary)
    return datasets

# funtion to get the Carto table name from a widget
def get_table_from_widget(id):
    table_pattern= re.compile('[a-zA-Z]{3}_[a-z0-9]{3,}[a-z]*_[\w,_]{4,}')
    table_list = []
    object = lmi.Widget(id)
    if 'data' in object.attributes['widgetConfig']:
        for data in object.attributes['widgetConfig']['data']:
            if 'url' in data:
                table_names = table_pattern.findall(data['url']) 
                table_list.extend([name for name in table_names if name not in table_list])
    dictionary = dict.fromkeys(table_list)
    tables = list(dictionary)
    return tables

# iterate through the ids in the json
for id in ids:
    # try to get widget information
    try:
        id, name, parent_dataset_id, parent_dataset_name, parent_wri_id, type = get_widget_info(id)
        # if the widget is not a chart, try to get dataset information from the layers in the widget
        if type != 'chart':
            tables = ""
            try: 
                datasets = get_datasets_from_widget(id)
            except:
                datasets = ""
        # otherwise get the catro table information from the widgetConfig
        else: 
            datasets = ""
            tables = get_table_from_widget(id)
        # add the widget and its information to the dataframe
        widgets = widgets.append({'name': name, 'id': id,  'type': type, 'parent_wri_id':parent_wri_id, 'parent_dataset_id': parent_dataset_id,  'datasets': datasets, 'tables': tables}, ignore_index=True)
    # if cant get widget information from API, pass, as it is a layer or dataset id
    except:
        pass

# list of old widgets that have been changed in staging but have not been pushed to production (as of 3/4/22)
old_widgets= [
        'bd2e07f0-f62a-42df-83e6-65a3ebcdbc29',
        '15b5ec89-0ea6-4cd4-beac-7caceb80e42c',
        'b8e454be-9a0f-4a8f-8e92-3d7b0fd6423f', 
        "3f531725-9d1f-436f-85f8-b1494b0262c1", 
        "80b7addc-f6ea-4d38-808c-359e49a8b84e",
        "d0b57543-e771-41e1-a9b6-a9487d5c3d5b"
        ]

# remove duplicate widgt ids
widgets = widgets.drop_duplicates(subset=['id'])

# remove old widgets
widgets = widgets[~widgets['id'].isin(old_widgets)]

# join the dataset information with information from the Resource Watch Data Tracking Sheet
METADATA_SHEET = "https://docs.google.com/spreadsheets/d/1A3RbymgsB5bwljFsL20Brj-M29as0m2yPCAoAK25N6k/export?format=csv&gid=0" 

# Read in RW metadata tracking sheet
mdata = pd.read_csv(METADATA_SHEET, header=0)
mdata.rename(columns = {'API_ID':'parent_dataset_id'}, inplace = True)

# Merge df with columns from RW metadata sheet
df = pd.merge(widgets,mdata[['parent_dataset_id','New WRI_ID']], on='parent_dataset_id', how='left')

# reorder columns
df = df[['name', 'id', 'type', 'parent_wri_id', 'parent_dataset_id',  'datasets', 'tables']]

# path to processed table
processed_table = os.path.join(os.getenv('OCEANWATCH_DATA_DIR'), 'generated_tracking_sheets/ow_widget_tracking_sheet.xlsx')

# save processed table to the Ocean Watch Data Directory
df.to_excel(processed_table, index= False)
