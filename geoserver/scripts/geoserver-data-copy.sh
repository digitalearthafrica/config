#!/bin/bash
#
# GeoServer data copy script. This script will be executed from 
# datakube-tools.
#----------------------------------------------------------------------

#######################################################################
## Functions
#######################################################################
function usage() {
  echo
  echo "Usage: ${scriptname} [OPTIONS] COMMAND"
  echo
  echo "GeoServer data copy script."
  echo
  echo "Options:"
  echo "  -c, --cluster         EKS cluster name"
  echo "  -s, --source-s3-uri   S3 URI for the S3 data source. E.g.: s3://deafrica-services/coastlines/v0.4.0"
  echo "  -t, --target-dir      Target directory on the GeoServer container"
  echo
  echo "Authentication environment variables:"
  echo "  AWS_ACCESS_KEY_ID          AWS access key"
  echo "  AWS_SECRET_ACCESS_KEY      AWS secret key"
  echo "  AWS_DEFAULT_REGION         Default AWS region - Optional"
  echo

}

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
default_namespace="web"

if [ -z ${SOURCE_S3_URI} ] ; then
  usage
  clean_exit 1 "Env var SOURCE_S3_URI not set."
fi

if [ -z ${TARGET_DIR} ] ; then
  usage
  clean_exit 1 "Env var TARGET_DIR not set."
fi

if [ -z ${EKS_CLUSTER} ] ; then
  usage
  clean_exit 1 "Env var EKS_CLUSTER not set."
fi

if [ -z ${AWS_ACCESS_KEY_ID} ] ; then
  usage
  clean_exit 1 "Env var AWS_ACCESS_KEY_ID not set."
fi

if [ -z ${AWS_SECRET_ACCESS_KEY} ] ; then
  usage
  clean_exit 1 "Env var AWS_SECRET_ACCESS_KEY not set."
fi

if ! [ -z ${AWS_DEFAULT_REGION} ] ; then
  default_region=${AWS_DEFAULT_REGION}
fi

# Start file copy
echo "Running: GeoServer data copy"
echo

echo "Update kubeconfig:"
aws eks update-kubeconfig --name ${EKS_CLUSTER} --region ${AWS_DEFAULT_REGION}
echo

echo "Starting copy from S3:"
mkdir ~/data
cd ~/data
aws s3 cp ${SOURCE_S3_URI} . --recursive
echo

echo "Starting copy to GeoServer:"
geoserver_pod=$(kubectl get pods -n web | grep geoserver |awk '{print $1}')

kubectl exec ${geoserver_pod} -n ${default_namespace} -- ls -la ${TARGET_DIR} > /dev/null 2>&1
ret_val=$?

if [ ${ret_val} -ne 0 ] ; then
  clean_exit 1 "Target directory not found: ${TARGET_DIR}"
fi

files_to_copy=0
for file in `ls -1` ; do  
  echo "Copy ${file}"
  kubectl cp ${file} ${geoserver_pod}:${TARGET_DIR} -n ${default_namespace}
  files_to_copy=1
done

if [ ${files_to_copy} -eq 0 ] ; then
  clean_exit 2 "No files found to copy."
fi

echo "Copy complete"

clean_exit 0
