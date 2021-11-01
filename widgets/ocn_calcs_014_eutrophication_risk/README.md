# Coastal Eutrophication Risk Widget
This file describes the data and processing used to create the [Coastal Eutrophication widget](https://bit.ly/3BlgYiK) on [Ocean Watch](https://oceanwatchdata.org)

## Style and Fuction
A bar chart depicting the proportion of river sub-basins at each Index of Coastal Eutrophication Potential (ICEP) within a country or territory. The widget was also produced at a global level. 

## Data
Data displayed in this widget comes from the [Aqueduct Coastal Eutrophication Potential](https://resourcewatch.org/data/explore/wat059-Aqueduct-Coastal-Eutrophication-Potential) datset on Resource Watch.

## Processing
The data was processesed prior to creating the widget. The sub-basin polygons from ICEP dataset were projected into a projected coordinate system (EPSG:3395). The centroids of the polygons were calculated and reprojected to a geographic coordiante system (EPSG:4326). The centroids were spatially joined to GADM country borders. We grouped the data by country and risk level to get the number of basins at each level within a country and globally, and summed across risk levels to get total number of basins. Using these two values, we calculated the proportion of sub-basins at each ICEP level.
