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

# mean ------------------------------------------------------
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


# std dev -----------------------------------------------------
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

# count -----------------------------------------------------
style_count = {
    "name": "count",
    "title": "Clear observation count",
    "abstract": "Count of valid observations included in calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count",
        },
    },
    "needed_bands": ["count"],
    "include_in_feature_info": False,
    "color_ramp": ,
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


layer = {
    "title": "NDVI Climatologies",
    "name": "ndvi_climatology_ls",
    "abstract": """

Enter layer description

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
        "default_style": "style_ndvi_mean",
        "styles": [style_ndvi_mean, style_ndvi_std, style_ndvi_count],
    },
}
