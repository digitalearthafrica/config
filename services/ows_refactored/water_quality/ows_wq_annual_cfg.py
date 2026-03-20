from ows_refactored.common.ows_reslim_cfg import reslim_continental
from ows_refactored.water_quality.style_wq_annual_cfg import (
    style_wq_annual_tsm,
    style_wq_annual_tsi,
    style_wq_annual_ndvi,
    style_wq_annual_fai,
    style_wq_annual_hue,
    style_wq_annual_owt,
    style_wq_annual_chla,
    style_wq_annual_tirs,
    style_wq_annual_water_mask,
    style_wq_annual_clear_water)

bands_wq_annual = {
    "agm_fai": ["fai", "FAI", "floating_algae_index"],
    "agm_hue": ["hue", "HUE"],
    "agm_ndvi": ["ndvi", "NDVI"],
    "agm_owt": ["owt", "OWT", "optical_water_type"],
    "chla": ["CHLA", "chlorophyll_a"],
    "clear_water": [],
    "tirs_st_ann_max": ["st_max", "max_surface_temperature"],
    "tirs_st_ann_med": ["st_median", "median_surface_temperature"],
    "tirs_st_ann_min": ["st_min", "min_surface_temperature"],
    "tsi": ["TSI", "trophic_state_index"],
    "tsm": ["TSM", "total_suspended_matter"],
    "water_mask": [],
}

layer = {
    "title": "Annual Water Quality Variables",
    "abstract": """The Digital Earth Africa water quality service
provides annual water quality data for surface water bodies derived from a
variety of optical sensors, at a spatial resolution of 10 meters. The data is
available from the year 2000 to 2024.

More technical information about the Water Quality Service can be found in the
User Guide (https://docs.digitalearthafrica.org/en/latest/data_specs/<insert page>.html)
This service is accessible through OGC Web Service (https://ows.digitalearth.africa/),
for analysis in DE Africa Sandbox (sandbox.digitalearth.africa) and for direct download
click on a tile in the explorer page (https://explorer.dev.digitalearth.africa/products/wq_annual).
""",
    "name": "wq_annual",
    "product_name": "wq_annual",
    "multi_product": False,
    "time_resolution": "summary",
    "default_time": "latest",
    "bands": bands_wq_annual,
    "native_crs": "EPSG:6933",
    "native_resolution": [10.0, 10.0],
    "resource_limits": reslim_continental,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "fuse_func": None,
        "manual_merge": False,
    },
    "styling": {
        "default_style": "wq_annual_tsm",
        "styles": [
            style_wq_annual_tsm,
            style_wq_annual_tsi,
            style_wq_annual_ndvi,
            style_wq_annual_fai,
            style_wq_annual_hue,
            style_wq_annual_owt,
            style_wq_annual_tirs,
            style_wq_annual_chla,
            style_wq_annual_water_mask,
            style_wq_annual_clear_water,
        ],
    },
}
