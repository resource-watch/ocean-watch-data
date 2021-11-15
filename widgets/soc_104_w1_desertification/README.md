# Desertification widget
This file describes the data and processing behind the [Desertification, 2015-2019 widget](https://bit.ly/2YHvi7k) on [Ocean Watch](https://oceanwatchdata.org)

## Style and Fuction
A stacked bar chart displaying area of land that transitioned from shrubland and grassland, forests, wetlands, and croplands to bare ground by year in a given country from 2015-2019. 

*Click the `i` button on the [widget](https://bit.ly/2YHvi7k) (this example is data for Mexico) to read the full description.*

## Data Source
Data displayed in this widget comes from the [Land Cover Change](../../datasets/ocn_calcs_016_land_cover_change/README.md) dataset on Ocean Watch.

## Processing
To create the widget, the Ocean Watch data team drew directly from the [table](https://resourcewatch.carto.com/u/wri-rw/dataset/ocn_calcs_016_land_cover_change_by_territory) for the Land Cover Change dataset stored on Carto. Within the widget configuration, the data was subsetted to the following tranisitions: 'Cropland to bare', 'Forest to bare', 'Wetland to bare', 'Vegetation to bare'.

## Supplemental Files 
| File | Description |
| --------------- | --------------- |
|  [`land-cover-change-desertification.ipynb`](land-cover-change-desertification.ipynb)  |    notebook describing the Vega specification to create the visualization| 
