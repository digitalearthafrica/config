from ows_refactored.common.ows_reslim_cfg import reslim_wms_min_zoom_15
from ows_refactored.vegetation.styles_ndvi_anom import (
    style_ndvi_mean,
    style_ndvi_anomaly,
    style_count,
)

bands_ndvi_anom = {"ndvi_std_anomaly": [], "ndvi_mean": [], "clear_count": []}


layer = {
    "title": "NDVI Anomaly",
    "name": "ndvi_anomaly",
    "abstract": """
Standardised NDVI Anomalies provide a measure of vegetation health relative to long term average conditions by measuring the departure, in units of standard devaiations, away from the long-term mean. These monthly NDVI anomalies were calculated by combining NDVI observations from Landsat 8, Landsat 9, and Sentinel-2 for a given month, subtracting those values from the long term NDVI mean, then dividing by the long-term NDVI standard deviation. Postive values indicate vegetation is greener than average conditions, and are usually due to increased rainfall in a region. Negative values indicate additional plant stress relative to the long-term average.

This service provides data monthly from January 2017 at a spatial resolution of 30 m. The long term means and standard deviations used are available through the "NDVI Climatology" layer.

More technical information about the NDVI Anomaly service can be found in the User Guide (https://docs.digitalearthafrica.org/en/latest/data_specs/NDVI_Anomaly_specs.html)

This service is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download click on a tile in the explorer page (https://explorer.digitalearth.africa/products/ndvi_anomaly)
""",
    "product_name": "ndvi_anomaly",
    "time_resolution": "month",
    "bands": bands_ndvi_anom,
    "resource_limits": reslim_wms_min_zoom_15,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:6933",
    "native_resolution": [30, -30],
    "styling": {
        "default_style": "style_ndvi_anomaly",
        "styles": [
            style_ndvi_anomaly,
            style_ndvi_mean,
            style_count,
        ],
    },
}
