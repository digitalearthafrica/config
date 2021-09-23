from ows_refactored.common.ows_reslim_cfg import reslim_wofs
from ows_refactored.wofs.band_wofs_cfg import bands_wofs_summary
from ows_refactored.wofs.style_wofs_ls import style_wofs_summary_alltime_frequency
from ows_refactored.wofs.style_wofs_ls_legacy import (
    legacy_style_wofs_summary_alltime_clear,
    legacy_style_wofs_summary_alltime_frequency,
    legacy_style_wofs_summary_alltime_frequency_blue,
    legacy_style_wofs_summary_alltime_wet)

layer = {
    "title": "Water Observations from Space All-Time Summary",
    "name": "wofs_ls_summary_alltime",
    "abstract": """
All time water summary is one of the statistical summaries of the Water Observation from Space (WOfS) product that shows what percentage of clear observations were detected as wet (ie. the ration of wet to clear as a percentage) over time.

This product has a spatial resolution of 30 m and a temporal coverage of 1980s to last calender year.

It is derived from Landsat Collection 2 surface reflectance product.

All time water summary can be used to understand water availability and flooding risk in a historical context.

WOfS shows surface water on the day and time that satellite passed overhead, which might be before, during or after a flood peak. Given the time between satellite passes (approximately once every 16 days) it is unlikely that the satellite will capture the maximum extent of any given flood. Instead, it aims to provide large scale, regional information on surface water.

For more information on the algorithm, see https://doi.org/10.1016/j.rse.2015.11.003

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
    "product_name": "wofs_ls_summary_alltime",
    "bands": bands_wofs_summary,
    "time_resolution": "year",
    "resource_limits": reslim_wofs,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:6933",
    "native_resolution": [30.0, -30.0],
    "wcs": {
        "default_bands": ["frequency"],
    },
    "styling": {
        "default_style": "wofs_summary_alltime_frequency",
        "styles": [
            style_wofs_summary_alltime_frequency,
            legacy_style_wofs_summary_alltime_frequency,
            legacy_style_wofs_summary_alltime_frequency_blue,
            legacy_style_wofs_summary_alltime_wet,
            legacy_style_wofs_summary_alltime_clear,
        ],
    },
}
