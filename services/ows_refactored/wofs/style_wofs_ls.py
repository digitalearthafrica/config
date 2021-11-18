# This file contains default OWS styling for Landsat WOfS, including
# wofs_ls, wofs_ls_summary_annual, wofs_ls_summary_alltime
# Sequential colour schemes based off mako_r colourmap
from ows_refactored.common.ows_legend_cfg import legend_idx_percentage_by_10

# styles used by wofs_ls_summary_annual
style_wofs_summary_annual_frequency = {
    "name": "wofs_summary_annual_frequency",
    "title": " Water frequency",
    "abstract": "WOfS summary showing the frequency of water",
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
        {"value": 0.05, "color": '#aee3c0', "alpha": 0.25},
        {"value": 0.1, "color": '#6dd3ad', "alpha": 0.75},
        {"value": 0.2, "color": '#44bcad'},
        {"value": 0.3, "color": '#35a1ab'},
        {"value": 0.4, "color": '#3487a6'},
        {"value": 0.5, "color": '#366da0'},
        {"value": 0.6, "color": '#3d5296'},
        {"value": 0.7, "color": '#403974'},
        {"value": 0.8, "color": '#35264c'},
        {"value": 0.9, "color": '#231526'},
    ],
    "legend": legend_idx_percentage_by_10,
}

style_wofs_summary_annual_clear = {
    "name": "wofs_summary_annual_clear",
    "title": "Count of clear observations",
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
            "color": "#FFFFFF",
            "alpha": 1,
        },
        {"value": 3, "color": "#f2fabc"},
        {"value": 6, "color": "#dcf1b2"},
        {"value": 10, "color": "#bbe4b5"},
        {"value": 12, "color": "#85cfba"},
        {"value": 15, "color": "#57bec1"},
        {"value": 18, "color": "#34a9c3"},
        {"value": 20, "color": "#1d8dbe"},
        {"value": 24, "color": "#2166ac"},
        {"value": 27, "color": "#24479d"},
        {"value": 30, "color": "#1d2e83"},
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

style_wofs_summary_annual_wet = {
    "name": "wofs_summary_annual_wet",
    "title": "Count of wet observations",
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
            "color": "#FFFFFF",
            "alpha": 1,
        },
        {"value": 2, "color": "#f1ebf5"},
        {"value": 4, "color": "#e0dded"},
        {"value": 6, "color": "#c9cee4"},
        {"value": 8, "color": "#a9bfdc"},
        {"value": 10, "color": "#86b0d3"},
        {"value": 12, "color": "#5ea0ca"},
        {"value": 14, "color": "#328dbf"},
        {"value": 16, "color": "#0d75b3"},
        {"value": 18, "color": "#04649d"},
        {"value": 20, "color": "#03517e"},
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

# styles used by wofs_ls_summary_alltime
style_wofs_summary_alltime_frequency = {
    "name": "wofs_summary_alltime_frequency",
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
        {"value": 0.002, "color": "#000000", "alpha": 0.0},
        {"value": 0.005, "color": '#b9e6c7', "alpha": 0.25},
        {"value": 0.01, "color": '#8bdab2', "alpha": 0.75},
        {"value": 0.02, "color": '#59ccad'},
        {"value": 0.05, "color": '#40b7ad'},
        {"value": 0.1, "color": '#36a3ab'},
        {"value": 0.2, "color": '#348fa7'},
        {"value": 0.3, "color": '#357aa2'},
        {"value": 0.4, "color": '#37659e'},
        {"value": 0.5, "color": '#3e5095'},
        {"value": 0.6, "color": '#413d7b'},
        {"value": 0.7, "color": '#3a2c59'},
        {"value": 0.8, "color": '#2e1e3b'},
        {"value": 0.9, "color": '#1e111f'},
    ],
    "legend": legend_idx_percentage_by_10,
}

style_wofs_summary_alltime_clear = {
    "name": "wofs_summary_alltime_clear",
    "title": "Count of clear observations",
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
            "color": "#FFFFFF",
            "alpha": 1,
        },
        {"value": 20, "color": "#f1faba"},
        {"value": 40, "color": "#d6efb3"},
        {"value": 60, "color": "#abdeb7"},
        {"value": 80, "color": "#73c8bd"},
        {"value": 100, "color": "#40b5c4"},
        {"value": 120, "color": "#2498c1"},
        {"value": 140, "color": "#2072b1"},
        {"value": 160, "color": "#234da0"},
        {"value": 180, "color": "#1f2f87"},
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

