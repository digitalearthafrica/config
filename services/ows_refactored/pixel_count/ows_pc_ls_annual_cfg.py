from ows_refactored.common.ows_reslim_cfg import reslim_srtm

bands_pc_ls8_annual = {
    "total": [],
    "clear": [],
    "clear_1_2_0": [],
    "clear_1_2_2": [],
    "clear_2_5_0": [],
    "clear_2_5_2": [],
    "clear_aerosol": [],
}

pc_annual_cmap = [
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
]

pc_annual_legend = {
    "begin": 0,
    "end": 20,
    "decimal_places": 0,
    "ticks_every": 10,
    "tick_labels": {
        "20": {"prefix": ">"},
    }
}

style_pc_annual_total = {
    "name": "pc_annual_total",
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
    "color_ramp": pc_annual_cmap,
    "legend": pc_annual_legend,
}

style_pc_annual_clear = {
    "name": "pc_annual_clear",
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
    "color_ramp": pc_annual_cmap,
    "legend": pc_annual_legend,
}

style_pc_annual_clear_aerosol = {
    "name": "pc_annual_clear_aerosol",
    "title": "Number of clear and low aerosol",
    "abstract": "Number of clear and low aerosol",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "clear_aerosol",
        },
    },
    "needed_bands": ["clear_aerosol"],
    "include_in_feature_info": False,
    "color_ramp": pc_annual_cmap,
    "legend": pc_annual_legend,
}

style_pc_annual_clear_1_2_0 = {
    "name": "pc_annual_clear_1_2_0",
    "title": "Number of clear (1, 2, 0)",
    "abstract": "Number of clear (1, 2, 0)",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "clear_1_2_0",
        },
    },
    "needed_bands": ["clear_1_2_0"],
    "include_in_feature_info": False,
    "color_ramp": pc_annual_cmap,
    "legend": pc_annual_legend,
}

style_pc_annual_clear_1_2_2 = {
    "name": "pc_annual_clear_1_2_2",
    "title": "Number of clear (1, 2, 2)",
    "abstract": "Number of clear (1, 2, 2)",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "clear_1_2_2",
        },
    },
    "needed_bands": ["clear_1_2_2"],
    "include_in_feature_info": False,
    "color_ramp": pc_annual_cmap,
    "legend": pc_annual_legend,
}

style_pc_annual_clear_2_5_0 = {
    "name": "pc_annual_clear_2_5_0",
    "title": "Number of clear (2, 5, 0)",
    "abstract": "Number of clear (2, 5, 0)",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "clear_2_5_0",
        },
    },
    "needed_bands": ["clear_2_5_0"],
    "include_in_feature_info": False,
    "color_ramp": pc_annual_cmap,
    "legend": pc_annual_legend,
}

style_pc_annual_clear_2_5_2 = {
    "name": "pc_annual_clear_2_5_2",
    "title": "Number of clear (2, 5, 2)",
    "abstract": "Number of clear (2, 5, 2)",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "clear_2_5_2",
        },
    },
    "needed_bands": ["clear_2_5_2"],
    "include_in_feature_info": False,
    "color_ramp": pc_annual_cmap,
    "legend": pc_annual_legend,
}

layer = {
    "title": "Landsat 8 annual clear pixel count",
    "name": "pc_ls8_annual",
    "abstract": """
Annual number of observations and number of clear observations. This product is for internal use.
""",
    "product_name": "pc_ls8_annual",
    "time_resolution": "year",
    "bands": bands_pc_ls8_annual,
    "resource_limits": reslim_srtm,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "pc_annual_clear",
        "styles": [
            style_pc_annual_clear,
            style_pc_annual_clear_aerosol,
            style_pc_annual_total,
            style_pc_annual_clear_1_2_0,
            style_pc_annual_clear_1_2_2,
            style_pc_annual_clear_2_5_0,
            style_pc_annual_clear_2_5_2,
        ],
    },
}
