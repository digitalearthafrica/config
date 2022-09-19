#!/bin/bash
#
# GeoServer config management through the GeoServer REST API script
#----------------------------------------------------------------------

#######################################################################
## Functions
#######################################################################
function usage() {
  echo
  echo "Usage: ${scriptname} [OPTIONS] COMMAND"
  echo
  echo "GeoServer config script."
  echo
  echo "Options:"
  echo "  -c, --collectionlist  Comma delimited list of collections to list or update"
  echo "  -g, --global          Update global settings and services"
  echo "  -p, --password        Basic auth password"
  echo "  -r, --resturl         REST API URL. E.g. http://localhost:8080/geoserver/rest"  
  echo "  -s, --scriptsdir      Set scripts directory if different from default: ./scripts"
  echo "  -u, --username        Basic auth user"
  echo
  echo "Commands:"
  echo "  list          List all configured objects"
  echo "  update        Update all configured objects"
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

# Datastore workspace
function get_datastore_workspace() {
  this_collection_datadir="${1}"
  this_datastore="${2}"
  this_workspace=`cat ${this_collection_datadir}/datastores/${this_datastore}.json | jq -r '.dataStore.workspace.name'`
  echo ${this_workspace}
}

# Style workspace
function get_style_workspace() {
  this_collection_datadir="${1}"
  this_style="${2}"
  this_workspace=`cat ${this_collection_datadir}/styles/${this_style}.json | jq -r '.style.workspace.name'`
  echo ${this_workspace}
}

# Featuretype workspace
function get_featuretype_workspace() {
  this_collection_datadir="${1}"
  this_featuretype="${2}"
  this_workspace=`cat ${this_collection_datadir}/featuretypes/${this_featuretype}.json | jq -r '.featureType.namespace.name'`
  echo ${this_workspace}
}

# Featuretype datastore
function get_featuretype_datastore() {
  this_collection_datadir="${1}"
  this_featuretype="${2}"
  this_datastore=`cat ${this_collection_datadir}/featuretypes/${this_featuretype}.json | jq -r '.featureType.store.name' | awk -F":" '{print $2}'`
  echo ${this_datastore}
}

# Layer workspace
function get_layer_workspace() {
  this_collection_datadir="${1}"
  this_layer="${2}"
  this_workspace=`cat ${this_collection_datadir}/layers/${this_layer}.json | jq -r '.layer.resource.name' | awk -F":" '{print $1}' 2>/dev/null`
  echo ${this_workspace}
}

# Layergroup workspace
function get_layergroup_workspace() {
  this_collection_datadir="${1}"
  this_layergroup="${2}"
  this_workspace=`cat ${this_collection_datadir}/layergroups/${this_layergroup}.json | jq -r '.layerGroup.workspace.name'`
  echo ${this_workspace}
}

# Check if remote workspace exists
function find_remote_workspace() {
  this_collection=${1}
  this_workspace=${2}
  remote_workspace=$(${geoserver_api_script} ${api_script_input} -c ${this_collection} get workspaces |jq -r '.workspaces.workspace[] | select(.name=="'${this_workspace}'") | .name' 2>/dev/null)
  if [ "${this_workspace}" == "${remote_workspace}" ] ; then
    return 0
  else
    return 1
  fi
}

# Check if remote datastore exists
function find_remote_datastore() {
  this_collection="${1}"
  this_workspace="${2}"
  this_datastore="${3}"
  ${geoserver_api_script} ${api_script_input} -c ${this_collection} -w ${this_workspace} get datastores > $tmp_file 2>&1
  cat $tmp_file | jq > /dev/null 2>&1 
  if [ $? -eq 0 ] ; then
    remote_datastore=$(cat ${tmp_file} |jq -r '.dataStores.dataStore[] | select(.name=="'${this_datastore}'") | .name' 2>/dev/null)
  else
    remote_datastore=""
  fi
  
  if [ "${this_datastore}" == "${remote_datastore}" ] ; then
    return 0
  else
    return 1
  fi
}

# Check if remote style exists
function find_remote_style() {
  this_collection="${1}"
  this_workspace="${2}"
  this_style="${3}"
  ${geoserver_api_script} ${api_script_input} -c ${this_collection} -w ${this_workspace} get styles > $tmp_file 2>&1
  cat $tmp_file | jq > /dev/null 2>&1 
  if [ $? -eq 0 ] ; then
    remote_style=$(cat $tmp_file |jq -r '.styles.style[] | select(.name=="'${this_style}'") | .name' 2>/dev/null)
  else
    remote_style=""
  fi
  
  if [ "${this_style}" == "${remote_style}" ] ; then
    return 0
  else
    return 1
  fi
}

# Check if remote featuretype exists
function find_remote_featuretype() {
  this_collection="${1}"
  this_workspace="${2}"
  this_datastore="${3}"
  this_featuretype="${4}"
  ${geoserver_api_script} ${api_script_input} -c ${this_collection} -w ${this_workspace} -s ${this_datastore} get featuretypes > $tmp_file 2>&1
  cat $tmp_file | jq > /dev/null 2>&1 
  if [ $? -eq 0 ] ; then
    remote_featuretype=$(cat $tmp_file |jq -r '.featureTypes.featureType[] | select(.name=="'${this_featuretype}'") | .name' 2>/dev/null)
  else
    remote_featuretype=""
  fi
  
  if [ "${this_featuretype}" == "${remote_featuretype}" ] ; then
    return 0
  else
    return 1
  fi
}

# Check if remote layer exists
function find_remote_layer() {
  this_collection="${1}"
  this_workspace="${2}"
  this_layer="${3}"
  ${geoserver_api_script} ${api_script_input} -c ${this_collection} -w ${this_workspace} get layers > $tmp_file 2>&1
  cat $tmp_file | jq > /dev/null 2>&1 
  if [ $? -eq 0 ] ; then
    remote_layer=$(cat $tmp_file |jq -r '.layers.layer[] | select(.name=="'${this_layer}'") | .name' 2>/dev/null)
  else
    remote_layer=""
  fi
  
  if [ "${this_layer}" == "${remote_layer}" ] ; then
    return 0
  else
    return 1
  fi
}

# Check if remote layergroup exists
function find_remote_layergroup() {
  this_collection="${1}"
  this_workspace="${2}"
  this_layergroup="${3}"
  ${geoserver_api_script} ${api_script_input} -c ${this_collection} -w ${this_workspace} get layergroups > $tmp_file 2>&1
  cat $tmp_file | jq > /dev/null 2>&1 
  if [ $? -eq 0 ] ; then
    remote_layergroup=$(cat $tmp_file |jq -r '.layerGroups.layerGroup[] | select(.name=="'${this_layergroup}'") | .name' 2>/dev/null)
  else
    remote_layergroup=""
  fi
  
  if [ "${this_layergroup}" == "${remote_layergroup}" ] ; then
    return 0
  else
    return 1
  fi
}

# Update or list all objects
function find_all_objects() {

  # Global settings
  if [ ${update_global_settings} -eq 1 ] ; then
    if [ -f "${data_dir}/global/settings.json" ] ; then
      echo "*** Global settings ***"
      if [ ${update_mode} -eq 1 ] ; then
        ${geoserver_api_script} ${api_script_input} update settings
        ret_val=$?
        if [ ${ret_val} -ne 0 ] ; then
          clean_exit 10 "Unable to update global settings."
        fi
      else
        echo "${data_dir}/global/settings.json"
      fi
    fi  

    # Services
    if [ -d "${data_dir}/global/services" ] ; then
      echo
      echo "*** Services ***"
      for service_file in `ls -1 ${data_dir}/global/services/*.json` ; do
        this_service=`basename ${service_file}`
        this_service="${this_service%.*}"
        if [ ${update_mode} -eq 1 ] ; then
          echo "Updating service: ${this_service}"
          ${geoserver_api_script} ${api_script_input} update services ${this_service}
          ret_val=$?
          if [ ${ret_val} -ne 0 ] ; then
            clean_exit 11 "Unable to update service: ${this_service}"
          fi
        else
          echo "Found service: ${this_service}"
        fi
      done
    fi
  fi

  # Collections  
  for collection in ${collection_list//,/ } ; do

    collection_data_dir="${data_dir}/collections/${collection}"
    
    # Workspaces
    if [ -d "${collection_data_dir}/workspaces" ] ; then      

      echo
      echo "*** Workspaces ***"

      for workspace_file in `ls -1 ${collection_data_dir}/workspaces/*.json` ; do
        this_workspace=`basename ${workspace_file}`
        this_workspace="${this_workspace%.*}"

        if [ ${update_mode} -eq 1 ] ; then
        
          if find_remote_workspace ${collection} ${this_workspace} ; then
            echo "Updating workspace: ${this_workspace}"
            ${geoserver_api_script} ${api_script_input} -c ${collection} update workspaces ${this_workspace}
            ret_val=$?
            if [ ${ret_val} -ne 0 ] ; then
              clean_exit 12 "Unable to update workspace ${this_workspace}."
            fi
          else
            echo "Creating workspace: ${this_workspace}"
            ${geoserver_api_script} ${api_script_input} -c ${collection} create workspaces ${this_workspace}
            ret_val=$?
            if [ ${ret_val} -ne 0 ] ; then
              clean_exit 13 "Unable to create workspace ${this_workspace}."
            fi
          fi
        
        else

          if find_remote_workspace ${collection} ${this_workspace} ; then
            echo "Update: ${this_workspace}"
          else
            echo "Create: ${this_workspace}"
          fi

        fi

      done

    fi # Workspaces

    # Datastores
    if [ -d "${collection_data_dir}/datastores" ] ; then
      echo
      echo "*** Data stores ***"

      for datastore_file in `ls -1 ${collection_data_dir}/datastores/*.json` ; do

        this_datastore=`basename ${datastore_file}`
        this_datastore="${this_datastore%.*}"
        store_workspace=$(get_datastore_workspace ${collection_data_dir} ${this_datastore})
        
        if [ ${update_mode} -eq 1 ] ; then

          if find_remote_datastore ${collection} ${store_workspace} ${this_datastore} ; then
            echo "Updating datastore: ${this_datastore}"
            ${geoserver_api_script} ${api_script_input} -c ${collection} update datastores ${this_datastore}
            ret_val=$?
            if [ ${ret_val} -ne 0 ] ; then
              clean_exit 14 "Unable to update datastore ${this_datastore}."
            fi
          else
            echo "Creating datastore: ${this_datastore}"
            ${geoserver_api_script} ${api_script_input} -c ${collection} create datastores ${this_datastore}
            ret_val=$?
            if [ ${ret_val} -ne 0 ] ; then
              clean_exit 15 "Unable to create datastore ${this_datastore}."
            fi
          fi

        else

          if find_remote_datastore ${collection} ${store_workspace} ${this_datastore} ; then
            echo "Update: ${this_datastore}"
          else
            echo "Create: ${this_datastore}"
          fi
        fi

      done

    fi # Datastores

    # Styles
    if [ -d "${collection_data_dir}/styles" ] ; then
      echo
      echo "*** Styles ***"

      for style_file in `ls -1 ${collection_data_dir}/styles/*.json` ; do

        this_style=`basename ${style_file}`
        this_style="${this_style%.*}"        
        style_workspace=$(get_style_workspace ${collection_data_dir} ${this_style})

        if [ ${update_mode} -eq 1 ] ; then

          if find_remote_style ${collection} ${style_workspace} ${this_style} ; then
            echo "Updating style: ${this_style}"
            ${geoserver_api_script} ${api_script_input} -c ${collection} update sld ${this_style}
            ret_val=$?
            if [ ${ret_val} -ne 0 ] ; then
              clean_exit 16 "Unable to update style ${this_style}."
            fi          
          else
            echo "Creating style: ${this_style}"
            ${geoserver_api_script} ${api_script_input} -c ${collection} create styles ${this_style}
            ret_val=$?
            if [ ${ret_val} -ne 0 ] ; then
              clean_exit 17 "Unable to create style ${this_style}."
            fi
            ${geoserver_api_script} ${api_script_input} -c ${collection} update sld ${this_style}
            ret_val=$?
            if [ ${ret_val} -ne 0 ] ; then
              clean_exit 18 "Unable to upload sld for style ${this_style}."
            fi
          fi

        else

          if find_remote_style ${collection} ${style_workspace} ${this_style} ; then
            echo "Update: ${this_style}"
          else
            echo "Create: ${this_style}"
          fi

        fi

      done

    fi # Styles

    # Featuretypes
    if [ -d "${collection_data_dir}/featuretypes" ] ; then
      echo
      echo "*** Featuretypes ***"

      for featuretype_file in `ls -1 ${collection_data_dir}/featuretypes/*.json` ; do

        this_featuretype=`basename ${featuretype_file}`
        this_featuretype="${this_featuretype%.*}"
        
        featuretype_workspace=$(get_featuretype_workspace ${collection_data_dir} ${this_featuretype})
        featuretype_datastore=$(get_featuretype_datastore ${collection_data_dir} ${this_featuretype})
        
        if [ ${update_mode} -eq 1 ] ; then

          if find_remote_featuretype ${collection} ${featuretype_workspace} ${featuretype_datastore} ${this_featuretype} ; then
            echo "Updating featuretype: ${this_featuretype}"
            ${geoserver_api_script} ${api_script_input} -c ${collection} update featuretypes ${this_featuretype}
            ret_val=$?
            if [ ${ret_val} -ne 0 ] ; then
              clean_exit 19 "Unable to update featuretype ${this_featuretype}."
            fi          
          else
            echo "Creating featuretype: ${this_featuretype}"
            ${geoserver_api_script} ${api_script_input} -c ${collection} create featuretypes ${this_featuretype}
            ret_val=$?
            if [ ${ret_val} -ne 0 ] ; then
              clean_exit 20 "Unable to create featuretype ${this_featuretype}."
            fi          
          fi

        else

          if find_remote_featuretype ${collection} ${featuretype_workspace} ${featuretype_datastore} ${this_featuretype} ; then
            echo "Update: ${this_featuretype}"
          else
            echo "Create: ${this_featuretype}"
          fi

        fi

      done

    fi # Featuretypes

    # Layers
    if [ -d "${collection_data_dir}/layers" ] ; then
      echo
      echo "*** Layers ***"

      for layer_file in `ls -1 ${collection_data_dir}/layers/*.json` ; do

        this_layer=`basename ${layer_file}`
        this_layer="${this_layer%.*}"        
        layer_workspace=$(get_layer_workspace ${collection_data_dir} ${this_layer})

        if [ ${update_mode} -eq 1 ] ; then

          if find_remote_layer ${collection} ${layer_workspace} ${this_layer} ; then
            echo "Updating layer: ${this_layer}"
            ${geoserver_api_script} ${api_script_input} -c ${collection} update layers ${this_layer}
            ret_val=$?
            if [ ${ret_val} -ne 0 ] ; then
              clean_exit 21 "Unable to update later ${this_layer}."
            fi          
          else
            echo "Creating layer: ${this_layer}"
            ${geoserver_api_script} ${api_script_input} -c ${collection} create layers ${this_layer}
            ret_val=$?
            if [ ${ret_val} -ne 0 ] ; then
              clean_exit 22 "Unable to create layer ${this_layer}."
            fi          
          fi

        else

          if find_remote_layer ${collection} ${layer_workspace} ${this_layer} ; then
            echo "Update: ${this_layer}"
          else
            echo "Create: ${this_layer}"
          fi

        fi

      done

    fi # Layers    

    # Layergroups
    if [ -d "${collection_data_dir}/layergroups" ] ; then
      echo
      echo "*** Layergroups ***"

      for layergroup_file in `ls -1 ${collection_data_dir}/layergroups/*.json` ; do

        this_layergroup=`basename ${layergroup_file}`
        this_layergroup="${this_layergroup%.*}"        
        layergroup_workspace=$(get_layergroup_workspace ${collection_data_dir} ${this_layergroup})

        if [ ${update_mode} -eq 1 ] ; then
        
          if find_remote_layergroup ${collection} ${layergroup_workspace} ${this_layergroup} ; then
            echo "Updating layergroup: ${this_layergroup}"
            ${geoserver_api_script} ${api_script_input} -c ${collection} update layergroups ${this_layergroup}
            ret_val=$?
            if [ ${ret_val} -ne 0 ] ; then
              clean_exit 23 "Unable to update layergroup ${this_layergroup}."
            fi          
          else
            echo "Creating layergroup: ${this_layergroup}"
            ${geoserver_api_script} ${api_script_input} -c ${collection} create layergroups ${this_layergroup}
            ret_val=$?
            if [ ${ret_val} -ne 0 ] ; then
              clean_exit 24 "Unable to create layergroup ${this_layergroup}."
            fi          
          fi

        else

          if find_remote_layergroup ${collection} ${layergroup_workspace} ${this_layergroup} ; then
            echo "Update: ${this_layergroup}"
          else
            echo "Create: ${this_layergroup}"
          fi

        fi

      done

    fi # Layergroups

  done
      
}

#######################################################################
## Script begins
#######################################################################
# Initialize
typeset -i setverbose=0
typeset -i update_global_settings=0
typeset -i update_mode=0
typeset -i list_mode=0
version="1.0"
scriptname=`basename "$0"`
tmp_file="/tmp/$$.${scriptname}"
geoserver_api_script="./geoserver_api.sh"
data_dir="../geoserver_data"

# Validate input
while [[ $# -gt 0 ]]; do
  case $1 in
    -c|--collectionlist)
      collection_list="${2}"
      if [ -z "${collection_list}" ] || [[ ${collection_list} =~ ^- ]] ; then
        usage
        clean_exit 1 "Invalid collection list."
      fi
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
    -g|--global)
      update_global_settings=1
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
    -s|--scripts_dir)
      scripts_dir="${2}"
      if ! [ -d "${scripts_dir}" ] ; then
        clean_exit 1 "Scripts directory not found: ${scripts_dir}"
      fi
      geoserver_api_script="${scripts_dir}/geoserver_api.sh"
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

if [ ${update_global_settings} -eq 1 ] && [ -z "${collection_list}" ] ; then
  usage
  clean_exit 1 "Nothing to update. Please provide a collection or global settings."
fi

if ! [ -f ${geoserver_api_script} ] ; then
  echo "API script not found: ${geoserver_api_script}"
  clean_exit 1
fi

api_script_input="-u ${username} -p ${password} -r ${resturl}"
if ! [ -z "${data_dir}" ] ; then
  api_script_input=${api_script_input}" -d ${data_dir}"
fi

# Execute commands
case "${command}" in
  update)
    update_mode=1
    echo "Updating objects."
    ;;
  list)
    list_mode=1
    echo "Listing objects."
    ;;
  *)
    usage
    clean_exit 1 "Invalid command."
    ;;
esac

find_all_objects

clean_exit 0