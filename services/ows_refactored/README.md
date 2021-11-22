# OWS CFG refactored
Goal: Split mega single file ows_cfg.py into multiple manageable/maintainable config files.

## Structure
### Root config
This file will act as an assembler which include all the layers required for the ows service. `ows_root_cfg.py`

### Resuable
- legend definition
- resource limit definition
- custom functions

### Deployment groups
- prod-af -> africa prod af-south-1 region
- dev-af -> africa dev deployment in af-south-1 region

### Best practices
#### Individual style
each style definition for layers is to be declared following naming convention `style_*`

#### Grouping of styles
Some layers share common style definitions and in the configuration file they should be declared following naming convention `styles_*`

#### Bands
each product's bands definition is to be declared following naming convention `bands_*`

#### Abstract
if several layers have long abstract move them to `abstract_*_cfg.py` and declared following naming convention `abstract_*`

### Resource limit
any unique resource limiting configuration should be declared in `ows_reslim_cfg.py` and be declared following naming convention `reslim_*`

#### Common legend definition
reusable legend definition should be declared in `ows_legend_cfg.py` and be declared following naming convention `legend_*`

#### Time resolution
Optional argument that prevents data-loading issues in Terria for layer definitions where the data has temporal resolution greater than a day (for example, annual/semiannual products). Annual products typically use `"time_resolution": "year",` and semiannual products `"time_resolution": "month",`.