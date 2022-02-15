# Ocean Watch Indicators
[Ocean Watch](https://oceanwatchdata.org) provides indicators at the global and country level. These include high level indicators featured in the top pane on the introduction page and country profiles, as well as the ranks and indicator values in the "Value of Coastal Ecosystems" section.

## List of Indicators
The Ocean Watch Data Team can find a list of all indicator values from Ocean Watch on Sharepoint
[`Sustainable Ocean Initiative\Documents\Ocean Watch\Development\Data\Indicator Tracking`](https://onewri.sharepoint.com/sites/WRI_ocean/Shared%20Documents/Ocean%20Watch/Development/Data/Indicator%20Tracking%20Sheet.xlsx)

## About Indicators
In general, indicators are generated by querying [Ocean Watch datasets](../datasets/) using the [Carto API](https://carto.com/developers/sql-api/). Queries are parameterized so that a corresponding geostore indentifier can be inserted based on the page where the `query` is called. Queries are stored in the [Ocean Watch json file](https://github.com/resource-watch/resource-watch/blob/develop/public/static/data/ocean-watch.json). Additional paramaters in the json specify the `format`, `unit`, and `description` for each indicator. Due to ease of testing, many queries return a formatted number and omit the formating paramater in the json. 

```javascript
{
    "description": "Average proportion of biodiversity hotspots within protected areas",
    "query": "https://wri-rw.carto.com/api/v2/sql?q=SELECT ROUND(value) AS value FROM ocn_024a_rw0_key_biodiversity_area_protection INNER JOIN ow_aliasing_countries AS alias ON alias.alias = geoareaname INNER JOIN gadm36_0 gadm ON alias.iso = gadm.gid_0 WHERE timeperiod = 2020 AND gadm.{{geostore_env}} ILIKE '{{geostore_id}}'",
    "unit": "%"
}
```
## Creating Queries
Indicators are queried from underlying Ocean Watch and Resource Watch datasets stored on Carto using SQL `SELECT` statements. All SQL statements can and should be built and tested in Carto (on the page for a data table, flip switch from "Metadata" to "SQL"). Also note that SQL queries below are written with tabs and newlines for readability, but what gets entered into the json needs to be one long, unbroken string, with all items/words separated only by spaces.
### Components
There are two components that must be present in the SQL statement: (1) the `value` (2) the geostore identifier. Once you SQL statement has the componenets, it is ready to be tested and converted into a query.

#### Value
The `value` is the numerical value produced by the query. It should correspond to the description of the indicator decided by the Ocean Watch Team. For example, the Biodiversity Protection indicator: 
```
"description": "Average proportion of biodiversity hotspots within protected areas"
```
In the SQL statement, the data should be transformed (if necessary). Once the data have been transformed, the final result should be set to `value` using `AS value` in the `SELECT` statement. If this variable is set to another name, it will not be recognized by the application. 
```sql 
SELECT ROUND(value) AS value FROM ocn_024a_rw0_key_biodiversity_area_protection
```
#### Geostore Identifier
The SQL statement must be parameterized so a geostore indentifier can be inserted. The application will replace this parameter with the geostore identifier of the corresponding country. Thus the queries must include `WHERE {{geostore_env}} = "{{geostore_id}}"`. `geostore_env` refers to the environment, either `geostore_staging` or `geostore_prod`. `geostore_id` refers to the unique 32 alphanumeric code for a country in the geostore. 

### Join the gadm table
Most datasets will not have the `geostore_staging` and `geostore_prod` columns. It is necessary to link these columns from the [`gadm36_0` table](https://resourcewatch.carto.com/u/wri-rw/dataset/gadm36_0) using a `JOIN` statement.
```sql
INNER JOIN gadm36_0 gadm ON data.{{iso_field}} = gadm.gid_0
```
In this case, the query pulls columns from the gadm table and attaches the rows of the table that same 3-letter ISO code with rows in the dataset.

### Join the aliasing table
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

## Test the SQL statement
When testing SQL statement, it will not execute with `WHERE {{geostore_env}} = "{{geostore_id}}"`. Swap out these parameters for an environment and identifier when testing

```sql	
SELECT ROUND(value) AS value FROM ocn_024a_rw0_key_biodiversity_area_protection 
INNER JOIN ow_aliasing_countries AS alias ON alias.alias = geoareaname 
INNER JOIN gadm36_0 gadm ON alias.iso = gadm.gid_0 
WHERE timeperiod = 2020 AND gadm.geostore_prod ILIKE '9bc50cce7f5b6ebd0452a3b839708ba9'
```
## Test the query
Once you have written the appropriate SQL statement, you will use the statement to query the Carto API. To do this, simply add the pre-fix url `https://wri-rw.carto.com/api/v2/sql?q=` infront of your query. Remember, the query passed to the API will not be executable without the geostore identifier being inserted, so keep these parameters swapped for actual values.

```sql
https://wri-rw.carto.com/api/v2/sql?q=SELECT ROUND(value) AS value FROM ocn_024a_rw0_key_biodiversity_area_protection INNER JOIN ow_aliasing_countries AS alias ON alias.alias = geoareaname INNER JOIN gadm36_0 gadm ON alias.iso = gadm.gid_0 WHERE timeperiod = 2020 AND gadm.geostore_prod ILIKE '9bc50cce7f5b6ebd0452a3b839708ba9'
```

Copy and paste the complete query url into your browser. If the result is as expected, swap the environemnt and the geostore identifier back to the parameterized versions

```sql
https://wri-rw.carto.com/api/v2/sql?q=SELECT ROUND(value) AS value FROM ocn_024a_rw0_key_biodiversity_area_protection INNER JOIN ow_aliasing_countries AS alias ON alias.alias = geoareaname INNER JOIN gadm36_0 gadm ON alias.iso = gadm.gid_0 WHERE timeperiod = 2020 AND gadm.{{geostore_env}} ILIKE '{{geostore_id}}'
```

## Update the Ocean Watch json
Indicators are stored in the [Ocean Watch json file](https://github.com/resource-watch/resource-watch/blob/develop/public/static/data/ocean-watch.json). To update or change a indicator you will need to edit this file. You can do this on Github browser by pressing the pencil icon. You can edit the file directly in the browser, or copy the file content and edit in a text editor and then copy it back when you are finished.

In the `staging` component of the file, navigate to the section for the appropriate indicator. Replace the value of the `query` key with the query you have created. You may also change the `format` or `unit` values if needed. Once you have finished ediing the file, submit a pull request. The developers at Vizzuality will review your changes and merge them if there are no issues. After your changes have been merged, check the [staging site](https://staging.resourcewatch.org/dashboards/ocean-watch) on a few countries to verify the change performs as expected.

If the changes pass your inspection, you can make the same edits to the json in the `production` section and submit a pull request. 

## Indicator Updates
When the dataset underlying an indicator is updated, it is possible that the indicator will need to be updated as well.
<b/r>__Workflow example: Ocean Biodiversity__
1. Update underlying dataset, `ocn_024`. See the [dataset update workflow](../datasets/README.md) for more information.
2. Retrieve the existing query from the `country-profile` page in the `production` component of the [Ocean Watch json file](https://github.com/resource-watch/resource-watch/blob/develop/public/static/data/ocean-watch.json) (most reliable) or the [Indicator Tracking Sheet](https://onewri.sharepoint.com/sites/WRI_ocean/Shared%20Documents/Ocean%20Watch/Development/Data/Indicator%20Tracking%20Sheet.xlsx) (maintained manually).
```sql	
https://wri-rw.carto.com/api/v2/sql?q=SELECT ROUND(value) AS value FROM ocn_024a_rw0_key_biodiversity_area_protection INNER JOIN ow_aliasing_countries AS alias ON alias.alias = geoareaname INNER JOIN gadm36_0 gadm ON alias.iso = gadm.gid_0 WHERE timeperiod = 2020 AND gadm.{{geostore_env}} ILIKE '{{geostore_id}}'
```
3. Edit the SQL statement to reflect the udpated dataset. Here we change `timeperiod = 2021`.
```sql	
SELECT ROUND(value) AS value FROM ocn_024a_rw0_key_biodiversity_area_protection 
INNER JOIN ow_aliasing_countries AS alias ON alias.alias = geoareaname 
INNER JOIN gadm36_0 gadm ON alias.iso = gadm.gid_0 
WHERE timeperiod = 2021 AND gadm.geostore_prod ILIKE '9bc50cce7f5b6ebd0452a3b839708ba9'
```
Follow the directions above to (4) __test the SQL statement__, (5) __test the query__, and (6) __update the Ocean Watch json__. 

## Generating list indicators 
To create an up-to-date list of all the indicators on Ocean Watch, their queries, and other values use the [`get_indicators` script](get_indicators.py). 