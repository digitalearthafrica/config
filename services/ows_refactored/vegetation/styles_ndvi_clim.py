from ows_refactored.common.ows_legend_cfg import (
    legend_mean_ndvi_ticks,
    legend_stddev_ndvi_ticks,
)

# colour ramps-------------------------------------
mean_cr = [
    {"value": -0.0, "color": "#000000", "alpha": 0.0},
    {"value": 0.0, "color": "#a50026", "alpha": 1.0},
    {"value": 0.1, "color": "#d73027"},
    {"value": 0.2, "color": "#f46d43"},
    {"value": 0.3, "color": "#fdae61"},
    {"value": 0.4, "color": "#fee08b"},
    {"value": 0.5, "color": "#ffffbf"},
    {"value": 0.6, "color": "#d9ef8b"},
    {"value": 0.7, "color": "#a6d96a"},
    {"value": 0.8, "color": "#66bd63"},
    {"value": 0.9, "color": "#1a9850"},
    {"value": 1.0, "color": "#006837"}
]

std_cr = [
    {"value": 0, "color": "#FFFFFF", "alpha": 0.0},
    {"value": 0.001, "color": "#000004"},
    {"value": 0.025, "color": "#0a0822"},
    {"value": 0.05, "color": "#1d1147"},
    {"value": 0.075, "color": "#36106b"},
    {"value": 0.1, "color": "#51127c"},
    {"value": 0.125, "color": "#6a1c81"},
    {"value": 0.15, "color": "#832681"},
    {"value": 0.175, "color": "#9c2e7f"},
    {"value": 0.2, "color": "#b73779"},
    {"value": 0.225, "color": "#d0416f"},
    {"value": 0.25, "color": "#e75263"},
    {"value": 0.275, "color": "#f56b5c"},
    {"value": 0.3, "color": "#fc8961"},
    {"value": 0.325, "color": "#fea772"},
    {"value": 0.35, "color": "#fec488"},
    {"value": 0.375, "color": "#fde2a3"},
    {"value": 0.4, "color": "#fcfdbf"},
]

count_cr = [
    {"value": 0, "color": "#FFFFFF", "alpha": 0.0},
    {"value": 1, "color": "#f7fbff"},
    {"value": 10, "color": "#ebf3fb"},
    {"value": 20, "color": "#deebf7"},
    {"value": 30, "color": "#d2e3f3"},
    {"value": 40, "color": "#c6dbef"},
    {"value": 50, "color": "#b2d2e8"},
    {"value": 60, "color": "#9ecae1"},
    {"value": 70, "color": "#84bcdc"},
    {"value": 80, "color": "#6baed6"},
    {"value": 90, "color": "#56a0ce"},
    {"value": 100, "color": "#4292c6"},
    {"value": 110, "color": "#3282be"},
    {"value": 120, "color": "#2171b5"},
    {"value": 130, "color": "#1461a9"},
    {"value": 160, "color": "#08519c"},
    {"value": 150, "color": "#084084"},
    {"value": 160, "color": "#08306b"},
]

# mean styles------------------------------------------------------
style_ndvi_mean_jan = {
    "name": "style_ndvi_mean_jan",
    "title": "Mean NDVI Climatology for January",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_jan"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mean_jan",
        },
    },
    "color_ramp": mean_cr,
    "legend": legend_mean_ndvi_ticks,
}

style_ndvi_mean_feb = {
    "name": "style_ndvi_mean_feb",
    "title": "Mean NDVI Climatology for February",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_feb"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mean_feb",
        },
    },
    "color_ramp": mean_cr,
    "legend": legend_mean_ndvi_ticks,
}

style_ndvi_mean_mar = {
    "name": "style_ndvi_mean_mar",
    "title": "Mean NDVI Climatology for March",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_mar"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mean_mar",
        },
    },
    "color_ramp": mean_cr,
    "legend": legend_mean_ndvi_ticks,
}

style_ndvi_mean_mar = {
    "name": "style_ndvi_mean_mar",
    "title": "Mean NDVI Climatology for March",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_mar"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mean_mar",
        },
    },
    "color_ramp": mean_cr,
    "legend": legend_mean_ndvi_ticks,
}

style_ndvi_mean_apr = {
    "name": "style_ndvi_mean_apr",
    "title": "Mean NDVI Climatology for April",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_apr"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mean_apr",
        },
    },
    "color_ramp": mean_cr,
    "legend": legend_mean_ndvi_ticks,
}

style_ndvi_mean_may = {
    "name": "style_ndvi_mean_may",
    "title": "Mean NDVI Climatology for May",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_may"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mean_may",
        },
    },
    "color_ramp": mean_cr,
    "legend": legend_mean_ndvi_ticks,
}

style_ndvi_mean_jun = {
    "name": "style_ndvi_mean_jun",
    "title": "Mean NDVI Climatology for June",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_jun"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mean_jun",
        },
    },
    "color_ramp": mean_cr,
    "legend": legend_mean_ndvi_ticks,
}

style_ndvi_mean_jul = {
    "name": "style_ndvi_mean_jul",
    "title": "Mean NDVI Climatology for July",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_jul"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mean_jul",
        },
    },
    "color_ramp": mean_cr,
    "legend": legend_mean_ndvi_ticks,
}

