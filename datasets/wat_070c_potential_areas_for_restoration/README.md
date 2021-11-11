## Potential Areas on Land for Restoration Dataset
This file describes the Potential Areas on Land for Restoration dataset on [Ocean Watch](https://www.oceanwatchdata.org)

### Function
Areas with greater than or equal to 50% soil erosion that experienced forest cover loss during the period from 2000 to 2020.

### Source
Tree cover loss: University of Maryland, Google, US Geological Suvery, National Aeronautics and Space Administration; Soil erosion: World Agroforestry Centre (ICRAF)

### About the data
- **Geographic coverage:** Global
- **Date of content:** 2020
- **Data type:** Raster
- **Spatial resolution:** 300 m
- **Frequency of updates:** Dependent on availabilty of soil erosion prevalence data

<br/>*Learn more about the underlying data: [Soil Erosion](https://resourcewatch.org/data/explore/wat070rw0-Soil-Erosion), [Tree Cover Loss](https://resourcewatch.org/data/explore/for008-Tree-Cover-Loss_1)

### Download the underlying data
[Soil erosion in the global tropics (2002, 2007, 2012, 2017)](http://landscapeportal.org/maps/3037) <br/>
[Global Forest Change 2000–2020](https://storage.googleapis.com/earthenginepartners-hansen/GFC-2020-v1.8/download.html) <br/>

### Pre-processing
The Ocean Watch data team used a [Googele Earth Engine script](https://code.earthengine.google.com/8662fb1936cfcb01d6ea27f82649955c?accept_repo=users%2Fresourcewatch%2Fdefault) to calculate areas with  high soil erosion and tree cover loss. The soil erosion dataset was subsetted to pixels where soil erosion prevalence was greater than or equal to 50%. The tree cover loss dataset was subsetted to pixels where there was tree cover loss over the study period (2000-2020). The two raster images were summed. The resulting data was saved as [a Google Earth Engine asset](https://code.earthengine.google.com/?asset=projects/resource-watch-gee/wat_070c_potential_areas_for_restoration). Ocean Watch displays the pixels with both high soil erosion prevalence and tree cover loss.

### Citation
Hansen, M. C., P. V. Potapov, R. Moore, M. Hancher, S. A. Turubanova, A. Tyukavina, D. Thau, S. V. Stehman, S. J. Goetz, T. R. Loveland, A. Kommareddy, A. Egorov, L. Chini, C. O. Justice, and J. R. G. Townshend. 2013. “High-Resolution Global Maps of 21st-Century Forest Cover Change.” Science 342 (15 November): 850–53. Data available on-line at: https://earthenginepartners.appspot.com/science-2013-global-forest. <br/>

Vågen, T.-G., & Winowiecki, L. A. (2019). Predicting the Spatial Distribution and Severity of Soil Erosion in the Global Tropics using Satellite Remote Sensing. Remote Sensing, 11(15), 1800. https://doi.org/10.3390/rs11151800 

