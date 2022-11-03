#!/bin/bash
#
# GeoServer REST API management script
#----------------------------------------------------------------------

#######################################################################
## Functions
#######################################################################
function usage() {
  echo
  echo "Usage: ${scriptname} [OPTIONS] COMMAND OBJECT_TYPE [OBJECT_NAME]"
  echo
  echo "GeoServer REST API management script."
  echo
  echo "Options:"
  echo "  -c, --collection  Configuration collection to process. This is usually the same as the workspace name."
  echo "  -d, --datadir     Override default data directory. Default: ./geoserver_data"
  echo "  -e, --environment Environment to use for applying global settings (dev/prod)"
  echo "  -p, --password    Basic auth password"
  echo "  -r  --resturl     REST API URL. E.g. http://localhost:8080/geoserver/rest"
  echo "  -s  --datastore   Datastore used to query featuretypes"
  echo "  -u, --username    Basic auth user"
  echo "  -w, --workspace   GeoServer workspace name"
  echo
  echo "Commands:"
  echo "  create        Create object"
  echo "  get           List object information"
  echo "  update        Update object"
  echo
  echo "Supported object types:"
  echo "  contact       Global contact information, get and update"
  echo "  datastores    Data store create, use with -w"
  echo "  featuretypes  GeoServer featuretypes/layers"
  echo "  layers        GeoServer layer confg"
  echo "  layergroups   GeoServer grouping of layers"
  echo "  logging       Logging settings"
  echo "  services      CSW,WMTS,WCS,WFS,WMS,WPS service settings, get and update"
  echo "  settings      Global server settings, get and update"  
  echo "  sld           Style layer descriptor, update"  
  echo "  styles        Style, create and get"
  echo "  workspaces    Workspace create, get and update"
  echo
  echo "Examples:"
  echo
  echo "List all workspaces:"
  echo "  ${scriptname} -c my_collection -u admin -p geoserver -r https://localhost/geoserver/rest get workspaces"
  echo
  echo "List one workspace:"
  echo "  ${scriptname} -c my_collection -u admin -p geoserver -r https://localhost/geoserver/rest get workspaces myworkspace"
  echo
  echo "Update SLD"
  echo "  ${scriptname} -c my_collection -u admin -p geoserver -r https://localhost/geoserver/rest update sld test_style"
  echo
}

function clean_exit() {
  exit_value=${1}
  exit_message="${2}"

  rm_file ${tmp_file}

  if [ "${exit_message}" != "" ] ; then
    echo "${exit_message}"
  fi

  exit ${exit_value}
}

function rm_file() {
  rm_filename="${1}"
  if [ -f "${rm_filename}" ] ; then
   rm "${rm_filename}"
  fi
}

# Style workspace
function get_style_workspace() {
  style="${1}"
  this_workspace=`cat ${collection_dir}/styles/${style}.json | jq -r '.style.workspace.name'`
  echo ${this_workspace}
}

# Datastore workspace
function get_datastore_workspace() {
  datastore="${1}"
  this_workspace=`cat ${collection_dir}/datastores/${datastore}.json | jq -r '.dataStore.workspace.name'`
  echo ${this_workspace}
}

# Featuretype workspace
function get_featuretype_workspace() {
  featuretype="${1}"
  this_workspace=`cat ${collection_dir}/featuretypes/${featuretype}.json | jq -r '.featureType.namespace.name'`
  echo ${this_workspace}
}

# Featuretype datastore
function get_featuretype_datastore() {
  featuretype="${1}"
  this_datastore=`cat ${collection_dir}/featuretypes/${featuretype}.json | jq -r '.featureType.store.name' | awk -F":" '{print $2}'`
  echo ${this_datastore}
}

# Layer workspace
function get_layer_workspace() {
  layer="${1}"
  this_workspace=`cat ${collection_dir}/layers/${layer}.json | jq -r '.layer.resource.name' | awk -F":" '{print $1}' 2>/dev/null`
  echo ${this_workspace}
}

# Layergroup workspace
function get_layergroup_workspace() {
  layergroup="${1}"
  this_workspace=`cat ${collection_dir}/layergroups/${layergroup}.json | jq -r '.layerGroup.workspace.name'`
  echo ${this_workspace}
}

