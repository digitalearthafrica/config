from ows_refactored.common.ows_reslim_cfg import reslim_alos_palsar

bands_alos = {"hh": [], "hv": [], "mask": [], "date": [], "linci": []}


style_alos_hh = {
    "name": "hh",
    "title": "HH",
    "abstract": "HH band",
    "needed_bands": ["hh"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "hh",
        },
    },
    "color_ramp": [
        {"value": 0, "color": "#f7fcf5"},
        {"value": 750, "color": "#e2f4dd"},
        {"value": 1000, "color": "#c0e6b9"},
        {"value": 1500, "color": "#94d390"},
        {"value": 2500, "color": "#60ba6c"},
        {"value": 4000, "color": "#329b51"},
        {"value": 6000, "color": "#0c7835"},
        {"value": 8000, "color": "#00441b"},
    ],
    "legend": {
        "begin": 0,
        "end": 8000,
        "ticks": ["0", "2000", "4000", "6000", "8000"],
        "tick_labels": {
            "0": {"label": "0"},
            "2000": {"label": "2000"},
            "4000": {"label": "4000"},
            "6000": {"label": "6000"},
            "8000": {"prefix": ">"},
        },
    },
}

style_alos_hv = {
    "name": "hv",
    "title": "HV",
    "abstract": "HV band",
    "needed_bands": ["hv"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "hv",
        },
    },
    "color_ramp": [
        {"value": 0, "color": "#f7fcf5"},
        {"value": 250, "color": "#e2f4dd"},
        {"value": 300, "color": "#c0e6b9"},
        {"value": 500, "color": "#94d390"},
        {"value": 800, "color": "#60ba6c"},
        {"value": 2000, "color": "#329b51"},
        {"value": 3500, "color": "#0c7835"},
        {"value": 4500, "color": "#00441b"},
    ],
    "legend": {
        "begin": 0,
        "end": 4500,
        "ticks": ["0", "500", "2000", "3500", "4500"],
        "tick_labels": {
            "0": {"label": "0"},
            "500": {"label": "500"},
            "2000": {"label": "2000"},
            "3500": {"label": "3500"},
            "4500": {"prefix": ">"},
        },
    },
}


style_alos_hv_over_hh = {
    "name": "hh_hv_hv_over_hh",
    "title": "HH, HV and HV/HH",
    "abstract": "False colour representation of HH, HV and HV over HH for R, G and B respectively",
    "additional_bands": [],
    "components": {
        "red": {"hh": 1.0, "scale_range": [500, 10000]},
        "green": {"hv": 1.0, "scale_range": [200, 4000]},
        "blue": {
            "function": "datacube_ows.band_utils.band_quotient",
            "mapped_bands": True,
            "kwargs": {"band1": "hv", "band2": "hh", "scale_from": [0.1, 1.0]},
        },
    },
}

style_alos_radar_veg_idx = {
    "name": "rvi",
    "title": "Radar Vegetation Index",
    "abstract": "Radar Vegetation Index (HH,HV)",
    "needed_bands": ["hh", "hv"],
    "index_function": {
        "function": "datacube_ows.band_utils.radar_vegetation_index",
        "mapped_bands": True,
        "kwargs": {
            "band_hv": "hv",
            "band_hh": "hh",
        },
    },
    "range": [0.2, 1.0],
    "mpl_ramp": "viridis",
    "legend": {
        "begin": "0.2",
        "end": "1.0",
        "ticks_every": "0.1",
        "tick_labels": {
            "0.2": {"prefix": "<"},
            "1.0": {"prefix": ">"},
        },
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
    "bands": bands_alos,
    "resource_limits": reslim_alos_palsar,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "product": "alos_palsar_mosaic",
            "band": "mask",
            "ignore_info_flags": [],
        },
    ],
    "wcs": {
        "native_crs": "EPSG:4326",
        "native_resolution": [0.000222222222222, -0.000222222222222],
        "default_bands": ["hh", "hv", "mask"],
    },
    "styling": {
        "default_style": "hh",
        "styles": [
            style_alos_hh,
            style_alos_hv,
            style_alos_hv_over_hh,
            style_alos_radar_veg_idx,
        ],
    },
}
