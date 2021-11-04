# Minerals and Energy Indicator Widget
This file describes the data and processing behind the [Renewable energy generation from the ocean widget](https://bit.ly/2Ye7esi) on [Ocean Watch](https://oceanwatchdata.org)

## Style and Fuction
A stacked bar chart displaying the energy generation in gigwatt hours from ocean-based renewables by year. Ocean-based renewables are divided into offshore wind energy and marine energy (includes wave, tidal, and salinity energy as well as ocean thermal gradient conversion). The widget is available at both a global and country/territory level. 

*Click the `i` button on the [widget](https://bit.ly/2Ye7esi) to read the full description.*

## Data Source
Data displayed in this widget comes from the [Annual Renerwable Energy Generation](https://resourcewatch.org/data/explore/ene009-Annual-Renewable-Generation) dataset on Resource Watch.

## Processing
To create the widget, the Ocean Watch data team drew data directly from the [table](https://resourcewatch.carto.com/u/wri-rw/dataset/ene_009_renewable_generation_annually_edit) for the Annual Renerwable Energy Generation dataset stored on Carto. Within the widget configuration the data are subsetted to `Marine` and `Offshore Wind` subtechnologies.


## Supplemental Files 
| File | Description |
| --------------- | --------------- |
|  [`renewable_energy_generation_visualization.ipynb`](renewable_energy_generation_visualization.ipynb)  |    notebook describing the Vega specification to create the visualization|  
