from ows_refactored.common.ows_reslim_cfg import reslim_wms_min_zoom_15
from ows_refactored.common.ows_legend_cfg import legend_idx_0_1_5ticks, legend_stddev_ticks

bands_ndvi_clim = {
    "mean_jan": [],
    "mean_feb": [],
    "mean_mar": [],
    "mean_apr": [],
    "mean_may": [],
    "mean_jun": [],
    "mean_jul": [],
    "mean_aug": [],
    "mean_sep": [],
    "mean_oct": [],
    "mean_nov": [],
    "mean_dec": [],
    "stddev_jan": [],
    "stddev_feb": [],
    "stddev_mar": [],
    "stddev_apr": [],
    "stddev_may": [],
    "stddev_jun": [],
    "stddev_jul": [],
    "stddev_aug": [],
    "stddev_sep": [],
    "stddev_oct": [],
    "stddev_nov": [],
    "stddev_dec": [],
    "count_jan": [],
    "count_feb": [],
    "count_mar": [],
    "count_apr": [],
    "count_may": [],
    "count_jun": [],
    "count_jul": [],
    "count_aug": [],
    "count_sep": [],
    "count_oct": [],
    "count_nov": [],
    "count_dec": [],
}

# colour ramps-------------------------------------
mean_cr = [
    {"value": -0.0, "color": "#8F3F20", "alpha": 0.0},
    {"value": 0.0, "color": "#8F3F20", "alpha": 1.0},
    {"value": 0.1, "color": "#A35F18"},
    {"value": 0.2, "color": "#B88512"},
    {"value": 0.3, "color": "#CEAC0E"},
    {"value": 0.4, "color": "#E5D609"},
    {"value": 0.5, "color": "#FFFF0C"},
    {"value": 0.6, "color": "#C3DE09"},
    {"value": 0.7, "color": "#88B808"},
    {"value": 0.8, "color": "#529400"},
    {"value": 0.9, "color": "#237100"},
    {"value": 1.0, "color": "#114D04"},
]

std_cr = [
    {"value": 0,"color": "black","alpha": 0.0},
    {"value": 0.05,"color": "#010007"},
    {"value": 0.10,"color": "#170b3b"},
    {"value": 0.15,"color": "#410967"},
    {"value": 0.20,"color": "#6b176e"},
    {"value": 0.25,"color": "#952666"},
    {"value": 0.30,"color": "#bb3754"},
    {"value": 0.35,"color": "#dd5238"},
    {"value": 0.40,"color": "#f37719"},
    {"value": 0.45,"color": "#fba60b"},
    {"value": 0.5,"color": "#f5d948"},
]

count_cr = [
        {"value": 0, "color": "#666666", "alpha": 0},
        {"value": 0.2,"color": "#FFFFFF", "alpha": 1},
        {"value": 10, "color": "#f3fabf"},
        {"value": 20, "color": "#e1f3b2"},
        {"value": 30, "color": "#c6e9b4"},
        {"value": 40, "color": "#97d6b9"},
        {"value": 50, "color": "#6bc6be"},
        {"value": 60, "color": "#42b6c4"},
        {"value": 70, "color": "#299dc1"},
        {"value": 80, "color": "#1f80b8"},
        {"value": 90, "color": "#225da8"},
        {"value": 100, "color": "#24419a"},
        {"value": 110, "color": "#1b2c80"},
        {"value": 120, "color": "#081d58"},
        {"value": 140, "color": "#071743"},
    ]

# mean styles------------------------------------------------------
style_ndvi_mean_jan = {
    "name": "Mean NDVI Climatology for January",
    "title": "Mean NDVI Climatology for January",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_jan"],
    "color_ramp": mean_cr,
    "legend": legend_idx_0_1_5ticks,
}

style_ndvi_mean_feb = {
    "name": "Mean NDVI Climatology for February",
    "title": "Mean NDVI Climatology for February",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_feb"],
    "color_ramp": mean_cr,
    "legend": legend_idx_0_1_5ticks,
}

style_ndvi_mean_mar = {
    "name": "Mean NDVI Climatology for March",
    "title": "Mean NDVI Climatology for March",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_mar"],
    "color_ramp": mean_cr,
    "legend": legend_idx_0_1_5ticks,
}

style_ndvi_mean_mar = {
    "name": "Mean NDVI Climatology for March",
    "title": "Mean NDVI Climatology for March",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_mar"],
    "color_ramp": mean_cr,
    "legend": legend_idx_0_1_5ticks,
}

style_ndvi_mean_apr = {
    "name": "Mean NDVI Climatology for April",
    "title": "Mean NDVI Climatology for April",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_apr"],
    "color_ramp": mean_cr,
    "legend": legend_idx_0_1_5ticks,
}

