#!/bin/bash --login
set -e

REPO_URL="https://github.com/digitalearthafrica/config.git"

# Clone git repo
echo "Cloning repo ${REPO_URL}"

cd /opt/dea-geoserver
git clone ${REPO_URL}
cd config
echo "Setting branch to ${GEOSERVER_CONFIG_GIT_BRANCH}"

git checkout ${GEOSERVER_CONFIG_GIT_BRANCH}

exec "$@"