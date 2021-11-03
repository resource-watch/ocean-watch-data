## Surface Concentration of Nutrients at River Mouths Dataset
This file describes the Surface Concentration of Nutrients at River Mouths dataset on [Ocean Watch](https://www.oceanwatchdata.org)

### Function
Mean concentration at surface of nitrate, phosphate, and dissolved oxygen at points representing major river outlets into the ocean

### Source
Copernicus Marine Environment Monitoring Service (CMEMS)

### About the data
- **Geographic coverage:** Global
- **Date of content:** 2019-2021
- **Data type:** Vector
- **Spatial resolution:** ~1/4° (source data)
- **Frequency of updates:** Monthly

<br/>*Learn more about the data [here](https://resources.marine.copernicus.eu/product-detail/GLOBAL_ANALYSIS_FORECAST_BIO_001_028/INFORMATION)*

### Download the data
[Global Ocean Biogeochemistry Analysis and Forecast](https://resources.marine.copernicus.eu/product-detail/GLOBAL_ANALYSIS_FORECAST_BIO_001_028/INFORMATION) 

### Pre-processing
The Ocean Watch data team used an extensive series of scripts and manual processing to construct this dataset, [as described in detail here](./river-mouths_process-overview.ipynb). In summary, a global set of river mouth points was generated from [MERIT Hydro](https://doi.org/10.1029/2019WR024873) and [HydroRIVERS](https://www.hydrosheds.org/page/hydrorivers). River names were pulled from [OpenStreetMap](https://www.openstreetmap.org/). Longitudinal river mouth surface water quality data for these locations (in the form of nutrient concentrations) were then drawn from the [Global Ocean Biogeochemistry Analysis and Forecast (GLOBAL_ANALYSIS_FORECAST_BIO_001_028) product](https://resources.marine.copernicus.eu/?option=com_csw&view=details&product_id=GLOBAL_ANALYSIS_FORECAST_BIO_001_028) of the [Copernicus Marine Service](https://marine.copernicus.eu/) using API calls demonstrated by their [Pretty View](https://view-cmems.mercator-ocean.fr/GLOBAL_ANALYSIS_FORECAST_BIO_001_028) WebGIS tool. The ultimate resulting data were uploaded to [a table on Carto](https://resourcewatch.carto.com/u/wri-rw/dataset/ocn_020alt_chemical_concentrations).

### Citation
Global Ocean Biogeochemistry Analysis and Forecast (2021), E.U. Copernicus Marine Service Information [Dataset]. Accessed through Resource Watch, (date). www.resourcewatch.org.