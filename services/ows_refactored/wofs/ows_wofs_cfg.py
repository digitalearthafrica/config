from ows_refactored.common.ows_reslim_cfg import (reslim_wofs_daily,
                                                  reslim_wofs_dry)
from ows_refactored.wofs.band_wofs_cfg import (bands_usgs_wofs_summary,
                                               bands_wofs_obs)
from ows_refactored.wofs.style_wofs_cfg import (
    style_wofs_annual_frequency_blue, style_wofs_annual_summary_frequency,
    style_wofs_obs, style_wofs_obs_wet_only)

layers = {
    "title": "Water Observations from Space",
    "abstract": """WOfS""",
    "layers": [
        {
            "title": "Water Observations from Space Feature Layer (Development)",
            "name": "ls_usgs_wofs_scene",
            "abstract": """
Water Observations from Space (WOfS) provides surface water observations derived from satellite imagery for all of Africa. The WOfS product allows users to get a better understanding of where water is normally present in a landscape, where water is seldom observed, and where inundation has occurred occasionally. Data is provided as Water Observation Feature Layers (WOFLs), in a 1 to 1 relationship with the input satellite data. Hence there is one WOFL for each satellite dataset processed for the occurrence of water.

This product has a spatial resolution of 30 m and a temporal coverage of 1984 to 2019.

It is derived from Landsat 5, 7 and 8 satellites observations as part of Landsat Collection 1, Level 2 surface reflectance products over five countries (Tanzania, Senegal, Sierra Leone, Ghana, and Kenya).

Daily water observations can be used to map historical flood and to understand surface water dynamics.

WOfS shows surface water on the day and time that satellite passed overhead, which might be before, during or after a flood peak. Given the time between satellite passes (approximately once every 16 days) it is unlikely that the satellite will capture the maximum extent of any given flood. Instead, it aims to provide large scale, regional information on surface water.

For more information on the algorithm, see https://doi.org/10.1016/j.rse.2015.11.003

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "ls_usgs_wofs_scene",
            "bands": bands_wofs_obs,
            "resource_limits": reslim_wofs_daily,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_bitflag",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "native_crs": "EPSG:3857",
            "native_resolution": [30.0, -30.0],
            "wcs": {
                "native_crs": "EPSG:3857",
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
        {
            "title": "Water Observations from Space Annual Summary (Development)",
            "name": "wofs_annual_summary_frequency",
            "abstract": """
Annual water summary is one of the statistical summaries of the Water Observation from Space (WOfS) product that shows what percentage of clear observations were detected as wet (ie. the ration of wet to clear as a percentage) from each calendar year.

This product has a spatial resolution of 30 m and a temporal coverage of 1984 to 2019.

It is derived from Landsat 5, 7 and 8 satellites observations as part of Landsat Collection 1, Level 2 surface reflectance products over five countries (Tanzania, Senegal, Sierra Leone, Ghana, and Kenya).

The annual summaries can be used to understand year to year changes in surface water extent.

WOfS shows surface water on the day and time that satellite passed overhead, which might be before, during or after a flood peak. Given the time between satellite passes (approximately once every 16 days) it is unlikely that the satellite will capture the maximum extent of any given flood. Instead, it aims to provide large scale, regional information on surface water.

For more information on the algorithm, see https://doi.org/10.1016/j.rse.2015.11.003

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "ls_usgs_wofs_summary",
            "time_resolution": "year",
            "bands": bands_usgs_wofs_summary,
            "resource_limits": reslim_wofs_dry,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "native_crs": "ESRI:102022",
            "native_resolution": [30.0, -30.0],
            "wcs": {
                "native_crs": "ESRI:102022",
                "native_resolution": [30.0, -30.0],
                "default_bands": ["frequency"],
            },
            "styling": {
                "default_style": "WOfS_frequency",
                "styles": [
                    style_wofs_annual_summary_frequency,
                    style_wofs_annual_frequency_blue,
                ],
            },
        },
        #                     {
        #                         "title": "Water Observations from Space Annual Count of Wet Observations (Development)",
        #                         "name": "wofs_annual_summary_wet",
        #                         "abstract": """
        # The count of wet observations is one of the statistical summaries of the Water Observation from Space (WOfS) product that shows how many times water was detected in observations that were clear. This product was used as a source layer for calculating annual water summary.
        # This product has a spatial resolution of 30 m and a temporal coverage of 1984 to 2019.
        # It is derived from Landsat 5, 7 and 8 satellites observations as part of Landsat Collection 1, Level 2 surface reflectance products over five countries (Tanzania, Senegal, Sierra Leone, Ghana, and Kenya).
        # For more information on the algorithm, see https://doi.org/10.1016/j.rse.2015.11.003
        # This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
        # """,
        #                         "product_name": "ls_usgs_wofs_summary",
        #                         "time_resolution": "year",
        #                         "bands": bands_usgs_wofs_summary,
        #                         "resource_limits": reslim_wofs_dry,
        #                         "image_processing": {
        #                             "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        #                             "always_fetch_bands": [],
        #                             "manual_merge": False,
        #                         },
        #                         "wcs": {
        #                             "native_crs": "ESRI:102022",
        #                             "native_resolution": [30.0, -30.0],
        #                             "default_bands": ["count_wet"]
        #                         },
        #                         "styling": {
        #                             "default_style": "water_observations",
        #                             "styles": [
        #                                     style_wofs_count_wet,
        #                             ]
        #                         }
        #                     },
        #                     {
        #                         "title": "Water Observations from Space Annual Count of Clear Observations (Development)",
        #                         "name": "wofs_annual_summary_clear",
        #                         "abstract": """
        # The count of clear observations is one of the statistical summaries of the Water Observations from Space (WOfS) product that shows how many times an area could be clearly seen (I.e. not affected by clouds, shadows or other satellite observation problems). This product was used as a source layer for calculating annual water summary.
        # This product has a spatial resolution of 30 m and a temporal coverage of 1984 to 2019.
        # It is derived from Landsat 5, 7 and 8 satellites observations as part of Landsat Collection 1, Level 2 surface reflectance products over five countries (Tanzania, Senegal, Sierra Leone, Ghana, and Kenya).
        # For more information on the algorithm, see https://doi.org/10.1016/j.rse.2015.11.003
        # This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
        # """,
        #                         "product_name": "ls_usgs_wofs_summary",
        #                         "bands": bands_usgs_wofs_summary,
        #                         "resource_limits": reslim_wofs_dry,
        #                         "image_processing": {
        #                             "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        #                             "always_fetch_bands": [],
        #                             "manual_merge": False,
        #                         },
        #                         "wcs": {
        #                             "native_crs": "ESRI:102022",
        #                             "native_resolution": [30.0, -30.0],
        #                             "default_bands": ["count_dry"]
        #                         },
        #                         "styling": {
        #                             "default_style": "annual_clear_observations",
        #                             "styles": [
        #                                     style_wofs_annual_clear,
        #                             ]
        #                         }
        #                     },
    ],
}
