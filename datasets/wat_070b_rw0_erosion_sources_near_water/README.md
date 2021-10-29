## Sources of Erosion near Water Bodies Dataset
This file describes the Sources of erosion near water bodies dataset on [Ocean Watch](https://www.oceanwatchdata.org)

### Function
Highlights areas of high soil erosion potential (>50%) within 7 meters of river banks.

### Source
World Agroforestry Centre (ICRAF), Global River Width from Landsat (GRWL), Hydrobasins (produced by the World Wildlife Fund)

### About the data
- **Geographic coverage:** Global
- **Date of content:** 2020
- **Data type:** Raster
- **Spatial resolution:** 20m
- **Frequency of updates:** Dependent on availabilty of soil erosion prevalence data

<br/>*Learn more about the underlying data: [Soil Erosion]({https://resourcewatch.org/data/explore/wat070rw0-Soil-Erosion), [River Widths](https://www.science.org/doi/10.1126/science.aat0636), [River Network](https://www.hydrosheds.org/page/hydrorivers)*

### Download the underlying data
[Soil erosion in the global tropics (2002, 2007, 2012, 2017)](http://landscapeportal.org/maps/3037) <br/>
[Simplified GRWL Vector Product](https://samapriya.github.io/awesome-gee-community-datasets/projects/grwl/) <br/>
[HydroRIVERS v1.0](https://www.hydrosheds.org/page/hydrorivers) 

### Pre-processing
The Ocean Watch data team used ArcMap model builder to create two python scripts (found [here]({link-to-script}) and [here]()) to assign widths to rivers (where data was available) and create a mask of areas in close proximity to river banks. The following steps were taken: 
1. Project the Hydrorivers and GRWL data into a Mollewide Equal Area Projection.
2. Subset the Hydrorivers data to first order, exhoreic rivers.
3. Subset the GRWL rivers to those that intersect with an area 5km from the coastline (source: [Natural Earth 10m coastline](https://www.naturalearthdata.com/downloads/10m-physical-vectors/) and 5km from the first order, exhoreic Hydrorivers network.
4. Create a GRWL mask by buffering the GRWL rivers to a distance of their width plus 7m on either side.
5. Subset the first Hydroivers subset to rivers where the center point does not fall within the GRWL mask. This isolates rivers where no width data is available.
6. The remaining Hydrorivers rivers were conservatively assumed to have a width of 10m and were buffered to 10m plus 7m on either side to create a Hydrivers mask.
7. The two masks were combined and uploaded as a single shapefile asset on [Google Earth Engine](https://code.earthengine.google.com/?asset=projects/resource-watch-gee/ocean-watch/merged-river-buffer)

The Ocean Watch data team then used a [javaScript script](https://code.earthengine.google.com/698444daba81ff9ee35c6f2fca30cb70?accept_repo=users%2Fresourcewatch%2Fdefault) to: 
1. Convert the shapefile asset to a raster image.
2. Extract a mask from the raster asset.
3. Subset the ICRAF soil eosion raster image to pixels where erosion is predcited to be greater than 50%.
4. Apply the river image mask to the soil erosion image
5. Save the resulting image to a [Google Earth Engine Asset](https://code.earthengine.google.com/?asset=projects/resource-watch-gee/wat_070b_erosion_sources_near_water_bodies)

### Citations
Vågen, T.-G., & Winowiecki, L. A. (2019). Predicting the Spatial Distribution and Severity of Soil Erosion in the Global Tropics using Satellite Remote Sensing. Remote Sensing, 11(15), 1800. https://doi.org/10.3390/rs11151800 <br/>

Allen, George H., & Pavelsky, Tamlin M. (2018). Global River Widths from Landsat (GRWL) Database (V01.01) [Data set]. Zenodo. https://doi.org/10.5281/zenodo.1297434 <br/>

Lehner, B., Grill G. (2013): Global river hydrography and network routing: baseline data and new approaches to study the world’s large river systems. Hydrological Processes, 27(15): 2171–2186. Data is available at www.hydrosheds.org
