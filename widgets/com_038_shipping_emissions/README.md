# Shipping emissions widgets
This file describes the data and processing behind the [Shipping emissions: Top emitting countries](https://bit.ly/3aQtAml) and the [Proportion of national CO<sub>2</sub> emissions from shipping
widget](https://bit.ly/3BI7C01) on [Ocean Watch](https://oceanwatchdata.org)

## Style and Fuction
A line chart displaying the proportion of total CO<sub>2</sub> emissions attributable to maritime bunker fuel, by country by year. At the global level, the widget shows the time series for the top 10  countries with the greatest proportion of emissions from maritime bunker fuel. 

*Click the `i` button on the [global](https://bit.ly/3aQtAml) or the [country/territory](https://bit.ly/3BI7C01) widget to read the full description.*

## Data Source
Data displayed in this widget comes from the [Shipping Emissions](../../datasets/com_038_rw0_shipping_emissions/README.md) dataset on Ocean Watch.

## Processing
To create the widget, the Ocean Watch data team drew data directly from the [table](https://resourcewatch.carto.com/u/wri-rw/dataset/com_038_rw0_shipping_emissions_edit) for the Shipping Emissions Dataset stored on Carto.

## Supplemental Files 
| File | Description |
| --------------- | --------------- |
|  [`shipping-emissions_visualization.ipynb`](shipping-emissions_visualization.ipynb)  |    notebook describing the Vega specification to create the visualization| 
