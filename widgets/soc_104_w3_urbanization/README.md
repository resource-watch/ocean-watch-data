# Urbanization widget
This file describes the data and processing behind the [Urbanization, 2015–2019 widget](https://bit.ly/3cjQFhW) on [Ocean Watch](https://oceanwatchdata.org)

## Style and Fuction
A bar chart displaying area of land that transitioned to urban area by year in a given country or territory from 2015-2019. 

*Click the `i` button on the [widget](https://bit.ly/3cjQFhW) (this example is data for Mexico) to read the full description.*

## Data Source
Data displayed in this widget comes from the [Land Cover Change](../../datasets/ocn_calcs_016_land_cover_change/README.md) dataset on Ocean Watch.

## Processing
To create the widget, the Ocean Watch data team drew directly from the [table](https://resourcewatch.carto.com/u/wri-rw/dataset/ocn_calcs_016_land_cover_change_by_territory) for the Land Cover Change dataset stored on Carto. Within the widget configuration, the data was subsetted to transition from any land cover class to urban.

## Supplemental Files 
| File | Description |
| --------------- | --------------- |
|  [`land-cover-change-urbanization.ipynb`](land-cover-change-urbanization.ipynb)  |    notebook describing the Vega specification to create the visualization| 
