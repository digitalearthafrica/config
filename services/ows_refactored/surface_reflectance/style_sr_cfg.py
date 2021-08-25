from ows_refactored.common.ows_legend_cfg import legend_idx_0_1_5ticks

style_gals_irg = {
    "name": "infrared_green",
    "title": "False colour - Green, SWIR, NIR",
    "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
    "components": {
        "red": {"swir_1": 1.0},
        "green": {"nir": 1.0},
        "blue": {"green": 1.0},
    },
    "scale_range": [7272.0, 18181.0],
}

style_s2_irg = {
    "name": "infrared_green",
    "title": "False colour - Green, SWIR, NIR",
    "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
    "components": {
        "red": {"swir_1": 1.0},
        "green": {"nir": 1.0},
        "blue": {"green": 1.0},
    },
    "scale_range": [0, 3000],
}

style_gm_irg = {
    "name": "infrared_green",
    "title": "Geomedian - SWIR, NIR, Green",
    "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
    "components": {
        "red": {"swir_1": 1.0},
        "green": {"nir": 1.0},
        "blue": {"green": 1.0},
    },
    "scale_range": [0, 3000],
}

style_ls_irg = {
    "name": "infrared_green",
    "title": "False colour - Green, SWIR, NIR",
    "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
    "components": {
        "red": {"swir1": 1.0},
        "green": {"nir": 1.0},
        "blue": {"green": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_ls_ndvi = {
    "name": "ndvi",
    "title": "NDVI - Red, NIR",
    "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "nir", "band2": "red"},
    },
    "needed_bands": ["red", "nir"],
    "color_ramp": [
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
    ],
    "legend": legend_idx_0_1_5ticks,
    "multi_date": [
        {
            "allowed_count_range": [2, 2],
            "animate": False,
            "preserve_user_date_order": True,
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_delta",
            },
            "mpl_ramp": "RdYlBu",
            "range": [-1.0, 1.0],
            "legend": {
                "begin": "-1.0",
                "end": "1.0",
                "ticks": [
                    "-1.0",
                    "0.0",
                    "1.0",
                ]
            },
            "feature_info_label": "ndvi_delta",
        },
        {"allowed_count_range": [3, 4], "animate": True},
    ],
}

style_ls_ndwi = {
    "name": "ndwi",
    "title": "NDWI - Green, NIR",
    "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water (McFeeters 1996)",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "green", "band2": "nir"},
    },
    "needed_bands": ["green", "nir"],
    "color_ramp": [
        {"value": -0.1, "color": "#f7fbff", "alpha": 0.0},
        {"value": 0.0, "color": "#d8e7f5", "legend": {"prefix": "<"}},
        {"value": 0.1, "color": "#b0d2e8"},
        {"value": 0.2, "color": "#73b3d8", "legend": {}},
        {"value": 0.3, "color": "#3e8ec4"},
        {"value": 0.4, "color": "#1563aa", "legend": {}},
        {"value": 0.5, "color": "#08306b", "legend": {"prefix": ">"}},
    ],
    "legend": {
        "begin": "0.0",
        "end": "0.5",
        "decimal_places": 1,
        "ticks": ["0.0", "0.2", "0.4", "0.5"],
        "tick_labels": {
            "0.0": {"prefix": "<"},
            "0.2": {"label": "0.2"},
            "0.4": {"label": "0.4"},
            "0.5": {"prefix": ">"},
        },
    },
    "multi_date": [
        {
            "allowed_count_range": [2, 2],
            "animate": False,
            "preserve_user_date_order": True,
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_delta",
            },
            "mpl_ramp": "RdYlBu",
            "range": [-1.0, 1.0],
            "legend": {
                "begin": "-1.0",
                "end": "1.0",
                "ticks": [
                    "-1.0",
                    "0.0",
                    "1.0",
                ]
            },
            "feature_info_label": "ndwi_delta",
        },
        {"allowed_count_range": [3, 4], "animate": True},
    ],
}

