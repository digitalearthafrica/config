from ows_refactored.common.ows_reslim_cfg import reslim_io_lulc

bands_esri = {
    "data": [],
}

style_colours = {
    "name": "style_colours",
    "title": "Coloured",
    "abstract": "Land cover colours",
    "needed_bands": ["data"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "data",
        },
    },
    "value_map": {
        "data": [
            {
                "title": "",
                "abstract": "",
                "values": [0],
                "alpha": 0.0,
                "color": "#707070",
            },
            {
                "title": "Water",
                "abstract": "",
                "values": [1],
                "color": "#419BDF",
            },
            {
                "title": "Trees",
                "abstract": "",
                "values": [2],
                "color": "#397D49",
            },
            {
                "title": "Grass",
                "abstract": "",
                "values": [3],
                "color": "#88B053",
            },
            {
                "title": "Flooded Vegetation",
                "abstract": "",
                "values": [4],
                "color": "#7A87C6",
            },
            {
                "title": "Crops",
                "abstract": "",
                "values": [5],
                "color": "#E49635",
            },
            {
                "title": "Scrub/Shrub",
                "abstract": "",
                "values": [6],
                "color": "#DFC35A",
            },
            {
                "title": "Built Area",
                "abstract": "",
                "values": [7],
                "color": "#C4281B",
            },
            {
                "title": "Bare Ground",
                "abstract": "",
                "values": [8],
                "color": "#A59B8F",
            },
            {
                "title": "Snow/Ice",
                "abstract": "",
                "values": [9],
                "color": "#A8EBFF",
            },
            {
                "title": "Clouds",
                "abstract": "",
                "values": [10],
                "color": "#616161",
            },
        ]
    },
    "legend": {"width": 3.0, "height": 3.0},
}

layer = {
    "title": "ESRI Land Use/Land Cover",
    "name": "esri_lulc",
    "abstract": """
Global estimates of 10-class land use/land cover (LULC) for 2020, derived from ESA Sentinel-2 imagery at 10m resolution.

This dataset was generated by Impact Observatory, who used billions of human-labeled pixels (curated by the National Geographic Society) to train a deep learning model for land classification.

The global map was produced by applying this model to the Sentinel-2 2020 scene collection on the Planetary Computer.
""",
    "product_name": "io_lulc",
    "time_resolution": "year",
    "bands": bands_esri,
    "resource_limits": reslim_io_lulc,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:6933",
    "native_resolution": [
        10.0,
        -10.0,
    ],
    "wcs": {
        "default_bands": ["data"],
    },
    "styling": {
        "default_style": "style_colours",
        "styles": [style_colours],
    },
}