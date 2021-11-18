## Fishing Effort by Zone Dataset
This file describes the Fishing Effort by Zone dataset on [Ocean Watch](https://www.oceanwatchdata.org)

### Function
Time spent fishing within each Exclusive Economic Zone (or other zone) disaggregated by year, as detected using an Automatic Identification System (AIS)

### Source
Global Fishing Watch 

### About the data
- **Geographic coverage:** Global
- **Date of content:** 2012-2020
- **Data type:** Tabular
- **Spatial resolution:** National
- **Frequency of updates:** Yearly

<br/>*Learn more about the data [here](https://globalfishingwatch.org/dataset-and-code-fishing-effort/)*

### Download the data
[Fishing effort](https://globalfishingwatch.org/data-download/datasets/public-fishing-effort) 

### Pre-processing
The Ocean Watch data team used a [python script](fishing-effort_collect-data.py) to request data and upload the selected data to [a table on Carto](https://resourcewatch.carto.com/u/wri-rw/dataset/com_030d_fishing_effort_by_zone). Data were requested through the Global Fishing Watch API. The API is still under construction and not available for use by the general public. Data was requested using polygons for Exclusive Economic Zones (`200NM`, 200 nautical miles from coastalin), overlapping claim areas, and joint regime areas from the [Maritime Boundaries dataset](https://resourcewatch.org/data/explore/com011rw1-Maritime-Boundaries) on Resource Watch. We checked for requests that failed and re-requested data using [an additional python script](fishing-effort_collect-data.py). This script can also be run to request data for new years.

### Citation
D.A. Kroodsma, J. Mayorga, T. Hochberg, N.A. Miller, K. Boerder, F. Ferretti, A. Wilson, B. Bergman, T.D. White, B.A. Block, P. Woods, B. Sullivan, C. Costello, and B. Worm. "Tracking the global footprint of fisheries." Science 361.6378 (2018).