style_gals_mndwi = {
    "name": "mndwi",
    "title": "MNDWI - Green, SWIR",
    "abstract": "Modified Normalised Difference Water Index - a derived index that correlates well with the existence of water (Xu 2006)",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "green", "band2": "swir_1"},
    },
    "needed_bands": ["green", "swir_1"],
    "color_ramp": [
        {"value": -0.1, "color": "#f7fbff", "alpha": 0.0},
        {"value": 0.0, "color": "#d8e7f5"},
        {"value": 0.2, "color": "#b0d2e8"},
        {"value": 0.4, "color": "#73b3d8"},
        {"value": 0.6, "color": "#3e8ec4"},
        {"value": 0.8, "color": "#1563aa"},
        {"value": 1.0, "color": "#08306b"},
    ],
    "legend": legend_idx_0_1_5ticks,
    "multi_date": [
        {
            "allowed_count_range": [2, 2],
            "animate": False,
            "preserve_user_date_order": True,
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_delta",
            },
            "mpl_ramp": "RdYlBu",
            "range": [-1.0, 1.0],
            "legend": {
                "begin": "-1.0",
                "end": "1.0",
                "ticks": [
                    "-1.0",
                    "0.0",
                    "1.0",
                ]
            },
            "feature_info_label": "mndwi_delta",
        },
        {"allowed_count_range": [3, 4], "animate": True},
    ],
}

style_ls_mndwi = {
    "name": "mndwi",
    "title": "MNDWI - Green, SWIR",
    "abstract": "Modified Normalised Difference Water Index - a derived index that correlates "
    "well with the existence of water (Xu 2006)",
    "index_function": {
        "function": "datacube_ows.band_utils.norm_diff",
        "mapped_bands": True,
        "kwargs": {"band1": "green", "band2": "swir1"},
    },
    "needed_bands": ["green", "swir1"],
    "color_ramp": [
        {"value": -0.1, "color": "#f7fbff", "alpha": 0.0},
        {"value": 0.0, "color": "#d8e7f5"},
        {"value": 0.2, "color": "#b0d2e8"},
        {"value": 0.4, "color": "#73b3d8"},
        {"value": 0.6, "color": "#3e8ec4"},
        {"value": 0.8, "color": "#1563aa"},
        {"value": 1.0, "color": "#08306b"},
    ],
    "legend": legend_idx_0_1_5ticks,
    "multi_date": [
        {
            "allowed_count_range": [2, 2],
            "animate": False,
            "preserve_user_date_order": True,
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_delta",
            },
            "mpl_ramp": "RdYlBu",
            "range": [-1.0, 1.0],
            "legend": {
                "begin": "-1.0",
                "end": "1.0",
                "ticks": [
                    "-1.0",
                    "0.0",
                    "1.0",
                ]
            },
            "feature_info_label": "mndwi_delta",
        },
        {"allowed_count_range": [3, 4], "animate": True},
    ],
}

style_gals_pure_blue = {
    "name": "blue",
    "title": "Blue - 480",
    "abstract": "Blue band, centered on 480nm",
    "components": {"red": {"blue": 1.0}, "green": {"blue": 1.0}, "blue": {"blue": 1.0}},
    "scale_range": [7272.0, 18181.0],
}

