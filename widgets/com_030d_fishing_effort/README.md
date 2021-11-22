# Fishing Indicator Widget
This file describes the data and processing behind the [Annual global fishing effort and fisheries production](https://bit.ly/2ZWnQWt) and the [Annual fishing effort and fisheries production in the country's marine area widget](https://bit.ly/31vPw50) on [Ocean Watch](https://oceanwatchdata.org)

## Style and Fuction
A line chart displaying (1) time spent fishing within marine areas under national jurisdiction and (2) fishery capture production in tons, by year, in a country/territory. The widget is also available at a global level. Because of limitations in data access, the global widget only reflects time spent fishing within *national* waters. This widget will be updated to include international waters when the data becomes available. 


*Click the `i` button on the [global widget](https://bit.ly/2ZWnQWt) and the [country/territory widget](https://bit.ly/31vPw50) to read the full description.*

## Data Source
Data displayed in this widget comes from the [Fishing Effort by Zone](../../datasets/com_030d_rw0_fishing_effort_by_zone/README.md) dataset on Ocean Watch and the [Fishery Production](https://resourcewatch.org/data/explore/foo062-Fishery-Production) dataset on Resource Watch.

### Caution
Global Fishing Watch (GFW) employs a sophisticated machine learning algorithm to identify where vessels are fishing, the gear they're using, and how long fishing takes place, among other variables. Global Fishing Watch’s fishing detection algorithm is a best effort mathematically to identify “apparent fishing activity.” As a result, it is possible that some fishing activity is not identified as such by Global Fishing Watch; conversely, Global Fishing Watch may show apparent fishing activity where fishing is not actually taking place. For these reasons, Global Fishing Watch qualifies designations of vessel fishing activity, including synonyms of the term “fishing activity,” such as “fishing” or “fishing effort,” as “apparent,” rather than certain. Any/all Global Fishing Watch information about “apparent fishing activity” should be considered an estimate and must be relied upon solely at your own risk. Global Fishing Watch is taking steps to make sure fishing activity designations are as accurate as possible.

## Processing
To create the widget, the Ocean Watch data team drew data directly from the [table](https://resourcewatch.carto.com/u/wri-rw/dataset/com_030d_fishing_effort_by_zone) for the Fishing Effort by Zone dataset and the [table](https://resourcewatch.carto.com/u/wri-rw/dataset/foo_062_rw0_fishery_production_edit) for the Fishery Production dataset, which are both stored on Carto. Within the widget configuration the data are transformed. See the synposis below.

**Synopsis:** The fishing effort data are subsetted to data for exclusive economic zones (EEZs, 200 nautical miles from the coastline). Joint regimes and overlapping claims are excluded. Fishing effort is assigned to the land area which directly relates to the EEZ (when not an island) or the state that has jurisdiction over the territory (when the land area is an island). For the global widget, the fishing effort data of all zones (including joint regimes are overlapping claims) are summed by year. The fishery production data are subsetted to data for capture production. For the global widget, country/territory data is summed by year.


## Supplemental Files 
| File | Description |
| --------------- | --------------- |
|  [`fishing-effort_production_visualization.ipynb`](fishing-effort_production_visualization.ipynb)  |    notebook describing the Vega specification to create the visualization| 
