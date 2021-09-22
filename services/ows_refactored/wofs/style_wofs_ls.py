# This file contains current styling for Landsat WOfS, including
# wofs_ls, wofs_ls_summary_annual, wofs_ls_summary_alltime
from ows_refactored.common.ows_legend_cfg import legend_idx_percentage_by_10

# styles used by wofs_ls_summary_annual

# colour scheme based off mako_r
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
        {"value": 0.05, "color": '#b2e4c2', "alpha": 0.25},
        {"value": 0.1, "color": '#79d6ae', "alpha": 0.75},
        {"value": 0.2, "color": '#49c1ad'},
        {"value": 0.3, "color": '#38aaac'},
        {"value": 0.4, "color": '#3492a8'},
        {"value": 0.5, "color": '#357ba3'},
        {"value": 0.6, "color": '#38629d'},
        {"value": 0.7, "color": '#40498e'},
        {"value": 0.8, "color": '#3e3469'},
        {"value": 0.9, "color": '#332345'},
        {"value": 0.95, "color": '#211423'},
    ],
    "legend": legend_idx_percentage_by_10,
}

# styles used by wofs_ls_summary_alltime

# colour scheme based off mako_r
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
        {"value": 0.005, "color": '#bbe7c8', "alpha": 0.25},
        {"value": 0.01, "color": '#91dbb4', "alpha": 0.75},
        {"value": 0.02, "color": '#60ceac'},
        {"value": 0.05, "color": '#45bdad'},
        {"value": 0.1, "color": '#38aaac'},
        {"value": 0.2, "color": '#3497a9'},
        {"value": 0.3, "color": '#3484a5'},
        {"value": 0.4, "color": '#3671a0'},
        {"value": 0.5, "color": '#395d9c'},
        {"value": 0.6, "color": '#40498e'},
        {"value": 0.7, "color": '#403872'},
        {"value": 0.8, "color": '#382a54'},
        {"value": 0.9, "color": '#2d1d38'},
        {"value": 0.95, "color": '#1d111d'},
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
