#!/bin/bash --login
set -e

# Clone git repo
cd /opt/dea-geoserver
git clone https://github.com/digitalearthafrica/config.git
cd config
git checkout origin/add-geoserver-config

exec "$@"