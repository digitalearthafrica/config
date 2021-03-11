from ows_refactored.common.ows_reslim_cfg import reslim_alos_palsar

bands_crop_mask = {"mask": ["crop_mask", "MASK"], "prob": ["crop_prob", "PROB"]}


style_crop_mask_magma = {
    "name": "magma",
    "title": "PROB",
    "abstract": "Prob band",
    "needed_bands": ["prob"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "prob",
        },
    },
    "color_ramp": [
        {"value": 50, "color": "#000003"},
        {"value": 100, "color": "#e2f4dd"},
    ],
    "legend": {
        "begin": 50,
        "end": 100,
        "decimal_places": 0,
        "ticks_every": 10,
    },
}

style_crop_mask_green = {
    "name": "green",
    "title": "Green",
    "abstract": "Classified as water by the decision tree",
    "value_map": {
        "crop": [
            {
                "title": "Green",
                "abstract": "Crop",
                "flags": {"mask": True},
                "color": "#00ff00",
            },
            {
                "title": "No Crop",
                "abstract": "No crop",
                "flags": {"mask": False},
                "color": "#00ff00",
                "alpha": 0.0
            },
        ]
    },
}

style_crop_mask_yellow = {
    "name": "yellow",
    "title": "Yellow",
    "abstract": "Classified as water by the decision tree",
    "value_map": {
        "crop": [
            {
                "title": "Yellow",
                "abstract": "Crop",
                "flags": {"mask": True},
                "color": "#ffff00",
            },
            {
                "title": "No Crop",
                "abstract": "No crop",
                "flags": {"mask": False},
                "color": "#ffff00",
                "alpha": 0.0
            },
        ]
    },
}

style_crop_mask_reversed = {
    "name": "reversed",
    "title": "Reversed",
    "abstract": "Classified as water by the decision tree",
    "value_map": {
        "crop": [
            {
                "title": "Yellow",
                "abstract": "Crop",
                "flags": {"mask": False},
                "color": "#cccccc",
            },
            {
                "title": "No Crop",
                "abstract": "No crop",
                "flags": {"mask": True},
                "color": "#cccccc",
                "alpha": 0.0
            },
        ]
    },
}

layer = {
    "title": "Crop Mask Prototype",
    "name": "crop_mask_eastern",
    "abstract": """
For more information on the product, see https://www.eorc.jaxa.jp/ALOS/en/palsar_fnf/fnf_index.htm

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
    "product_name": "crop_mask_eastern",
    "time_resolution": "year",
    "bands": bands_crop_mask,
    "resource_limits": reslim_alos_palsar,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "wcs": {
        "native_crs": "EPSG:4326",
        "native_resolution": [0.000222222222222, -0.000222222222222],
        "default_bands": ["mask", "prob"],
    },
    "styling": {
        "default_style": "green",
        "styles": [
            style_crop_mask_green,
            style_crop_mask_magma,
            style_crop_mask_yellow,
            style_crop_mask_reversed,
        ],
    },
}
