from ows_refactored.common.ows_reslim_cfg import reslim_landsat

bands_fc = {
    "bs": ["BS", "bare_soil"],
    "pv": ["PV", "green_vegetation"],
    "npv": ["NPV", "brown_vegetation"],
    "ue": ["UE", "unmixing_error"],
}

style_fc_rgb_masked = {
    "name": "fc_rgb_masked",
    "title": "Fractional cover (masked) - BS, PV, NPV",
    "abstract": "Fractional cover representation, with green vegetation in green, brown vegetation in blue, and bare soil in red",
    "components": {"red": {"BS": 1.0}, "green": {"PV": 1.0}, "blue": {"NPV": 1.0}},
    "scale_range": [0.0, 100.0],
    "pq_masks": [
        {
            "band": "water",
            "flags": {"dry": True},
        },
        {
            "band": "water",
            "flags": {"cloud_shadow": False, "cloud": False},
        },
    ],
    "legend": {
        "show_legend": True,
        "url": {
            "en": "https://deafrica-services.s3.af-south-1.amazonaws.com/fc_ls/fc_legend.png",
        }
    },
}

style_fc_rgb_unmasked = {
    "name": "fc_rgb_unmasked",
    "title": "Fractional cover (unmasked) - BS, PV, NPV",
    "abstract": "Fractional cover representation, with green vegetation in green, brown vegetation in blue, and bare soil in red",
    "components": {"red": {"BS": 1.0}, "green": {"PV": 1.0}, "blue": {"NPV": 1.0}},
    "scale_range": [0.0, 100.0],
    "legend": {
        "show_legend": True,
        "url": {
            "en": "https://deafrica-services.s3.af-south-1.amazonaws.com/fc_ls/fc_legend.png",
        }
    },
}

layer = {
    "title": "Fractional cover (provisional)",
    "name": "fc_ls",
    "abstract": """
Fractional cover describes the landscape in terms of coverage by green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.) and bare soil. It provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time.

This product has a spatial resolution of 30 m and a temporal coverage of 1980s to current. It is derived from Landsat Collection 2 Surface Reflectance product.

Fractional cover allows users to understand the large scale patterns and trends and inform evidence based decision making and policy on topics including wind and water erosion risk, soil carbon dynamics, land surface process monitoring, land management practices, vegetation studies, fuel load estimation, ecosystem modelling, and rangeland condition.

The fractional cover algorithm was developed by the Joint Remote Sensing Research Program: http://data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Seasonal+Fractional+Cover

More techincal information about the fractional cover product can be found in the User Guide (https://docs.digitalearthafrica.org/en/latest/data_specs/Fractional_Cover_specs.html)
""",
    "product_name": "fc_ls",
    "bands": bands_fc,
    "resource_limits": reslim_landsat,
    "dynamic": True,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "product": "wofs_ls",
            "band": "water",
            "fuse_func": "datacube_ows.wms_utils.wofls_fuser",
            "ignore_info_flags": [],
        },
    ],
    "native_crs": "EPSG:3857",
    "native_resolution": [30.0, -30.0],
    "styling": {
        "default_style": "fc_rgb_unmasked",
        "styles": [
            style_fc_rgb_unmasked,
            style_fc_rgb_masked
        ],
    },
}
