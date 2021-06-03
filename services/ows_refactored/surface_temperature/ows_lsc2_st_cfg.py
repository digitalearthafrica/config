from ows_refactored.common.ows_reslim_cfg import reslim_landsat

bands_ls5_st = {"ST_B6": ["st", "surface_temperature"], "QA_PIXEL": ["pq", "pixel_quality"]}
bands_ls7_st = {"ST_B6": ["st", "surface_temperature"], "QA_PIXEL": ["pq", "pixel_quality"]}
bands_ls8_st = {"ST_B10": ["st", "surface_temperature"], "QA_PIXEL": ["pq", "pixel_quality"]}

style_lsc2_st = {
    "name": "surface_temperature",
    "title": "Surface temperature - Celsius",
    "abstract": "Surface temperature in degrees Celsius",
    "index_expression": "(0.00341802*st - 124.15)",
    "mpl_ramp": "magma",
    "range": [-10.0, 40.0],
    "pq_masks": [
        {
            "band": "pixel_quality",
            "flags": {
                "clear": True,
                "cloud_shadow": "not_high_confidence",
                "nodata": False
            },
        },
    ],
    "legend": {
        "begin": "-10.0",
        "end": "40.0",
        "decimal_places": 0,
        "ticks": ["-10.0", "0.0", "10.0", "20.0", "30.0", "40.0"],
        "tick_labels": {
            "-10.0": {"prefix": "<"},
            "0.0": {"label": "0.0"},
            "10.0": {"label": "10.0"},
            "20.0": {"label": "20.0"},
            "30.0": {"label": "30.0"},
            "40.0": {"suffix": "<"},
        },
    },
}


layer_ls8 = {
    "title": "Surface Temperature Landsat 8 (USGS Collection 2)",
    "name": "ls8_st",
    "abstract": """
Surface temperature measures the Earth’s surface temperature and is an important geophysical parameter in global energy balance studies and hydrologic modeling. Surface temperature is also useful for monitoring crop and vegetation health, and extreme heat events such as natural disasters (e.g., volcanic eruptions, wildfires), and urban heat island effects.

DE Africa provides access to Landsat Collection 2 Level-2 Surface Temperature products over Africa. USGS Landsat Collection 2 offers improved processing, geometric accuracy, and radiometric calibration compared to previous Collection 1 products. The Level-2 products are endorsed by the Committee on Earth Observation Satellites (CEOS) to be Analysis Ready Data for Land (CARD4L)-compliant.

More techincal information about the Landsat Surface Temperature product can be found in the User Guide (https://docs.digitalearthafrica.org/en/latest/data_specs/Landsat_C2_ST_specs.html).

Landsat 8 product has a spatial resolution of 30 m and a temporal coverage of 2013 to present.

Landsat Level- 2 Surface Temperature Science Product courtesy of the U.S. Geological Survey.

For more information on Landsat products, see https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-level-2-science-products.

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
    "product_name": "ls8_st",
    "bands": bands_ls8_st,
    "dynamic": True,
    "resource_limits": reslim_landsat,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,  # True
        "apply_solar_corrections": False,
    },
    "flags": [
        {
            "product": "ls8_st",
            "band": "pixel_quality",
        },
    ],
    "wcs": {
        "native_crs": "EPSG:4326",
        "native_resolution": [30.0, -30.0],
        "default_bands": ["st", "pq"],
    },
    "styling": {
        "default_style": "surface_temperature",
        "styles": [
            style_lsc2_st,
        ],
    },
}

layer_ls7 = {
    "title": "Surface Temperature Landsat 7 (USGS Collection 2)",
    "name": "ls7_st",
    "abstract": """
Surface temperature measures the Earth’s surface temperature and is an important geophysical parameter in global energy balance studies and hydrologic modeling. Surface temperature is also useful for monitoring crop and vegetation health, and extreme heat events such as natural disasters (e.g., volcanic eruptions, wildfires), and urban heat island effects.

DE Africa provides access to Landsat Collection 2 Level-2 Surface Temperature products over Africa. USGS Landsat Collection 2 offers improved processing, geometric accuracy, and radiometric calibration compared to previous Collection 1 products. The Level-2 products are endorsed by the Committee on Earth Observation Satellites (CEOS) to be Analysis Ready Data for Land (CARD4L)-compliant.

More techincal information about the Landsat Surface Temperature product can be found in the User Guide (https://docs.digitalearthafrica.org/en/latest/data_specs/Landsat_C2_ST_specs.html).

Landsat 7 product has a spatial resolution of 30 m and a temporal coverage of 1999 to present.

Landsat Level- 2 Surface Temperature Science Product courtesy of the U.S. Geological Survey.

For more information on Landsat products, see https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-level-2-science-products.

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
    "product_name": "ls7_st",
    "bands": bands_ls7_st,
    "dynamic": True,
    "resource_limits": reslim_landsat,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,  # True
        "apply_solar_corrections": False,
    },
    "flags": [
        {
            "product": "ls7_st",
            "band": "pixel_quality",
        },
    ],
    "wcs": {
        "native_crs": "EPSG:4326",
        "native_resolution": [30.0, -30.0],
        "default_bands": ["st", "pq"],
    },
    "styling": {
        "default_style": "surface_temperature",
        "styles": [
            style_lsc2_st,
        ],
    },
}

layer_ls5 = {
    "title": "Surface Temperature Landsat 5 (USGS Collection 2)",
    "name": "ls5_st",
    "abstract": """
Surface temperature measures the Earth’s surface temperature and is an important geophysical parameter in global energy balance studies and hydrologic modeling. Surface temperature is also useful for monitoring crop and vegetation health, and extreme heat events such as natural disasters (e.g., volcanic eruptions, wildfires), and urban heat island effects.

DE Africa provides access to Landsat Collection 2 Level-2 Surface Temperature products over Africa. USGS Landsat Collection 2 offers improved processing, geometric accuracy, and radiometric calibration compared to previous Collection 1 products. The Level-2 products are endorsed by the Committee on Earth Observation Satellites (CEOS) to be Analysis Ready Data for Land (CARD4L)-compliant.

More techincal information about the Landsat Surface Temperature product can be found in the User Guide (https://docs.digitalearthafrica.org/en/latest/data_specs/Landsat_C2_ST_specs.html).

Landsat 5 product has a spatial resolution of 30 m and a temporal coverage of 1984 to 2012.

Landsat Level- 2 Surface Temperature Science Product courtesy of the U.S. Geological Survey.

For more information on Landsat products, see https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-level-2-science-products.

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
    "product_name": "ls5_st",
    "bands": bands_ls5_st,
    "resource_limits": reslim_landsat,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,  # True
        "apply_solar_corrections": False,
    },
    "flags": [
        {
            "product": "ls5_st",
            "band": "pixel_quality",
        },
    ],
    "wcs": {
        "native_crs": "EPSG:4326",
        "native_resolution": [30.0, -30.0],
        "default_bands": ["st", "pq"],
    },
    "styling": {
        "default_style": "surface_temperature",
        "styles": [
            style_lsc2_st,
        ],
    },
}
