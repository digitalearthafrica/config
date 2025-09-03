from ows_refactored.common.ows_reslim_cfg import reslim_land_cover

style_activecropland = {
    "name": "style_colours",
    "title": "Coloured",
    "abstract": "Land cover colours",
    "needed_bands": ["classification"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "classification",
        },
    },
    "value_map": {
        "classification": [
            {
                "title": "Inactive cropland",
                "abstract": "",
                "values": [0],
                "alpha": 0.0,
                "color": "#fcfc44",
            },
            {
                "title": "Active cropland",
                "abstract": "",
                "values": [100],
                "color": "#004f01",
            },
        ]
    },
    "legend": {"width": 3.0, "height": 4.0},
}

style_irrigated = {
    "name": "style_colours",
    "title": "Coloured",
    "abstract": "Land cover colours",
    "needed_bands": ["classification"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "classification",
        },
    },
    "value_map": {
        "classification": [
            {
                "title": "Rainfed",
                "abstract": "",
                "values": [0],
                "alpha": 0.0,
                "color": "#fc44ce",
            },
            {
                "title": "Irrigated",
                "abstract": "",
                "values": [100],
                "color": "#4494fc",
            }
        ]
    },
    "legend": {"width": 3.0, "height": 4.0},
}

style_maize = {
    "name": "style_colours",
    "title": "Coloured",
    "abstract": "Land cover colours",
    "needed_bands": ["classification"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "classification",
        },
    },
    "value_map": {
        "classification": [
            {
                "title": "Maize cropland",
                "abstract": "",
                "values": [100],
                "color": "#fcfc44",
            },
        ]
    },
    "legend": {"width": 3.0, "height": 4.0},
}

style_temporarycrops = {
    "name": "style_colours",
    "title": "Coloured",
    "abstract": "Land cover colours",
    "needed_bands": ["classification"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "classification",
        },
    },
    "value_map": {
        "classification": [
            {
                "title": "Temporary crops",
                "abstract": "",
                "values": [100],
                "color": "#f50707",
            },
        ]
    },
    "legend": {"width": 3.0, "height": 4.0},
}

style_wintercereals = {
    "name": "style_colours",
    "title": "Coloured",
    "abstract": "Land cover colours",
    "needed_bands": ["classification"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "classification",
        },
    },
    "value_map": {
        "classification": [
            {
                "title": "Winter cereals",
                "abstract": "",
                "values": [100],
                "color": "#f7882d",
            },
        ]
    },
    "legend": {"width": 3.0, "height": 4.0},
}


activecropland_layer = {
    "title": "ESA Worldcereal Active Cropland",
    "name": "esa_worldcereal_activecropland",
    "abstract": """
ESA WorldCereal 10m 2021 v1.0.0 active cropland map for the main cereals season defined in a region (tc-wintercereals). 

For more information, see https://esa-worldcereal.org/en/products/global-maps
""",
    "product_name": "esa_worldcereal_activecropland",
    "time_resolution": "year",
    "bands": {
        "classification": [],
    },
    "resource_limits": reslim_land_cover,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [
        0.000083333333333,
        -0.000083333333333,
    ],
    "styling": {
        "default_style": "style_colours",
        "styles": [style_activecropland],
    },
}

maize_active_layer = {
    "title": "ESA Worldcereal Active Maize Cropland",
    "name": "esa_worldcereal_maize_active",
    "abstract": """
ESA WorldCereal 10m 2021 v1.0.0 active cropland map for the main maize season defined in a region (tc-maize-main). 
For more information, see https://esa-worldcereal.org/en/products/global-maps
""",
    "product_name": "esa_worldcereal_maize_active",
    "time_resolution": "year",
    "bands": {
        "classification": [],
    },
    "resource_limits": reslim_land_cover,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [
        0.000083333333333,
        -0.000083333333333,
    ],
    "styling": {
        "default_style": "style_colours",
        "styles": [style_activecropland],
    },
}

maize_irrigation_layer = {
    "title": "ESA Worldcereal Irrgiated Maize",
    "name": "esa_worldcereal_maize_irrigation",
    "abstract": """
ESA WorldCereal 10m 2021 v1.0.0 irrigation map for the main maize season defined in a region (tc-maize-main).
For more information, see https://esa-worldcereal.org/en/products/global-maps
""",
    "product_name": "esa_worldcereal_maize_irrigation",
    "time_resolution": "year",
    "bands": {
        "classification": [],
    },
    "resource_limits": reslim_land_cover,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [
        0.000083333333333,
        -0.000083333333333,
    ],
    "styling": {
        "default_style": "style_colours",
        "styles": [style_irrigated],
    },
}

wintercereals_irrigation_layer = {
    "title": "ESA WorldCereal Winter Cereals – Irrigation",
    "name": "esa_worldcereal_wintercereals_irrigation",
    "abstract": """
ESA WorldCereal 10m 2021 v1.0.0 irrigation map for the main cereals season defined in a region (tc-wintercereals).
For more information, see https://esa-worldcereal.org/en/products/global-maps
""",
    "product_name": "esa_worldcereal_wintercereals_irrigation",
    "time_resolution": "year",
    "bands": {
        "classification": [],
    },
    "resource_limits": reslim_land_cover,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [
        0.000083333333333,
        -0.000083333333333,
    ],
    "styling": {
        "default_style": "style_colours",
        "styles": [style_irrigated],
    },
}

maize_main_layer = {
    "title": "ESA WorldCereal Main-Season Maize",
    "name": "esa_worldcereal_maize_main",
    "abstract": """
ESA WorldCereal 10m 2021 v1.0.0 maize crop map for main maize season defined in a region.
For more information, see https://esa-worldcereal.org/en/products/global-maps
""",
    "product_name": "esa_worldcereal_maize_main",
    "time_resolution": "year",
    "bands": {
        "classification": [],
    },
    "resource_limits": reslim_land_cover,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [
        0.000083333333333,
        -0.000083333333333,
    ],
    "styling": {
        "default_style": "style_colours",
        "styles": [style_maize],
    },
}

temporarycrops_layer = {
    "title": "ESA WorldCereal Temporary Cropland Extent",
    "name": "esa_worldcereal_temporarycrops",
    "abstract": """
ESA WorldCereal 10m 2021 v1.0.0 temporary crops map for the 2021 tc-annual season.
For more information, see https://esa-worldcereal.org/en/products/global-maps
""",
    "product_name": "esa_worldcereal_temporarycrops",
    "time_resolution": "year",
    "bands": {
        "classification": [],
    },
    "resource_limits": reslim_land_cover,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [
        0.000083333333333,
        -0.000083333333333,
    ],
    "styling": {
        "default_style": "style_colours",
        "styles": [style_temporarycrops],
    },
}

wintercereals_layer = {
    "title": "ESA WorldcerealWinter Cerealsd",
    "name": "esa_worldcereal_wintercereals",
    "abstract": """
ESA WorldCereal 10m 2021 v1.0.0 wintercereals crop map for the main cereals season defined in a region (tc-wintercereals).
For more information, see https://esa-worldcereal.org/en/products/global-maps
""",
    "product_name": "esa_worldcereal_wintercereals",
    "time_resolution": "year",
    "bands": {
        "classification": [],
    },
    "resource_limits": reslim_land_cover,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "": [
        0.native_resolution000083333333333,
        -0.000083333333333,
    ],
    "styling": {
        "default_style": "style_colours",
        "styles": [style_wintercereals],
    },
}
