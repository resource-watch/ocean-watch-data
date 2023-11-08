import logging
from cartoframes.auth import set_default_credentials
from cartoframes import read_carto, to_carto
import pandas as pd
import geopandas as gpd
from datetime import date
from datetime import datetime
from pprint import pprint
import json
import time
import requests
from requests.exceptions import HTTPError
from pathlib import Path
import os
import contextlib


# set up logging

# get top-level logger object
logger = logging.getLogger()
for handler in logger.handlers: logger.removeHandler(handler)
# manually set level 
logger.setLevel(logging.DEBUG)
# print to console
console = logging.StreamHandler()
logger.addHandler(console)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# name of table on Carto where you want to upload data
# this should be a table name that is not currently in use
dataset_name = 'com_030d_fishing_effort_by_zone'

logger.debug('Authenticate Carto credentials')
CARTO_USER = os.getenv('CARTO_WRI_RW_USER')
CARTO_KEY = os.getenv('CARTO_WRI_RW_KEY')
set_default_credentials(username=CARTO_USER,
                        base_url="https://{user}.carto.com/".format(user=CARTO_USER),
                        api_key=CARTO_KEY)

# fixed items defined by gfw
INITIATE_REPORT_ENDPOINT = 'https://gateway.api.globalfishingwatch.org/v2/4wings/report?spatialResolution=low&temporalResolution=yearly&groupBy=flag&datasets[0]=public-global-fishing-effort:latest&date-range={year}-01-01,{year}-12-31&format=json'

# related objects
INITIATE_REPORT_HEADERS = {
    'Content-Type':'application/json',
    'Authorization':os.getenv('GFW_API_KEY')
}

# set working directory
WORKING_DIR = os.path.join(os.getenv('DOWNLOAD_DIR'), 'gfw-api-data')
Path(WORKING_DIR).mkdir(parents=True, exist_ok=True)

# generate a list of missing entries 
logger.debug('Generate list of missing entries (zone-year pairs)')
entries_table = dataset_name
query_missing = (
    "SELECT zone.mrgid, zone.geoname, zone.pol_type, zone.year, zone.iso_ter1, zone.iso_sov1, zone.iso_ter2, zone.iso_sov2, zone.iso_ter3, zone.iso_sov3, effort.value " 
    "    FROM ("
    "       SELECT zone.mrgid, zone.geoname, zone.pol_type, zone.iso_ter1, zone.iso_sov1, zone.iso_ter2, zone.iso_sov2, zone.iso_ter3, zone.iso_sov3, "
    "       UNNEST(ARRAY[2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]) AS year "
    "       FROM com_011_rw1_maritime_boundaries_edit zone "
    "       WHERE zone.pol_type IN ('200NM','Overlapping claim','Joint regime')"
    "           ) AS zone "
    "LEFT OUTER JOIN com_030d_fishing_effort_by_zone effort ON (zone.mrgid = effort.mrgid AND zone.year = effort.year) "
    "WHERE effort.value IS NULL "
    "ORDER BY geoname ASC, year ASC "
)
gdf_missing = read_carto(query_missing)
print(len(gdf_missing))

gdf_missing=gdf_missing.astype({'mrgid':'int'})

# create object to track api activity & results
# mrgid, geoname, year, id, url, zip, csv, value
# needed from original table: geoname, pol_type, iso_ter1, iso_sov1, iso_ter2, iso_sov2, iso_ter3, iso_sov3
col_type_dict = {
    'mrgid':'int',
    'geoname':'str',
    'pol_type':'str',
    'iso_ter1':'str',
    'iso_sov1':'str',
    'iso_ter2':'str',
    'iso_sov2':'str',
    'iso_ter3':'str',
    'iso_sov3':'str',
    'year':'int',
    'id':'str',
    'value':'float',
}
df_attempts = pd.DataFrame({c: pd.Series(dtype=t) for c, t in col_type_dict.items()})

logger.info('Initiate report generation for missing entries (zone-year pairs)')
report_name_template = 'Total Observed Fishing Effort in {}, {}'

# iterate through list of missing entries, request, process, and store data
for index, row in gdf_missing.iterrows():
    # get unique id for missing EEZ
    id = gdf_missing.at[index,'mrgid']
    # get missing year
    year = gdf_missing.at[index,'year']
    # use id and year to build request
    body = { "region": {"dataset": "public-eez-areas", "id":int(id)}}
    r = requests.post(INITIATE_REPORT_ENDPOINT.format(year= year), headers=INITIATE_REPORT_HEADERS, data= json.dumps(body))
    report_name = report_name_template.format(row.geoname, year)
    try: 
        r.raise_for_status()
    except HTTPError as e:
        logger.error('Failed report generation request for: ' + report_name)
        logger.error(e.response.text)
        hours = None
    else: #if request is successful, sum the number of fishing hours in the EEZ
        resp_body = r.json()
        resp_data = resp_body[0]['public-global-fishing-effort:v20201001']
        df = pd.DataFrame (resp_data, columns = ['date','flag','hours','lat','lon'])
        hours= df['hours'].sum()
    finally: #store processed data
        df_attempts.loc[len(df_attempts.index)] = [
            row.mrgid, row.geoname, row.pol_type,
            row.iso_ter1, row.iso_sov1, row.iso_ter2, row.iso_sov2, row.iso_ter3, row.iso_sov3, 
            year, None, hours,
        ]
        time.sleep(5)

# record reports that failed, whose reports are thus missing
record_index = pd.notnull(df_attempts['value'])
df_failures = df_attempts[~record_index]
if len(df_failures) > 0:
    failures_csv = os.path.join(WORKING_DIR, 'gfw-api_fishing-effort_retry-failures.csv')
    with contextlib.suppress(FileNotFoundError):
        os.remove(failures_csv)
    df_failures.to_csv(failures_csv, header=True, index=False, )

record_index = pd.notnull(df_attempts['value'])
# append data to table on Carto
if len(df_attempts[record_index]) > 0:
    to_carto(df_attempts[record_index], dataset_name, if_exists='append')
