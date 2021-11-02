# Digital Earth Africa Config
Config files for Digital Earth Africa datacube and associated applications

[![OWS Configuration Test and Build](https://github.com/digitalearthafrica/config/actions/workflows/ows-config-test-build.yaml/badge.svg)](https://github.com/digitalearthafrica/config/actions/workflows/ows-config-test-build.yaml)
![Terria catalog Linting](https://github.com/digitalearthafrica/config/workflows/Terria%20catalog%20Linting/badge.svg)
[![Check Product Lists](https://github.com/digitalearthafrica/config/actions/workflows/product-lists-test.yaml/badge.svg)](https://github.com/digitalearthafrica/config/actions/workflows/product-lists-test.yaml)

Changes to this repo will generate a new docker image that includes the config files. Changes will be tagged as an unstable build.
To release to production, create a git tag for the current code and a stable version will be created using that value.

## Pull Request Template
There are three pull request Templates available for the following changes:
- ows config changes (ows_cfg.md)
- terria json changes (terria.md)
- product yaml file changes (product.md)

To access the PR templates
- open up a new pull request page and add `&template=ows_cfg.md`, `&template=terria.md` or `&template=product.md` at the end of the url

for example https://github.com/digitalearthafrica/config/compare/ows-fix-depreciated?expand=1&template=ows_cfg.md

## Formatting for Terria Data Description section in `ows_cfg.py`
#### Bold
```
**Overview**
```
#### Italic
```
*Overview*
```

## Process for updating OWS
Prod and dev config files are titled accordingly. Note any `/services` additions must be reflected in the corresponding `/inventory` json.
 - Edit the appropriate files
 - Merge changes into `/master` branch via a PR
 - Run the appropriate (prod, dev) `ows-update` workflow (external to this repository)
 - Update the translation: https://poeditor.com/join/project?hash=Iciv4SqUeH
 - Confirm correct deployment to OWS by inspecting the relevant OWS URLs and/or importing them to Terria using the 'My Data' option in the catalogue.
     - Dev: https://ows.dev.digitalearth.africa/
     - Unstable prod: https://ows-latest.digitalearth.africa/ 
 - Merge with stable prod by releasing a tagged version
 - Access stable prod via https://ows.digitalearth.africa/
