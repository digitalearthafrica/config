from ows_refactored.common.ows_reslim_cfg import reslim_alos_palsar

bands_crop_mask = {"mask": [], "prob": [], "filtered": []}


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
    "mpl_ramp": "magma",
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

style_crop_mask_prob = {
    "name": "prob",
    "title": "Crop probability",
    "abstract": "Crop probability",
    "needed_bands": ["prob"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "prob",
        },
    },
    "mpl_ramp": "inferno",
    "range": [0, 100],
    "legend": {
        "begin": "0",
        "end": "100",
        "ticks_every": "20",
    },
}

style_crop_mask_green = {
    "name": "green",
    "title": "Crop area (green)",
    "abstract": "Classified as crop",
    "value_map": {
        "mask": [
            {
                "title": "Crop",
                "color": "#00FF00",  # (Or #FFFF00)
                "values": [1],
            }
        ]
    },
}

style_crop_mask_yellow = {
    "name": "yellow",
    "title": "Crop area (yellow)",
    "abstract": "Classified as crop",
    "value_map": {
        "mask": [
            {
                "title": "Crop",
                "color": "#FFFF00",  # (Or #FFFF00)
                "values": [1],
            }
        ]
    },
}

style_crop_mask_filtered_green = {
    "name": "filtered_green",
    "title": "Crop area (filtered, green)",
    "abstract": "Classified as crop and filtered",
    "value_map": {
        "filtered": [
            {
                "title": "Crop",
                "color": "#00FF00",  # (Or #FFFF00)
                "values": [1],
            }
        ]
    },
}

style_crop_mask_filtered_yellow = {
    "name": "filtered_yellow",
    "title": "Crop area (filtered, yellow)",
    "abstract": "Classified as crop and filtered",
    "value_map": {
        "filtered": [
            {
                "title": "Crop",
                "color": "#FFFF00",  # (Or #FFFF00)
                "values": [1],
            }
        ]
    },
}

style_crop_mask_reversed = {
    "name": "reversed",
    "title": "Reversed",
    "abstract": "Classified as crop by the mask band",
    "value_map": {
        "mask": [
            {
                "title": "Crop",
                "color": "#CCCCCC",  # (Or #FFFF00)
                "values": [1],
                "mask": True,  # transparent
            },
            {
                "title": "No Crop",
                "color": "#CCCCCC",  # (Or #FFFF00)
                "values": [0],
            },
        ]
    },
}

layer = {
    "title": "Cropland Extent Map for Eastern Africa",
    "name": "crop_mask_eastern",
    "abstract": """
Digital Earth Africa's cropland extent map for eastern Africa shows the location of croplands in the countries of Tanzania, Kenya, Uganda, Ethiopia, Rwanda, and Burundi.  Cropland is defined as: "a piece of land of minimum 0.04 ha that is sowed/planted and harvest-able at least once within the 12 months after the sowing/planting date."

The product contains two bands, the first band displays the extent of the crop and non-crop classes as a binary map, the second band displays the probabilities of each class prediction as a percentage.  This prototype cropland extent map has a resolution of 20m, and was built using Copernicus Sentinel-2 satellite images from 2019.

The cropland extent map was produced using extensive training data from eastern Africa, coupled with a Random Forest machine learning model. For a detailed exploration of the methods used to produce the cropland extent map, read the jupyter notebooks in DE Africa's crop-mask github repository.

Cropland extent maps are a foundational, baseline layer in high-order crop health and crop productivity products which necessarily rely on knowing where cropping occurs before further analysis can take place.

A preliminary accuracy assessment suggests an overall accuracy of > 85 %. The algorithm tends to report more omission errors (labelling actual crops as non-crops) than commission errors (labelling non-crops as crops). Where commission errors occur they tend to be focussed around wetlands and seasonal grasslands (e.g. in the Serengeti) which spectrally resemble some kinds of cropping.

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
        "native_crs": "epsg:6933",
        "native_resolution": [20, -20],
        "default_bands": ["mask", "prob"],
    },
    "styling": {
        "default_style": "filtered_green",
        "styles": [
            style_crop_mask_filtered_green,
            style_crop_mask_filtered_yellow,
            style_crop_mask_prob,
            style_crop_mask_green,
            style_crop_mask_yellow,
            style_crop_mask_reversed,
        ],
    },
}
