from ows_refactored.common.ows_legend_cfg import legend_idx_percentage_by_10
from ows_refactored.common.ows_reslim_cfg import reslim_wofs
from ows_refactored.wofs.band_wofs_cfg import bands_wofs_summary

style_wofs_summary_wet = {
    "name": "water_summary_wet",
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
    "color_ramp": [
        {"value": 0, "color": "#666666", "alpha": 0},
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 0.2,
            "color": "#890000",
            "alpha": 1,
        },
        {"value": 20, "color": "#990000"},
        {"value": 30, "color": "#E38400"},
        {"value": 40, "color": "#E3DF00"},
        {"value": 50, "color": "#A6E300"},
        {"value": 60, "color": "#00E32D"},
        {"value": 70, "color": "#00E3C8"},
        {"value": 80, "color": "#0097E3"},
        {"value": 90, "color": "#005FE3"},
        {"value": 100, "color": "#000FE3"},
        {"value": 110, "color": "#000EA9"},
        {"value": 120, "color": "#5700E3"},
    ],
    "legend": {
        "begin": "0",
        "end": "120",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "120": {"prefix": ">"},
        },
    },
}

style_wofs_summary_frequency = {
    "name": "wofs_summary_frequency",
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
    "color_ramp": [
        {"value": 0.0, "color": "#000000", "alpha": 0.0},
        {"value": 0.002, "color": "#000000", "alpha": 0.0},
        {"value": 0.005, "color": "#8e0101", "alpha": 0.25},
        {"value": 0.01, "color": "#cf2200", "alpha": 0.75},
        {"value": 0.02, "color": "#e38400"},
        {"value": 0.05, "color": "#e3df00"},
        {"value": 0.1, "color": "#a6e300"},
        {"value": 0.2, "color": "#62e300"},
        {"value": 0.3, "color": "#00e32d"},
        {"value": 0.4, "color": "#00e384"},
        {"value": 0.5, "color": "#00e3c8"},
        {"value": 0.6, "color": "#00c5e3"},
        {"value": 0.7, "color": "#0097e3"},
        {"value": 0.8, "color": "#005fe3"},
        {"value": 0.9, "color": "#000fe3"},
        {"value": 1.0, "color": "#5700e3"},
    ],
    "legend": {
        "url": "https://data.dea.ga.gov.au/WOfS/filtered_summary/v2.1.0/wofs_full_summary_legend.png",
    },
}


style_wofs_summary_frequency_blue = {
    "name": "wofs_summary_frequency_blue",
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

style_wofs_summary_clear = {
    "name": "wofs_summary_clear",
    "title": "Count of clear",
    "abstract": "WOfS summary showing the count of clear observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_clear",
        },
    },
    "needed_bands": ["count_clear"],
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
        {"value": 20, "color": "#B21800"},
        {"value": 30, "color": "#ef8500"},
        {"value": 40, "color": "#ffb800"},
        {"value": 60, "color": "#ffd000"},
        {"value": 80, "color": "#fff300"},
        {"value": 100, "color": "#fff300"},
        {"value": 120, "color": "#c1ec00"},
        {"value": 140, "color": "#6ee100"},
        {"value": 160, "color": "#39a500"},
        {"value": 180, "color": "#026900"},
    ],
    "legend": {
        "begin": "0",
        "end": "180",
        "decimal_places": 0,
        "ticks_every": 20,
        "legend_strip_location": [0.05, 0.5, 0.89, 0.15],
        "tick_labels": {
            "180": {"prefix": ">"},
        },
    },
}


layer = {
    "title": "Water Observations from Space All Time Summary",
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
    "wcs": {
        "native_crs": "EPSG:6933",
        "native_resolution": [30.0, -30.0],
        "default_bands": ["frequency"],
    },
    "styling": {
        "default_style": "wofs_summary_frequency",
        "styles": [
            style_wofs_summary_frequency,
            style_wofs_summary_frequency_blue,
            style_wofs_summary_wet,
            style_wofs_summary_clear,
        ],
    },
}
