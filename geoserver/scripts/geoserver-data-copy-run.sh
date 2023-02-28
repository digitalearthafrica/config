#!/bin/bash
#
# GeoServer data copy wrapper script
#----------------------------------------------------------------------

#######################################################################
## Functions
#######################################################################
function usage() {
  echo
  echo "Usage: ${scriptname} [OPTIONS]"
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
default_region="af-south-1"

# Validate input
while [[ $# -gt 0 ]]; do
  case $1 in
    -c|--cluster)
      eks_cluster_name="${2}"
      shift
      shift
      ;;
    -s|--source-s3-uri)
      source_s3_uri="${2}"
      shift
      shift
      ;;
    -t|--target-dir)
      target_dir="${2}"
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

if [ -z "${eks_cluster_name}" ] ; then
  usage
  clean_exit 1 "Cluster name not specified."
fi

if [ -z "${source_s3_uri}" ] ; then
  usage
  clean_exit 1 "Source S3 URI not specified."
fi

if [ -z "${target_dir}" ] ; then
  usage
  clean_exit 1 "Target directory not specified."
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

# Run file copy using datakube-tools
docker run -it --rm \
  -e AWS_ACCESS_KEY_ID="${AWS_ACCESS_KEY_ID}" \
  -e AWS_SECRET_ACCESS_KEY="${AWS_SECRET_ACCESS_KEY}" \
  -e AWS_DEFAULT_REGION="${default_region}" \
  -e SOURCE_S3_URI="${source_s3_uri}" \
  -e TARGET_DIR="${target_dir}" \
  -e EKS_CLUSTER="${eks_cluster_name}" \
  -v .:/root/scripts \
  digitalearthafrica/datakube-tools \
  bash -c '/root/scripts/geoserver-data-copy.sh'

clean_exit $?