style_ndvi_mean_aug = {
    "name": "style_ndvi_mean_aug",
    "title": "Mean NDVI Climatology for August",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_aug"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mean_aug",
        },
    },
    "color_ramp": mean_cr,
    "legend": legend_mean_ndvi_ticks,
}

style_ndvi_mean_sep = {
    "name": "style_ndvi_mean_sep",
    "title": "Mean NDVI Climatology for September",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_sep"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mean_sep",
        },
    },
    "color_ramp": mean_cr,
    "legend": legend_mean_ndvi_ticks,
}

style_ndvi_mean_oct = {
    "name": "style_ndvi_mean_oct",
    "title": "Mean NDVI Climatology for October",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_oct"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mean_oct",
        },
    },
    "color_ramp": mean_cr,
    "legend": legend_mean_ndvi_ticks,
}

style_ndvi_mean_nov = {
    "name": "style_ndvi_mean_nov",
    "title": "Mean NDVI Climatology for November",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_nov"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mean_nov",
        },
    },
    "color_ramp": mean_cr,
    "legend": legend_mean_ndvi_ticks,
}

style_ndvi_mean_dec = {
    "name": "style_ndvi_mean_dec",
    "title": "Mean NDVI Climatology for December",
    "abstract": "Long-term Mean NDVI Climatology (1984-2020)",
    "needed_bands": ["mean_dec"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mean_dec",
        },
    },
    "color_ramp": mean_cr,
    "legend": legend_mean_ndvi_ticks,
}

# std dev styles-----------------------------------------------------
style_ndvi_std_jan = {
    "name": "style_ndvi_std_jan",
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
    "legend": legend_stddev_ndvi_ticks,
}

style_ndvi_std_feb = {
    "name": "style_ndvi_std_feb",
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
    "legend": legend_stddev_ndvi_ticks,
}

style_ndvi_std_mar = {
    "name": "style_ndvi_std_mar",
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
    "legend": legend_stddev_ndvi_ticks,
}

style_ndvi_std_apr = {
    "name": "style_ndvi_std_apr",
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
    "legend": legend_stddev_ndvi_ticks,
}

style_ndvi_std_may = {
    "name": "style_ndvi_std_may",
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
    "legend": legend_stddev_ndvi_ticks,
}

style_ndvi_std_jun = {
    "name": "style_ndvi_std_jun",
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
    "legend": legend_stddev_ndvi_ticks,
}

style_ndvi_std_jul = {
    "name": "style_ndvi_std_jul",
    "title": "Std. Dev. NDVI Climatology for July",
    "abstract": "Long-term Standard Deviation NDVI Climatology (1984-2020)",
    "needed_bands": ["stddev_jul"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "stddev_jul",
        },
    },
    "color_ramp": std_cr,
    "range": [0, 0.5],
    "legend": legend_stddev_ndvi_ticks,
}

style_ndvi_std_aug = {
    "name": "style_ndvi_std_aug",
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
    "legend": legend_stddev_ndvi_ticks,
}

style_ndvi_std_sep = {
    "name": "style_ndvi_std_sep",
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
    "legend": legend_stddev_ndvi_ticks,
}

style_ndvi_std_oct = {
    "name": "style_ndvi_std_oct",
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
    "legend": legend_stddev_ndvi_ticks,
}

style_ndvi_std_nov = {
    "name": "style_ndvi_std_nov",
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
    "legend": legend_stddev_ndvi_ticks,
}

style_ndvi_std_dec = {
    "name": "style_ndvi_std_dec",
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
    "legend": legend_stddev_ndvi_ticks,
}

# count styles-----------------------------------------------------
style_count_jan = {
    "name": "style_count_jan",
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
        "end": "160",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "160": {"suffix": "<"},
        },
    },
}

style_count_feb = {
    "name": "style_count_feb",
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
        "end": "160",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "160": {"suffix": "<"},
        },
    },
}

style_count_mar = {
    "name": "style_count_mar",
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
        "end": "160",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "160": {"suffix": "<"},
        },
    },
}

style_count_apr = {
    "name": "style_count_apr",
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
        "end": "160",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "160": {"suffix": "<"},
        },
    },
}

style_count_may = {
    "name": "style_count_may",
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
        "end": "160",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "160": {"suffix": "<"},
        },
    },
}

style_count_jun = {
    "name": "style_count_jun",
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
        "end": "160",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "160": {"suffix": "<"},
        },
    },
}

style_count_jul = {
    "name": "style_count_jul",
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
        "end": "160",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "160": {"suffix": "<"},
        },
    },
}

style_count_aug = {
    "name": "style_count_aug",
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
        "end": "160",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "160": {"suffix": "<"},
        },
    },
}

style_count_sep = {
    "name": "style_count_sep",
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
        "end": "160",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "160": {"suffix": "<"},
        },
    },
}

style_count_oct = {
    "name": "style_count_oct",
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
        "end": "160",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "160": {"suffix": "<"},
        },
    },
}

style_count_nov = {
    "name": "style_count_nov",
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
        "end": "160",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "160": {"suffix": "<"},
        },
    },
}

style_count_dec = {
    "name": "style_count_dec",
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
        "end": "160",
        "decimal_places": 0,
        "ticks_every": 20,
        "tick_labels": {
            "160": {"suffix": "<"},
        },
    },
}