#---------------------------------------------
# function create_object()
#---------------------------------------------
function create_object() {

  object_type=`echo "${1}" | awk '{print $1}'`
  object_name=`echo "${1}" | awk '{print $2}'`

  content_type="application/json"

  case "${object_type}" in
    datastores)
      data_file="${collection_dir}/datastores/${object_name}.json"
      if ! [ -f ${data_file} ] ; then
        clean_exit 11 "Data store json file not found: ${data_file}"
      fi
      datastore_workspace=$(get_datastore_workspace ${object_name})
      uri="/workspaces/${datastore_workspace}/datastores"      
      ;;
    featuretypes)
      data_file="${collection_dir}/featuretypes/${object_name}.json"
      if ! [ -f ${data_file} ] ; then
        clean_exit 12 "featuretype json file not found: ${data_file}"
      fi
      featuretype_workspace=$(get_featuretype_workspace ${object_name})
      featuretype_datastore=$(get_featuretype_datastore ${object_name})      
      uri="/workspaces/${featuretype_workspace}/datastores/${featuretype_datastore}/featuretypes"      
      ;;
    layers)      
      data_file="${collection_dir}/layers/${object_name}.json"
      if ! [ -f ${data_file} ] ; then
        clean_exit 13 "layer json file not found: ${data_file}"
      fi
      layer_workspace=$(get_layer_workspace ${object_name})
      uri="/workspaces/${layer_workspace}/layers/${object_name}.json"
      ;;
    layergroups)      
      data_file="${collection_dir}/layergroups/${object_name}.json"
      if ! [ -f ${data_file} ] ; then
        clean_exit 14 "layergroup json file not found: ${data_file}"
      fi
      layergroup_workspace=$(get_layergroup_workspace ${object_name})
      uri="/workspaces/${layergroup_workspace}/layergroups"
      ;;
    styles)
      uri="/styles"
      data_file="${collection_dir}/styles/${object_name}.json"
      if ! [ -f ${data_file} ] ; then
        clean_exit 15 "Style json file not found: ${data_file}"
      fi
      ;;
    workspaces)
      uri="/workspaces"
      data_file="${collection_dir}/workspaces/${object_name}.json"
      if ! [ -f ${data_file} ] ; then
        clean_exit 16 "Workspace json file not found: ${data_file}"
      fi
      ;;
    *)
      usage
      clean_exit 2 "Invalid object: '${object_type}'."
      ;;
  esac
  
  ${curl_bin} ${curl_verbose} ${curl_flags} -u ${username}:${password} -H "${content_type_header} ${content_type}" -d @"${data_file}" -XPOST ${resturl}${uri} -w '\n%{http_code}\n' > ${tmp_file} 2>&1
  ret_val=$?

  http_code=`tail -1 ${tmp_file}`

  if [ ${ret_val} -ne 0 ] || ! [[ "${http_code}" =~ ^2.* ]]; then
    echo "Create failed. HTTP code: ${http_code}"
    echo
    echo "Error output from the REST API:"
    cat ${tmp_file}
    echo
    clean_exit 3
  fi

  echo "Create successful."  

}

#---------------------------------------------
# function get_object()
#---------------------------------------------
function get_object() {

  object_type=`echo "${1}" | awk '{print $1}'`
  object_name=`echo "${1}" | awk '{print $2}'`

  case "${object_type}" in
    contact)
      uri="/settings/contact"
      ;;
    datastores)
      if [ -z "${workspace}" ] ; then
        clean_exit 20 "Workspace not provided."
      fi
      if [ -z "${object_name}" ] ; then
        uri="/workspaces/${workspace}/datastores"
      else
        uri="/workspaces/${workspace}/datastores/${object_name}"
      fi
      ;;
    featuretypes)
      if [ -z "${workspace}" ] ; then
        clean_exit 21 "Workspace not provided."
      fi
      if [ -z "${datastore}" ] ; then
        clean_exit 22 "Datastore not provided."
      fi
      if [ -z "${object_name}" ] ; then
        uri="/workspaces/${workspace}/datastores/${datastore}/featuretypes.json"
      else
        uri="/workspaces/${workspace}/datastores/${datastore}/featuretypes/${object_name}.json"
      fi
      ;;
    layers)
      if [ -z "${workspace}" ] ; then
        clean_exit 23 "Workspace not provided."
      fi
      if [ -z "${object_name}" ] ; then
        uri="/workspaces/${workspace}/layers.json"
      else
        uri="/workspaces/${workspace}/layers/${object_name}.json"
      fi
      ;;
    layergroups)
      if [ -z "${workspace}" ] ; then
        clean_exit 24 "Workspace not provided."
      fi
      if [ -z "${object_name}" ] ; then
        uri="/workspaces/${workspace}/layergroups.json"
      else
        uri="/workspaces/${workspace}/layergroups/${object_name}.json"
      fi
      ;;
    logging)
      uri="/logging"
      ;;
    services)
      uri="/services/${object_name}/settings"
      ;;
    settings)
      uri="/settings"
      ;;
    styles)      
      if ! [ -z "${workspace}" ] ; then
        uri="/workspaces/${workspace}/styles"
      else
        uri="/styles"
      fi

      if [ "${object_name}" != "" ] ; then
        uri="${uri}/${object_name}.json"
      fi
      ;;
    workspaces)
      uri="/workspaces"
      if [ "${object_name}" != "" ] ; then
        uri="${uri}/${object_name}"
      fi
      ;;
    *)
      usage
      clean_exit 2 "Invalid object: '${object_type}'."
  esac    
  
  ${curl_bin} ${curl_verbose} ${curl_flags} -u ${username}:${password} -XGET ${resturl}${uri} > ${tmp_file} 2>&1
  cat ${tmp_file} | jq > /dev/null 2>&1
  if [ $? -eq 0 ] ; then
    cat ${tmp_file} | jq
  else
    cat ${tmp_file}
  fi
  
}

