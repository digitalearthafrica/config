# DE Africa Terria catalogue

The Terria catalogue is a list of all datasets available to users on the Digital Earth Africa Map https://maps.digitalearth.africa/. 
It is built from the `africa-prod.json` file.

## `africa-prod.json`

The Terria catalogue is generated as a `wms-group` based on the structure of `../services/ows_refactored/prod_af_ows_root_cfg.py`. 
Any product added to that root config file and released in a tagged version (i.e. in live production) will be visible to users of the Map portal. The Map portal will use the layer `title` and `abstract` as defined in the individual layer configs.

## Exclude layers 

Exclude layers from the Map portal Terria catalogue by adding the name of the layer to the `excludeMembers` list. An example of `excludeMembers` in use can be viewed in [this file](https://github.com/GeoscienceAustralia/dea-config/blob/master/dev/terria/terria-cube-v8.json).

## Are tagged versions required to see changes to `africa-prod.json`?

No. Changes to the `africa-prod.json` file itself do not require a tagged version to go live; for example adding or removing items from `excludeMembers`. Caution: changing the `wms-group` name is not recommended as it may cause all exisiting sharelinks to break.

However, any changes to files it builds from (such as the `prod_af_ows_root_cfg.py` file, or any layer definition in the `ows_refactored` folder) **do** require tagged releases to move from unstable prod to live prod.

## Superseded - `africa-prod-archived.json`

The pre-2022 manually defined Terria catalogue. It does not draw information from layer configs (for example `abstract` fields are missing and would have to be individually copied over and updated). It has not been updated with products past January 2022.