style_ls_pure_blue = {
    "name": "blue",
    "title": "Blue - 480",
    "abstract": "Blue band, centered on 480nm",
    "components": {"red": {"blue": 1.0}, "green": {"blue": 1.0}, "blue": {"blue": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_sentinel_pure_blue = {
    "name": "blue",
    "title": "Blue - 490",
    "abstract": "Blue band, centered on 490nm",
    "components": {"red": {"blue": 1.0}, "green": {"blue": 1.0}, "blue": {"blue": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_gals_pure_green = {
    "name": "green",
    "title": "Green - 560",
    "abstract": "Green band, centered on 560nm",
    "components": {
        "red": {"green": 1.0},
        "green": {"green": 1.0},
        "blue": {"green": 1.0},
    },
    "scale_range": [7272.0, 18181.0],
}

style_ls_pure_green = {
    "name": "green",
    "title": "Green - 560",
    "abstract": "Green band, centered on 560nm",
    "components": {
        "red": {"green": 1.0},
        "green": {"green": 1.0},
        "blue": {"green": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_ls_simple_rgb = {
    "name": "simple_rgb",
    "title": "Simple RGB",
    "abstract": "Simple true-colour image, using the red, green and blue bands",
    "components": {"red": {"red": 1.0}, "green": {"green": 1.0}, "blue": {"blue": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_gm_simple_rgb = {
    "name": "simple_rgb",
    "title": "Geomedian - Red, Green, Blue",
    "abstract": "Simple true-colour image, using the red, green and blue bands",
    "components": {"red": {"red": 1.0}, "green": {"green": 1.0}, "blue": {"blue": 1.0}},
    "scale_range": [0.0, 3000.0],
    "multi_date": [{"allowed_count_range": [2, 4], "animate": True}],
}

style_gals_simple_rgb = {
    "name": "simple_rgb",
    "title": "Simple RGB",
    "abstract": "Simple true-colour image, using the red, green and blue bands",
    "components": {"red": {"red": 1.0}, "green": {"green": 1.0}, "blue": {"blue": 1.0}},
    # The raw band value range to be compressed to an 8 bit range for the output image tiles.
    # Band values outside this range are clipped to 0 or 255 as appropriate.
    "scale_range": [7272.0, 18181.0],
}


style_gals_pure_red = {
    "name": "red",
    "title": "Red - 660",
    "abstract": "Red band, centered on 660nm",
    "components": {"red": {"red": 1.0}, "green": {"red": 1.0}, "blue": {"red": 1.0}},
    "scale_range": [7272.0, 18181.0],
}

style_ls_pure_red = {
    "name": "red",
    "title": "Red - 660",
    "abstract": "Red band, centered on 660nm",
    "components": {"red": {"red": 1.0}, "green": {"red": 1.0}, "blue": {"red": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_gals_pure_nir = {
    "name": "nir",
    "title": "Near Infrared (NIR) - 840",
    "abstract": "Near infra-red band, centered on 840nm",
    "components": {"red": {"nir": 1.0}, "green": {"nir": 1.0}, "blue": {"nir": 1.0}},
    "scale_range": [7272.0, 18181.0],
}

style_ls_pure_nir = {
    "name": "nir",
    "title": "Near Infrared (NIR) - 840",
    "abstract": "Near infra-red band, centered on 840nm",
    "components": {"red": {"nir": 1.0}, "green": {"nir": 1.0}, "blue": {"nir": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_sentinel_pure_nir = {
    "name": "nir",
    "title": "Near Infrared (NIR) - 870",
    "abstract": "Near infra-red band, centered on 870nm",
    "components": {"red": {"nir": 1.0}, "green": {"nir": 1.0}, "blue": {"nir": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_gals_pure_swir1 = {
    "name": "swir_1",
    "title": "Shortwave Infrared (SWIR) - 1610",
    "abstract": "Short wave infra-red band 1, centered on 1610nm",
    "components": {
        "red": {"swir_1": 1.0},
        "green": {"swir_1": 1.0},
        "blue": {"swir_1": 1.0},
    },
    "scale_range": [7272.0, 18181.0],
}


style_s2_pure_swir1 = {
    "name": "swir_1",
    "title": "Shortwave Infrared (SWIR) - 1610",
    "abstract": "Short wave infra-red band 1, centered on 1610nm",
    "components": {"red": {"B11": 1.0}, "green": {"B11": 1.0}, "blue": {"B11": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_ls_pure_swir1 = {
    "name": "swir1",
    "title": "Shortwave Infrared (SWIR) - 1650",
    "abstract": "Short wave infra-red band 1, centered on 1650nm",
    "components": {
        "red": {"swir1": 1.0},
        "green": {"swir1": 1.0},
        "blue": {"swir1": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_sentinel_pure_swir1 = {
    "name": "swir1",
    "title": "Shortwave Infrared (SWIR) - 1610",
    "abstract": "Short wave infra-red band 1, centered on 1610nm",
    "components": {
        "red": {"swir1": 1.0},
        "green": {"swir1": 1.0},
        "blue": {"swir1": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_gals_pure_swir2 = {
    "name": "swir_2",
    "title": "Shortwave Infrared (SWIR) - 2200",
    "abstract": "Short wave infra-red band 2, centered on 2200nm",
    "components": {
        "red": {"swir_2": 1.0},
        "green": {"swir_2": 1.0},
        "blue": {"swir_2": 1.0},
    },
    "scale_range": [7272.0, 18181.0],
}

style_s2_pure_swir2 = {
    "name": "swir_2",
    "title": "Shortwave Infrared (SWIR) - 2200",
    "abstract": "Short wave infra-red band 2, centered on 2200nm",
    "components": {
        "red": {"swir_2": 1.0},
        "green": {"swir_2": 1.0},
        "blue": {"swir_2": 1.0},
    },
    "scale_range": [0, 3000.0],
}

style_ls_pure_swir2 = {
    "name": "swir2",
    "title": "Shortwave Infrared (SWIR) - 2220",
    "abstract": "Short wave infra-red band 2, centered on 2220nm",
    "components": {
        "red": {"swir2": 1.0},
        "green": {"swir2": 1.0},
        "blue": {"swir2": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_s2_ndci = {
    "name": "ndci",
    "title": "NDCI - Red Edge, Red",
    "abstract": "Normalised Difference Chlorophyll Index - a derived index that correlates well with the existence of chlorophyll",
    "index_function": {
        "function": "datacube_ows.band_utils.sentinel2_ndci",
        "mapped_bands": True,
        "kwargs": {
            "b_red_edge": "red_edge_1",
            "b_red": "red",
            "b_green": "green",
            "b_swir": "swir_2",
        },
    },
    "needed_bands": ["red_edge_1", "red", "green", "swir_2"],
    "color_ramp": [
        {"value": -0.1, "color": "#1696FF"},
        {"value": -0.1, "color": "#1696FF"},
        {"value": 0.0, "color": "#00FFDF"},
        {
            "value": 0.1,
            "color": "#FFF50E",
        },
        {"value": 0.2, "color": "#FFB50A"},
        {
            "value": 0.4,
            "color": "#FF530D",
        },
        {"value": 0.5, "color": "#FF0000"},
    ],
    "legend": {
        "begin": "-0.1",
        "end": "0.5",
        "decimal_places": 1,
        "ticks": ["-0.1", "0.0", "0.2", "0.5"],
        "tick_labels": {
            "-0.1": {"prefix": "<"},
            "0.5": {"prefix": ">"},
        },
    },
    "multi_date": [
        {
            "allowed_count_range": [2, 2],
            "animate": False,
            "preserve_user_date_order": True,
            "aggregator_function": {
                "function": "datacube_ows.band_utils.multi_date_delta",
            },
            "mpl_ramp": "RdYlBu",
            "range": [-1.0, 1.0],
            "legend": {
                "begin": "-1.0",
                "end": "1.0",
                "ticks": [
                    "-1.0",
                    "0.0",
                    "1.0",
                ]
            },
            "feature_info_label": "ndci_delta",
        },
        {"allowed_count_range": [3, 4], "animate": True},
    ],
}

style_s2_pure_aerosol = {
    "name": "aerosol",
    "title": "Narrow Blue - 440",
    "abstract": "Coastal Aerosol or Narrow Blue band, approximately 435nm to 450nm",
    "components": {
        "red": {"coastal_aerosol": 1.0},
        "green": {"coastal_aerosol": 1.0},
        "blue": {"coastal_aerosol": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_redge_1 = {
    "name": "red_edge_1",
    "title": "Vegetation Red Edge - 710",
    "abstract": "Near infra-red band, centred on 710nm",
    "components": {
        "red": {"red_edge_1": 1.0},
        "green": {"red_edge_1": 1.0},
        "blue": {"red_edge_1": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_redge_2 = {
    "name": "red_edge_2",
    "title": "Vegetation Red Edge - 740",
    "abstract": "Near infra-red band, centred on 740nm",
    "components": {
        "red": {"red_edge_2": 1.0},
        "green": {"red_edge_2": 1.0},
        "blue": {"red_edge_2": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}


style_s2_pure_redge_3 = {
    "name": "red_edge_3",
    "title": "Vegetation Red Edge - 780",
    "abstract": "Near infra-red band, centred on 780nm",
    "components": {
        "red": {"red_edge_3": 1.0},
        "green": {"red_edge_3": 1.0},
        "blue": {"red_edge_3": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_s2_pure_narrow_nir = {
    "name": "narrow_nir",
    "title": "Narrow Near Infrared - 870",
    "abstract": "Near infra-red band, centred on 865nm",
    "components": {"red": {"nir": 1.0}, "green": {"nir": 1.0}, "blue": {"nir": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_sentinel_pure_swir2 = {
    "name": "swir2",
    "title": "Shortwave Infrared (SWIR) - 2200",
    "abstract": "Short wave infra-red band 2, centered on 2200nm",
    "components": {
        "red": {"swir2": 1.0},
        "green": {"swir2": 1.0},
        "blue": {"swir2": 1.0},
    },
    "scale_range": [0.0, 3000.0],
}

style_s2_scl = {
    "name": "scl",
    "title": "Scene Classification",
    "abstract": "Sentinel-2 Scene Classification Layer",
    "value_map": {
        "SCL": [
            {
                "title": "",
                "abstract": "",
                "values": [0],
                "alpha": 0.0,
                "color": "#707070",
            },
            {
                "title": "Saturated or Defective",
                "abstract": "",
                "values": [1],
                "color": "#ff0004",
            },
            {
                "title": "Dark Areas",
                "abstract": "",
                "values": [2],
                "color": "#000000",
            },
            {
                "title": "Cloud Shadow",
                "abstract": "",
                "values": [3],
                "color": "#616161",
            },
            {
                "title": "Vegetation",
                "abstract": "",
                "values": [4],
                "color": "#038b50",
            },
            {
                "title": "Bare Soil",
                "abstract": "",
                "values": [5],
                "color": "#c0840c",
            },
            {
                "title": "Water",
                "abstract": "",
                "values": [6],
                "color": "#15678d",
            },
            {
                "title": "Unclassified",
                "abstract": "",
                "values": [7],
                "color": "#75001b",
            },
            {
                "title": "Medium Probability Cloud",
                "abstract": "",
                "values": [8],
                "color": "#d0d0d0",
            },
            {
                "title": "High Probability Cloud",
                "abstract": "",
                "values": [9],
                "color": "#f4f4f4",
            },
            {
                "title": "Cirrus",
                "abstract": "",
                "values": [10],
                "color": "#c3e7f0",
            },
            {
                "title": "Snow or Ice",
                "abstract": "",
                "values": [11],
                "color": "#de9dcc",
            },
        ]
    },
    "legend": {"width": 3.0, "height": 3.0},
}


style_sentinel_count = {
    "name": "count",
    "title": "Included observation count",
    "abstract": "Count of observations included in geomedian/MAD calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count",
        },
    },
    "needed_bands": ["count"],
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

style_gm_count = {
    "name": "count",
    "title": "Clear observation count",
    "abstract": "Count of observations included in geomedian/MAD calculations",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "count",
        },
    },
    "needed_bands": ["count"],
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

# styles tmad
sdev_scaling = [0.020, 0.18]
edev_scaling = [6.2, 7.3]
bcdev_scaling = [0.025, 0.13]

style_tmad_sdev_std = {
    "name": "arcsec_sdev",
    "title": "Spectral MAD (SMAD)",
    "abstract": "Good for cropland and forest",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_arcsec",
        "mapped_bands": True,
        "kwargs": {"band": "sdev", "scale_from": sdev_scaling, "scale_to": [0.0, 4.0]},
    },
    "needed_bands": ["sdev"],
    "mpl_ramp": "coolwarm",
    "range": [0.0, 4.0],
    "legend": {
        "start": "0.0",
        "end": "4.0",
        "ticks": ["0.0", "4.0"],
        "tick_labels": {
            "0.0": {"label": "Low\nSMAD"},
            "4.0": {"label": "High\nSMAD"},
        },
    },
}

style_tmad_edev_std = {
    "name": "log_edev",
    "title": "Euclidean MAD (EMAD)",
    "abstract": "Good for cropland and forest",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_offset_log",
        "mapped_bands": True,
        "kwargs": {"band": "edev", "scale_from": edev_scaling, "scale_to": [0.0, 4.0]},
    },
    "needed_bands": ["edev"],
    "mpl_ramp": "coolwarm",
    "range": [0.0, 4.0],
    "legend": {
        "start": "0.0",
        "end": "4.0",
        "ticks": ["0.0", "4.0"],
        "tick_labels": {
            "0.0": {"label": "Low\nEMAD"},
            "4.0": {"label": "High\nEMAD"},
        },
    },
}


style_tmad_bcdev_std = {
    "name": "log_bcdev",
    "title": "Bray-Curtis MAD (BCMAD)",
    "abstract": "Good for cropland and forest",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band_offset_log",
        "mapped_bands": True,
        "kwargs": {
            "band": "bcdev",
            "scale_from": bcdev_scaling,
            "scale_to": [0.0, 4.0],
        },
    },
    "needed_bands": ["bcdev"],
    "mpl_ramp": "coolwarm",
    "range": [0.0, 4.0],
    "legend": {
        "start": "0.0",
        "end": "4.0",
        "ticks": ["0.0", "4.0"],
        "tick_labels": {
            "0.0": {"label": "Low\nBCMAD"},
            "4.0": {"label": "High\nBCMAD"},
        },
    },
}

style_tmad_rgb_std = {
    "name": "tmad_rgb_std",
    "title": "MADs - SMAD, EMAD, BCMAD",
    "abstract": "Good for cropland and forest",
    "components": {
        "red": {
            "function": "datacube_ows.band_utils.single_band_arcsec",
            "mapped_bands": True,
            "kwargs": {
                "band": "sdev",
                "scale_from": sdev_scaling,
            },
        },
        "green": {
            "function": "datacube_ows.band_utils.single_band_offset_log",
            "mapped_bands": True,
            "kwargs": {
                "band": "edev",
                "scale_from": edev_scaling,
            },
        },
        "blue": {
            "function": "datacube_ows.band_utils.single_band_offset_log",
            "mapped_bands": True,
            "kwargs": {
                "band": "bcdev",
                "scale_from": bcdev_scaling,
            },
        },
    },
    "additional_bands": ["sdev", "bcdev", "edev"],
}

style_tmad_rgb_sens = {
    "inherits": style_tmad_rgb_std,
    "name": "tmad_rgb_sens",
    "title": "MADs (desert) - SMAD, EMAD, BCMAD",
    "abstract": "Good for arid land and desert",
    "components": {
        "red": {
            "kwargs": {
                "scale_from": [0.0005, 0.11],
            }
        },
        "green": {
            "kwargs": {
                "scale_from": [5.9, 6.9],
            }
        },
        "blue": {
            "kwargs": {
                "scale_from": [0.008, 0.07],
            }
        },
    },
}

styles_ls8c_list = [
    style_gals_simple_rgb,
    style_gals_irg,
    style_gals_pure_blue,
    style_gals_pure_green,
    style_gals_pure_red,
    style_gals_pure_nir,
    style_gals_pure_swir1,
    style_gals_pure_swir2,
]

styles_s2_list = [
    style_ls_simple_rgb,
    style_s2_irg,
    style_ls_ndvi,
    style_ls_ndwi,
    style_gals_mndwi,
    style_s2_ndci,
    style_s2_pure_aerosol,
    style_sentinel_pure_blue,
    style_ls_pure_green,
    style_ls_pure_red,
    style_s2_pure_redge_1,
    style_s2_pure_redge_2,
    style_s2_pure_redge_3,
    style_ls_pure_nir,
    style_s2_pure_narrow_nir,
    style_s2_pure_swir1,
    style_s2_pure_swir2,
    style_s2_scl,
]

styles_gm_list = [
    style_gm_simple_rgb,
    style_gm_irg,
    style_tmad_rgb_std,
    style_tmad_rgb_sens,
    style_ls_ndvi,
    style_ls_ndwi,
    style_gals_mndwi,
    style_s2_ndci,
    style_sentinel_pure_blue,
    style_ls_pure_green,
    style_ls_pure_red,
    style_s2_pure_redge_1,
    style_s2_pure_redge_2,
    style_s2_pure_redge_3,
    style_ls_pure_nir,
    style_s2_pure_narrow_nir,
    style_s2_pure_swir1,
    style_s2_pure_swir2,
    style_tmad_sdev_std,
    style_tmad_edev_std,
    style_tmad_bcdev_std,
    style_gm_count,
]

styles_sr_list = [
    style_ls_simple_rgb,
    style_ls_irg,
    style_ls_ndvi,
    style_ls_ndwi,
    style_ls_mndwi,
    style_ls_pure_blue,
    style_ls_pure_green,
    style_ls_pure_red,
    style_sentinel_pure_nir,
    style_sentinel_pure_swir1,
    style_sentinel_pure_swir2,
]

# styles for Landsat C2
# Band wavelengths have been removed as they differ
# between LS5, 7 and 8
# Scale range is set as per Collection 1, but scaled to
# 65455 instead of 10000

style_lsc2_sr_simple_rgb = {
    "name": "simple_rgb",
    "title": "True colour - RGB",
    "abstract": "True-colour image, using the red, green and blue bands",
    "components": {
        "red": {"red": 1.0},
        "green": {"green": 1.0},
        "blue": {"blue": 1.0}
    },
    "scale_range": [7272.0, 18181.0],
}

style_lsc2_sr_irg = {
    "name": "infrared_green",
    "title": "False colour - SWIR, NIR, Green",
    "abstract": "False colour image with SWIR1->Red, NIR->Green, and Green->Blue",
    "components": {
        "red": {"swir_1": 1.0},
        "green": {"nir": 1.0},
        "blue": {"green": 1.0},
    },
    "scale_range": [7272.0, 18181.0],
}

style_lsc2_sr_ndvi = {
    "name": "ndvi",
    "title": "NDVI - Red, NIR",
    "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
    "index_expression": "(nir*1.0-red)/(nir+red-14545.4545)",
    "color_ramp": [
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
    ],
    "legend": legend_idx_0_1_5ticks,
}

style_lsc2_sr_ndwi = {
    "name": "ndwi",
    "title": "NDWI - Green, NIR",
    "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water (McFeeters 1996)",
    "index_expression": "(green*1.0-nir)/(green+nir-14545.4545)",
    "color_ramp": [
        {"value": -0.1, "color": "#f7fbff", "alpha": 0.0},
        {"value": 0.0, "color": "#d8e7f5", "legend": {"prefix": "<"}},
        {"value": 0.1, "color": "#b0d2e8"},
        {"value": 0.2, "color": "#73b3d8", "legend": {}},
        {"value": 0.3, "color": "#3e8ec4"},
        {"value": 0.4, "color": "#1563aa", "legend": {}},
        {"value": 0.5, "color": "#08306b", "legend": {"prefix": ">"}},
    ],
    "legend": {
        "begin": "0.0",
        "end": "0.5",
        "decimal_places": 1,
        "ticks": ["0.0", "0.2", "0.4", "0.5"],
        "tick_labels": {
            "0.0": {"prefix": "<"},
            "0.2": {"label": "0.2"},
            "0.4": {"label": "0.4"},
            "0.5": {"prefix": ">"},
        },
    },
}

style_lsc2_sr_mndwi = {
    "name": "mndwi",
    "title": "MNDWI - Green, SWIR",
    "abstract": "Modified Normalised Difference Water Index - a derived index that correlates "
    "well with the existence of water (Xu 2006)",
    "index_expression": "(green*1.0-swir_1)/(green+swir_1-14545.4545)",
    "color_ramp": [
        {"value": -0.1, "color": "#f7fbff", "alpha": 0.0},
        {"value": 0.0, "color": "#d8e7f5"},
        {"value": 0.2, "color": "#b0d2e8"},
        {"value": 0.4, "color": "#73b3d8"},
        {"value": 0.6, "color": "#3e8ec4"},
        {"value": 0.8, "color": "#1563aa"},
        {"value": 1.0, "color": "#08306b"},
    ],
    "legend": legend_idx_0_1_5ticks,
}

style_lsc2_sr_pure_blue = {
    "name": "blue",
    "title": "Blue",
    "abstract": "Blue band",
    "components": {"red": {"blue": 1.0}, "green": {"blue": 1.0}, "blue": {"blue": 1.0}},
    "scale_range": [7272.0, 18181.0],
}

style_lsc2_sr_pure_green = {
    "name": "green",
    "title": "Green",
    "abstract": "Green band",
    "components": {
        "red": {"green": 1.0},
        "green": {"green": 1.0},
        "blue": {"green": 1.0},
    },
    "scale_range": [7272.0, 18181.0],
}

style_lsc2_sr_pure_red = {
    "name": "red",
    "title": "Red",
    "abstract": "Red band",
    "components": {
        "red": {"red": 1.0},
        "green": {"red": 1.0},
        "blue": {"red": 1.0},
    },
    "scale_range": [7272.0, 18181.0],
}

style_lsc2_sr_pure_nir = {
    "name": "nir",
    "title": "Near Infrared (NIR)",
    "abstract": "Near infra-red band",
    "components": {
        "red": {"nir": 1.0},
        "green": {"nir": 1.0},
        "blue": {"nir": 1.0}
    },
    "scale_range": [7272.0, 18181.0],
}

style_lsc2_sr_swir_1 = {
    "name": "swir_1",
    "title": "Shortwave Infrared 1 (SWIR1)",
    "abstract": "Shortwave infrared band 1",
    "components": {
        "red": {"swir_1": 1.0},
        "green": {"swir_1": 1.0},
        "blue": {"swir_1": 1.0},
    },
    "scale_range": [7272.0, 18181.0],
}

style_lsc2_sr_swir_2 = {
    "name": "swir_2",
    "title": "Shortwave Infrared 2 (SWIR2)",
    "abstract": "Shortwave infrared band 2",
    "components": {
        "red": {"swir_2": 1.0},
        "green": {"swir_2": 1.0},
        "blue": {"swir_2": 1.0},
    },
    "scale_range": [7272.0, 18181.0],
}

style_lsc2_pq = {
    "name": "pixel_quality",
    "title": "Pixel Quality",
    "abstract": "Pixel Quality",
    "value_map": {
        "pq": [
            {
                "title": "",
                "abstract": "",
                "flags": {"nodata": True},
                "alpha": 0.0,
                "color": "#707070",
            },
            {
                "title": "Water",
                "abstract": "",
                "flags": {"water": "water"},
                "color": "#4F81BD",
            },
            {
                "title": "Cloud",
                "abstract": "",
                "flags": {"cloud": "high_confidence"},
                "color": "#c2c1c0",
            },
            {
                "title": "Dilated cloud",
                "abstract": "",
                "flags": {"dilated_cloud": "dilated"},
                "color": "#707070",
            },
            {
                "title": "Cloud Shadow",
                "abstract": "",
                "flags": {"cloud_shadow": "high_confidence"},
                "color": "#4b4b37",
            },
            {
                "title": "Snow",
                "abstract": "",
                "flags": {"snow": "high_confidence"},
                "color": "Beige",
            },
            {
                "title": "Land",
                "abstract": "",
                "flags": {"water": "land_or_cloud"},
                "color": "#96966e",
            },
        ]
    }
}

style_ls8c2_pq = {
    "name": "pixel_quality",
    "title": "Pixel Quality",
    "abstract": "Pixel Quality",
    "value_map": {
        "pq": [
            {
                "title": "",
                "abstract": "",
                "flags": {"nodata": True},
                "alpha": 0.0,
                "color": "#707070",
            },
            {
                "title": "Water",
                "abstract": "",
                "flags": {"water": "water"},
                "color": "#4F81BD",
            },
            {
                "title": "Cloud",
                "abstract": "",
                "flags": {"cloud": "high_confidence"},
                "color": "#c2c1c0",
            },
            {
                "title": "Dilated cloud",
                "abstract": "",
                "flags": {"dilated_cloud": "dilated"},
                "color": "#707070",
            },
            {
                "title": "Cirrus",
                "abstract": "",
                "flags": {"cirrus": "high_confidence"},
                "color": "#708090",
            },
            {
                "title": "Cloud Shadow",
                "abstract": "",
                "flags": {"cloud_shadow": "high_confidence"},
                "color": "#4b4b37",
            },
            {
                "title": "Snow",
                "abstract": "",
                "flags": {"snow": "high_confidence"},
                "color": "Beige",
            },
            {
                "title": "Land",
                "abstract": "",
                "flags": {"water": "land_or_cloud"},
                "color": "#96966e",
            },
        ]
    }
}

styles_lsc2_sr_list = [
    style_lsc2_sr_simple_rgb,
    style_lsc2_sr_irg,
    style_lsc2_sr_ndvi,
    style_lsc2_sr_ndwi,
    style_lsc2_sr_mndwi,
    style_lsc2_sr_pure_blue,
    style_lsc2_sr_pure_green,
    style_lsc2_sr_pure_red,
    style_lsc2_sr_pure_nir,
    style_lsc2_sr_swir_1,
    style_lsc2_sr_swir_2,
    style_lsc2_pq,
]

styles_ls8c2_sr_list = [
    style_lsc2_sr_simple_rgb,
    style_lsc2_sr_irg,
    style_lsc2_sr_ndvi,
    style_lsc2_sr_ndwi,
    style_lsc2_sr_mndwi,
    style_lsc2_sr_pure_blue,
    style_lsc2_sr_pure_green,
    style_lsc2_sr_pure_red,
    style_lsc2_sr_pure_nir,
    style_lsc2_sr_swir_1,
    style_lsc2_sr_swir_2,
    style_ls8c2_pq,
]

# detangle common styles from satellite names!
