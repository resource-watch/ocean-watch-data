## Population Affected by Sea Level Rise (Grid, 100m) Dataset
This file describes the Population Affected by Sea Level Rise (Grid, 100m) dataset on [Ocean Watch](https://www.oceanwatchdata.org)

### Function
Gridded estimated count of population in areas that will likely be flooded at different amounts rising water due to a combination of sea level rise, tide, and storm surge

### Source
WorldPop and Climate Central

### About the data
- **Geographic coverage:** Global coastline
- **Date of content:** 2020
- **Frequency of updates:** Yearly

<br/>*Learn more about the [Global population](https://resourcewatch.org/data/explore/d6e42176-90c4-429d-8cae-7619c545a458) and the [Projected sea-level rise](https://resourcewatch.org/data/explore/Projected-Sea-Level-Rise) data on [Resource Wacth](https://resourcewatch.org/)*

### Download the data
[Global population](https://www.worldpop.org/project/categories?id=3)
[Projected sea-level rise](https://coastal.climatecentral.org/map/12/-73.9728/40.7085/?theme=water_level&map_type=water_level_above_mhhw&basemap=roadmap&contiguous=true&elevation_model=best_available&refresh=true&water_level=3.0&water_unit=m) 

### Pre-processing
The Ocean Watch data team used a [java script](https://code.earthengine.google.com/f2ebfdf6d65ca832c60957ac6e062e51?accept_repo=users%2Fresourcewatch%2Fdefault) to subset global population estimates by projected sea-level rise and save the selected data to [Google Earth Engine](https://code.earthengine.google.com/?asset=projects/resource-watch-gee/soc_107_population)


### Citation
WorldPop. (2020). WorldPop Global Project Population Data \[Data set]. Available from https://www.worldpop.org/.
Climate Central. (2018). Coastal Risk Screening Tool \[database]. Available from https://www.worldpop.org/.