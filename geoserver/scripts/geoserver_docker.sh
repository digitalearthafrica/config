#!/bin/bash
#
# GeoServer config docker wrapper. Use ENV vars to pass parameters to 
# GeoServer config script.
#----------------------------------------------------------------------

#######################################################################
## Functions
#######################################################################
function clean_exit() {
  exit_value=${1}
  exit_message="${2}"  

  if [ "${exit_message}" != "" ] ; then
    echo "${exit_message}"
  fi

  exit ${exit_value}
}

#######################################################################
## Script begins
#######################################################################
# Initialize
version="1.0"
scriptname=`basename "$0"`

geoserver_config_script="/opt/dea-geoserver/scripts/geoserver_config.sh"
geoserver_data_dir="/opt/dea-geoserver/config/geoserver/geoserver_data"
geoserver_scripts_dir="/opt/dea-geoserver/scripts"
username="${GEOSERVER_ADMIN_USER}"
password="${GEOSERVER_ADMIN_PASSWORD}"
collection_list="${GEOSERVER_COLLECTION_LIST}"
geoserver_url="${GEOSERVER_DOMAIN}/geoserver/rest"
geoserver_env_inventory="${geoserver_data_dir}/inventory/${GEOSERVER_ENV}/inventory.json"

if ! [ -f ${geoserver_env_inventory} ] ; then
  clean_exit 1 "GeoServer inventory file not found: ${geoserver_env_inventory}"
fi

for collection in $(cat ${geoserver_env_inventory} | jq -r '.[]') ; do
  if [ "${collection_list}" == "" ] ; then
    collection_list=${collection}
  else
    collection_list=${collection_list},${collection}
  fi
done

if [ "${collection_list}" == "" ] ; then
  clean_exit 2 "Invalid collection list."
fi

${geoserver_config_script} -g -u ${username} -p ${password} -r ${geoserver_url} -d ${geoserver_data_dir} -s ${geoserver_scripts_dir} -c ${collection_list} update

clean_exit $?