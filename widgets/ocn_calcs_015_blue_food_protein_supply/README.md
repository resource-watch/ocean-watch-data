# Blue food widget
This file describes the data and processing behind the [Contribution of blue food to protein supply](https://bit.ly/3bTG79a) on [Ocean Watch](https://oceanwatchdata.org)

## Style and Fuction
A [sunburst chart](https://vega.github.io/vega/examples/sunburst/) displaying the commodities that conribute to a country's protein supply. Each commodity that makes up a country's protein supply is a piece of the outermost ring. The size of its arc represents the size of the contribution of that commodity to the country's daily protein supply in grams per person per day (g/capita/day). Each commodity is categorized in a heirarchical relationship defined by how the production of the commodity affect the ocean. A given commodity can be sourced from the ocean, sourced from a land-based practice that generates pressure on the ocean, or sourced from other land-based practices.

*Click the `i` button on the [widget](https://bit.ly/3bTG79a)(this example is data for Mexico) to read the full description.*

## Data Source
Data displayed in this widget comes from the [Food from the Sea](https://resourcewatch.org/data/explore/foo061rw0-Blue-Food-Supply) dataset on Resource Watch. This widget also incorporates additional data from the underlying dataset ([FAO Food Balance Sheet](https://www.fao.org/faostat/en/#data/FBS))

## Processing
To create the widget, the Ocean Watch data team processed the dataset using a [python script](ocn_calcs_015_blue_food.py). 

**Synopsis:** The Food Balance Sheets produced by the FAO contains comphrensive information on counties' food supply. We extracted information on the protein supply available per person for each individual food item in a countries food supply. The food items are arregated into groups by the FAO. The Ocean Watch Data Team assigned each group to one of three categories depending on how the item was produced; either sourced from the ocean, sourced from land-based practices that put pressure on the ocean, or sourced from other land-based practices. The data were joined to a table to match each item to its FAO item group and the assigned category. The data was then restructured to reflect a 'parent' hierarchical relationship by adding rows for the "parents" (cateogies and the total). The [processed table](https://resourcewatch.carto.com/u/wri-rw/dataset/ocn_calcs_015_blue_food_protein_supply) is stored on Carto.

## Supplemental Files 
| File | Description |
| --------------- | --------------- |
|  [`blue_food_visualization.ipynb`](blue_food_visulization.ipynb)  |    notebook describing the Vega specification to create the visualization| 
| [`ocn_calcs_015_blue_food.py`](ocn_calcs_015_blue_food.py)  |     script used to process and upload the data to Carto | 
