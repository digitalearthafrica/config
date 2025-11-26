from ows_refactored.common.ows_reslim_cfg import reslim_continental
from ows_refactored.surface_reflectance.band_sr_cfg import bands_s3_olci_l2_land
from ows_refactored.surface_reflectance.style_sr_cfg import styles_s3_land_list, styles_s3_water_list

layer_s3_olci_l2_land = {
    "title": "Surface reflectance (Sentinel-3 OLCI L2 LAND)",
    "name": "s3_olci_l2_lfr",
    "abstract": """
Sentinel-3 is a European Earth Observation satellite mission developed to support Copernicus ocean, land, atmospheric, emergency, security, and cryospheric applications.

The primary goal of the Sentinel-3 mission is to measure sea surface topography, sea and land surface temperature, and ocean and land surface color with high accuracy and reliability. This data is used to support ocean forecasting systems, environmental monitoring, and climate monitorinsml

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
    "product_name": "s3_olci_l2_lfr",
    "bands": bands_s3_olci_l2_land,
    "dynamic": True,
    "resource_limits": reslim_continental,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,  # True
        "apply_solar_corrections": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [0.003, -0.003],
    "styling": {
        "default_style": "gifapar",
        "styles": styles_s3_land_list,
    },
}

layer_s3_olci_l2_water = {
    "title": "Surface reflectance (Sentinel-3 OLCI L2 WATER)",
    "name": "s3_olci_l2_wfr",
    "abstract": """
Sentinel-3 is a European Earth Observation satellite mission developed to support Copernicus ocean, land, atmospheric, emergency, security, and cryospheric applications.

The primary goal of the Sentinel-3 mission is to measure sea surface topography, sea and land surface temperature, and ocean and land surface color with high accuracy and reliability. This data is used to support ocean forecasting systems, environmental monitoring, and climate monitorinsml

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
    "product_name": "s3_olci_l2_wfr",
    "bands": bands_s3_olci_l2_water,
    "dynamic": True,
    "resource_limits": reslim_continental,

    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
        "apply_solar_corrections": False,
    },

    "native_crs": "EPSG:4326",
    "native_resolution": [0.003, -0.003],

    "styling": {
        "default_style": "chl_nn",
        "styles": styles_s3_water_list,
    },
}
