from cartoframes.auth import set_default_credentials
from cartoframes import read_carto, to_carto
import geopandas as gpd
import pandas as pd
import os
import logging 
from shapely import geometry


# set up logging

# get top-level logger object
logger = logging.getLogger()
for handler in logger.handlers: logger.removeHandler(handler)
# manually set level 
logger.setLevel(logging.INFO)
# print to console
console = logging.StreamHandler()
logger.addHandler(console)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# authenticate carto account 
CARTO_USER = os.getenv('CARTO_WRI_RW_USER')
CARTO_KEY = os.getenv('CARTO_WRI_RW_KEY')
set_default_credentials(username=CARTO_USER, base_url="https://{user}.carto.com/".format(user=CARTO_USER),api_key=CARTO_KEY)

# read in data 
                        
logger.info('Pull ICEP Basins from Carto table')
# read in Aqueduct Index Coastal Eutrophication Potentional Data (ICEP)
gdf_icep= read_carto('wat_059_aqueduct_coastal_eutrophication_potential')
# project to a projected CRS
gdf_icep.to_crs('epsg:3395', inplace=True)

# assign basins to a country

logger.info('Calculate basin centroids')
# calculate the centroids for each basin polygon in the ICEP dataset
gdf_icep['points'] = gdf_icep['the_geom'].centroid
# remname the points column to geometry
gdf_icep.rename(columns = {'points': 'geometry'}, inplace = True)
# drop the polygon geometry
gdf_icep.drop(columns=['the_geom'], inplace= True)
# create a new geodataframe with the centroids as the geometry and set CRS
gdf_icep =gpd.GeoDataFrame(gdf_icep)
gdf_icep.set_crs('epsg:3395', inplace=True)
# reproject CRS to geographic CRS to match gadm polygons
gdf_icep.to_crs('epsg:4326', inplace=True)


logger.info('Pull country boundaries from Carto table')
# read in the GADM country boundaries used in the OW geostore
gdf_gadm = read_carto("gadm36_0")
# rename the_geom column to geometry
gdf_gadm.rename(columns = {'the_geom': 'geometry'}, inplace = True)
logger.info('Join centroids with country boundaries')
# join the centroid and country polygons (intersection)
gdf= gpd.sjoin(gdf_icep,gdf_gadm,how = 'inner')

# calculate total number and proportion of basins at each risk level by country

# group and aggregate the dataframe by the country and risk level, counting the number of centroids at each level    
gdf = gdf.groupby(['gid_0','cep_label']).agg({'name_0': 'first', 'pfaf_id':'nunique'}).reset_index()
# rename count column
gdf.rename(columns = {'pfaf_id': 'count'}, inplace = True)
# subset the dataframe to remove geometry
df = gdf[['gid_0', 'name_0', 'cep_label', 'count']]

# calculate proportions
# group by country and risk level to the number of basins at each level
df_grouped = df.groupby(['gid_0']).agg({'count':'sum'}).reset_index()
# group by country to get the total number of basins
df_grouped.rename(columns = {'count': 'country_total'}, inplace = True)
df = pd.merge(df,df_grouped[['gid_0', 'country_total']], on='gid_0', how='left')
# create a column for the proportion of basins at each risk level
df['proportion'] = df['count']/df['country_total']


# calculate global gtatistics
# group by risk level to get global totals at each level
df_global = df.groupby(['cep_label']).agg({'count':'sum'}).reset_index()
# sum the global totals at each to get a grand total
total_basins = sum(df_global['count'])
# calculate the proportion of basins at each risk level
df_global['proportion'] = df_global['count']/total_basins
# assign the rows the appropriate attributes 
df_global['gid_0'] = 'GLB'
df_global['name_0'] = 'Global'
df_global['country_total'] = total_basins

# merge the country and global calculations
df = pd.concat([df,df_global]).reset_index()
# convert the name column to a string 
df['name'] = df.name_0.astype(str)


# upload data

logger.info('Upload dataframe to Carto')
# upload data frame to Carto
to_carto(df, 'ocn_calcs_014_eutrophication_risk', if_exists='replace')
