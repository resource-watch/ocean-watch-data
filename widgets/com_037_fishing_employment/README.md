# Fishing Employment Widget
This file describes the data and processing behind the [Employment in fisheries and other natural sectors](https://bit.ly/3o6lVGU) on [Ocean Watch](https://oceanwatchdata.org)

## Style and Fuction
A stacked bar chart chart displaying employment in fishing compared to other natural sectors (agriculture, forestry, and hunting) by year for a given country or territory. The data can be disaggregated by sex.

*Click the `i` button on the [widget](https://bit.ly/3o6lVGU) (this example is data for Mexico) to read the full description.*

## Data Source
Data displayed in this widget comes from the [Fishing Employment](../../datasets/com_037_rw0_fishing_employment/README.md) dataset on Ocean Watch.

## Processing
To create the widget, the Ocean Watch data team drew data directly from the [table](https://resourcewatch.carto.com/u/wri-rw/dataset/com_037_rw0_fishing_employment_edit) for the Fishing Employment dataset stored on Carto. Within the widget configuration the data are transformed. See the synposis below.

**Synopsis:** The widget only displays data collected according to the most recent International Standard Industrial Classification revision. In most cases this is Revision 4. There are [23 countries](https://wri-rw.carto.com/api/v2/sql?q=SELECT%20DISTINCT%20(gadm.gid_0)%20AS%20iso,%20gadm.name_0%20AS%20name_0%20FROM%20(SELECT%20area,%20year,%20obs_value,%20rev,%20concat(type,%20%27%20Employment%20%27)%20AS%20type,%20sex,%20%271000%20people%27%20AS%20unit%20FROM%20com_037_rw0_fishing_employment_edit%20WHERE%20obs_value%20IS%20NOT%20NULL)%20data%20LEFT%20JOIN%20(SELECT%20DISTINCT(area),%20obs_value%20as%20rev4%20FROM%20com_037_rw0_fishing_employment_edit%20WHERE%20obs_value%20IS%20NOT%20NULL%20AND%20rev%20=%204)%20rev4%20ON%20rev4.area%20=%20data.area%20LEFT%20JOIN%20(SELECT%20DISTINCT(gid_0),%20name_0,%20geostore_prod%20FROM%20gadm36_0)%20AS%20gadm%20ON%20data.area%20=%20gadm.gid_0%20WHERE%20gadm.geostore_prod%20IS%20NOT%20NULL%20AND%20rev4.rev4%20IS%20NULL) where data categorized according to Rev 3 is displayed. The selected data table is the pivoted to a wide form so for a given year, there is a column for fishing employment and natural sector employment. Fishing emmployment is subtracted from natural sector employment to get empolyment in other natural sectors besides fishing. The table is then folded back to the long form and stacked to create the stack bar chart.


## Supplemental Files 
| File | Description |
| --------------- | --------------- |
|  [`fisheries_employment.ipynb`](fisheries_employment.ipynb)  |    notebook describing the Vega specification to create the visualization| 