style_ndvi_mean_may = {
    "name": "Mean NDVI Climatology for May",
    "title": "Mean NDVI Climatology for May",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_may"],
    "color_ramp": mean_cr,
    "legend": legend_idx_0_1_5ticks,
}

style_ndvi_mean_jun = {
    "name": "Mean NDVI Climatology for June",
    "title": "Mean NDVI Climatology for June",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_jun"],
    "color_ramp": mean_cr,
    "legend": legend_idx_0_1_5ticks,
}

style_ndvi_mean_jul = {
    "name": "Mean NDVI Climatology for July",
    "title": "Mean NDVI Climatology for July",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_jul"],
    "color_ramp": mean_cr,
    "legend": legend_idx_0_1_5ticks,
}

style_ndvi_mean_aug = {
    "name": "Mean NDVI Climatology for August",
    "title": "Mean NDVI Climatology for August",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_aug"],
    "color_ramp": mean_cr,
    "legend": legend_idx_0_1_5ticks,
}

style_ndvi_mean_sep = {
    "name": "Mean NDVI Climatology for September",
    "title": "Mean NDVI Climatology for September",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_sep"],
    "color_ramp": mean_cr,
    "legend": legend_idx_0_1_5ticks,
}

style_ndvi_mean_oct = {
    "name": "Mean NDVI Climatology for October",
    "title": "Mean NDVI Climatology for October",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_oct"],
    "color_ramp": mean_cr,
    "legend": legend_idx_0_1_5ticks,
}

style_ndvi_mean_nov = {
    "name": "Mean NDVI Climatology for November",
    "title": "Mean NDVI Climatology for November",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_nov"],
    "color_ramp": mean_cr,
    "legend": legend_idx_0_1_5ticks,
}

style_ndvi_mean_dec = {
    "name": "Mean NDVI Climatology for December",
    "title": "Mean NDVI Climatology for December",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_dec"],
    "color_ramp": mean_cr,
    "legend": legend_idx_0_1_5ticks,
}

# std dev styles-----------------------------------------------------
style_ndvi_std_jan = {
    "name": "Std. Dev. NDVI Climatology for January",
    "title": "Std. Dev. NDVI Climatology for January",
    "abstract": "Long-term Standard Deviation NDVI Climatology (1984-2020)",
    "needed_bands": ["stddev_jan"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "stddev_jan",
        },
    },
    "color_ramp": std_cr,
    "range": [0, 0.5],
    "legend": legend_stddev_ticks
}

style_ndvi_std_feb = {
    "name": "Std. Dev. NDVI Climatology for February",
    "title": "Std. Dev. NDVI Climatology for February",
    "abstract": "Long-term Standard Deviation NDVI Climatology (1984-2020)",
    "needed_bands": ["stddev_feb"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "stddev_feb",
        },
    },
    "color_ramp": std_cr,
    "range": [0, 0.5],
    "legend": legend_stddev_ticks
}

style_ndvi_std_mar = {
    "name": "Std. Dev. NDVI Climatology for March",
    "title": "Std. Dev. NDVI Climatology for March",
    "abstract": "Long-term Standard Deviation NDVI Climatology (1984-2020)",
    "needed_bands": ["stddev_mar"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "stddev_mar",
        },
    },
    "color_ramp": std_cr,
    "range": [0, 0.5],
    "legend": legend_stddev_ticks
}

style_ndvi_std_apr = {
    "name": "Std. Dev. NDVI Climatology for April",
    "title": "Std. Dev. NDVI Climatology for April",
    "abstract": "Long-term Standard Deviation NDVI Climatology (1984-2020)",
    "needed_bands": ["stddev_apr"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "stddev_apr",
        },
    },
    "color_ramp": std_cr,
    "range": [0, 0.5],
    "legend": legend_stddev_ticks
}

style_ndvi_std_may = {
    "name": "Std. Dev. NDVI Climatology for May",
    "title": "Std. Dev. NDVI Climatology for May",
    "abstract": "Long-term Standard Deviation NDVI Climatology (1984-2020)",
    "needed_bands": ["stddev_may"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "stddev_may",
        },
    },
    "color_ramp": std_cr,
    "range": [0, 0.5],
    "legend": legend_stddev_ticks
}

style_ndvi_std_jun = {
    "name": "Std. Dev. NDVI Climatology for June",
    "title": "Std. Dev. NDVI Climatology for June",
    "abstract": "Long-term Standard Deviation NDVI Climatology (1984-2020)",
    "needed_bands": ["stddev_jun"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "stddev_jun",
        },
    },
    "color_ramp": std_cr,
    "range": [0, 0.5],
    "legend": legend_stddev_ticks
}

