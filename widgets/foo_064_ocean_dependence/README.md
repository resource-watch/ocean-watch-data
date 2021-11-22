# Ocean Dependence Indicator Widget
This file describes the data and processing behind the [Food secuirty and dependence on marine protein widget](https://bit.ly/3BWhuE9) on [Ocean Watch](https://oceanwatchdata.org)

## Style and Fuction
A bubble chart. The size of a circle represents the average prevalence of moderate to severe food insecurity 2018-2020. The color gradient represents the proportion of protein supply from marine protein from 2018. Countries or territories without both data do not have a circle. When the widget is displayed at a country/territory-level, the borders of the country/territory and its associated circle are highlighted. 

*Click the `i` button on the [widget](https://bit.ly/3BWhuE9) to read the full description.*

## Data Sources
Data displayed in this widget comes from the [Food from the sea](https://resourcewatch.org/data/explore/9e1b3cad-db6f-44b0-b6fb-048df7b6c680) dataset on Resource Watch and the [Food Insecurity](../../datasets/foo_064_rw0_food_insecurity/README.md) dataset on Ocean Watch .

## Processing
To create the widget, the Ocean Watch data team drew data directly from the [table](https://resourcewatch.carto.com/u/wri-rw/dataset/foo_061_rw0_blue_food_supply_edit) for the Food From the Sea (Blue Food Supply) dataset and the [table](https://resourcewatch.carto.com/u/wri-rw/dataset/foo_064_rw0_food_insecurity_edit) for the Food Insecurity dataset, which are both stored on Carto. Within the widget configuration the data are transformed. See the synposis below.

**Synopsis:** The Food From the Sea dataset is subsetted to only include values for protein supply. The data are aggregated by country and year. The resulting table is then pivotted so each country has a value for total protein supply and marine-sourced protein supply. These values are then used to calculate the proportion of total protein supply from marine protein. The Food From the Sea data and the Food Insecurity data are joined to country and territory geometries. The centriods of these geometries are calculated and minor adjustments are made to the coordinates of the centroids of countries and territories with multiple geometries and those close to the anti-meridean. The centroids and geometries are then projected into the [Natural Earth projection](http://www.shadedrelief.com/NE_proj/). Circular symbols are plotted at the projected centroids. 

## Supplemental Files 
| File | Description |
| --------------- | --------------- |
|  [`ocean_dependence_visualization.ipynb`](ocean_dependence_visualization.ipynb)  |    notebook describing the Vega specification to create the visualization| 
