## Coastal Population Dataset
This file describes the Coastal Population dataset on [Ocean Watch](https://www.oceanwatchdata.org)

### Function
Estimated residential population living within 5km of the coastline per 100m by 100m grid cell

### Source
WorldPop

### About the data
- **Geographic coverage:** Global
- **Date of content:** 2020
- **Data type:** Raster
- **Spatial resolution:** 100m
- **Frequency of updates:** Yearly

<br/>*This data is a subset of the Globl Population dataset on Resource Watch. Learn more about the data [here](https://resourcewatch.org/data/explore/d6e42176-90c4-429d-8cae-7619c545a458)*

### Download the data
[Global population](https://www.worldpop.org/project/categories?id=3)

### Pre-processing
The Ocean Watch data team used a [javaScript script](https://code.earthengine.google.com/987a86e51122fd1516f545208f27d2e0?accept_repo=users%2Fresourcewatch%2Fdefault) to mask data to an area 5km from the coast and upload the selected data to [Google Earth Engine](https://code.earthengine.google.com/?asset=projects/resource-watch-gee/ocn_021_coastal_population).

### Citation
WorldPop. (2020). WorldPop Global Project Population Data \[Data set]. Available from https://www.worldpop.org/.