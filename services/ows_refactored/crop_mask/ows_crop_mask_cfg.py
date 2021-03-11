from ows_refactored.common.ows_reslim_cfg import reslim_alos_palsar

bands_crop_mask = {"mask": ["crop_mask", "MASK"], "prob": ["crop_prob", "PROB"]}


style_crop_mask_magma = {
    "name": "magma",
    "title": "PROB",
    "abstract": "Prob band Magma",
    "needed_bands": ["prob"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "prob",
        },
    },
    "mpl_ramp": "plasma",
    "range": [50, 100],
    "legend": {
        "begin": "50",
        "end": "100",
        "ticks_every": "10",
        "tick_labels": {
            "50": {"prefix": "<"},
        },
    },
}

style_crop_mask_green = {
    "name": "green",
    "title": "Green",
    "abstract": "Classified as crop by the mask band",
    "value_map": {
        "crop": [
            {
                "title": "Crop",
                "abstract": "",
                "flags": {"mask": True},
                "color": "#00ff00",
            },
            {
                "title": "No Crop",
                "abstract": "",
                "flags": {"mask": False},
                "color": "#00ff00",
                "alpha": 0.0,
            },
        ]
    },
}

style_crop_mask_yellow = {
    "name": "yellow",
    "title": "Yellow",
    "abstract": "Classified as crop by the mask band",
    "value_map": {
        "crop": [
            {
                "title": "Crop",
                "abstract": "",
                "flags": {"mask": True},
                "color": "#ffff00",
            },
            {
                "title": "No Crop",
                "abstract": "",
                "flags": {"mask": False},
                "color": "#ffff00",
                "alpha": 0.0,
            },
        ]
    },
}

style_crop_mask_reversed = {
    "name": "reversed",
    "title": "Reversed",
    "abstract": "Classified as crop by the mask band",
    "value_map": {
        "crop": [
            {
                "title": "Crop",
                "abstract": "",
                "flags": {"mask": True},
                "color": "#cccccc",
                "alpha": 0.0,
            },
            {
                "title": "No Crop",
                "abstract": "",
                "flags": {"mask": False},
                "color": "#cccccc",
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
