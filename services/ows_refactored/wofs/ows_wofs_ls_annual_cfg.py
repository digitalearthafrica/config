from ows_refactored.common.ows_legend_cfg import legend_idx_percentage_by_10
from ows_refactored.common.ows_reslim_cfg import reslim_wofs
from ows_refactored.wofs.band_wofs_cfg import bands_wofs_summary

style_wofs_summary_annual_wet = {
    "name": "wofs_summary_annual_wet",
    "title": "Count of wet",
    "abstract": "WOfS summary showing the count of water observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_wet",
        },
    },
    "needed_bands": ["count_wet"],
    "include_in_feature_info": False,
    "color_ramp": [
        {"value": 0, "color": "#666666", "alpha": 0},
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 0.2,
            "color": "#990000",
            "alpha": 1,
        },
        {"value": 2, "color": "#990000"},
        {"value": 4, "color": "#E38400"},
        {"value": 6, "color": "#E3DF00"},
        {"value": 8, "color": "#00E32D"},
        {"value": 10, "color": "#00E3C8"},
        {"value": 12, "color": "#0097E3"},
        {"value": 14, "color": "#005FE3"},
        {"value": 16, "color": "#000FE3"},
        {"value": 18, "color": "#000EA9"},
        {"value": 20, "color": "#5700E3"},
    ],
    "legend": {
        "begin": 0,
        "end": 20,
        "decimal_places": 0,
        "ticks_every": 10,
        "tick_labels": {
            "20": {"prefix": ">"},
        },
    },
}

style_wofs_summary_annual_frequency = {
    "name": "wofs_summary_annual_frequency",
    "title": " Water frequency",
    "abstract": "WOfS summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
    "needed_bands": ["frequency"],
    "include_in_feature_info": False,
    "color_ramp": [
        {"value": 0.0, "color": "#000000", "alpha": 0.0},
        {"value": 0.02, "color": "#000000", "alpha": 0.0},
        {"value": 0.05, "color": "#8e0101", "alpha": 0.25},
        {"value": 0.1, "color": "#cf2200", "alpha": 0.75},
        {"value": 0.2, "color": "#e38400"},
        {"value": 0.3, "color": "#e3df00"},
        {"value": 0.4, "color": "#a6e300"},
        {"value": 0.5, "color": "#00e32d"},
        {"value": 0.6, "color": "#00e3c8"},
        {"value": 0.7, "color": "#0097e3"},
        {"value": 0.8, "color": "#005fe3"},
        {"value": 0.9, "color": "#000fe3"},
        {"value": 1.0, "color": "#5700e3"},
    ],
    "legend": legend_idx_percentage_by_10,
}

style_wofs_summary_annual_frequency_blue = {
    "name": "wofs_summary_annual_frequency_blue",
    "title": "Water frequency (Blue)",
    "abstract": "WOfS summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
    "needed_bands": ["frequency"],
    "include_in_feature_info": False,
    "color_ramp": [
        {
            "value": 0.0,
            "color": "#ffffff",
            "alpha": 0.0,
        },
        {
            "value": 0.001,
            "color": "#d5fef9",
            "alpha": 0.0,
        },
        {
            "value": 0.02,
            "color": "#d5fef9",
        },
        {"value": 0.2, "color": "#71e3ff"},
        {"value": 0.4, "color": "#01ccff"},
        {"value": 0.6, "color": "#0178ff"},
        {"value": 0.8, "color": "#2701ff"},
        {"value": 1.0, "color": "#5700e3"},
    ],
    "legend": legend_idx_percentage_by_10,
}

style_wofs_summary_annual_clear = {
    "name": "wofs_summary_annual_clear",
    "title": "Count of clear",
    "abstract": "WOfS annual summary showing the count of clear observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_clear",
        },
    },
    "needed_bands": ["count_clear"],
    "include_in_feature_info": False,
    "color_ramp": [
        {"value": 0, "color": "#FFFFFF", "alpha": 0},
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 0,
            "color": "#B21800",
            "alpha": 1,
        },
        {"value": 3, "color": "#B21800"},
        {"value": 6, "color": "#ef8500"},
        {"value": 10, "color": "#ffb800"},
        {"value": 12, "color": "#ffd000"},
        {"value": 15, "color": "#fff300"},
        {"value": 18, "color": "#fff300"},
        {"value": 20, "color": "#c1ec00"},
        {"value": 24, "color": "#6ee100"},
        {"value": 27, "color": "#39a500"},
        {"value": 30, "color": "#026900"},
    ],
    "legend": {
        "begin": "0",
        "end": "30",
        "decimal_places": 0,
        "ticks_every": 10,
        "tick_labels": {
            "30": {"prefix": ">"},
        },
    },
}


layer = {
    "title": "Water Observations from Space Annual Summary",
    "name": "wofs_ls_summary_annual",
    "abstract": """
Annual water summary is one of the statistical summaries of the Water Observation from Space (WOfS) product that shows what percentage of clear observations were detected as wet (ie. the ration of wet to clear as a percentage) from each calendar year.

This product has a spatial resolution of 30 m and a temporal coverage of 1980s to last calender year.

It is derived from Landsat Collection 2 surface reflectance product.

The annual summaries can be used to understand year to year changes in surface water extent.

WOfS shows surface water on the day and time that satellite passed overhead, which might be before, during or after a flood peak. Given the time between satellite passes (approximately once every 16 days) it is unlikely that the satellite will capture the maximum extent of any given flood. Instead, it aims to provide large scale, regional information on surface water.

For more information on the algorithm, see https://doi.org/10.1016/j.rse.2015.11.003

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
    "product_name": "wofs_ls_summary_annual",
    "time_resolution": "year",
    "bands": bands_wofs_summary,
    "resource_limits": reslim_wofs,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "wcs": {
        "native_crs": "EPSG:6933",
        "native_resolution": [30.0, -30.0],
        "default_bands": ["frequency", "count_wet", "count_clear"],
    },
    "styling": {
        "default_style": "wofs_summary_annual_frequency",
        "styles": [
            style_wofs_summary_annual_frequency,
            style_wofs_summary_annual_frequency_blue,
            style_wofs_summary_annual_wet,
            style_wofs_summary_annual_clear,
        ],
    },
}