style_ndvi_std_jul = {
    "name": "Std. Dev. NDVI Climatology for July",
    "title": "Std. Dev. NDVI Climatology for July",
    "abstract": "Long-term Standard Deviation NDVI Climatology (1984-2020)",
    "needed_bands": ["stddev_jul"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "stddev_jun",
        },
    },
    "color_ramp": std_cr,
    "range": [0, 0.5],
    "legend": legend_stddev_ticks
}

style_ndvi_std_aug = {
    "name": "Std. Dev. NDVI Climatology for August",
    "title": "Std. Dev. NDVI Climatology for August",
    "abstract": "Long-term Standard Deviation NDVI Climatology (1984-2020)",
    "needed_bands": ["stddev_aug"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "stddev_aug",
        },
    },
    "color_ramp": std_cr,
    "range": [0, 0.5],
    "legend": legend_stddev_ticks
}

style_ndvi_std_sep = {
    "name": "Std. Dev. NDVI Climatology for Septemeber",
    "title": "Std. Dev. NDVI Climatology for September",
    "abstract": "Long-term Standard Deviation NDVI Climatology (1984-2020)",
    "needed_bands": ["stddev_sep"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "stddev_sep",
        },
    },
    "color_ramp": std_cr,
    "range": [0, 0.5],
    "legend": legend_stddev_ticks
}

style_ndvi_std_oct = {
    "name": "Std. Dev. NDVI Climatology for October",
    "title": "Std. Dev. NDVI Climatology for October",
    "abstract": "Long-term Standard Deviation NDVI Climatology (1984-2020)",
    "needed_bands": ["stddev_oct"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "stddev_oct",
        },
    },
    "color_ramp": std_cr,
    "range": [0, 0.5],
    "legend": legend_stddev_ticks
}

style_ndvi_std_nov = {
    "name": "Std. Dev. NDVI Climatology for November",
    "title": "Std. Dev. NDVI Climatology for November",
    "abstract": "Long-term Standard Deviation NDVI Climatology (1984-2020)",
    "needed_bands": ["stddev_nov"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "stddev_nov",
        },
    },
    "color_ramp": std_cr,
    "range": [0, 0.5],
    "legend": legend_stddev_ticks
}

style_ndvi_std_dec = {
    "name": "Std. Dev. NDVI Climatology for December",
    "title": "Std. Dev. NDVI Climatology for December",
    "abstract": "Long-term Standard Deviation NDVI Climatology (1984-2020)",
    "needed_bands": ["stddev_dec"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "stddev_dec",
        },
    },
    "color_ramp": std_cr,
    "range": [0, 0.5],
    "legend": legend_stddev_ticks
}

# count styles-----------------------------------------------------
style_count_jan = {
    "name": "Clear count for January",
    "title": "Clear observation count for January",
    "abstract": "Count of valid observations included in calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_jan",
        },
    },
    "needed_bands": ["count_jan"],
    "include_in_feature_info": False,
    "color_ramp": count_cr,
    "legend": {
        "begin": "0",
        "end": "140",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "140": {"suffix": "<"},
        },
    },
}

style_count_feb = {
    "name": "Clear count for February",
    "title": "Clear observation count for February",
    "abstract": "Count of valid observations included in calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_feb",
        },
    },
    "needed_bands": ["count_feb"],
    "include_in_feature_info": False,
    "color_ramp": count_cr,
    "legend": {
        "begin": "0",
        "end": "140",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "140": {"suffix": "<"},
        },
    },
}

style_count_mar = {
    "name": "Clear count for March",
    "title": "Clear observation count for March",
    "abstract": "Count of valid observations included in calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_mar",
        },
    },
    "needed_bands": ["count_mar"],
    "include_in_feature_info": False,
    "color_ramp": count_cr,
    "legend": {
        "begin": "0",
        "end": "140",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "140": {"suffix": "<"},
        },
    },
}

style_count_apr = {
    "name": "Clear count for April",
    "title": "Clear observation count for April",
    "abstract": "Count of valid observations included in calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_apr",
        },
    },
    "needed_bands": ["count_apr"],
    "include_in_feature_info": False,
    "color_ramp": count_cr,
    "legend": {
        "begin": "0",
        "end": "140",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "140": {"suffix": "<"},
        },
    },
}

style_count_may = {
    "name": "Clear count for May",
    "title": "Clear observation count for May",
    "abstract": "Count of valid observations included in calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_may",
        },
    },
    "needed_bands": ["count_may"],
    "include_in_feature_info": False,
    "color_ramp": count_cr,
    "legend": {
        "begin": "0",
        "end": "140",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "140": {"suffix": "<"},
        },
    },
}