#---------------------------------------------
# function update_object()
#---------------------------------------------
function update_object() {

  object_type=`echo "${1}" | awk '{print $1}'`
  object_name=`echo "${1}" | awk '{print $2}'`  
  
  content_type="application/json"

  case "${object_type}" in
    contact)
      uri="/settings/contact"
      data_file="${data_dir}/global/${geoserver_env}/contact.json"
      ;;
    datastores)
      if [ -z "${object_name}" ] ; then
        usage
        clean_exit 30 "No datastore provided."        
      fi
      data_file="${collection_dir}/datastores/${object_name}.json"
      if ! [ -f ${data_file} ] ; then
        clean_exit 31 "Data store json file not found: ${data_file}"
      fi
      datastore_workspace=$(get_datastore_workspace ${object_name})
      uri="/workspaces/${datastore_workspace}/datastores/${object_name}.json"
      ;;
    featuretypes)
      if [ -z "${object_name}" ] ; then
        usage
        clean_exit 32 "No featuretype provided."
      fi
      data_file="${collection_dir}/featuretypes/${object_name}.json"
      if ! [ -f ${data_file} ] ; then
        clean_exit 33 "Featuretype json file not found: ${data_file}"
      fi
      featuretype_workspace=$(get_featuretype_workspace ${object_name})
      featuretype_datastore=$(get_featuretype_datastore ${object_name})      
      uri="/workspaces/${featuretype_workspace}/datastores/${featuretype_datastore}/featuretypes/${object_name}.json"      
      ;;
    layers)
      if [ -z "${object_name}" ] ; then
        usage
        clean_exit 34 "No layer provided."
      fi
      data_file="${collection_dir}/layers/${object_name}.json"
      if ! [ -f ${data_file} ] ; then
        clean_exit 35 "layer json file not found: ${data_file}"
      fi
      layer_workspace=$(get_layer_workspace ${object_name})
      uri="/workspaces/${layer_workspace}/layers/${object_name}.json"
      ;;
    layergroups)
      if [ -z "${object_name}" ] ; then
        usage
        clean_exit 36 "No layergroup provided."
      fi
      data_file="${collection_dir}/layergroups/${object_name}.json"
      if ! [ -f ${data_file} ] ; then
        clean_exit 37 "layergroup json file not found: ${data_file}"
      fi
      layergroup_workspace=$(get_layergroup_workspace ${object_name})
      uri="/workspaces/${layergroup_workspace}/layergroups/${object_name}.json"      
      ;;
    logging)
      uri="/logging"
      data_file="${data_dir}/global/${geoserver_env}/logging.json"
      ;;
    services)
      if [ -z "${object_name}" ] ; then
        usage
        clean_exit 38 "No service provided."
      fi      
      data_file="${data_dir}/global/${geoserver_env}/services/${object_name}.json"
      if ! [ -f ${data_file} ] ; then
        clean_exit 39 "Service json file not found: ${data_file}"
      fi
      uri="/services/${object_name}/settings"      
      ;;
    settings)
      uri="/settings"
      data_file="${data_dir}/global/${geoserver_env}/settings.json"
      ;;
    sld)
      if [ -z "${object_name}" ] ; then
        usage
        clean_exit 40 "No sld name provided."
      fi
      data_file="${collection_dir}/styles/${object_name}.sld"
      content_type="application/vnd.ogc.sld+xml"
      if ! [ -f ${data_file} ] ; then
        clean_exit 41 "Style sld file not found: ${data_file}"
      fi
      style_workspace=$(get_style_workspace ${object_name})
      uri="/workspaces/${style_workspace}/styles/${object_name}.sld"      
    ;;
    workspaces)
      if [ -z "${object_name}" ] ; then
        usage
        clean_exit 42 "No workspace name provided."
      fi
      data_file="${collection_dir}/workspaces/${object_name}.json"
      if ! [ -f ${data_file} ] ; then
        clean_exit 43 "Workspace config file not found: ${data_file}"
      fi
      uri="/workspaces/${object_name}.json"      
      ;;
    *)
      usage
      clean_exit 2 "Invalid object: '${object_type}'."
  esac
  
  ${curl_bin} ${curl_verbose} ${curl_flags} -u ${username}:${password} -H "${content_type_header} ${content_type}" -d @"${data_file}" -XPUT ${resturl}${uri} -w '\n%{http_code}\n' > ${tmp_file} 2>&1
  ret_val=$?

  http_code=`tail -1 ${tmp_file}`

  if [ ${ret_val} -ne 0 ] || ! [[ "${http_code}" =~ ^2.* ]]; then
    echo "Update failed. HTTP code: ${http_code}"
    echo
    echo "Error output from the REST API:"
    cat ${tmp_file}
    echo
    clean_exit 3
  fi

  echo "Update successful."  

}

