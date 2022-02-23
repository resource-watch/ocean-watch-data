# Deforestation and crop expansion widget
This file describes the data and processing behind the [Deforestation and crop expansion, 2015–2019](https://bit.ly/31YijiJ) on [Ocean Watch](https://oceanwatchdata.org)

## Style and Fuction
A bar chart displaying the area of land that transitioned from forest to cropland and from cropland to forest by year in a given country or territory from 2015-2019. 

*Click the `i` button on the [widget](https://bit.ly/31YijiJ) (this example is data for Mexico) to read the full description.*

## Data Source
Data displayed in this widget comes from the [Land Cover Change](../../datasets/soc_104b_land_cover_change/README.md) dataset on Ocean Watch.

## Processing
To create the widget, the Ocean Watch data team drew directly from the [table](https://resourcewatch.carto.com/u/wri-rw/dataset/soc_104b_land_cover_change) for the Land Cover Change dataset stored on Carto. Within the widget configuration, the data was subsetted to the following tranisitions: 'Forest to cropland', 'Cropland to forest'. The areas for 'Forest to cropland' were multiplied by -1 to reflect loss of forest. The areas for the two transition classes were then plotted as a stacked bar chart. The data for these two transition classes were also summed across years and plotted as a line to show net change.

## Supplemental Files 
| File | Description |
| --------------- | --------------- |
|  [`land-cover-change-deforestation-crop-expansion.ipynb`](land-cover-change-deforestation-crop-expansion.ipynb)  |    notebook describing the Vega specification to create the visualization| 
