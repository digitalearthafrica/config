from ows_refactored.common.ows_reslim_cfg import reslim_landsat

bands_ls5_st = {
    "ST_B6": ["st"],
    "ST_QA": ["st_qa"],
    "QA_PIXEL": ["pq"]
}
bands_ls7_st = {
    "ST_B6": ["st"],
    "ST_QA": ["st_qa"],
    "QA_PIXEL": ["pq"]
}
bands_ls8_st = {
    "ST_B10": ["st"],
    "ST_QA": ["st_qa"],
    "QA_PIXEL": ["pq"]
}

style_lsc2_st = {
    "name": "surface_temperature",
    "title": "Surface temperature - Celsius",
    "abstract": "Surface temperature in degrees Celsius",
    "index_expression": "(0.00341802*st - 124.15)",
    "mpl_ramp": "plasma",
    "range": [0.0, 50.0],
    "legend": {
        "begin": "0.0",
        "end": "50.0",
        "decimal_places": 1,
        "ticks": ["0.0", "10.0", "20.0", "30.0", "40.0", "50.0"],
        "tick_labels": {
            "0.0": {"prefix": "<"},
            "10.0": {"label": "10.0"},
            "20.0": {"label": "20.0"},
            "30.0": {"label": "30.0"},
            "40.0": {"label": "50.0"},
            "50.0": {"prefix": ">"},
        },
    },
}

style_lsc2_st_masked = {
    "name": "surface_temperature_masked",
    "title": "Surface temperature (cloud masked) - Celsius",
    "abstract": "Surface temperature in degrees Celsius",
    "index_expression": "(0.00341802*st - 124.15)",
    "mpl_ramp": "plasma",
    "range": [0.0, 50.0],
    "legend": {
        "begin": "0.0",
        "end": "50.0",
        "decimal_places": 1,
        "ticks": ["0.0", "10.0", "20.0", "30.0", "40.0", "50.0"],
        "tick_labels": {
            "0.0": {"prefix": "<"},
            "10.0": {"label": "10.0"},
            "20.0": {"label": "20.0"},
            "30.0": {"label": "30.0"},
            "40.0": {"label": "50.0"},
            "50.0": {"prefix": ">"},
        },
    },
}

style_lsc2_st_masked_ls8 = {
    "name": "surface_temperature_masked_ls8",
    "title": "Surface temperature (cloud masked) - Celsius",
    "abstract": "Surface temperature in degrees Celsius",
    "index_expression": "(0.00341802*st - 124.15)",
    "mpl_ramp": "plasma",
    "range": [0.0, 50.0],
    "pq_masks": [
        {
            "band": "pq",
            "flags": {
                "clear": True,
                "cirrus": "not_high_confidence"
            },
        },
    ],
    "legend": {
        "begin": "0.0",
        "end": "50.0",
        "decimal_places": 1,
        "ticks": ["0.0", "10.0", "20.0", "30.0", "40.0", "50.0"],
        "tick_labels": {
            "0.0": {"prefix": "<"},
            "10.0": {"label": "10.0"},
            "20.0": {"label": "20.0"},
            "30.0": {"label": "30.0"},
            "40.0": {"label": "50.0"},
            "50.0": {"prefix": ">"},
        },
    },
}

style_lsc2_st_qa = {
    "name": "surface_temperature_uncertainty",
    "title": "Surface temperature uncertainty - Celsius",
    "abstract": "Surface temperature uncertainty in degrees Celsius",
    "index_expression": "(0.01*st_qa)",
    "mpl_ramp": "viridis",
    "range": [0.0, 6.0],
    "legend": {
        "begin": "0.0",
        "end": "6.0",
        "decimal_places": 1,
        "ticks": ["0.0", "1.0", "2.0", "3.0", "4.0", "5.0", "6.0"],
        "tick_labels": {
            "0.0": {"label": "0.0"},
            "1.0": {"label": "1.0"},
            "2.0": {"label": "2.0"},
            "3.0": {"label": "3.0"},
            "4.0": {"label": "4.0"},
            "5.0": {"label": "5.0"},
            "6.0": {"prefix": ">"},
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
            "band": "pq",
        },
    ],
    "wcs": {
        "native_crs": "EPSG:4326",
        "native_resolution": [30.0, -30.0],
        "default_bands": ["st", "st_qa", "pq"],
    },
    "styling": {
        "default_style": "surface_temperature",
        "styles": [
            style_lsc2_st,
            style_lsc2_st_qa,
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
            "band": "pq",
        },
    ],
    "wcs": {
        "native_crs": "EPSG:4326",
        "native_resolution": [30.0, -30.0],
        "default_bands": ["st", "st_qa", "pq"],
    },
    "styling": {
        "default_style": "surface_temperature",
        "styles": [
            style_lsc2_st,
            style_lsc2_st_qa,
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
            "band": "pq",
        },
    ],
    "wcs": {
        "native_crs": "EPSG:4326",
        "native_resolution": [30.0, -30.0],
        "default_bands": ["st", "st_qa", "pq"],
    },
    "styling": {
        "default_style": "surface_temperature",
        "styles": [
            style_lsc2_st,
            style_lsc2_st_qa,
        ],
    },
}
