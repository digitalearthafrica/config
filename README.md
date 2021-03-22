# Digital Earth Africa Config
Config files for Digital Earth Africa datacube and associated applications

![Docker Image CI](https://github.com/digitalearthafrica/config/workflows/Docker%20Image%20CI/badge.svg)
![Terria catalog Linting](https://github.com/digitalearthafrica/config/workflows/Terria%20catalog%20Linting/badge.svg)

Changes to this repo will generate a new docker image that includes the config files,

changes will be tagged as an unstable build, to release to production create a git tag for the current code and a stable version will be created using that value

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