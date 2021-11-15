## Land Cover Change Dataset
This file describes the Land Cover Change dataset on [Ocean Watch](https://www.oceanwatchdata.org)

### Function
Change in land cover class (as defined by [Copernicus Global Land Cover](https://lcviewer.vito.be/about)) by year.

### Source
Copernicus Global Land Service (CGLS)

### About the data
- **Geographic coverage:** Global
- **Date of content:** 2017-2019
- **Data type:** Raster
- **Spatial resolution:** 100 m
- **Frequency of updates:** Yearly

<br/>*Learn more about the underlying data [on Resource Watch](https://resourcewatch.org/data/explore/Global-Land-Cover-UN-FAO-LCCS-Classification)*

### Download the underlying data
[Global Land Cover](https://lcviewer.vito.be/download) 

### Pre-processing
The Ocean Watch data team used a [Google Earth Engine script](https://code.earthengine.google.com/1a106a75689826e6bf7283b7d7c7f6f5) to calculate the area of specific types of land cover change transitions across a country/territory polygon set. The resulting data were downloaded as a series of csv's by year. The data team then used a [python script](land-cover-change-structuring.py) to restructure and upload the data to [a table on Carto](https://resourcewatch.carto.com/u/wri-rw/dataset/ocn_calcs_016_land_cover_change_by_territory).

### Citation
Buchhorn, M. ; Lesiv, M. ; Tsendbazar, N. - E. ; Herold, M. ; Bertels, L. ; Smets, B. Copernicus Global Land Cover Layers — Collection 2. Remote Sensing 2020, 12, Volume 108, 1044. DOI 10.3390/rs12061044. Accessed through Resource Watch, (date). www.resourcewatch.org.
