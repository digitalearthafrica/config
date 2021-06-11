from ows_refactored.common.ows_reslim_cfg import reslim_srtm

bands_fc = {
    "bs": ["BS", "bare_soil"],
    "pv": ["PV", "green_vegetation"],
    "npv": ["NPV", "brown_vegetation"],
    "ue": ["UE", "unmixing_error"],
}


style_fc_simple_rgb = {
    "name": "simple_rgb",
    "title": "Simple RGB",
    "abstract": "Simple true-colour image, using the red, green and blue bands",
    "components": {
        "red": {"BS_PC_50": 1.0},
        "green": {"PV_PC_50": 1.0},
        "blue": {"NPV_PC_50": 1.0},
    },
    "scale_range": [0.0, 100.0],
    "pq_masks": [
        {
            "flags": {
                "sea": True,
            },
            "invert": True,
        },
    ],
}


style_fc_simple = {
    "name": "simple_fc",
    "title": "Fractional Cover",
    "abstract": "Fractional cover representation, with green vegetation in green, dead vegetation in blue, and bare soil in red",
    "components": {"red": {"BS": 1.0}, "green": {"PV": 1.0}, "blue": {"NPV": 1.0}},
    "scale_range": [0.0, 100.0],
    "pq_masks": [
        {
            "flags": {"dry": True},
        },
        {"flags": {"cloud_shadow": False, "cloud": False}},
    ],
    "legend": {
        "url": "https://data.digitalearth.africa/usgs/pc2/ga_ls8c_fractional_cover_2/FC_legend.png",
    },
}

style_fc_unmasked = {
    "name": "simple_fc_unmasked",
    "title": "Fractional Cover",
    "abstract": "Fractional cover representation, with green vegetation in green, dead vegetation in blue, and bare soil in red",
    "components": {"red": {"BS": 1.0}, "green": {"PV": 1.0}, "blue": {"NPV": 1.0}},
    "scale_range": [0.0, 100.0],
    "legend": {
        "url": "https://data.digitalearth.africa/usgs/pc2/ga_ls8c_fractional_cover_2/FC_legend.png",
    },
}

layer = {
    "title": "Fractional Cover (development)",
    "name": "fc_ls",
    "abstract": """
Fractional cover describes the landscape in terms of coverage by green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.) and bare soil. It provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time.

This product has a spatial resolution of 30 m and a temporal coverage of 1980s to current.

It is derived from Landsat Collection 2 surface reflectance product.

Fractional cover allows users to understand the large scale patterns and trends and inform evidence based decision making and policy on topics including wind and water erosion risk, soil carbon dynamics, land surface process monitoring, land management practices, vegetation studies, fuel load estimation, ecosystem modelling, and rangeland condition.

The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, for more information see http://data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Seasonal+Fractional+Cover

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
    "product_name": "fc_ls",
    "bands": bands_fc,
    "resource_limits": reslim_srtm,
    "dynamic": True,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "wcs": {
        "native_crs": "EPSG:4326",
        "native_resolution": [30.0, -30.0],
        "default_bands": ["BS", "PV", "NPV"],
    },
    "styling": {
        "default_style": "simple_fc_unmasked",
        "styles": [style_fc_unmasked],
    },
}
