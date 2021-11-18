# This file contains default OWS styling for Landsat WOfS, including
# wofs_ls, wofs_ls_summary_annual, wofs_ls_summary_alltime
# Sequential colour schemes based off mako_r colourmap
from ows_refactored.common.ows_legend_cfg import legend_idx_percentage_by_10

# styles used by wofs_ls_summary_annual
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
