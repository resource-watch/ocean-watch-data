# Ocean Watch Datasets
This folder in contains metadata information and processing workflows and scripts for all __unpublished__ datasets on Ocean Watch (more information below). For more information on viewing, creating, and updating published and unpublished datasets, see the [wiki](https://github.com/resource-watch/ocean-watch-data/wiki)

# Directory sturcture
Each unpublished dataset on Ocean Watch has its own sub-directory here. They sub-directories names start with the `wri_id` of the dataset. Inside you'll find a `README` describing the contents of the sub-directory as well dataset metadata. In most sub-directories you will find a preprocessing script that downloads, transforms, and uploads the data to Carto (vector/tabular) or GEE (raster). The sub-directory name also reflects te name of the data table or asset. If multiple scripts were used to process the dataset, you may find a notebook outlining the workflow steps as well. 

## Generating a catalog of datasets on Ocean Watch 
Run the [`get_datasets.py`](get_datasets.py) script to generate a list of all the datasets that are currently used on Ocean Watch.