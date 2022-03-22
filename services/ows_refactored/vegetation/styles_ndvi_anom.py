from ows_refactored.common.ows_legend_cfg import legend_mean_ndvi_ticks

# colour ramps-------------------------------------
mean_cr = [
    {"value": -0.0, "color": "#000000", "alpha": 0.0},
    {"value": 0.0, "color": "#d73027"},
    {"value": 0.1, "color": "#f46d43"},
    {"value": 0.2, "color": "#fdae61"},
    {"value": 0.3, "color": "#fee08b"},
    {"value": 0.4, "color": "#ffffbf"},
    {"value": 0.5, "color": "#d9ef8b"},
    {"value": 0.6, "color": "#a6d96a"},
    {"value": 0.7, "color": "#66bd63"},
    {"value": 0.8, "color": "#1a9850"},
    {"value": 0.9, "color": "#006837"},
]

anomaly_cr = [
    {"value": -4.0, "color": "#543005"},
    {"value": -3.5, "color": "#774508"},
    {"value": -3.0, "color": "#995d13"},
    {"value": -2.5, "color": "#b97b29"},
    {"value": -2.0, "color": "#cfa155"},
    {"value": -1.5, "color": "#e2c786"},
    {"value": -1.0, "color": "#f0deb1"},
    {"value": -0.5, "color": "#f6edd6"},
    {"value": 0.0, "color": "#f5f5f5"},
    {"value": 0.5, "color": "#d8eeeb"},
    {"value": 1.0, "color": "#b5e3dc"},
    {"value": 1.5, "color": "#89d1c6"},
    {"value": 2.0, "color": "#5bb2a8"},
    {"value": 2.5, "color": "#2f9189"},
    {"value": 3.0, "color": "#0e726a"},
    {"value": 3.5, "color": "#01564d"},
    {"value": 4.0, "color": "#003c30"},
]

# only shows standard deviations of 2 or above
anomaly_cr_2std = [
    {"value": -4.0, "color": "#543005"},
    {"value": -3.5, "color": "#774508"},
    {"value": -3.0, "color": "#995d13"},
    {"value": -2.5, "color": "#b97b29"},
    {"value": -2.0, "color": "#cfa155", "alpha": 0.0},
    {"value": -1.5, "color": "#e2c786", "alpha": 0.0},
    {"value": -1.0, "color": "#f0deb1", "alpha": 0.0},
    {"value": -0.5, "color": "#f6edd6", "alpha": 0.0},
    {"value": 0.0, "color": "#f5f5f5", "alpha": 0.0},
    {"value": 0.5, "color": "#d8eeeb", "alpha": 0.0},
    {"value": 1.0, "color": "#b5e3dc", "alpha": 0.0},
    {"value": 1.5, "color": "#89d1c6", "alpha": 0.0},
    {"value": 2.0, "color": "#5bb2a8", "alpha": 0.0},
    {"value": 2.5, "color": "#2f9189"},
    {"value": 3.0, "color": "#0e726a"},
    {"value": 3.5, "color": "#01564d"},
    {"value": 4.0, "color": "#003c30"},
]

count_cr = [
    {"value": 0, "color": "#440154"},
    {"value": 2, "color": "#482475"},
    {"value": 4, "color": "#414487"},
    {"value": 6, "color": "#355f8d"},
    {"value": 8, "color": "#2a788e"},
    {"value": 10, "color": "#21918c"},
    {"value": 12, "color": "#22a884"},
    {"value": 14, "color": "#44bf70"},
    {"value": 16, "color": "#7ad151"},
    {"value": 18, "color": "#bddf26"},
    {"value": 20, "color": "#fde725"},
]

# mean styles------------------------------------------------------
style_ndvi_mean = {
    "name": "style_ndvi_mean",
    "title": "Mean NDVI",
    "abstract": "Mean NDVI for the month",
    "needed_bands": ["ndvi_mean"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "ndvi_mean",
        },
    },
    "color_ramp": mean_cr,
    "legend": legend_mean_ndvi_ticks,
}

# std dev styles-----------------------------------------------------
style_ndvi_anomaly = {
    "name": "style_ndvi_anomaly",
    "title": "Standardised NDVI Anomaly",
    "abstract": "Standardised NDVI Anomaly",
    "needed_bands": ["ndvi_std_anomaly"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "ndvi_std_anomaly",
        },
    },
    "color_ramp": anomaly_cr,
    "range": [0, 0.5],
    "legend": {
        "begin": "-4",
        "end": "4",
        "decimal_places": 1,
        "ticks_every": 1,
    },
}

# only shows standard deviations of 2 or above
style_ndvi_anomaly_2std = {
    "name": "style_ndvi_anomaly_2std",
    "title": "Standardised NDVI Anomaly",
    "abstract": "Standardised NDVI Anomaly",
    "needed_bands": ["ndvi_std_anomaly"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "ndvi_std_anomaly",
        },
    },
    "color_ramp": anomaly_cr_2std,
    "range": [0, 0.5],
    "legend": {
        "begin": "-4",
        "end": "4",
        "decimal_places": 1,
        "ticks_every": 1,
    },
}

# count styles-----------------------------------------------------
style_count = {
    "name": "style_count",
    "title": "Clear observation count",
    "abstract": "Count of valid observations included in calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "clear_count",
        },
    },
    "needed_bands": ["clear_count"],
    "include_in_feature_info": False,
    "color_ramp": count_cr,
    "legend": {
        "begin": "0",
        "end": "20",
        "decimal_places": 0,
        "ticks_every": 5,
        "tick_labels": {
            "20": {"suffix": "<"},
        },
    },
}
