## Ocean Nationally Determined Contributions Dataset
This file describes the Ocean Nationally Determined Contributions (NDC) dataset on [Ocean Watch](https://www.oceanwatchdata.org)

### Function
The data shows whether sectoral adaptation and mitigation measures have been made by each country- in their nationally determined contribution-  in subsectors related to ocean management.

### Source
Climate Watch

### About the data
- **Geographic coverage:** Global  
- **Date of content:** 2021
- **Data type:** Tabular
- **Spatial resolution:** National
- **Frequency of updates:** Weekly

<br/>*Learn more about the data [here](https://www.climatewatchdata.org/data-explorer/ndc-content?ndc-content-categories=unfccc_process&ndc-content-countries=All%20Selected&ndc-content-indicators=All%20Selected&ndc-content-sectors=All%20Selected&page=1#meta)*

### Download the data
[Climate Watch NDC Content](https://www.climatewatchdata.org/data-explorer/ndc-content?ndc-content-categories=unfccc_process&ndc-content-countries=All%20Selected&ndc-content-indicators=All%20Selected&ndc-content-sectors=All%20Selected&page=1#data) 

### Pre-processing
The Ocean Watch data team used a [python script](ocn_025_rw0_ocean_ndcs/ocn_025_rw0_ocean_ndcs.py) to request this data through the Climate Watch API. The dataset on Ocean Watch contains measures in subsectors that can _only_ be related to ocean management and excludes measures related to other biomes. These subsectors are Renewable Energy: Ocean, Mangroves, Fisheries and Aquaculture, Maritime, Coastal management, Coastal fisheries, Coastal Zone: General, and Sea-level Rise Protection. The data team uploaded the selected data to [a table on Carto.](https://resourcewatch.carto.com/u/wri-rw/dataset/ocn_025_rw0_ocean_ndc_measures)


### Citation
Climate Watch NDC Content. 2021. Washington, DC: World Resources Institute. Available online at: https://www.climatewatchdata.org