style_count_jun = {
    "name": "Clear count for June",
    "title": "Clear observation count for June",
    "abstract": "Count of valid observations included in calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_jun",
        },
    },
    "needed_bands": ["count_jun"],
    "include_in_feature_info": False,
    "color_ramp": count_cr,
    "legend": {
        "begin": "0",
        "end": "140",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "140": {"suffix": "<"},
        },
    },
}

style_count_jul = {
    "name": "Clear count for July",
    "title": "Clear observation count for July",
    "abstract": "Count of valid observations included in calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_jul",
        },
    },
    "needed_bands": ["count_jul"],
    "include_in_feature_info": False,
    "color_ramp": count_cr,
    "legend": {
        "begin": "0",
        "end": "140",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "140": {"suffix": "<"},
        },
    },
}

style_count_aug = {
    "name": "Clear count for August",
    "title": "Clear observation count for August",
    "abstract": "Count of valid observations included in calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_aug",
        },
    },
    "needed_bands": ["count_aug"],
    "include_in_feature_info": False,
    "color_ramp": count_cr,
    "legend": {
        "begin": "0",
        "end": "140",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "140": {"suffix": "<"},
        },
    },
}

style_count_sep = {
    "name": "Clear count for September",
    "title": "Clear observation count for September",
    "abstract": "Count of valid observations included in calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_sep",
        },
    },
    "needed_bands": ["count_sep"],
    "include_in_feature_info": False,
    "color_ramp": count_cr,
    "legend": {
        "begin": "0",
        "end": "140",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "140": {"suffix": "<"},
        },
    },
}

style_count_oct = {
    "name": "Clear count for October",
    "title": "Clear observation count for October",
    "abstract": "Count of valid observations included in calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_oct",
        },
    },
    "needed_bands": ["count_oct"],
    "include_in_feature_info": False,
    "color_ramp": count_cr,
    "legend": {
        "begin": "0",
        "end": "140",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "140": {"suffix": "<"},
        },
    },
}

style_count_nov = {
    "name": "Clear count for November",
    "title": "Clear observation count for November",
    "abstract": "Count of valid observations included in calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_nov",
        },
    },
    "needed_bands": ["count_nov"],
    "include_in_feature_info": False,
    "color_ramp": count_cr,
    "legend": {
        "begin": "0",
        "end": "140",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "140": {"suffix": "<"},
        },
    },
}

style_count_dec = {
    "name": "Clear count for December",
    "title": "Clear observation count for December",
    "abstract": "Count of valid observations included in calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_dec",
        },
    },
    "needed_bands": ["count_dec"],
    "include_in_feature_info": False,
    "color_ramp": count_cr,
    "legend": {
        "begin": "0",
        "end": "140",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "140": {"suffix": "<"},
        },
    },
}

#---------------------------------------------
layer = {
    "title": "NDVI Climatologies",
    "name": "ndvi_climatology_ls",
    "abstract": """

Standardised NDVI Anomalies provide a measure of vegetation health relative to long term average conditions by measuring the departure, in units of standard devaiations, away from the long-term average. These NDVI climatologies (both mean and standard deviation) represent the long-term average conditions of vegetation condition. NDVI climatologies are available for each month, and were calculated by aggregating data from 1984-2020.

""",
    "product_name": "ndvi_climatology_ls",
    "time_resolution": "year",
    "bands": bands_ndvi_clim,
    "resource_limits": reslim_wms_min_zoom_15,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:6933",
    "native_resolution": [30, -30],
    "styling": {
        "default_style": "style_ndvi_mean_jan",
        "styles": [style_ndvi_mean_jan,
                   style_ndvi_mean_feb,
                   style_ndvi_mean_mar,
                   style_ndvi_mean_apr,
                   style_ndvi_mean_may,
                   style_ndvi_mean_jun,
                   style_ndvi_mean_jul,
                   style_ndvi_mean_aug,
                   style_ndvi_mean_sep,
                   style_ndvi_mean_oct,
                   style_ndvi_mean_nov,
                   style_ndvi_mean_dev,
                   style_ndvi_std_jan,
                   style_ndvi_std_feb,
                   style_ndvi_std_mar,
                   style_ndvi_std_apr,
                   style_ndvi_std_may,
                   style_ndvi_std_jun,
                   style_ndvi_std_jul,
                   style_ndvi_std_aug,
                   style_ndvi_std_sep,
                   style_ndvi_std_oct,
                   style_ndvi_std_nov,
                   style_ndvi_std_dec,
                   style_count_jan,
                   style_count_feb,
                   style_count_mar,
                   style_count_apr,
                   style_count_may,
                   style_count_jun,
                   style_count_jul,
                   style_count_aug,
                   style_count_sep,
                   style_count_oct,
                   style_count_nov,
                   style_count_dec
                  ],
    },
}
