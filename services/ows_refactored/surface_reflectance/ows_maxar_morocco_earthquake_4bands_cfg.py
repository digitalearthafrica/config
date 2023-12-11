from ows_refactored.common.ows_reslim_cfg import reslim_smart5

bands_Maxar_4bands = {
    "ms_analytic_band_B": ["blue"],
    "ms_analytic_band_G": ["green"],
    "ms_analytic_band_R": ["red"],
    "ms_analytic_band_N": ["nir"],
    "pan_analytic": ["panchromatic"],
    "visual_band_R": ["visual_red"],
    "visual_band_G": ["visual_green"],
    "visual_band_B": ["visual_blue"],
}

style_maxar_simple_rgb = {
    "name": "simple_rgb",
    "title": "Maxar - Red, Green, Blue",
    "abstract": "Simple true-colour image, using the red, green and blue bands",
    "components": {"red": {"visual_red": 1.0}, "green": {"visual_green": 1.0}, "blue": {"visual_blue": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_maxar_blue = {
    "name": "blue",
    "title": "Blue",
    "abstract": "Blue band",
    "components": {"red": {"blue": 1.0}, "green": {"blue": 1.0}, "blue": {"blue": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_maxar_green = {
    "name": "green",
    "title": "Green",
    "abstract": "Green band",
    "components": {"red": {"green": 1.0}, "green": {"green": 1.0}, "blue": {"green": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_maxar_red = {
    "name": "red",
    "title": "Red",
    "abstract": "Red band",
    "components": {"red": {"red": 1.0}, "green": {"red": 1.0}, "blue": {"red": 1.0}},
    "scale_range": [0.0, 3000.0],
}

style_maxar_nir = {
    "name": "nir",
    "title": "NIR",
    "abstract": "NIR band",
    "components": {"red": {"nir": 1.0}, "green": {"nir": 1.0}, "blue": {"nir": 1.0}},
    "scale_range": [0.0, 3000.0],
}

styles_maxar_list = [
    style_maxar_simple_rgb,
    style_maxar_blue,
    style_maxar_green,
    style_maxar_red,
    style_maxar_nir
]

layer = {
    "title": "Maxar Morocco Earthquake 4 bands",
    "name": "maxar_morocco_earthquake_4bands",
    "abstract": """
Maxar Open Data for the 2023 Morocco Earthquake that struck Morocco at 11:11 p.m. local time on Friday, September 8, 2023, with a strong magnitude 6.8.


""",
    "product_name": "maxar_morocco_earthquake_4bands",
    "bands": bands_Maxar_4bands,
    "dynamic": False,
    "resource_limits": reslim_smart5,
    "time_resolution": "summary",
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:32629",
    "native_resolution": [0.47, -0.47],
    "styling": {
        "default_style": "simple_rgb",
        "styles": styles_maxar_list,
    },
}
