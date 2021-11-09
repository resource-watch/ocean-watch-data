# Production, export and import widget
This file describes the data and processing behind the [Production, export and import of marine food](https://bit.ly/3H6k1yx) on [Ocean Watch](https://oceanwatchdata.org)

## Style and Fuction
A area and line chart displaying the change in production, import, and export of marine food items over time for a given country. 

*Click the `i` button on the [widget](https://bit.ly/3H6k1yx) (this expample is data for Mexico) to read the full description.*

## Data Source
Data displayed in this widget comes from the [Food from the Sea](https://resourcewatch.org/data/explore/foo061rw0-Blue-Food-Supply) dataset on Resource Watch.

## Processing
To create the widget, the Ocean Watch data team drew data directly from the [table](https://resourcewatch.carto.com/u/wri-rw/dataset/foo_061_rw0_blue_food_supply_edit) for the Food from the Sea (Blue Food)dataset stored on Carto. Within the widget the dataset is subsetted to values for import, export, and production of marine food items for a given country. 

## Supplemental Files 
| File | Description |
| --------------- | --------------- |
|  [`blue-food-import-export.ipynb`](blue-food-import-export.ipynb)  |    notebook describing the Vega specification to create the visualization| 
