

bands_ls8c = {
    "red": [],
    "green": [],
    "blue": [],
    "nir": [],
    "swir_1": [],
    "swir_2": [],
}



bands_s2_gm = {
    "B02": ["band_02", "blue"],
    "B03": ["band_03", "green"],
    "B04": ["band_04", "red"],
    "B05": ["band_05", "red_edge_1"],
    "B06": ["band_06", "red_edge_2"],
    "B07": ["band_07", "red_edge_3"],
    "B08": ["band_08", "nir", "nir_1"],
    "B8A": ["band_8a", "nir_narrow", "nir_2"],
    "B11": ["band_11", "swir_1", "swir_16"],
    "B12": ["band_12", "swir_2", "swir_22"],
    "SMAD": ["smad", "sdev"],
    "EMAD": ["emad", "edev"],
    "BCMAD": ["bcmad", "bcdev", "BCDEV"],
    "COUNT": ["count"]
}

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
        {"value": -0.1, "color": "#1696FF", "legend": {"prefix": "<"}},
        {"value": -0.1, "color": "#1696FF"},
        {"value": 0.0, "color": "#00FFDF", "legend": {}},
        {
            "value": 0.1,
            "color": "#FFF50E",
        },
        {"value": 0.2, "color": "#FFB50A", "legend": {}},
        {
            "value": 0.4,
            "color": "#FF530D",
        },
        {"value": 0.5, "color": "#FF0000", "legend": {"prefix": ">"}},
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
        }
    },
}


# styles tmad
sdev_scaling = [0.020, 0.18]
edev_scaling = [6.2, 7.3]
bcdev_scaling = [0.025, 0.13]

style_tmad_sdev_std = {
    "name": "arcsec_sdev",
    "title": "SMAD",
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
            "0.0": {"label": "Low\ntmad"},
            "4.0": {"label": "High\ntmad"},
        },
    },
}

style_tmad_edev_std = {
    "name": "log_edev",
    "title": "EMAD",
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
            "0.0": {"label": "Low\ntmad"},
            "4.0": {"label": "High\ntmad"},
        },
    },
}


style_tmad_bcdev_std = {
    "name": "log_bcdev",
    "title": "BCMAD",
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
            "0.0": {"label": "Low\ntmad"},
            "4.0": {"label": "High\ntmad"},
        },
    },
}