#######################################################################
## Script begins
#######################################################################
# Initialize
typeset -i setverbose=0
version="1.0"
scriptname=`basename "$0"`
curl_bin=`which curl`
jq_bin=`which jq`
curl_verbose=""
curl_flags="-s"
data_dir="../geoserver_data"
tmp_file="/tmp/$$.${scriptname}"
content_type_header="Content-type:"

if [ $# -eq 0 ] ; then
  usage
  clean_exit 1
fi

if [ -z "${curl_bin}" ] ; then
  clean_exit 1 "curl not found."
fi

if [ -z "${jq_bin}" ] ; then
  clean_exit 1 "jq not found."
fi

# Validate input
while [[ $# -gt 0 ]]; do
  case $1 in
    -c|--collection)
      collection="${2}"      
      shift
      shift
      ;;  
    -d|--datadir)
      data_dir="${2}"
      if ! [ -d "${data_dir}" ] ; then
        clean_exit 1 "Data directory not found: ${data_dir}"
      fi
      shift
      shift
      ;;
    -e|--environment)
      geoserver_env="${2}"
      shift
      shift
      ;;
    -p|--password)
      password="${2}"
      if [ -z "${password}" ] ; then
        usage
        clean_exit 1 "Invalid username."
      fi
      shift
      shift
      ;;
    -r|--resturl)
      resturl="${2}"
      if [ -z "${resturl}" ] || ! [[ ${resturl} =~ ^(http) ]]; then
        usage
        clean_exit 1 "Invalid url."
      fi
      shift
      shift
      ;;
    -s|--datastore)
      datastore="${2}"
      if [ -z "${datastore}" ] || [[ ${datastore} =~ ^- ]]; then
        usage
        clean_exit 1 "Invalid datastore."
      fi
      shift
      shift
      ;;
    -u|--username)
      username="${2}"
      if [ -z "${username}" ] || [[ ${username} =~ ^- ]]; then
        usage
        clean_exit 1 "Invalid username."
      fi
      shift
      shift
      ;;
    -v|--verbose)
      setverbose=1
      curl_verbose="-v"
      shift
      ;;
    -w|--workspace)
      workspace="${2}"
      if [ -z "${workspace}" ] || [[ ${workspace} =~ ^- ]] ; then
        usage
        clean_exit 1 "Invalid workspace name."
      fi
      shift
      shift
      ;;
    -h|--help)
      usage
      clean_exit 0
      ;;
    -*|--*)
      usage
      clean_exit 1 "Error: Unknown option $1"      
      ;;
    *)
      command="${1}"      
      shift
      break
      ;;
  esac
done

if [ -z "${username}" ] ; then
  usage
  clean_exit 1 "Username not specified."
fi

if [ -z "${password}" ] ; then
  usage
  clean_exit 1 "Password not specified."
fi

if [ -z "${resturl}" ] ; then
  usage
  clean_exit 1 "Rest URL not specified."
fi

if ! [ -z ${collection} ] ; then
  if ! [ -d "${data_dir}/collections/${collection}" ] ; then
    usage
    clean_exit 1 "Collection not found. ${data_dir}/collections/${collection}"
  else
    collection_dir=${data_dir}/collections/${collection}
  fi
fi

# Execute commands
case "${command}" in
  create)
    create_object "${1} ${2}"
    ;;
  get)
    get_object "${1} ${2}"
    ;;
  update)
    update_object "${1} ${2}"
    ;;
  *)
    usage
    clean_exit 1 "Invalid command."
    ;;
esac

clean_exit 0