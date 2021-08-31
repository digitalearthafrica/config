from ows_refactored.common.ows_reslim_cfg import reslim_srtm

bands_pc_s2_annual = {
    "total": [],
    "clear": [],
    "clear_0_5": [],
    "clear_2_5": [],
}

pc_s2_annual_cmap = [
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
]

pc_s2_annual_legend = {
    "begin": 0,
    "end": 120,
    "decimal_places": 0,
    "ticks_every": 20,
    "tick_labels": {
        "120": {"prefix": ">"},
    }
}

style_pc_s2_annual_total = {
    "name": "pc_s2_annual_total",
    "title": "Total number of observations",
    "abstract": "Total number of observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "total",
        },
    },
    "needed_bands": ["total"],
    "include_in_feature_info": False,
    "color_ramp": pc_s2_annual_cmap,
    "legend": pc_s2_annual_legend,
}

style_pc_s2_annual_clear = {
    "name": "pc_s2_annual_clear",
    "title": "Number of clear observations",
    "abstract": "Number of clear observations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "clear",
        },
    },
    "needed_bands": ["clear"],
    "include_in_feature_info": False,
    "color_ramp": pc_s2_annual_cmap,
    "legend": pc_s2_annual_legend,
}

style_pc_s2_annual_clear_0_5 = {
    "name": "pc_s2_annual_clear_0_5",
    "title": "Number of clear (0, 5)",
    "abstract": "Number of clear (0, 5)",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "clear_0_5",
        },
    },
    "needed_bands": ["clear_0_5"],
    "include_in_feature_info": False,
    "color_ramp": pc_s2_annual_cmap,
    "legend": pc_s2_annual_legend,
}

style_pc_s2_annual_clear_2_5 = {
    "name": "pc_s2_annual_clear_2_5",
    "title": "Number of clear (2, 5)",
    "abstract": "Number of clear (2, 5)",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "clear_2_5",
        },
    },
    "needed_bands": ["clear_2_5"],
    "include_in_feature_info": False,
    "color_ramp": pc_s2_annual_cmap,
    "legend": pc_s2_annual_legend,
}

layer = {
    "title": "Sentinel-2 annual clear pixel count",
    "name": "pc_s2_annual",
    "abstract": """
Annual number of observations and number of clear observations. This product is for internal use.
""",
    "product_name": "pc_s2_annual",
    "time_resolution": "year",
    "bands": bands_pc_s2_annual,
    "resource_limits": reslim_srtm,
    "native_crs": "EPSG:6933",
    "native_resolution": [20.0, -20.0],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "pc_s2_annual_clear",
        "styles": [
            style_pc_s2_annual_clear,
            style_pc_s2_annual_total,
            style_pc_s2_annual_clear_0_5,
            style_pc_s2_annual_clear_2_5,
        ],
    },
}
