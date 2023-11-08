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

# fixed items defined by gfw
INITIATE_REPORT_ENDPOINT = 'https://gateway.api.globalfishingwatch.org/v2/4wings/report?spatialResolution=low&temporalResolution=yearly&groupBy=flag&datasets[0]=public-global-fishing-effort:latest&date-range={year}-01-01,{year}-12-31&format=json'

# related objects
INITIATE_REPORT_HEADERS = {
    'Content-Type':'application/json',
    'Authorization':os.getenv('GFW_API_KEY')
}

year= 2021

body = {
  "geojson": {
    "type": "Polygon",
    "coordinates": [
      [
        [
          -180,
          -85.051128
        ],
        [
          180,
          -85.051128
        ],
        [
          180,
          85.051128
        ],
        [
          -180,
          85.051128
        ],
        [
          -180,
          -85.051128
        ]
      ]
    ]
  }
}

r = requests.post(INITIATE_REPORT_ENDPOINT.format(year= year), headers=INITIATE_REPORT_HEADERS, data= json.dumps(body))

try: 
    r.raise_for_status()
except HTTPError as e:
    logger.error('Failed report generation request')
    logger.error(e.response.text)
    hours = None
else: #if request is successful, sum the number of fishing hours in the EEZ
    resp_body = r.json()
    resp_data = resp_body[0]['public-global-fishing-effort:v20201001']
    df = pd.DataFrame (resp_data, columns = ['date','flag','hours','lat','lon'])
    hours= df['hours'].sum()