style_wofs_summary_alltime_wet = {
    "name": "wofs_summary_alltime_wet",
    "title": "Count of wet observations",
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
            "color": "#FFFFFF",
            "alpha": 1,
        },
        {"value": 20, "color": "#f2ecf5"},
        {"value": 30, "color": "#e3e0ee"},
        {"value": 40, "color": "#d0d1e6"},
        {"value": 50, "color": "#b4c4df"},
        {"value": 60, "color": "#96b6d7"},
        {"value": 70, "color": "#73a9cf"},
        {"value": 80, "color": "#4a98c5"},
        {"value": 90, "color": "#2685bb"},
        {"value": 100, "color": "#056faf"},
        {"value": 110, "color": "#046198"},
        {"value": 120, "color": "#034e7b"},
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

# wofs_ls (WOFL) styles
style_wofs_ls_obs = {
    "name": "observations",
    "title": "Observations",
    "abstract": "Observations",
    "value_map": {
        "water": [
            {
                "title": "",
                "abstract": "",
                "flags": {
                    "or": {
                        "nodata": True,
                        "noncontiguous": True,
                        "low_solar_angle": True
                    }
                },
                "alpha": 0.0,
                "color": "#707070",
            },
            {
                "title": "Terrain Shaded Water",
                "abstract": "",
                "flags": {
                    "and": {
                        "water_observed": True,
                        "terrain_shadow": True
                    }
                },
                "color": "#03396c",
            },
            {
                "title": "Terrain Shadow",
                "abstract": "",
                "flags": {"terrain_shadow": True},
                "color": "#2f2922",
            },
            {
                "title": "Water on Slope",
                "abstract": "",
                "flags": {
                    "and": {
                        "water_observed": True,
                        "high_slope": True
                    }
                },
                "color": "#005b96",
            },
            {
                "title": "Steep Terrain",
                "abstract": "",
                "flags": {"high_slope": True},
                "color": "#776857",
            },
            {
                "title": "Shaded Water",
                "abstract": "",
                "flags": {
                    "and": {
                        "water_observed": True,
                        "cloud_shadow": True
                    }
                },
                "color": "#6497b1",
            },
            {
                "title": "Cloud Shadow",
                "abstract": "",
                "flags": {"cloud_shadow": True},
                "color": "#4b4b37",
            },
            {
                "title": "Cloudy Water",
                "abstract": "",
                "flags": {
                    "and": {
                        "water_observed": True,
                        "cloud": True
                    }
                },
                "color": "#b3cde0",
            },
            {
                "title": "Cloud",
                "abstract": "",
                "flags": {"cloud": True},
                "color": "#c2c1c0",
            },
            {
                "title": "Water",
                "abstract": "",
                "flags": {"water_observed": True},
                "color": "#4F81BD",
            },
            {
                "title": "Dry",
                "abstract": "",
                "flags": {
                    "water_observed": False,
                },
                "color": "#96966e",
            },
        ],
    },
    "legend": {"width": 3.0, "height": 2.5},
}

style_wofs_ls_wet = {
    "name": "wet",
    "title": "Wet Only",
    "abstract": "Wet Only",
    "value_map": {
        "water": [
            {
                "title": "Invalid",
                "abstract": "Slope or Cloud",
                "flags": {
                    "or": {
                        "terrain_shadow": True,
                        "low_solar_angle": True,
                        "cloud_shadow": True,
                        "cloud": True,
                        "high_slope": True,
                        "noncontiguous": True,
                    }
                },
                "color": "#707070",
                "alpha": 0.0,
            },
            {
                # Possible Sea Glint, also mark as invalid
                "title": "Dry",
                "abstract": "Dry",
                "flags": {
                    "dry": True,
                },
                "color": "#D99694",
                "alpha": 0.0,
            },
            {
                "title": "Wet",
                "abstract": "",
                "flags": {"wet": True},
                "color": "#4F81BD",
            },
        ],
    },
}
