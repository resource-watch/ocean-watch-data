# Ocean Watch Widgets
This section of the repository contains the workflows, processing scripts, and Vega configurations used to create the custom chart widgets on [Ocean Watch](https://oceanwatchdata.org). This repository _only_ contains information regarding the chart-type widgets on Ocean Watch. Map-type widgets are (mostly) created and maintained by Vizzuality.

## Catalog of widgets
A catalog of all widgets (charts and maps) can be found on SharePoint[`Sustainable Ocean Initiative\Documents\Ocean Watch\Development\Data\Dataset Tracking`](https://onewri.sharepoint.com/sites/WRI_ocean/Shared%20Documents/Ocean%20Watch/Development/Data/Widget%20Tracking%20Sheet.xlsx)

## What is a widget?
A widget is a visual specification of how to style and render the data of a dataset (think pie, bar or line charts). Each widget is associated with a single dataset on the Resource Watch API. You can represent the same data in different ways by creating different widgets for the same dataset. [Widgets](https://resource-watch.github.io/doc-api/concepts.html#widget) are well documented in the RW API documentation. 

## Vega
Widgets are rendered using a widget condifuration (`widgetConfig`). The standard approach for building widget configuration objects uses Vega grammar.
The RW API does not apply any restriction to the data saved in the widget configuration field (widgetConfig). This allows for a very high level of flexibility but has the downside of making it harder to document how to use widgets. It is recommended that you take a look at the API documentation section about [Widget consiguration using vega grammar](https://resource-watch.github.io/doc-api/concepts.html#widget-configuration-using-vega-grammar) as well as the [Vega documention](https://vega.github.io/vega/docs/).  

## Creating the widgetConfig paramter
The widgetConfiguration is a JSON specification that controls the rendering of a widget. It is usually written using a [Vega Specification](https://vega.github.io/vega/docs/specification/) Creating a widgetConfig is a free-form process. It is easiest to start with an existing widgetConfig instead of creating one from sratch.

### Getting an existing widgetConfig
There are several sources of example widget configs.

1. __From an Ocean Watch chart widget__: To get the widget config of an existing widget, get the widget alpha-numeric API ID. You can get the widget ID from the catalog/tracking sheet mentioned above. You can also click on the `share` button on the widget on the OW page to generate a shareable link. Copy and paste the bit.ly link into your browser to reveal the widget ID in the URL. You can get the body of a widget (including the `widgetConfig`) by querying the RW API at https://api.resourcewatch.org/v1/widget/{{widget_id}}. 
_Note: We recomened installing a  JSONson viewer [like this one](https://chrome.google.com/webstore/detail/jsonvue/chklaanhfefbnpoihckbnefhakgolnmc), so you can easily view and copy components of a JSON file. Use a JSON formatter [like this one](https://jsonformatter.org/) to keep the parsed formatting of the the `widgetConfig`_

2. __From a Vega example__: Vega has tons of [examples](https://vega.github.io/vega/examples/) of JSON specifications that can be used as `widgetConfigs`. Click on the one you like, and copy the specification or open it in the "Online Vega Editor." 

3. __From the Widget Editor__: The [Widget Editor]() was created by Vizzuality to explore datasets and create customizable widgets. All of the documentation is stored inside the `widget-editor` [wiki](https://github.com/Vizzuality/widget-editor/wiki/Widget-editor). You can use the default dataset to create a widget that closely matches your intended vizualization. Then switch to "Advanced" mode to see the Vega JSON specification. 

### Editing the widgetConfig
There are also several options of tools you can use to edit and view a widget specification before creating the final version on Resource Watch. In this section, we will explain the recomended workflow. 

#### Develop in the Vega Editor
__Setup__
The [Online Vega Editor](https://vega.github.io/editor/#/) is a great tool to test your specification. In the pane in the lower right you can access error logs, a data viewer, and a signal viewer. These features make the Vega editor a great tool for developing and debugging your `widgetConfig`. The Widget Editor on Resource Watch has default [config](https://vega.github.io/vega/docs/config/) properties to match charts to the Resource Watch "styling". These defaults are different than those of the Vega Editor. To change the default configuration, copy and paste this specification into the `CONFIG` tab in the upper left. 
``` JSON
{
  "range": {
    "dotSize": [20, 250],
    "category20": [
      "#3BB2D0",
      "#2C75B0",
      "#FAB72E",
      "#EF4848",
      "#65B60D",
      "#C32D7B",
      "#F577B9",
      "#5FD2B8",
      "#F1800F",
      "#9F1C00",
      "#A5E9E3",
      "#B9D765",
      "#393F44",
      "#CACCD0",
      "#717171"
    ],
    "ordinal": { "scheme": "greens" },
    "ramp": { "scheme": "purples" }
  },
  "axis": {
    "labelFontSize": 13,
    "labelFont": "Lato",
    "labelColor": "#717171",
    "labelPadding": 10,
    "ticks": true,
    "tickSize": 8,
    "tickColor": "#A9ABAD",
    "tickOpacity": 0.5,
    "tickExtra": false
  },
  "axisX": {
    "bandPosition": 0.5,
    "domainWidth": 1.2,
    "domainColor": "#A9ABAD",
    "labelAlign": "center",
    "labelBaseline": "top"
  },
  "axisY": {
    "domain": false,
    "labelAlign": "left",
    "labelBaseline": "bottom",
    "tickOpacity": 0.5,
    "grid": true,
    "ticks": false,
    "gridColor": "#A9ABAD",
    "gridOpacity": 0.5
  },
  "mark": {
    "fill": "#3BB2D0"
  },
  "symbol": {
    "fill": "#3BB2D0",
    "stroke": "#fff"
  },
  "rect": {
    "fill": "#3BB2D0"
  },
  "line": {
    "interpolate": "linear",
    "stroke": "#3BB2D0",
    "fillOpacity": 0
  }
}
```
_A note on fonts: The Resource Watch Widget Editor uses the default font "Lato". This font renders differently (and very unappealingly) in the Vega Editor. Don't worry -- you will see it looks much better in the Widget Editor. Its recomended to use the "Lato" font to maintain consistent styling. The Widget Editor only specifies "Lato" as default in the `["axis"]["labelFont"]`. It is recomended to manually set all text to "Lato". This includes `["axes"]["titleFont"]`, `["legends"]["titleFont"]`, `["legends"]["labelFont"]`._

__Load data__
Once you have copied an existing specification and the `CONFIG` into the Vega Editor, you can adjust the specification to read and render the new data.

You can paste the exisiting specification into the `VEGA` tab and edit it directly (once you change the data, this will produce lots of errors until all column and variable names are fixed), or you can build the new specification from scratch, using the existing specification as a guide. 

To pull in the new data, you will need to edit the [`data`](https://vega.github.io/vega/docs/data/) properies. Load the dataset using the `url` property. We use a call to the [Carto's SQL API](https://carto.com/developers/sql-api/). It is helpful to at least partially transform the data with your `SELECT` statement. Here's and example:
```js
[
  {
    "name": "effort_table",
    "url": "https://wri-rw.carto.com/api/v2/sql?q=SELECT year, SUM(value::NUMERIC) AS effort FROM com_030d_fishing_effort_by_zone AS data WHERE year <= 2021 AND year >= 2017 GROUP BY year ORDER BY year ASC",
    "format": {
      "type": "json",
      "property": "rows"
    },
    "transform": [...]
  }
]
```

__Parameterization__
 To pull data for the correct page, Ocean Watch widgets are "parameterized." This means there is a placeholder in the url for the API call. Please refer to the `ocean-watch-data` [`README`](../README.md) for information on how to parameterize queries. It is recomended to build the specification using a url that loads data for a specific geostore identifier. Test the specification with a multiple different identifiers. Once you have finalized the specification and are ready to create the widget on Resource Watch, swap in the `{{geostore_env}}` and `{{geostore_id}}` placeholders.

__Create Specification__
After loading the data, you can inspect it in the Data Viewer tab. Perform any additional transformations using the [`transform`](https://vega.github.io/vega/docs/transforms/) property. Now you are ready to add or edit the rest of the properties including [`scales`](https://vega.github.io/vega/docs/scales/), [`axes`](https://vega.github.io/vega/docs/axes/), [`marks`](https://vega.github.io/vega/docs/marks/), [`legends`](https://vega.github.io/vega/docs/legends/), and [`singals`](https://vega.github.io/vega/docs/signals/).

_A note on tooltips: While the Resource Watch Widget Editor can display the [Vega tooltip](https://vega.github.io/vega-tooltip/vega-examples.html) it renders rather poorly. It is recomended to use the custom [Widget Editor tooltip](https://vega.github.io/vega-tooltip/vega-examples.html) to match the Resource Watch styling. Unfortunately this custom portion of the specification cannot be tested in the Vega Editor. It is recomended to use the Vega tooltip while developing and convert to the Widget Editor tooltip in the final stage of development (see below)_

__Sharing a design__: The Vega Editor allows you to share a rendering of your configuration. This can be useful for getting feedback on versions as you develop.

__Refine in the Widget Editor__:
Once you have your widgetConfiguration, you are ready to test and refine in the [Widget Editor](https://vizzuality.github.io/widget-editor/). Switch to "Advanced" mode, and copy and paste your specification. This will render the `widgetConfig` as it will appear on Resource Watch (if you encounter any differences, it may be becuase the version of `vega` used on Resource Watch is slightly behind the Widget Editor). It is recomended to change the tooltip to the Widget Editor custom tooltip and remove the Vega tooltip parameter (see above note). At this point, you can also remove the `width` and `height` properties, as those will get overwritten. If you are creating a parameterized widget, the final step will be to swap in the `{{geostore_env}}` and `{{geostore_id}}` placeholders in  `url` in the `data` property. Once you add the placeholders, the data cannot load and the specification will no longer render.

## Creating an advanced widget on Resource Watch
Once you have tested your `widgetConfig` in the Widget Editor (and paramterized the `data` url query if necessary), you are ready to ingest it into Resource Watch.

Although it is possible to create advanced widgets in the Resource Watch backoffice, it is more reliable and effcient to use the API. In this section you'll find information on the process of creating a widget in the RW API. Creating a widget is done using a POST request and passing the relevant data as body files. The Ocean/Resource Watch data team use the [advanced-widget-writer`](../../data-team-tools/advanced_widget_writer/) to create and edit widgets and their metadata. Refer to the [creating a widget](https://resource-watch.github.io/doc-api/reference.html#creating-a-widget) section of the RW API documentation for information on the `POST` request. [Reference information](https://resource-watch.github.io/doc-api/reference.html#widget-reference) about each of the supported body fields is also available in the API documentation. To create a new widget, use the [`advanced_chart_widget_create` script](../../data-team-tools/advanced_widget_writer/advanced_chart_widget_create.py) Fill in the fields, including the `widgetConfig`, the `title`, and the `description`. 

Titles appear at the top of the widget and the description appears on the back (when a user clicks the `i` button). Titles and description are written by the Ocean Watch Data team and reviewed by the WRI Communications team. Titles of widgets on Ocean Watch can be parameterized by adding the placeholder `{{geostore_country_name}}`. For example, 
```python
name = 'Contribution of blue food to protein supply in {{geostore_country_name}}'
``` 
After you run the script, it will return the id of the newly created widget.

## Creating widget metadata on Resource Watch
After you have created the widget, you can use the [`advanced_chart_widget_metadata_create` script](../../data-team-tools/advanced_widget_writer/advanced_chart_widget_metadata_create.py) to create metadata for the widget. Metadata fields inlcude `links` and a `caption`. 

The content of the `links` property depends on the type of underlying datasets. Always include a link to the source(s) website(s). Include a link to the Resource Watch explore page for any published datasets. Include a link to the dataset folder in github is the dataset is unpublished. If the widget is a chart widget, include a link to the widget folder in github. Use the below as an example.

``` js
"widgetLinks": [
        {"link":"https://land.copernicus.eu/global/products/lc","name":"Copernicus Land Cover"},
        {"link":"https://resourcewatch.org/data/explore/Global-Land-Cover-UN-FAO-LCCS-Classification","name":"Explore the underlying Land Cover data on Resource Watch",
        {"link":"https://github.com/resource-watch/ocean-watch-data/tree/main/datasets/ocn_calcs_016_land_cover_change","name":"Learn more about the dataset"},
        {"link":"https://github.com/resource-watch/ocean-watch-data/tree/main/widgets/soc_104_w3_urbanization","name":"How the data team created this widget"}
        ]
```

The `caption` appears at the bottom of the widget are usually omitted on Ocean Watch widgets.

## Editing Widgets 
To edit an existing widget or its metadata, the Ocean Watch data team uses the [`advanced_chart_widget_edit` script](../../data-team-tools/advanced_widget_writer/advanced_chart_widget_edit.py) and the [`advanced_chart_widget_metadata_edit` script](../../data-team-tools/advanced_widget_writer/advanced_chart_widget_metadata_edit.py) respectively. 

