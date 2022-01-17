# -*- coding: utf-8 -*-
from ows_refactored.common.ows_reslim_cfg import reslim_landsat

bands_s1 = {"vv": [], "vh": [], "angle": [], "area": [], "mask": []}


style_s1_vv = {
    "name": "vv",
    "title": "VV",
    "abstract": "VV band",
    "additional_bands": [],
    "components": {
        "red": {"vv": 1.0, "scale_range": [0.0, 0.28]},
        "green": {"vv": 1.0, "scale_range": [0.0, 0.28]},
        "blue": {"vv": 1.0, "scale_range": [0.0, 0.28]},
    },
    "pq_masks": [
        {
            "band": "mask",
            "enum": 1,
        },
    ],
}

style_s1_vh = {
    "name": "vh",
    "title": "VH",
    "abstract": "VH band",
    "additional_bands": [],
    "components": {
        "red": {"vh": 1.0, "scale_range": [0.0, 0.06]},
        "green": {"vh": 1.0, "scale_range": [0.0, 0.06]},
        "blue": {"vh": 1.0, "scale_range": [0.0, 0.06]},
    },
    "pq_masks": [
        {
            "band": "mask",
            "enum": 1,
        },
    ],
}

style_s1_vh_over_vv = {
    "name": "vv_vh_vh_over_vv",
    "title": "VV, VH and VH/VV",
    "abstract": "False colour representation of VV, VH and VH/VV for R, G and B respectively",
    "additional_bands": [],
    "components": {
        "red": {"vv": 1.0, "scale_range": [0.0, 0.28]},
        "green": {"vh": 1.0, "scale_range": [0.0, 0.06]},
        "blue": {
            "function": "datacube_ows.band_utils.band_quotient",
            "mapped_bands": True,
            "kwargs": {"band1": "vh", "band2": "vv", "scale_from": [0.0, 0.49]},
        },
    },
    "pq_masks": [
        {
            "band": "mask",
            "enum": 1,
        },
    ],
}

style_s1_rvi = {
    "name": "rvi",
    "title": "Radar Vegetation Index",
    "abstract": "Dual-pol radar vegetation index for Sentinel-1",
    "index_expression": "4*vh/(vv + vh)",
    "mpl_ramp": "YlGnBu_r",
    "range": [0.0, 1.0],
    "legend": {
        "begin": "0.0",
        "end": "1.0",
        "decimal_places": 1,
        "ticks": ["0.0", "0.2", "0.4", "0.6", "0.8", "1.0"],
    },
    "pq_masks": [
        {
            "band": "mask",
            "enum": 1,
        },
    ],
}


layer = {
    "title": "Normalised radar backscatter (Sentinel-1)",
    "name": "s1_rtc",
    "abstract": """

Synthetic Aperture Radar (SAR) data have been shown to provide different and complementary information to the more common optical remote sensing data. Radar backscatter response is a function of topography, land cover structure, orientation, and moisture characteristics—including vegetation biomass—and the radar signal can penetrate clouds, providing information about the earth’s surface where optical sensors cannot. Digital Earth Africa provides access to Normalized Radar Backscatter data, for which Radiometric Terrain Correction (RTC) has been applied so data acquired with different imaging geometries over the same region can be compared.

The twin Sentinel-1 satellites, launched in 2014 and 2016, are operated by the European Space Agency (ESA) as part of European Commission's Copernicus Programme. They currently collects C-band SAR data every 6 to 12 days over Africa.

This product contains radar measurement in C-band and in VV and VH polarizations. It has a spatial resolution of approximate 20 m, a temporal coverage of July 2018 to current and is updated as new images are acquired. Data is provided as Gamma0 in linear power, which can be converted to backscatter in decibel unit using 10*log10(DN).

This dataset is processed by Sinergise Sentinel Hub using Sentinel-1 GRD product provided by ESA as input. RTC has been calcuated using 30 m Copernicus Digital Elevation Model.

More techincal information about the Sentinel-1 Normalized Backscatter can be found in the User Guide (https://docs.digitalearthafrica.org/en/latest/data_specs/Sentinel-1_specs.html)

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
    "product_name": "s1_rtc",
    "bands": bands_s1,
    "dynamic": True,
    "resource_limits": reslim_landsat,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "product": "s1_rtc",
            "band": "mask",
        },
    ],
    "native_crs": "EPSG:4326",
    "native_resolution": [0.0002, -0.0002],
    "styling": {
        "default_style": "vv_vh_vh_over_vv",
        "styles": [
            style_s1_vh_over_vv,
            style_s1_vv,
            style_s1_vh,
            style_s1_rvi,
        ],
    },
}
