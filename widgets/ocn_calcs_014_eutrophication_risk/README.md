# Coastal Eutrophication Risk Widget
This file describes the data and processing behind the [Coastal Eutrophication widget](https://bit.ly/3BlgYiK) on [Ocean Watch](https://oceanwatchdata.org)

## Style and Fuction
A bar chart displaying the proportion of river sub-basins at each Index of Coastal Eutrophication Potential (ICEP) within a country or territory. The widget is also available at a global level. 

*Click the `i` button on the [widget](https://bit.ly/3BlgYiK) to read the full description.*

## Data Source
Data displayed in this widget comes from the [Aqueduct Coastal Eutrophication Potential](https://resourcewatch.org/data/explore/wat059-Aqueduct-Coastal-Eutrophication-Potential) dataset on Resource Watch.

## Processing
To create the widget, the Ocean Watch data team processed the dataset using a [python script](https://github.com/resource-watch/ocean-watch-data/blob/main/widgets/ocn_calcs_014_eutrophication_risk/ocn_calcs_014_eutrophication_risk_processing.py). 

**Synopsis:** We projected the sub-basin polygons from ICEP dataset into a projected coordinate system `(epsg:3395)`. Centroids of the polygons were calculated and transformed to a geographic coordiante system `(epsg:4326)`. The centroids were spatially joined to GADM country borders. We grouped the data by country and risk level to get the number of basins at each level within a country and globally and summed across risk levels to get total number of basins. Using these two values, we calculated the proportion of sub-basins at each ICEP level. The [processed table](https://resourcewatch.carto.com/u/wri-rw/dataset/ocn_calcs_014_eutrophication_risk) is stored on Carto.

## Supplemental Files 
| File | Description |
| --------------- | --------------- |
|  [`eutrophication_risk_visualization.ipynb`](https://github.com/resource-watch/ocean-watch-data/blob/main/widgets/ocn_calcs_014_eutrophication_risk/eutrophication_risk_visualization.ipynb)  |    notebook describing the Vega specification to create the visualization| 
| [`ocn_calcs_014_eutrophication_risk_processing.py`](https://github.com/resource-watch/ocean-watch-data/blob/main/widgets/ocn_calcs_014_eutrophication_risk/ocn_calcs_014_eutrophication_risk_processing.py)  |     script used to process and upload the data to Carto | 
