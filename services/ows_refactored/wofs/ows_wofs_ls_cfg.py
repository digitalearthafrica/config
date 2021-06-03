from ows_refactored.common.ows_reslim_cfg import reslim_wofs_daily
from ows_refactored.wofs.band_wofs_cfg import bands_wofs_obs
from ows_refactored.wofs.style_wofs_cfg import style_wofs_obs, style_wofs_obs_wet_only

layers = {
    "title": "Water Observations from Space (Prototype)",
    "abstract": """WOfS""",
    "layers": [
        {
            "title": "Water Observations from Space Feature Layer (Prototype)",
            "name": "wofs_ls",
            "abstract": """
Water Observations from Space (WOfS) provides surface water observations derived from satellite imagery for all of Africa. The WOfS product allows users to get a better understanding of where water is normally present in a landscape, where water is seldom observed, and where inundation has occurred occasionally. Data is provided as Water Observation Feature Layers (WOFLs), in a 1 to 1 relationship with the input satellite data. Hence there is one WOFL for each satellite dataset processed for the occurrence of water.

This product has a spatial resolution of 30 m and a temporal coverage of 2013 to 2019.

It is derived from Landsat 8 satellite observations as part of a provisional Landsat Collection 2 surface reflectance product.

Daily water observations can be used to map historical flood and to understand surface water dynamics.

WOfS shows surface water on the day and time that satellite passed overhead, which might be before, during or after a flood peak. Given the time between satellite passes (approximately once every 16 days) it is unlikely that the satellite will capture the maximum extent of any given flood. Instead, it aims to provide large scale, regional information on surface water.

For more information on the algorithm, see https://doi.org/10.1016/j.rse.2015.11.003

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "wofs_ls",
            "bands": bands_wofs_obs,
            "resource_limits": reslim_wofs_daily,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_bitflag",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:4326",
                "native_resolution": [30.0, -30.0],
                "default_bands": ["water"],
            },
            "styling": {
                "default_style": "observations",
                "styles": [
                    style_wofs_obs,
                    style_wofs_obs_wet_only,
                ],
            },
        },
    ],
}
