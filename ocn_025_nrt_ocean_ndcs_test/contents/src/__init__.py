from cartoframes.auth import set_default_credentials
from cartoframes import read_carto, to_carto
import pandas as pd
import os
import logging 
import requests
import json

# get top-level logger object
logger = logging.getLogger()
for handler in logger.handlers: logger.removeHandler(handler)
# manually set level 
logger.setLevel(logging.INFO)
# print to console
console = logging.StreamHandler()
logger.addHandler(console)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')



# set credientials for carto frames
CARTO_USER = os.getenv('CARTO_WRI_RW_USER')
CARTO_KEY = os.getenv('CARTO_WRI_RW_KEY')
set_default_credentials(username=CARTO_USER, base_url="https://{user}.carto.com/".format(user=CARTO_USER),api_key=CARTO_KEY)


# Get a list of ocean subsector indicator ids from Climate Watch. The ids are not fixed, and change each time the data is uploaded.

# define the list of "slugs" that point to the ocean related subsectors on Climate Watch - these are fixed 
slugs = ["a_coastal_zone_general_auto","a_coastal_fisheries_auto","a_coastal_management_auto","a_mangroves_auto","a_sea_level_rise_protection_auto","a_fisheries_and_aquaculture_auto","m_fisheries_and_aquaculture_auto","m_renewable_energy_ocean_auto","m_maritime_auto"]

# the url for the match table between slugs and ids
indicator_url = 'https://www.climatewatchdata.org/api/v1/data/ndc_content/indicators'
def main():
    # get the table from a json
    req = requests.get(indicator_url)
    json_dict= json.loads(req.text)
    # convert to a pandas datafrome
    df = pd.DataFrame.from_dict(json_dict['data'])
    # subset the table to the list of ocean related subsectors
    df = df = df.loc[df['slug'].isin(slugs)]
    # create a list of ids
    ids =[id for id in df['id']]

    # define a template for the API request
    url_shell= 'https://www.climatewatchdata.org/api/v1/data/ndc_content?indicator_ids[]={}&indicator_ids[]={}&indicator_ids[]={}&indicator_ids[]={}&indicator_ids[]={}&indicator_ids[]={}&indicator_ids[]={}&indicator_ids[]={}&indicator_ids[]={}&per_page=1000'
    # format the template with the list of ids
    url_template = url_shell.format(*tuple(ids)) + '&page={}'

    # empty list to store the API request returns
    paginated_dfs = []

    # request the data from the Climate Watch API
    # data is paginated - loop through the pages and store the dataframes in a list
    for i in range(1,20):
        # format url with page number
        url = url_template.format(i)
        # request the data
        req = requests.get(url)
        text_data= req.text
        # load as a json
        json_dict= json.loads(text_data)
        # convert to a pandas dataframe
        df = pd.DataFrame.from_dict(json_dict['data'])
        # append to the list of dataframes
        paginated_dfs.append(df)

    # combine all pages of the data in to one dataframe
    df = pd.concat(paginated_dfs).reset_index()

    # remove duplicate ids from looping through the pagination more than once
    df=df.drop_duplicates(['id'])

    # create a row 'count' to store a boolean Y/N (Y - 'Sectoral Measure Specificed; 'N'- 'No Sectoral Measure Specified')
    df['count'] =''
    for index, row in df.iterrows():
        if 'No' in row['value']:
            df.loc[index, 'count'] = 0
        else: 
            df.loc[index, 'count'] = 1

    # Group the data by indicator and sum the count column to get global totals for each indicator
    df_world = df.groupby(['indicator_id']).agg({'indicator_name':'first', 'sector':'first', 'subsector':'first','count':'sum'}).reset_index()

    # Add the necessary attribute columns
    df_world['iso_code3'] = 'GLB'
    df_world['country'] = 'Global'

    # Combine the global and country level dataframs
    df = pd.concat([df, df_world]).reset_index()

    # drop unnecessary and blank columns 
    df=df.drop(['index','id','country','source', 'global_category', 'overview_category'], axis = 1)

    logger.info('Upload dataframe to Carto')
    # upload data frame to Carto
    to_carto(df, 'ocn_025_rw0_ocean_ndc_measures_nrt_TEST', if_exists='replace')