# Digital Earth Africa GeoServer Config
This directory contains scripts and config files used for the management of Digital Earth Africa GeoServer application configuration.

GeoServer config is managed through the GeoServer REST API. See references below for more information.

- [GeoServer Documentation](https://docs.geoserver.org/)
- [GeoServer REST API](https://docs.geoserver.org/stable/en/user/rest/)

## Scripts
- `geoserver-api.sh`: Script used to create, update and query individual GeoServer objects through the GeoServer REST API.
- `geoserver-config.sh`: Wrapper script to list or update all objects using geoserver-api.sh
- `geoserver-docker.sh`: Docker wrapper script to call geoserver-config.sh. 

## GeoServer Configuration
### Directory Structure
Configuration is saved in `geoserver_data` in the directories listed below. All config files are in JSON format.

- `collections`: This directory contains a collection of GeoServer objects.
- `global`: Contains the following GeoServer global settings: general settings, contact information, service configuration and logging settings. The gloabl settings are split by environment.
- `inventory`: Contains a directory and `invertory.json` per environment. The `inventory.json` lists all the active collections for the environment.

### Collection Structure
Collections are groupings of GeoServer objects and can include the following GeoServer objects:
- Workspaces
- Data stores
- Styles
- Feature types
- Layers
- Layer groups

### Config Change Deployment
The deployment of the changes to GeoServer config files are managed through two GitHub workflow actions:
1. Dev action: Triggered when a PR is created for changes in `geoserver_data`
2. Prod action: Triggered when a PR is merged to master that includes changes in `geoserver_data`

GeoServer REST API credentials are stored in the repo secrets.

### Change Steps
Follow the steps below to apply new collections, objects or current configuration changes.
1. Create a branch from master.
2. Push changes to the new branch.
3. Create a pull request -> This will apply the config to Dev.
4. Merge branch to master -> This will apply the config to Prod.
