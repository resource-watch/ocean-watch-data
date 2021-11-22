import logging
import pandas as pd
import numpy as np
import os
import sys
import requests
from zipfile import ZipFile
from cartoframes.auth import set_default_credentials
from cartoframes import read_carto, to_carto
import shutil

# Set up logging
# Get the top-level logger object
logger = logging.getLogger()
for handler in logger.handlers: logger.removeHandler(handler)
logger.setLevel(logging.INFO)
# make it print to the console.
console = logging.StreamHandler()
logger.addHandler(console)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# name of table on Carto where you want to upload data
# using preexisting table for this dataset
dataset_name = 'ocn_calcs_015_blue_food_protein_supply' #check

data_dir = os.getenv('OCEANWATCH_PROCESSING_DIR')+'/widgets/' + dataset_name + '/data'

logger.info('Executing script for dataset: ' + dataset_name)

'''
Download data and save to your data directory
'''
# The data is provided as two data sets ('New' and 'Historic')
# Create a data dictionary to store the relevant information about each file 
    # version: version of data (string)
    # url: url to retrieve data (string)
    # raw_data_file: empty list for raw data files (list)
    # processed_dfs: empty list for processed dataframes (list)

data_dict= {
    'version' : [' new', 'historic'],
    'urls': ['http://fenixservices.fao.org/faostat/static/bulkdownloads/FoodBalanceSheets_E_All_Data_(Normalized).zip','http://fenixservices.fao.org/faostat/static/bulkdownloads/FoodBalanceSheetsHistoric_E_All_Data_(Normalized).zip'],
    'raw_data_file': [],
    'processed_dfs': []
  } 

for url in data_dict['urls']:
    # download the data from the source
    raw_data_file = os.path.join(data_dir, os.path.basename(url))
    r = requests.get(url)  
    with open(raw_data_file, 'wb') as f:
        f.write(r.content)

    # unzip source data
    raw_data_file_unzipped = raw_data_file.split('.')[0]
    zip_ref = ZipFile(raw_data_file, 'r')
    zip_ref.extractall(raw_data_file_unzipped)
    data_dict['raw_data_file'].append(raw_data_file_unzipped)
    zip_ref.close()

# Copy item aliasing sheet into the data directory
source = os.path.join(os.getenv("OCEANWATCH_DATA_DIR"),'FBS_item_category_analysis.xlsx')
dest_dir = os.path.abspath(data_dir)
shutil.copy(source, dest_dir)

'''
Process the data 
'''
'''
Process the data 
'''
# list of areas we want to exclude from our dataframe
# so that we only have countries and not aggregated regions
areas_list = ['Africa', 'Eastern Africa',
    'Middle Africa', 'Northern Africa', 'Southern Africa',
    'Western Africa', 'Americas', 'Northern America',
    'Central America', 'Caribbean', 'South America', 'Asia',
    'Central Asia', 'Eastern Asia', 'Southern Asia',
    'South-eastern Asia', 'Western Asia', 'Europe', 'Eastern Europe',
    'Northern Europe', 'Southern Europe', 'Western Europe', 'Oceania',
    'Australia and New Zealand', 'Melanesia', 'Micronesia',
    'Polynesia', 'European Union (28)', 'European Union (27)',
    'Least Developed Countries', 'Land Locked Developing Countries',
    'Small Island Developing States',
    'Low Income Food Deficit Countries',
    'Net Food Importing Developing Countries','Australia & New Zealand', 
    'Belgium-Luxembourg', 'China', 'Czechoslovakia','Ethiopia PDR', 
    'European Union', 'Netherlands Antilles (former)', 'Serbia and Montenegro', 
    'South-Eastern Asia', 'Sudan (former)', 'USSR', 'Yugoslav SFR']

for file in data_dict['raw_data_file']:
    # read in the data as a pandas dataframe 
    df = pd.read_csv(os.path.join(file, file.split('/')[-1] + '.csv'),encoding='latin-1')
    # read in the category alias sheet as a dataframe
    alias = pd.read_excel(os.path.join(data_dir, 'FBS_item_category_analysis.xlsx'))
    # match the items in the food balance sheet with their assigned category in the category alias sheet
    df = pd.merge(df, alias[['Item Code','Analysis Category','Product', 'Parent']], on='Item Code', how='left')
    
    # filter out items that were not matched to a category alias
    df= df[df['Analysis Category'].notnull()]

    # filter data to the element "Protein supply quantity (g/capita/day)"
    elements = [674]
    df= df[df['Element Code'].isin(elements)]

    # filter out excluded areas 
    df = df[~df['Area'].isin(areas_list)]

    # create a data frame for the 4th level (items)
    df_item = df[df['Item'] != 'Grand Total']
    df_item['Size'] = df_item['Value']

    # create a data fram for the 3rd level (groups)
    df_group = df_item.groupby(['Area','Year Code', 'Parent']).agg({'Area Code':'first', 'Analysis Category':'first', 'Element': 'first', 'Value':'sum', 'Unit': 'first'}).reset_index()
    df_group.rename(columns={'Parent':'Item'}, inplace=True)
    df_group['Parent'] = df_group['Analysis Category']

    # create a data frame for the 2nd level (categories) 
    df_category = df_item.groupby(['Area','Year Code', 'Analysis Category']).agg({'Area Code':'first', 'Element': 'first', 'Value':'sum', 'Unit': 'first'}).reset_index()
    df_category['Parent'] = 'Grand Total'
    df_category['Item']=df_category['Analysis Category']
    
    #create a data frame for the 1st level (total)
    df_total = df[df['Item'] == 'Grand Total']
    df_total['Parent'] = None
    df_total['Size'] = None

    # combine dfs
    df= pd.concat([df_total, df_category, df_group, df_item])

    # store the processed df
    data_dict['processed_dfs'].append(df)

# join the new and historic datasets
df= pd.concat(data_dict['processed_dfs'])

# rename the value and year columns
df.rename(columns={'Year Code':'year'}, inplace=True)

# replace whitespaces with underscores in column headers
df.columns = df.columns.str.replace(' ', '_')

# turn all column names to lowercase 
df.columns = [x.lower() for x in df.columns]

# remove duplicate columns
df = df.loc[:,~df.columns.duplicated()]

# convert Year column to date time object
df['datetime'] = pd.to_datetime(df.year, format='%Y')

# convert value column to a float
df['value'] = df['value'].astype('float64')

# sort the new data frame by country and year
df= df.sort_values(by=['area','year','analysis_category', 'product', 'item'])


'''
Upload processed data to Carto
'''

# save processed dataset to csv
processed_data_file = os.path.join(data_dir, dataset_name+'.csv')
df.to_csv(processed_data_file, index=False)

logger.info('Uploading processed data to Carto.')
# authenticate carto account 
CARTO_USER = os.getenv('CARTO_WRI_RW_USER')
CARTO_KEY = os.getenv('CARTO_WRI_RW_KEY')
set_default_credentials(username=CARTO_USER, base_url="https://{user}.carto.com/".format(user=CARTO_USER),api_key=CARTO_KEY)

# upload data frame to Carto
to_carto(df, 'ocn_calcs_015_blue_food_protein_supply', if_exists='replace')