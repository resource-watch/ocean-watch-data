## Shipping Emissions Dataset
This file describes the Shipping Emissions dataset on [Ocean Watch](https://www.oceanwatchdata.org)

### Function
Share of total CO<sub>2</sub> emissions attributable to maritime bunker fuel, by country by year.

### Source
The Organisation for Economic Co-operation and Development (OECD)

### About the data
- **Geographic coverage:** 42 countries
- **Date of content:** 2006-2018
- **Data type:** Tabular
- **Spatial resolution:** National
- **Frequency of updates:** Not stated

<br/>The OEECD took these data from the International Energy Agency's World Energy Balances and Statistics: CO<sub>2</sub> emissions from fuel combustion database.

<br/>*Learn more about the data [here](https://www.iea.org/reports/greenhouse-gas-emissions-from-energy-overview)*


### Download the data
[Sustainable Ocean Economy: International marine bunker CO<sub>2</sub> emissions as share of total CO<sub>2</sub> emissions from fuel combustion, %](http://stats.oecd.org/index.aspx?datasetcode=OCEAN) <br>

### Pre-processing
The Ocean Watch data team used a [python script](com_038_rw0_shipping_emissions.py) to subset and upload the selected data to [a table on Carto](https://resourcewatch.carto.com/u/wri-rw/dataset/com_038_rw0_shipping_emissions_edit). The source provided the data as a single CSV file, which contained country-/territory-level time series data for a variety of indicators related to transportation and emissions. We extracted a single indicator, `IND-ENE-MAR`, which describes the "share of CO2 emissions from international maritime bunkers in total CO2 emissions". The time series data for all countries was saved in a standalone CSV file, which was then uploaded to Carto.

You can view the processed dataset for [display on Resource Watch](https://resourcewatch.org/data/explore/ac9c2f07-9f23-4a33-9958-e02c571ec009).

### Citation
OECD (2020), [Sustainable Ocean Economy \[Data set]. Available from https://stats.oecd.org.