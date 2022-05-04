from ows_refactored.common.ows_reslim_cfg import reslim_continental

# styles

style_mrvbf = {
    "name": "style_mrvbf",
    "title": "Multi-resolution Valley Bottom Flatness (MrVBF)",
    "abstract": "Multi-resolution Valley Bottom Flatness (MrVBF) derived from SRTM elevation model",
    "needed_bands": ["mrvbf"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mrvbf",
        },
    },
    "color_ramp": srtm_deriv_ylgnbu,
    "legend": {
        "title": "MrVBF ",
        "begin": "0",
        "end": "7",
        "ticks_every": 1,
    },
}

style_mrrtf = {
    "name": "style_mrrtf",
    "title": "Multi-resolution Ridge Top Flatness (MrRTF)",
    "abstract": "Multi-resolution Ridge Top Flatness (MrRTF) derived from SRTM elevation model",
    "needed_bands": ["mrrtf"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "mrrtf",
        },
    },
    "color_ramp": srtm_deriv_ylorred,
    "legend": {
        "title": "MrRTF ",
        "begin": "0",
        "end": "7",
        "ticks_every": 1,
    },
}

style_slope = {
    "name": "style_slope",
    "title": "Slope",
    "abstract": "Slope (percentage) derived from SRTM elevation model",
    "needed_bands": ["slope"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "slope",
        },
    },
    "color_ramp": [
        {"value": -0, "color": "#00224e"},
        {"value": 10, "color": "#35456c"},
        {"value": 20, "color": "#666970"},
        {"value": 30, "color": "#948e77"},
        {"value": 40, "color": "#c8b866"},
        {"value": 50, "color": "#fee838"},
    ],
    "legend": {
        "title": "Slope ",
        "begin": "0",
        "end": "50",
        "ticks_every": 10,
        "units": "%",
        "tick_labels": {
        "50": {"prefix": ">"},
        },
    },
}

# colour ramps
# mrvbf and mrrtf colour styles are interchangeable (scale of 0-7)

srtm_deriv_ylgnbu = [
    {"value": -0, "color": "#ffffd9",
    },
    {"value": 1, "color": "#edf8b1"},
    {"value": 2, "color": "#c7e9b4"},
    {"value": 3, "color": "#7fcdbb"},
    {"value": 4, "color": "#41b6c4"},
    {"value": 5, "color": "#1d91c0"},
    {"value": 6, "color": "#225ea8"},
    {"value": 7, "color": "#0c2c84"}
]

srtm_deriv_ylorred = [
    {"value": -0, "color": "#ffffcc",
    },
    {"value": 1, "color": "#ffeda0"},
    {"value": 2, "color": "#fed976"},
    {"value": 3, "color": "#feb24c"},
    {"value": 4, "color": "#fd8d3c"},
    {"value": 5, "color": "#fc4e2a"},
    {"value": 6, "color": "#e31a1c"},
    {"value": 7, "color": "#b10026"}
]

# layers

layer_srtm_deriv = {
    "title": "SRTM-derived Slope and Flatness Indices (30 m)",
    "name": "srtm_deriv",
    "abstract": """
Derivative products of a Digital Elevation Model (DEM) can be used to better understand the Earth's topography and model illumination, geometry, and aspect. DE Africa provides three Shuttle Radar Topography Mission (SRTM) derivative products:

 - Slope: rate of elevation change, expressed as a percentage
 - Multi-resolution Valley Bottom Flatness (MrVBF): topographic index used to identify valley bottoms, which are useful for hydrological and sedimentation modelling. In this product, 0 indicates areas which are not valley bottom areas, while 1 - 7 indicate increasingly flatter and larger valley bottoms
 - Multi-resolution Ridge Top Flatness (MrRTF): topographic index used for landform classification. It uses a scale of 0 -- 7 inclusive; 0 indicates steep or low locations while 1 - 7 indicate increasingly larger areas of high flat land 
 
The latter two identify the dominant nature of the topography as either ridge-like or valley-like (Gallant and Dowling, 2003).

These derivative products have a spatial resolution of 30 m and are derived from data collected by NASA's Shuttle Radar Topography Mission in 2000.

SRTM data is provided by NASA's Land Processes Distributed Active Archive Center (LP DAAC).

For more information on SRTM, see https://lpdaac.usgs.gov/products/srtmgl1v003/
For more information on generating the derivative product, see https://github.com/digitalearthafrica/dem-derivative

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki).
""",
    "product_name": "dem_srtm_deriv",
    "time_resolution": "year",
    "bands": {
        "elevation": []
    },
    "resource_limits": reslim_continental,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [
        0.00027777777778,
        -0.00027777777778,
    ],
    "styling": {
        "default_style": "style_slope",
        "styles": [style_slope, 
                   style_mrvbf,
                   style_mrrtf],
    },
}