# ocean-watch-data
[Ocean Watch](https://oceanwatchdata.org) is a custom static [dashboard](https://resource-watch.github.io/doc-api/reference.html#dashboard) on Resource Watch featuring ocean-data resources. 

This repository contains code related documentation for dataset proccessing, analysis, and visualization of resources managed by the Ocean Watch data team. This repository focuses on the resources that require data-processing: [`datasets`](datasets/), [`widgets`](widgets/), and [`indicators`](indicators/). To better understand the processing workflows in the repositiory, it is helpful to understand two key concepts: 
1. The Ocean Watch JSON
2. Resource Parameterization

_Note: Because Ocean Watch is a custom page on Resource Watch, it also utilizes some existing resources (mostly datasets) managed by the Resource Watch Data Team. Information about these resources can be found in the [Resource Watch repository](https://github.com/resource-watch)._

## The Ocean Watch JSON
Ocean Watch is a custom [dashboard](https://resource-watch.github.io/doc-api/reference.html#dashboard) on Resource Watch. The configuration of resources on the page is stored in a [JSON file](https://github.com/resource-watch/resource-watch/blob/develop/public/static/data/ocean-watch.json). 

### Resources
Resouce Watch API Resources: The majority of the resources on Ocean Watch are managed in the Resource Watch API, including [datasets](https://resource-watch.github.io/doc-api/concepts.html#dataset) and their assets - [layers](https://resource-watch.github.io/doc-api/concepts.html#layer) and [widgets](https://resource-watch.github.io/doc-api/concepts.html#widget). These resources are referenced using a unique API identifier. 

Non-API Resources: The JSON also directly stores additional resources not managed by the Resource Watch API, including `text`, `indicators`, and `mini-explore` maps.

### Configuration
The JSON file has a `staging` property and a `production` proporty. The properties and values in these two sections should be the same. These properties have the following format:
``` js
{
  "intro": {
    "indicators": [...],
    "steps": [...]
  },
  "country-profile": [
    [
      {
        "content": [...]
      }
    ],
    [
      {
        "title": "How is land based pollution generated?",
        "anchor": "how-is-land-based-pollution-generated",
        "anchorTitle": "Land-Based Pollution",
        "content": [...]
      }
    ],
    [
      {
        "title": "How do pollutants travel to the ocean?",
        "anchor": "how-do-pollutants-travel-to-the-ocean",
        "anchorTitle": "Movement of Ocean Pollutants",
        "content": [...]
      }
    ],
    [
      {
        "title": "How does pollution damage coastal ecosystems?",
        "anchor": "how-does-pollution-damage-coastal-ecosystems",
        "anchorTitle": "Effects of Coastal Pollution",
        "content": [...]
      }
    ],
    [
      {
        "title": "Why is the ocean so valuable?",
        "anchor": "why-is-the-ocean-so-valuable",
        "anchorTitle": "Value of Coastal Ecosystems",
        "content": [...]
      }
    ]
  ]
}

```
There is a configuration for the `intro` and`country-profile`. The `intro` page has global data while the `country-profile` page has country specific data. Country level data is loaded through "parameterization" (see below). Each page contains sections with a `content` property. The `content` includes a list of "blocks." Each block contains properities that describe the text and resources that will be loaded. 

### Updating the Ocean Watch JSON 
To update content on Ocean Watch. Changes will be made to the resources themselves, the JSON file, or both. Changes to the propoerties of a resources, such as updating a layer or editing a widget configuration can be made through the backoffice or the API, and do not require updating the JSON file. Changes to which resources are loaded on the page are "top-level" changes that require updating the JSON. Examples include editing text, adding a layer to a mini-explore map, or switching one chart widget for another.

The JSON file is managed by the Vizzuality development team. The Ocean Watch data team can edit the JSON by creating a fork, making the necessary edits to the file, commiting changes, and submitting a pull request. It is recomended to make any intial updates in the `staging` property first. Then review these changes in the [staging site](https://staging.resourcewatch.org/dashboards/ocean-watch). If the updates pass in `staging`, make the corresponding changes in the production property and submit a second pull request.

## Resource Parameterization 
The data behind the resources on Ocean Watch are "parameterized" inorder to load data for a specific region (global or country/territroy). This means there is a placeholder in a propoerty of the resource that loads the data. When a page is loaded, the property is then formatted to fill the placeholder with a name or geostore identifier which is associated with a coastal country or territory in the Ocean Watch [geostore](https://resource-watch.github.io/doc-api/concepts.html#geostore). When this placeholder is in a data query, the resource only loads data for referenced country or territory. To create a paramaterized query, follow the guidance below.

### Creating Parameterized Queries
Data are queried from underlying Ocean Watch and Resource Watch datasets stored on Carto using SQL `SELECT` statements. All SQL statements can and should be built and tested in Carto (on the page for a data table, flip switch from "Metadata" to "SQL"). Also note that SQL queries below are written with tabs and newlines for readability, but what gets entered into the json needs to be one long, unbroken string, with all items/words separated only by spaces.

#### Abbout the Geostore Identifier
The SQL statement must be parameterized so a geostore indentifier can be inserted into a "placeholder." The application will replace the placeholder with the geostore identifier of the corresponding country. Thus the queries must include `WHERE {{geostore_env}} = "{{geostore_id}}"`. `geostore_env` refers to the environment, either `geostore_staging` or `geostore_prod`. `geostore_id` refers to the unique 32 alphanumeric code for a country in the geostore. 

#### 1. Join the gadm table
Ocean Watch datasets will not have the `geostore_staging` and `geostore_prod` columns. These columns are only stored in the [`gadm36_0` table](https://resourcewatch.carto.com/u/wri-rw/dataset/gadm36_0). They are stored seperately, so any changes or updates to the geostore only neccessitate changing this table. When querying a dataset in a parameterized query, you need to link these `geostore_staging` and `geostore+prod` columns from the `gadm36_0` table using a `JOIN` statement.

```sql
INNER JOIN gadm36_0 gadm ON data.{{iso_field}} = gadm.gid_0
```
In this case, the query pulls columns from the gadm table and attaches the rows of the table that same 3-letter ISO code with rows in the dataset.

#### 2. Join the aliasing table
When the dataset does not have ISO codes, parameterization requires associating the underlying data with the appropriate ISO codes. This is accomplished by using an "aliasing" table, where each non-standard name for a given country is linked to its standard name and ISO code. For example, a dataset with an entry for South Korea referred to that country as "Korea South", which has no matches in the gadmm countries table. In this case "Korea South" is an alias for South Korea and its ISO code is "KOR". The [`ow_aliasing_countries` table](https://resourcewatch.carto.com/u/wri-rw/dataset/ow_aliasing_countries) is different than that for Resource Watch (Ocean Watch uses GADM countrys instead of Natural Earth). 

```sql 
SELECT ROUND(value) AS value FROM ocn_024a_rw0_key_biodiversity_area_protection
INNER JOIN ow_aliasing_countries AS alias ON alias.alias = data.geoname
INNER JOIN gadm36_0 gadm ON alias.iso = gadm.gid_0
```
When joining tables to the `gadm36_0` and/or the `ow_aliasing_countries` table, it is imporant to verify that all country rows were matched. This can be done using an SQL query. Carefully inspect any rows that were not joined, and add missing items to the aliasing table if relevnat.

```sql
SELECT geoareaname FROM ocn_024a_rw0_key_biodiversity_area_protection 
LEFT OUTER JOIN ow_aliasing_countries AS alias ON alias.alias = geoareaname 
WHERE alias.alias is NULL
```
Be careful not to add duplicate aliases to the table. This will result in duplicated rows in the query results. To check if there are duplicate aliases in the table, use the following SQL statement:

```sql
SELECT alias, COUNT(*)
FROM ow_aliasing_countries
GROUP BY alias
HAVING COUNT(*) > 1
```

#### 3. Test the SQL statement
When testing SQL statement, it will not execute with `WHERE {{geostore_env}} = "{{geostore_id}}"`. Swap out these parameters for an environment and identifier when testing

```sql	
SELECT ROUND(value) AS value FROM ocn_024a_rw0_key_biodiversity_area_protection 
INNER JOIN ow_aliasing_countries AS alias ON alias.alias = geoareaname 
INNER JOIN gadm36_0 gadm ON alias.iso = gadm.gid_0 
WHERE timeperiod = 2020 AND gadm.geostore_prod ILIKE '9bc50cce7f5b6ebd0452a3b839708ba9'
```
#### 4. Test the query
Once you have written the appropriate SQL statement, you will use the statement to query the Carto API. To do this, simply add the pre-fix url `https://wri-rw.carto.com/api/v2/sql?q=` infront of your query. Remember, the query passed to the API will not be executable without the geostore identifier being inserted, so keep these parameters swapped for actual values.

```sql
https://wri-rw.carto.com/api/v2/sql?q=SELECT ROUND(value) AS value FROM ocn_024a_rw0_key_biodiversity_area_protection INNER JOIN ow_aliasing_countries AS alias ON alias.alias = geoareaname INNER JOIN gadm36_0 gadm ON alias.iso = gadm.gid_0 WHERE timeperiod = 2020 AND gadm.geostore_prod ILIKE '9bc50cce7f5b6ebd0452a3b839708ba9'
```

Copy and paste the complete query url into your browser. If the result is as expected, swap the environemnt and the geostore identifier back to the parameterized versions

```sql
https://wri-rw.carto.com/api/v2/sql?q=SELECT ROUND(value) AS value FROM ocn_024a_rw0_key_biodiversity_area_protection INNER JOIN ow_aliasing_countries AS alias ON alias.alias = geoareaname INNER JOIN gadm36_0 gadm ON alias.iso = gadm.gid_0 WHERE timeperiod = 2020 AND gadm.{{geostore_env}} ILIKE '{{geostore_id}}'
```

## A note on links
When referencing other files in the contents of this repository, we use relative links. If the repository is cloned, these links will point to the local files. When viewing in the github browser, these links must be clicked directly (rather than a right click to open in a new tab).  The relative links seem to fuction consistently in markdown files; however, the relative links in ipython notebooks render unreliably. If a link does not direct you as expected, we suggest you inspect the link and navigate to the appropriate file in the repository content tree.

