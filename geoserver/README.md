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

## GeoServer Data Copy
As an interim solution, data is copied directly to a persistent volume mounted to the GeoServer container. The source data is stored in the deafrica-services S3 bucket linked to the PDS account.

### Data Copy Process
Data can be copied to GeoServer by running `geoserver-data-copy-run.sh` from a local docker environment. The script will use the datakube-tools image to download files from S3 storage and upload to GeoServer.

Script usage:
```
Usage: geoserver-data-copy-run.sh [OPTIONS]

GeoServer data copy script.

Options:
  -c, --cluster         EKS cluster name
  -s, --source-s3-uri   S3 URI for the S3 data source. E.g.: s3://deafrica-services/coastlines/v0.4.0
  -t, --target-dir      Target directory on the GeoServer container
  -u, --username        Basic auth user

Authentication environment variables:
  AWS_ACCESS_KEY_ID          AWS access key
  AWS_SECRET_ACCESS_KEY      AWS secret key
  AWS_DEFAULT_REGION         Default AWS region - Optional

```

Example:

```
./geoserver-data-copy-run.sh -c deafrica-dev-eks -s s3://deafrica-services/coastlines/v0.4.0/WGS84_SHP/ -t /opt/geoserver/data_dir/coastlines/v0.4.0
```