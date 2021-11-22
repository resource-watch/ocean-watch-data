# Marine Protected Areas Widget
This file describes the data and processing behind the [Progress toward protecting 30% of the ocean widget](https://bit.ly/2Z25ORW) on [Ocean Watch](https://oceanwatchdata.org)

## Style and Fuction
**Global:** A stacked area chart displaying the area in km<sup>2</sup> of the global marine environment that is protected over time. Areas are by marine area under national/territorial jurisdiction and areas beyond national jurisdiction. A dashed line reflects the emerging Post 2020 Biodiversity Framework target of protecting 30% of the ocean. <br>
**Country or territory:** An area chart displaying the proportion of marine area that is protected by country or territory over time. The total marine area includes shared marine areas and any overseas territories.

*Click the `i` button on the [widget](https://bit.ly/2Z25ORW) to read the full description.*

## Data Source
Data displayed in this widget comes from the [Marine Protected Areas](../../datasets/ocn_023_rw1_marine_protection/README.md) dataset on Ocean Watch.

## Processing
To create the widget, the Ocean Watch data team drew data directly from the [table](https://resourcewatch.carto.com/u/wri-rw/dataset/ocn_023_rw1_marine_protection_edit) for the Marine Protected Areas dataset stored on Carto.

## Supplemental Files 
| File | Description |
| --------------- | --------------- |
|  [`protected_areas_visualization.ipynb`](protected_areas_visualization.ipynb)  |    notebook describing the Vega specification to create the visualization| 
