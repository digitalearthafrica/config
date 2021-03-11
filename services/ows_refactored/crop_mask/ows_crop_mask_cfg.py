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
    "title": "Radar Backscatter Annual Mosaic (ALOS/PALSAR)",
    "name": "alos_palsar_mosaic",
    "abstract": """
Synthetic Aperture Radar (SAR) data have been shown to provide different and complementary information to the more common optical remote sensing data. Radar backscatter response is a function of topography, land cover structure, orientation, and moisture characteristics—including vegetation biomass—and the radar signal can penetrate clouds, providing information about the earth’s surface where optical sensors cannot. Digital Earth Africa provides access to Normalized Radar Backscatter data, for which Radiometric Terrain Correction (RTC) has been applied so data acquired with different imaging geometries over the same region can be compared.

The ALOS/PALSAR annual mosaic is a global 25 m resolution dataset that combines data from many images captured by JAXA's PALSAR and PALSAR-2 sensors on ALOS-1 and ALOS-2 satellites respectively.

This product contains radar measurement in L-band and in HH and HV polarizations. It has a spatial resolution of 25 m and is available annually for 2007 to 2010 (ALOS/PALSAR) and 2015 to 2018 (ALOS-2/PALSAR-2). Data is provided as digital number (DN), which can be converted to backscatter in decibel unit using 10*log10(𝐷𝑁^2)-83.0.

It is part of a global dataset provided by the Japan Aerospace Exploration Agency (JAXA) Earth Observation Research Center.

For more information on the product, see https://www.eorc.jaxa.jp/ALOS/en/palsar_fnf/fnf_index.htm

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
    "product_name": "alos_palsar_mosaic",
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
