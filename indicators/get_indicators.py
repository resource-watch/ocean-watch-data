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

# read the content as a string, so we can search for assets (dataset, widget, and layer) ids
res = requests.get(ow_json_url)
ow_json = json.loads(res.text)

# empty data frame to store information about each indicator
indicator_df = pd.DataFrame(columns=['indicator', 'query', 'description'])

'''
FUNCTIONS
'''

def getQueryInfo(content):

    '''
    Get information about an indicator, if it exists, from a piece of indicator content from the OW json.
    INPUT   content: part of the OW json
    RETURN  description: (string) text description of indicator value
            query: (string) parameterized carto url for an SQL query coresponding to the indicator value
    '''

    # the indicator information is nested in an element under the the 'widget' or 'widgets' key (not consistently named in the json)
    # get a list of the values in the widget/widgets key
    if 'widget' in content: 
        widget_list = content['widget']
    elif 'widgets' in content:
        widget_list = content['widgets']
    else:
        return None, None
    # iterate through the list of values to find the appropriate entry (should contain either a 'query' key, a 'description' key or both)
    for item in widget_list: 
        if 'query' in item:
            query = item['query']
            if 'description' in item:
                description = item['description']
            elif 'text' in item:
                description = item['text']
            else:
                description = None
            break     
        else: 
            query = None
            if 'description' in item:
                description = item['description']
                break
            # note Viz has renamied 'description' to 'instructions' for the oceans-climate indicator
            elif 'instructions' in item:
                description = item['instructions']
                break
            else:
                description = None
    return query, description

# function to iterate through each section of the json
def iterateStep(indicator_name, content): 
    '''
    Given a piece of indicator content from the OW json, give the content a more appropriate name and retrieve indicator information if it exists.
    INPUT   indicator_name: (string) name given in the section of content one level higher
            content: (json object) indicator content from the the OW json
    RETURN  description: (string) text description of indicator value
            query: (string) parameterized carto url for an SQL query coresponding to the indicator value
    '''

    if 'title' in content:
        indicator_name = content['title']
    elif 'id' in content: 
        indicator_name = content['id']
    query, description = getQueryInfo(content)
    return indicator_name, query, description


'''
There are two main sections in the json where indicator information can be found: 
(1) high level indicators on the intro page and country profiles 
(2) values of goods and services indicators and ranks on the country profiles
'''

'''
HIGH LEVEL INDICATORS
'''

# list of elements of the json with high level indicators
high_level_indicators = [ow_json['production']['intro']['steps'], ow_json['production']['country-profile'][0][0]['content'][0][0]['config']['indicators']]

# iterate through the list
for page in high_level_indicators:
    # for each element iterate through the list and define the "step" which is the key whose values we will iterate though
    for list in page:
        # if the list has a 'content' key, grab the name of this content. We define it as the step. 
        if 'content' in list:
            indicator_name= list['indicator']
            step = list['content']
        # if the list does not have a 'content' key, it already represents the list of values we will iterate through. We will give it a more specific name later
        else: 
            step = list
            indicator_name = None
        
        # if the redefined step contains a 'sections' key, we will redefine the step again
        if 'sections' in step:
            step = step['sections']

        # iterate through the steps to get information about each indicator         
        indicator_name, query, description = iterateStep(indicator_name,step)
        
        # append the information to the working dataframe
        indicator_df = indicator_df.append({'indicator': indicator_name, 'query': query, 'description': description}, ignore_index=True)

'''
VALUE OF GOODS AND SERVICES 
'''


# list of indicators in the json
value_section = ow_json['production']['country-profile'][4][0]['content'][1][0]['config']['indicators']
# for each element in the list iterate through the sub-list and grab the rank and the indicator information
for indicator in value_section:
    # in the higher level list, grab information about the rank
    indicator_name = indicator['id']
    description = indicator['title']
    query = indicator['query']
    # append the information to the working dataframe
    indicator_df= indicator_df.append({'indicator': indicator_name, 'query': query, 'description': description}, ignore_index=True)
    # if the indicator has an indicator value, it will be in the 'widgets' key
    if 'widgets' in indicator:
        # iterate through the indicator elements to grab the indicator information
        query, description = getQueryInfo(indicator)
        # append the information to the working dataframe
        indicator_df= indicator_df.append({'indicator': indicator_name, 'query': query, 'description': description}, ignore_index=True)

# subset of indicators that have either a query or a description
indicator_df_sub = indicator_df.loc[~(indicator_df['query'].isnull() & indicator_df['description'].isnull())]

# path to processed table
processed_table = os.path.join(os.getenv('OCEANWATCH_DATA_DIR'), 'generated_tracking_sheets/ow_indicator_tracking_sheet.xlsx')

# save processed table to the Ocean Watch Data Directory
indicator_df.to_excel(processed_table, index= False)