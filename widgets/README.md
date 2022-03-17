# Ocean Watch Widgets
This section of the repository contains the workflows, processing scripts, and Vega configurations used to create the custom chart widgets on [Ocean Watch](https://oceanwatchdata.org). This repository _only_ contains information regarding the chart-type widgets on Ocean Watch. For more information on chart and map widgets, see the [wiki]
(../wiki)

# Directory sturcture
Each chart widget on Ocean Watch has its own sub-directory here. They sub-directories names start with the wri_id of the underlying dataset, unless additional post-processing was required (to generate a new dataset). In both cases, the sub0directory name also reflects te name of the data table or asset used to create the widget. Inside you'll find a `README` describing the contents of the sub-directory as well as metadata. Inside most sub-directories is a notebook describing the workflow required to create the `widgetConfig`. In some cases, additional post-processing transformation of the underlying dataset was required. This transforamtion occured after the initial pre-processing required for the creation of the dataset. If this is the case, inside these sub-directories, you'll find any preprocessing scripts and workflow notebooks used for post-processing transformations.

## Generating a catalog of datasets on Ocean Watch 
Run the [`get_widgets.py`](get_widgets.py) script to generate a list of all the datasets that are currently used on Ocean Watch.