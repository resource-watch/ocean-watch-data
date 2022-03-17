# ocean-watch-data
[Ocean Watch](https://oceanwatchdata.org) is a custom static [dashboard](https://resource-watch.github.io/doc-api/reference.html#dashboard) on Resource Watch featuring ocean-data resources. 

This repository contains code related documentation for dataset proccessing, analysis, and visualization of resources managed by the Ocean Watch data team. This repository focuses on the resources that require data-processing: [`datasets`](datasets/), [`widgets`](widgets/), and [`indicators`](indicators/). For information on all resources on Ocean Watch as well as how they can be viewed, created, and updated, please see the [wiki](../../wiki/). Each of the resource types covered in this repository has its own directory. Inside you'll find a sub-directory for each indivdiual resource - whether a dataset or a widget - with metadata and pre-processing materials. 

_Note: Because Ocean Watch is a custom page on Resource Watch, it also utilizes some existing resources (mostly datasets) managed by the Resource Watch Data Team. Information about these resources can be found in the [Resource Watch repository](https://github.com/resource-watch)._

## A note on links
When referencing other files in the contents of this repository, we use relative links. If the repository is cloned, these links will point to the local files. When viewing in the github browser, these links must be clicked directly (rather than a right click to open in a new tab).  The relative links seem to fuction consistently in markdown files; however, the relative links in ipython notebooks render unreliably. If a link does not direct you as expected, we suggest you inspect the link and navigate to the appropriate file in the repository content tree.
