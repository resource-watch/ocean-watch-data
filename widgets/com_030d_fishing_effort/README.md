# Fishing Indicator Widget
This file describes the data and processing behind the [Annual global fishing effort and fisheries production](https://bit.ly/2ZWnQWt) and the [Annual fishing effort and fisheries production in the country's marine area widget](https://bit.ly/31vPw50) on [Ocean Watch](https://oceanwatchdata.org)

## Style and Fuction
A line chart displaying (1) time spent fishing within marine areas under national jurisdiction and (2) fishery capture production in tons, by year, in a country/territory. The widget is also available at a global level. Because of limitations in data access, the global widget only reflects time spent fishing within *national* waters. This widget will be updated to include international waters when the data becomes available. 


*Click the `i` button on the [global widget](https://bit.ly/2ZWnQWt) and the [country/territory widget](https://bit.ly/31vPw50) to read the full description.*

## Data Source
Data displayed in this widget comes from the [Fishing Effort by Zone](../../datasets/com_030d_rw0_fishing_effort_by_zone/README.md) dataset on Ocean Watch and the [Fishery Production](https://resourcewatch.org/data/explore/foo062-Fishery-Production) dataset on Resource Watch.

## Processing
To create the widget, the Ocean Watch data team drew data directly from the [table](https://resourcewatch.carto.com/u/wri-rw/dataset/com_030d_fishing_effort_by_zone) for the Fishing Effort by Zone dataset and the [table](https://resourcewatch.carto.com/u/wri-rw/dataset/foo_062_rw0_fishery_production_edit) for the Fishery Production dataset, which are both stored on Carto. Within the widget configuration the data are transformed. See the synposis below.

**Synopsis:** The fishing effort data are subsetted to data for exclusive economic zones (EEZs, 200 nautical miles from the coastline). Joint regimes and overlapping claims are excluded. Fishing effort is assigned to the land area which directly relates to the EEZ (when not an island) or the state that has jurisdiction over the territory (when the land area is an island). For the global widget, the fishing effort data of all zones (including joint regimes are overlapping claims) are summed by year. The fishery production data are subsetted to data for capture production. For the global widget, country/territory data is summed by year.


## Supplemental Files 
| File | Description |
| --------------- | --------------- |
|  [`fishing-effort_production_visualization.ipynb`](fishing-effort_production_visualization.ipynb)  |    notebook describing the Vega specification to create the visualization| 
