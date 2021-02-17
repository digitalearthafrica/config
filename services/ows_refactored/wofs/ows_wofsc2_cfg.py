from ows_refactored.wofs.style_wofs_cfg import (
    style_wofs_beta_summary_clear,
    style_wofs_water_annual_wet,
    style_wofs_annual_summary_frequency_blue,
    style_wofs_annual_summary_frequency,
    style_wofs_summary_clear,
    style_wofs_frequency,
    style_wofs_frequency_blue,
    style_wofs_count_wet,
)
from ows_refactored.wofs.band_wofs_cfg import (
    bands_wofs_2_annual_summary,
)
from ows_refactored.common.ows_reslim_cfg import reslim_wofs

layers = {
    "title": "Water Observations from Space c2",
    "abstract": """WOfS""",
    "layers": [
        {
            "title": "Water Observations from Space Annual Summary (Beta)",
            "name": "wofs_2_annual_summary_frequency",
            "abstract": """
Annual water summary is one of the statistical summaries of the Water Observation from Space (WOfS) product that shows what percentage of clear observations were detected as wet (ie. the ration of wet to clear as a percentage) from each calendar year.

This product has a spatial resolution of 30 m and a temporal coverage of 2013 to 2019.

It is derived from Landsat 8 satellite observations as part of a provisional Landsat Collection 2 surface reflectance product.

The annual summaries can be used to understand year to year changes in surface water extent.

WOfS shows surface water on the day and time that satellite passed overhead, which might be before, during or after a flood peak. Given the time between satellite passes (approximately once every 16 days) it is unlikely that the satellite will capture the maximum extent of any given flood. Instead, it aims to provide large scale, regional information on surface water.

For more information on the algorithm, see https://doi.org/10.1016/j.rse.2015.11.003

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "ga_ls8c_wofs_2_annual_summary",
            "time_resolution": "year",
            "bands": bands_wofs_2_annual_summary,
            "resource_limits": reslim_wofs,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:6933",
                "native_resolution": [30.0, -30.0],
                "default_bands": ["frequency"],
            },
            "styling": {
                "default_style": "WOfS_frequency",
                "styles": [
                    style_wofs_annual_summary_frequency,
                    style_wofs_annual_summary_frequency_blue,
                ],
            },
        },
        {
            "title": "Water Observations from Space Annual Count of Wet Observations (Beta)",
            "name": "wofs_2_annual_summary_wet",
            "abstract": """
The count of wet observations is one of the statistical summaries of the Water Observation from Space (WOfS) product that shows how many times water was detected in observations that were clear. This product was used as a source layer for calculating annual water summary.

This product has a spatial resolution of 30 m and a temporal coverage of 2013 to 2019.

It is derived from Landsat 8 satellite observations as part of a provisional Landsat Collection 2 surface reflectance product.

For more information on the algorithm, see https://doi.org/10.1016/j.rse.2015.11.003

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "ga_ls8c_wofs_2_annual_summary",
            "time_resolution": "year",
            "bands": bands_wofs_2_annual_summary,
            "resource_limits": reslim_wofs,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:6933",
                "native_resolution": [30.0, -30.0],
                "default_bands": ["count_wet"],
            },
            "styling": {
                "default_style": "water_observations",
                "styles": [
                    style_wofs_water_annual_wet,
                ],
            },
        },
        {
            "title": "Water Observations from Space Annual Count of Clear Observations (Beta)",
            "name": "wofs_2_annual_summary_clear",
            "abstract": """
The count of clear observations is one of the statistical summaries of the Water Observations from Space (WOfS) product that shows how many times an area could be clearly seen (I.e. not affected by clouds, shadows or other satellite observation problems). This product was used as a source layer for calculating annual water summary.

This product has a spatial resolution of 30 m and a temporal coverage of 2013 to 2019.

It is derived from Landsat 8 satellite observations as part of a provisional Landsat Collection 2 surface reflectance product.

For more information on the algorithm, see https://doi.org/10.1016/j.rse.2015.11.003

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "ga_ls8c_wofs_2_annual_summary",
            "time_resolution": "year",
            "bands": bands_wofs_2_annual_summary,
            "resource_limits": reslim_wofs,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:6933",
                "native_resolution": [30.0, -30.0],
                "default_bands": ["count_clear"],
            },
            "styling": {
                "default_style": "annual_clear_observations",
                "styles": [
                    style_wofs_beta_summary_clear,
                ],
            },
        },
        {
            "title": "Water Observations from Space All Time Summary (Beta)",
            "name": "wofs_2_summary_frequency",
            "abstract": """
All time water summary is one of the statistical summaries of the Water Observation from Space (WOfS) product that shows what percentage of clear observations were detected as wet (ie. the ration of wet to clear as a percentage) over time.

This product has a spatial resolution of 30 m and a temporal coverage of 2013 to 2019.

It is derived from Landsat 8 satellite observations as part of a provisional Landsat Collection 2 surface reflectance product.

All time water summary can be used to understand water availability and flooding risk in a historical context.

WOfS shows surface water on the day and time that satellite passed overhead, which might be before, during or after a flood peak. Given the time between satellite passes (approximately once every 16 days) it is unlikely that the satellite will capture the maximum extent of any given flood. Instead, it aims to provide large scale, regional information on surface water.

For more information on the algorithm, see https://doi.org/10.1016/j.rse.2015.11.003

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "ga_ls8c_wofs_2_summary",
            "bands": bands_wofs_2_annual_summary,
            "time_resolution": "year",
            "resource_limits": reslim_wofs,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:6933",
                "native_resolution": [30.0, -30.0],
                "default_bands": ["frequency"],
            },
            "styling": {
                "default_style": "WOfS_frequency",
                "styles": [
                    style_wofs_frequency,
                    style_wofs_frequency_blue,
                ],
            },
        },
        {
            "title": "Water Observations from Space All Time Count of Wet Observations (Beta)",
            "name": "wofs_2_summary_wet",
            "abstract": """
The count of wet observations is one of the statistical summaries of the Water Observation from Space (WOfS) product that shows how many times water was detected in observations that were clear. This product was used as a source layer for calculating all time water summary.

This product has a spatial resolution of 30 m and a temporal coverage of 2013 to 2019.

It is derived from Landsat 8 satellite observations as part of a provisional Landsat Collection 2 surface reflectance product.

For more information on the algorithm, see https://doi.org/10.1016/j.rse.2015.11.003

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "ga_ls8c_wofs_2_summary",
            "time_resolution": "year",
            "bands": bands_wofs_2_annual_summary,
            "resource_limits": reslim_wofs,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:6933",
                "native_resolution": [30.0, -30.0],
                "default_bands": ["count_wet"],
            },
            "styling": {
                "default_style": "water_observations",
                "styles": [
                    style_wofs_count_wet,
                ],
            },
        },
        {
            "title": "Water Observations from Space All Time Count of Clear Observations (Beta)",
            "name": "wofs_2_summary_clear",
            "abstract": """
The count of clear observations is one of the statistical summaries of the Water Observations from Space (WOfS) product that shows how many times an area could be clearly seen (I.e. not affected by clouds, shadows or other satellite observation problems). This product was used as a source layer for calculating all time water summary.

This product has a spatial resolution of 30 m and a temporal coverage of 2013 to 2019.

It is derived from Landsat 8 satellite observations as part of a provisional Landsat Collection 2 surface reflectance product.

For more information on the algorithm, see https://doi.org/10.1016/j.rse.2015.11.003

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "ga_ls8c_wofs_2_summary",
            "bands": bands_wofs_2_annual_summary,
            "resource_limits": reslim_wofs,
            "time_resolution": "year",
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "wcs": {
                "native_crs": "EPSG:6933",
                "native_resolution": [30.0, -30.0],
                "default_bands": ["count_clear"],
            },
            "styling": {
                "default_style": "annual_clear_observations",
                "styles": [
                    style_wofs_summary_clear,
                ],
            },
        },
    ],
}