style_tmad_rgb_std = {
    "name": "tmad_rgb_std",
    "title": "TMAD multi-band false-colour (standard)",
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
    "title": "TMAD multi-band false-colour (sensitive)",
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


layers = {
                    "title": "Annual Geometric Median",
                    "abstract": "Landsat Geomedian based on USGS Provisional Collection 2 Level 2 Scenes",
                    "layers": [
                        {
                            "title": "Surface Reflectance Annual Geomedian Landsat 8 (Beta)",
                            "name": "ga_ls8c_gm_2_annual",
                            "abstract": """
Individual remote sensing images can be affected by noisy data, including clouds, cloud shadows, and haze. To produce cleaner images that can be compared more easily across time, we can create 'summary' images or 'composites' that combine multiple images into one image to reveal the median or 'typical' appearance of the landscape for a certain time period. One approach is to create a geomedian. A geomedian is based on a high-dimensional statistic called the 'geometric median' (Small 1990), which effectively trades a temporal stack of poor-quality observations for a single high-quality pixel composite with reduced spatial noise (Roberts et al. 2017).

In contrast to a standard median, a geomedian maintains the relationship between spectral bands. This allows for conducting further analysis on the composite images just as we would on the original satellite images (e.g. by allowing the calculation of common band indices like NDVI). An annual median image is calculated from the surface reflectance values drawn from a calendar year.

This product has a spatial resolution of 30 m and a temporal coverage of 2018. The surface reflectance values are scaled to be between 0 and 65,455.

It is derived from Landsat 8 satellite observations as part of a provisional Landsat Collection 2 surface reflectance product.

Annual geomedian images enable easy visual and algorithmic interpretation, e.g. understanding urban expansion, at annual intervals. They are also useful for characterising permanent landscape features such as woody vegetation.

For more information on the algorithm, see https://doi.org/10.1109/TGRS.2017.2723896

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
                            "product_name": "ga_ls8c_gm_2_annual",
                            "time_resolution": "year",
                            "bands": bands_ls8c,
                            "resource_limits": reslim_srtm,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": False,
                            },
                            "wcs": {
                                "native_crs": "EPSG:6933",
                                "native_resolution": [30.0, -30.0],
                                "default_bands": ["red", "green", "blue"],
                            },
                            "styling": {
                                "default_style": "simple_rgb",
                                "styles": [
                                    style_gals_simple_rgb,
                                    style_gals_irg,
                                    # style_ls_ndvi, style_ls_ndwi,
                                    # style_gals_mndwi,
                                    style_gals_pure_blue,
                                    style_gals_pure_green,
                                    style_gals_pure_red,
                                    style_gals_pure_nir,
                                    style_gals_pure_swir1,
                                    style_gals_pure_swir2,
                                ],
                            },
                        },
                        {
                            "title": "Surface Reflectance Annual Geomedian Sentinel-2 (Beta)",
                            "name": "ga_s2_gm",
                            "abstract": """
Individual remote sensing images can be affected by noisy data, including clouds, cloud shadows, and haze. To produce cleaner images that can be compared more easily across time, we can create 'summary' images or 'composites' that combine multiple images into one image to reveal the median or 'typical' appearance of the landscape for a certain time period. One approach is to create a geomedian. A geomedian is based on a high-dimensional statistic called the 'geometric median' (Small 1990), which effectively trades a temporal stack of poor-quality observations for a single high-quality pixel composite with reduced spatial noise (Roberts et al. 2017).

In contrast to a standard median, a geomedian maintains the relationship between spectral bands. This allows for conducting further analysis on the composite images just as we would on the original satellite images (e.g. by allowing the calculation of common band indices like NDVI). An annual median image is calculated from the surface reflectance values drawn from a calendar year.

This product has a spatial resolution of 10 m and a temporal coverage of 2019.

It is derived from Surface Reflectance Sentinel-2 data. This product contains modified Copernicus Sentinel data 2019.

Annual geomedian images enable easy visual and algorithmic interpretation, e.g. understanding urban expansion, at annual intervals. They are also useful for characterising permanent landscape features such as woody vegetation.

For more information on the algorithm, see https://doi.org/10.1109/TGRS.2017.2723896

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
 """,
                            "product_name": "ga_s2_gm",
                            # Low product name
                            #
                            # Leave commented until we have an appropriate summary product.
                            # (Packaged like the main product, but with much much lower
                            # resolution and much much higher area covered in each dataset.
                            #
                            "low_res_product_name": "ga_s2_gm_lowres",
                            "bands": bands_s2_gm,
                            "dynamic": False,
                            "resource_limits": reslim_sentinel2,
                            "time_resolution": "year",
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": False,  # True
                                "apply_solar_corrections": False,
                            },
                            "wcs": {
                                "native_crs": "EPSG:6933",
                                "native_resolution": [10.0, -10.0],
                                "default_bands": ["red", "green", "blue"],
                            },
                            "styling": {
                                "default_style": "simple_rgb",
                                "styles": [
                                    style_ls_simple_rgb,
                                    style_s2_irg,
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
                                    style_sentinel_count,
                                ],
                            },
                        },
                        {
                            "title": "Surface Reflectance Annual Median Absolute Deviations Sentinel-2 (Beta)",
                            "name": "ga_s2_tmad",
                            "abstract": """
Variability is an important characteric that can be used to map and distinguish different types of land surfaces. The median absolute deviation (MAD) is a robust measure (resilient to outliers) of the variability within a dataset. For multi-spectral Earth observation, deviation can be measured against the geomedian of a time-series using a number of distance metrics. Three of these metrics are adopted in this product: - Euclidean distance (EMAD), which is more sensitive to changes in target brightness. - Cosine (spectral) distance (SMAD), which is more sensitive to changes in target spectral response. - Bray Curtis dissimilarity (BCMAD), which is more sensitive to the distribution of the observation values through time. Together, the triple MADs provide information on variance in the input data over a given time period. The metrics are selected to highlight different types of changes in the landscape.

This product has a spatial resolution of 10 m and a temporal coverage of 2019.

It is derived from Surface Reflectance Sentinel-2 data. This product contains modified Copernicus Sentinel data 2019.

The MADs can be used on their own or together with geomedian to gain insights about the land surface, e.g. for land cover classificiation and for change detection from year to year.

For more information on the algorithm, see https://doi.org/10.1109/IGARSS.2018.8518312

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
 """,
                            "product_name": "ga_s2_gm",
                            # Low product name
                            #
                            # Leave commented until we have an appropriate summary product.
                            # (Packaged like the main product, but with much much lower
                            # resolution and much much higher area covered in each dataset.
                            #
                            "low_res_product_name": "ga_s2_gm_lowres",
                            "bands": bands_s2_gm,
                            "dynamic": False,
                            "resource_limits": reslim_sentinel2,
                            "time_resolution": "year",
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": False,  # True
                                "apply_solar_corrections": False,
                            },
                            "wcs": {
                                "native_crs": "EPSG:6933",
                                "native_resolution": [10.0, -10.0],
                                "default_bands": ["red", "green", "blue"],
                            },
                            "styling": {
                                "default_style": "tmad_rgb_std",
                                "styles": [
                                    style_tmad_rgb_std,
                                    style_tmad_rgb_sens,
                                    style_tmad_sdev_std,
                                    style_tmad_edev_std,
                                    style_tmad_bcdev_std,
                                    style_sentinel_count,
                                ],
                            },
                        },
                    ],
                }