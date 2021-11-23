## Fishing Effort by Zone Dataset
This file describes the Fishing Effort by Zone dataset on [Ocean Watch](https://www.oceanwatchdata.org)

### Function
Time spent fishing within within 200 nautical miles of country and territory coastlines (Exclusive Economic Zones), or other zone, disaggregated by year. Vessels are detected using an Automatic Identification System (AIS). Machine learning models are used to classify vessels and predict when they are fishing.

### Source
Global Fishing Watch 

### About the data
- **Geographic coverage:** Global
- **Date of content:** 2012-2020
- **Data type:** Tabular
- **Spatial resolution:** National
- **Frequency of updates:** Yearly

### Caution
Global Fishing Watch (GFW) employs a sophisticated machine learning algorithm to identify where vessels are fishing, the gear they're using, and how long fishing takes place, among other variables. Global Fishing Watch’s fishing detection algorithm is a best effort mathematically to identify “apparent fishing activity.” As a result, it is possible that some fishing activity is not identified as such by Global Fishing Watch; conversely, Global Fishing Watch may show apparent fishing activity where fishing is not actually taking place. For these reasons, Global Fishing Watch qualifies designations of vessel fishing activity, including synonyms of the term “fishing activity,” such as “fishing” or “fishing effort,” as “apparent,” rather than certain. Any/all Global Fishing Watch information about “apparent fishing activity” should be considered an estimate and must be relied upon solely at your own risk. Global Fishing Watch is taking steps to make sure fishing activity designations are as accurate as possible.

<br/>*Learn more about the data [here](https://globalfishingwatch.org/dataset-and-code-fishing-effort/)* 

<br/>

### Download the data
[Fishing effort](https://globalfishingwatch.org/data-download/datasets/public-fishing-effort) 


### Pre-processing
The Ocean Watch data team used a [python script](fishing-effort_collect-data.py) to request data and upload the selected data to [a table on Carto](https://resourcewatch.carto.com/u/wri-rw/dataset/com_030d_fishing_effort_by_zone). Data were requested through the Global Fishing Watch API. The API is still under construction and not available for use by the general public. Data was requested using polygons for Exclusive Economic Zones (`200NM`, 200 nautical miles from coastalin), overlapping claim areas, and joint regime areas from the [Maritime Boundaries dataset](https://resourcewatch.org/data/explore/com011rw1-Maritime-Boundaries) on Resource Watch. We checked for requests that failed and re-requested data using [an additional python script](fishing-effort_collect-data.py). This script can also be run to request data for new years.

### Citation
D.A. Kroodsma, J. Mayorga, T. Hochberg, N.A. Miller, K. Boerder, F. Ferretti, A. Wilson, B. Bergman, T.D. White, B.A. Block, P. Woods, B. Sullivan, C. Costello, and B. Worm. "Tracking the global footprint of fisheries." Science 361.6378 (2018).

### License 
Global Fishing Watch data is licensed foruse through WRI for educational or other non-commercialpurposes subject toCC BY-NC 4.0. Reproduction ofthis data and API access for resale or other commercialpurposes is prohibited without prior written permission.
