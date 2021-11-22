# Nutrient balance widget
This file describes the data and processing behind the [Nutrient balance widget](https://bit.ly/3n0IVaW) on [Ocean Watch](https://oceanwatchdata.org)

## Style and Fuction
A line chart displaying the excess or deficit of nutrients (in kg) per hectare of agricultural land in a given country.

*Click the `i` button on the [widget](https://bit.ly/3n0IVaW) (this example is data for Mexico) to read the full description.*

## Data Source
Data displayed in this widget comes from the [Nutrient Balance](../../datasets/foo_063_rw0_nutrient_balance/README.md) dataset on Ocean Watch.

## Processing
To create the widget, the Ocean Watch data team drew data directly from the [table](https://resourcewatch.carto.com/u/wri-rw/dataset/foo_063_rw0_nutrient_balance_edit) for the Nutrient Balance dataset stored on Carto. Within the widget, the data was subsetted to values for nutrient balance measured in `kg/ha`.

## Supplemental Files 
| File | Description |
| --------------- | --------------- |
|  [`nutrient-balance.ipynb`](nutrient-balance.ipynb)  |    notebook describing the Vega specification to create the visualization| 
