from ows_refactored.common.ows_reslim_cfg import reslim_wms_min_zoom_15
from ows_refactored.vegetation.styles_ndvi_clim import (
    style_ndvi_mean_jan,
    style_ndvi_mean_feb,
    style_ndvi_mean_mar,
    style_ndvi_mean_apr,
    style_ndvi_mean_may,
    style_ndvi_mean_jun,
    style_ndvi_mean_jul,
    style_ndvi_mean_aug,
    style_ndvi_mean_sep,
    style_ndvi_mean_oct,
    style_ndvi_mean_nov,
    style_ndvi_mean_dec,
    style_ndvi_std_jan,
    style_ndvi_std_feb,
    style_ndvi_std_mar,
    style_ndvi_std_apr,
    style_ndvi_std_may,
    style_ndvi_std_jun,
    style_ndvi_std_jul,
    style_ndvi_std_aug,
    style_ndvi_std_sep,
    style_ndvi_std_oct,
    style_ndvi_std_nov,
    style_ndvi_std_dec,
    style_count_jan,
    style_count_feb,
    style_count_mar,
    style_count_apr,
    style_count_may,
    style_count_jun,
    style_count_jul,
    style_count_aug,
    style_count_sep,
    style_count_oct,
    style_count_nov,
    style_count_dec,
)

bands_ndvi_clim = {
    "mean_jan": [],
    "mean_feb": [],
    "mean_mar": [],
    "mean_apr": [],
    "mean_may": [],
    "mean_jun": [],
    "mean_jul": [],
    "mean_aug": [],
    "mean_sep": [],
    "mean_oct": [],
    "mean_nov": [],
    "mean_dec": [],
    "stddev_jan": [],
    "stddev_feb": [],
    "stddev_mar": [],
    "stddev_apr": [],
    "stddev_may": [],
    "stddev_jun": [],
    "stddev_jul": [],
    "stddev_aug": [],
    "stddev_sep": [],
    "stddev_oct": [],
    "stddev_nov": [],
    "stddev_dec": [],
    "count_jan": [],
    "count_feb": [],
    "count_mar": [],
    "count_apr": [],
    "count_may": [],
    "count_jun": [],
    "count_jul": [],
    "count_aug": [],
    "count_sep": [],
    "count_oct": [],
    "count_nov": [],
    "count_dec": [],
}


layer = {
    "title": "NDVI Climatology",
    "name": "ndvi_climatology_ls",
    "abstract": """

Standardised NDVI Anomalies provide a measure of vegetation health relative to long term average conditions by measuring the departure, in units of standard devaiations, away from the long-term average. These NDVI climatologies (both mean and standard deviation) represent the long-term average baseline conditions of vegetation condition. 

NDVI climatologies are available for each month at a spatial resolution of 30 m, and were calculated by aggregating data from 1984-2020.

More technical information about the NDVI Anomaly service can be found in the User Guide (https://docs.digitalearthafrica.org/en/latest/data_specs/NDVI_Climatology_specs.html)

This service is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download click on a tile in the explorer page (https://explorer.digitalearth.africa/products/ndvi_climatology_ls)

""",
    "product_name": "ndvi_climatology_ls",
    "time_resolution": "year",
    "bands": bands_ndvi_clim,
    "resource_limits": reslim_wms_min_zoom_15,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:6933",
    "native_resolution": [30, -30],
    "styling": {
        "default_style": "style_ndvi_mean_jan",
        "styles": [
            style_ndvi_mean_jan,
            style_ndvi_mean_feb,
            style_ndvi_mean_mar,
            style_ndvi_mean_apr,
            style_ndvi_mean_may,
            style_ndvi_mean_jun,
            style_ndvi_mean_jul,
            style_ndvi_mean_aug,
            style_ndvi_mean_sep,
            style_ndvi_mean_oct,
            style_ndvi_mean_nov,
            style_ndvi_mean_dec,
            style_ndvi_std_jan,
            style_ndvi_std_feb,
            style_ndvi_std_mar,
            style_ndvi_std_apr,
            style_ndvi_std_may,
            style_ndvi_std_jun,
            style_ndvi_std_jul,
            style_ndvi_std_aug,
            style_ndvi_std_sep,
            style_ndvi_std_oct,
            style_ndvi_std_nov,
            style_ndvi_std_dec,
            style_count_jan,
            style_count_feb,
            style_count_mar,
            style_count_apr,
            style_count_may,
            style_count_jun,
            style_count_jul,
            style_count_aug,
            style_count_sep,
            style_count_oct,
            style_count_nov,
            style_count_dec,
        ],
    },
}
