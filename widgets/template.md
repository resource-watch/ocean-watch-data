# {Widget name} widget
This file describes the data and processing behind the [{Widget name}]({link-to-stand-alone-widget}) on [Ocean Watch](https://oceanwatchdata.org)

## Style and Fuction
A {style} chart displaying {description of values}. The widget is also available at a global level. 

*Click the `i` button on the [widget]({link-to-stand-alone-widget}) to read the full description.*

## Data Source
Data displayed in this widget comes from the [{underlying dataset}]({link-to-github-readme-for-dataset-or-RW-page}) dataset on {Resource Watch or Ocean Watch}.

## Processing
To create the widget, the Ocean Watch data team processed the dataset using a [python script]({link-to-processing-script}). 

**Synopsis:** We projected the sub-basin polygons from the ICEP dataset into a projected coordinate system `(epsg:3395)`. Centroids of the polygons were calculated and transformed to a geographic coordiante system `(epsg:4326)`. The centroids were spatially joined to GADM country borders. We grouped the data by country and risk level to get the number of basins at each level, within a country and globally, and summed across risk levels to calculate the total number of basins. Using these two values, we calculated the proportion of sub-basins at each ICEP level. The [processed table](https://resourcewatch.carto.com/u/wri-rw/dataset/ocn_calcs_014_eutrophication_risk) is stored on Carto.

## Supplemental Files 
| File | Description |
| --------------- | --------------- |
|  [`{notebook-file-name}`]({local-link})  |    notebook describing the Vega specification to create the visualization| 
| [`{processing-script-file-name}`]({local-link})  |     script used to process and upload the data to Carto | 
