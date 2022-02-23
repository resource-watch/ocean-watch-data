# Ocean Watch Datasets
[Ocean Watch](https://oceanwatchdata.org) provides data analysis and visualizations for ocean-related datasets. The catalog of Ocean Watch datasets underly all charts, maps, and indicators on the introduction and coastal-profile pages. This folder in contains metadata information and processing workflows and scripts for all __unpublished__ datasets on Ocean Watch (more information below).

## Catalog of Datasets
The Ocean Watch Data Team can find a catalog of all datasets on Ocean Watch on Sharepoint
[`Sustainable Ocean Initiative\Documents\Ocean Watch\Development\Data\Dataset Tracking`](https://onewri.sharepoint.com/sites/WRI_ocean/Shared%20Documents/Ocean%20Watch/Development/Data/Dataset%20Tracking%20Sheet.xlsx)

## About Datasets
All datasets on Ocean Watch are stored on [Resource Watch](https://resourcewatch.org/). 

### Published Datasets
Many of the Ocean Watch datasets are "published" on Resource Watch and are part of Resource Watch's public data catalog. If a dataset is published on Resource Watch, it can be access through the [explore page](https://resourcewatch.org/data/explore?section=All%20data&topics=[%22ocean%22]). Specific datasets can also be accessed from Ocean Watch. Click the "i" button on the upper right hand corner of any of the relevant data assets and find a link to the dataset on Resource Watch. You can learn more about each dataset on its "Metadata page." For information on how the dataset was processed, refer to the [`resource-watch/data-preprocessing`](https://github.com/resource-watch/data-pre-processing) or [`resource-watch/nrt-script`](https://github.com/resource-watch/nrt-scripts) repositories. You will find links directly to the applicable repository and folder from the Metadata page.

### Unpublished Datasets
Other datasets on Ocean Watch are "unpublished" are are not accessible on Resource Watch's public data catalog. While these datasets are stored on Resource Watch, they are specific to the Ocean Watch data narrative and are often tabular data. These datasets are "unpublished" becuased they do not serve the needs of the general Resource Watch user. To learn more about unpublished datasets, refer to this repository (`ocean-watch-data/datasets`). Specific datasets can also be accessed from Ocean Watch. Click the "i" button on the upper right hand corner of any of the relevant data assets and find a link to learn more about the data.

## Uploading datasets
For the data work flow to upload and publish a dataset on Resource Watch for use on Ocean Watch, refer to the [Resource Watch Data Workflow Manual](https://docs.google.com/document/d/1DiBLbbQ25L2lx7aopUWJp-6hSaA4aFaWi9yRch_9ub0/edit#). For datasets that will not be published in the public catalog, there are a few exceptions. 
### Document Data
Key metadata information for unpublished datasets is documented in this repository. Create a new folder named `unique id_title`. Copy the [`template`](template.md) and fill in the key information. 
### Prepare Data
The Ocean Watch Data team is responsible for processing, cleaning, and reformating data to allow proper visualization and/or widget creation. All data workflows should be reproducible to enable regular updates. Notebooks containing workflows and python scripts are stored in the relevant dataset folder and cataloged in the folder's `README.md`.
### Visualize Data	
After the dataset has been connected to Resource Watch the dataset will be visualized as a layer, a widget, or both. This depends on how the dataset fits into the Ocean Watch data narrative. If the dataset will be visualized in a map, create layers according to the [Resource Watch Data Workflow Manual](https://docs.google.com/document/d/1DiBLbbQ25L2lx7aopUWJp-6hSaA4aFaWi9yRch_9ub0/edit#). Since many of the unpublished datasets are tabular, they will not have layers. The visualizing step of the RW data workflow can be skipped.
### Analyze Data
If the dataset will be analyzed and visualized in a widget do not use the default widget editor. Instead, follow the information in the [`widgets` folder](../widgets/)

## Updating datasets
Datasets on Ocean Watch should be evaluated at least twice a year to ensure the assets are kept up-to-date. Refer to the `Latest Check` and `Last Update` columns of the [RW Data Tracking Spreadsheet](https://docs.google.com/spreadsheets/d/1A3RbymgsB5bwljFsL20Brj-M29as0m2yPCAoAK25N6k/edit#gid=0). Evaluate all datasets with `Ocean Watch` in `Project` column. If you determine a dataset needs to be updated, refer to the `Update Strategy` column and complete the necessary workflow. Once a dataset has been updated, update the `Latest Check` and `Last Update` columns.
_note: many of the Ocean Watch datasets have not been updated since the launch of the site in November 2021. The first update will likely uncover bugs in workflows and scripts that were written an run on the authors local machine_

## Generating a catalog of datasets on Ocean Watch 
Run the `get_datasets.py` script to generate a list of all the datasets that are currently used on Ocean Watch.