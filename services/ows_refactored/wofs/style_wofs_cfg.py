from ows_refactored.common.ows_legend_cfg import legend_idx_percentage_by_10

style_wofs_count_wet = {
    "name": "water_observations",
    "title": "Count Wet",
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

style_wofs_water_annual_wet = {
    "name": "water_observations",
    "title": "Count Wet",
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
        "ticks_every": 10,
        "tick_labels": {
            "20": {"prefix": ">"},
        },
    },
}

style_wofs_frequency = {
    "name": "WOfS_frequency",
    "title": " Water Summary",
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

style_wofs_annual_summary_frequency = {
    "name": "WOfS_frequency",
    "title": " Water Summary",
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

style_wofs_annual_frequency = {
    "name": "WOfS_frequency",
    "title": " Water Summary",
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
    "legend": legend_idx_percentage_by_10,
}

style_wofs_frequency_blue = {
    "name": "WOfS_frequency_blues_transparent",
    "title": "Water Summary (Blue)",
    "abstract": "WOfS summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
    "include_in_feature_info": False,
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

style_wofs_annual_summary_frequency_blue = {
    "name": "WOfS_frequency_blues_transparent",
    "title": "Water Summary (Blue)",
    "abstract": "WOfS summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
    "include_in_feature_info": False,
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

style_wofs_annual_frequency_blue = {
    "name": "WOfS_frequency_blues_transparent",
    "title": "Water Summary (Blue)",
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
    "name": "annual_clear_observations",
    "title": "Clear Count",
    "abstract": "WOfS annual summary showing the count of clear observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_clear",
        },
    },
    "include_in_feature_info": False,
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

style_wofs_beta_summary_clear = {
    "name": "annual_clear_observations",
    "title": "Clear Count",
    "abstract": "WOfS annual summary showing the count of clear observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_clear",
        },
    },
    "include_in_feature_info": False,
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

# The only layer that uses this style is disabled
# style_wofs_annual_clear = {
#     "name": "annual_clear_observations",
#     "title": "Clear Count",
#     "abstract": "WOfS annual summary showing the count of clear observations",
#     "needed_bands": ["count_dry"],
#     "index_function": {
#         "function": "datacube_ows.band_utils.single_band",
#         "mapped_bands": True,
#         "kwargs": {
#             "band": "count_dry",
#         }
#     },
#     "color_ramp": [
#         {
#             "value": 0,
#             "color": "#FFFFFF",
#             "alpha": 0
#         },
#         {
#             # purely for legend display
#             # we should not get fractional
#             # values in this styles
#             "value": 0.2,
#             "color": "#B21800",
#             "alpha": 1
#         },
#         {
#             "value": 1,
#             "color": "#B21800"
#         },
#         {
#             "value": 6,
#             "color": "#ef8500"
#         },
#         {
#             "value": 10,
#             "color": "#ffb800"
#         },
#         {
#             "value": 14,
#             "color": "#ffd000"
#         },
#         {
#             "value": 18,
#             "color": "#fff300"
#         },
#         {
#             "value": 22,
#             "color": "#fff300"
#         },
#         {
#             "value": 28,
#             "color": "#c1ec00"
#         },
#         {
#             "value": 32,
#             "color": "#6ee100"
#         },
#         {
#             "value": 36,
#             "color": "#39a500"
#         },
#         {
#             "value": 40,
#             "color": "#026900",
#             "legend": {
#                 "prefix": ">"
#             }
#         }
#     ],
#     "legend": {
#         "radix_point": 0,
#         "scale_by": 1,
#         "major_ticks": 10,
#         "axes_position": [0.05, 0.5, 0.89, 0.15]
#     }
# }

style_annual_wofs_summary_frequency = {
    "name": "annual_WOfS_frequency",
    "title": "Water Summary",
    "abstract": "WOfS annual summary showing the frequency of Wetness",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["frequency"],
    "color_ramp": [
        {"value": 0.0, "color": "#000000", "alpha": 0.0},
        {"value": 0.02, "color": "#000000", "alpha": 0.0},
        {"value": 0.05, "color": "#8e0101", "alpha": 0.25},
        {"value": 0.1, "color": "#cf2200", "alpha": 0.75},
        {"value": 0.2, "color": "#e38400"},
        {"value": 0.3, "color": "#e3df00"},
        {"value": 0.4, "color": "#62e300"},
        {"value": 0.5, "color": "#00e32d"},
        {"value": 0.6, "color": "#00e3c8"},
        {"value": 0.7, "color": "#0097e3"},
        {"value": 0.8, "color": "#005fe3"},
        {"value": 0.9, "color": "#000fe3"},
        {"value": 1.0, "color": "#5700e3"},
    ],
    "legend": legend_idx_percentage_by_10,
}

style_seasonal_wofs_summary_frequency = {
    "name": "seasonal_WOfS_frequency",
    "title": " Water Summary",
    "abstract": "WOfS seasonal summary showing the frequency of Wetness",
    "needed_bands": ["frequency"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "frequency",
        },
    },
    "color_ramp": [
        {"value": 0.0, "color": "#000000", "alpha": 0.0},
        {"value": 0.02, "color": "#000000", "alpha": 0.0},
        {"value": 0.05, "color": "#8e0101", "alpha": 0.25},
        {"value": 0.1, "color": "#cf2200", "alpha": 0.75},
        {"value": 0.2, "color": "#e38400"},
        {"value": 0.3, "color": "#e3df00"},
        {"value": 0.4, "color": "#62e300"},
        {"value": 0.5, "color": "#00e32d"},
        {"value": 0.6, "color": "#00e3c8"},
        {"value": 0.7, "color": "#0097e3"},
        {"value": 0.8, "color": "#005fe3"},
        {"value": 0.9, "color": "#000fe3"},
        {"value": 1.0, "color": "#5700e3"},
    ],
    "legend": legend_idx_percentage_by_10,
}


style_wofs_obs = {
    "name": "observations",
    "title": "Observations",
    "abstract": "Classified as water by the decision tree",
    "value_map": {
        "water": [
            {
                "title": "Invalid",
                "abstract": "Slope or Cloud",
                "flags": {"or": {"cloud_shadow": True, "cloud": True}},
                "color": "#707070",
            },
            {
                "title": "Dry",
                "abstract": "Dry",
                "flags": {
                    "dry": True,
                    "sea": False,
                    "cloud_shadow": False,
                    "cloud": False,
                    "nodata": False,
                },
                "color": "#D99694",
            },
            {
                "title": "Wet",
                "abstract": "Wet or Sea",
                "flags": {"or": {"wet": True, "sea": True}},
                "color": "#4F81BD",
            },
        ]
    },
}

style_wofs_obs_wet_only = {
    "name": "wet",
    "title": "Wet Only",
    "abstract": "Clear and Wet",
    "value_map": {
        "water": [
            {
                "title": "Invalid",
                "abstract": "Slope or Cloud",
                "flags": {
                    "or": {
                        "cloud_shadow": True,
                        "cloud": True,
                        "nodata": True,
                    }
                },
                "color": "#707070",
                "mask": True,
            },
            {
                "title": "Dry",
                "abstract": "Dry",
                "flags": {
                    "dry": True,
                    "sea": False,
                },
                "color": "#D99694",
                "mask": True,
            },
            {
                "title": "Wet",
                "abstract": "Wet or Sea",
                "flags": {"or": {"wet": True, "sea": True}},
                "color": "#4F81BD",
            },
        ]
    },
}

style_wofs_dry_observations = {
    "name": "dry_observations",
    "title": "Count Dry",
    "abstract": "WOfS summary showing the count of dry observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count_dry",
        },
    },
    "needed_bands": ["count_dry"],
    "color_ramp": [
        {"value": 0, "color": "#FFFFFF", "alpha": 0},
        {
            # purely for legend display
            # we should not get fractional
            # values in this styles
            "value": 10,
            "color": "#b21800",
            "alpha": 1,
        },
        {"value": 100, "color": "#ef8500"},
        {"value": 200, "color": "#ffb800"},
        {"value": 300, "color": "#ffd300"},
        {"value": 400, "color": "#ffe300"},
        {"value": 500, "color": "#fff300"},
        {"value": 600, "color": "#d0f800"},
        {"value": 700, "color": "#a0fd00"},
        {"value": 800, "color": "#6ee100"},
        {"value": 901, "color": "#39a500"},
        {"value": 1000, "color": "#026900"},
    ],
    "legend": {
        "begin": "0",
        "end": "1000",
        "decimal_places": 0,
        "ticks_every": 100,
        "legend_strip_location": [0.05, 0.5, 0.89, 0.15],
        "tick_labels": {
            "1000": {"prefix": ">"},
        },
    },
}
