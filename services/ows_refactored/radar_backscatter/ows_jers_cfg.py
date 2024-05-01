from ows_refactored.common.ows_reslim_cfg import reslim_alos_palsar

bands_jers = {"hh": [], "mask": [], "date": [], "linci": []}

style_jers_hh = {
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
        {"value": 908, "color": "#e2f4dd"},  # 750 * 1.21
        {"value": 1210, "color": "#c0e6b9"},
        {"value": 1815, "color": "#94d390"},
        {"value": 3025, "color": "#60ba6c"},
        {"value": 4840, "color": "#329b51"},
        {"value": 7260, "color": "#0c7835"},
        {"value": 9680, "color": "#00441b"},  # 8000 * 1.21
    ],
    "legend": {
        "begin": 0,
        "end": 9680,
        "ticks": ["0", "2420", "4840", "7260", "9680"],
        "tick_labels": {
            "0": {"label": "0"},
            "2420": {"label": "2420"},
            "4840": {"label": "4840"},
            "7260": {"label": "7260"},
            "9680": {"prefix": ">"},
        },
    },
}

layer = {
    "title": "Annual mosaic (JERS)",
    "name": "jers_sar_mosaic",
    "abstract": """
Synthetic Aperture Radar (SAR) data have been shown to provide different and complementary information to the more common optical remote sensing data. Radar backscatter response is a function of topography, land cover structure, orientation, and moisture characteristics—including vegetation biomass—and the radar signal can penetrate clouds, providing information about the earth’s surface where optical sensors cannot. Digital Earth Africa provides access to Normalized Radar Backscatter data, for which Radiometric Terrain Correction (RTC) has been applied so data acquired with different imaging geometries over the same region can be compared.
The JERS annual mosaic is generated from images acquired by the SAR sensor on the Japanese Earth Resources Satellite-1 (JERS-1) satellite.

This product contains radar measurement in L-band and HH polarization. It has a spatial resolution of 25 m and is available for 1996. Data is provided as digital number (DN), which can be converted to backscatter in decibel unit using 10*log10(𝐷𝑁^2)-84.66.

It is part of a global dataset provided by the Japan Aerospace Exploration Agency (JAXA) Earth Observation Research Center.

For more information on the product, see https://docs.digitalearthafrica.org/en/latest/data_specs/ALOS_PALSAR_annual_mosaic_specs.html

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
    "product_name": "jers_sar_mosaic",
    "time_resolution": "year",
    "bands": bands_jers,
    "resource_limits": reslim_alos_palsar,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "flags": [
        {
            "product": "jers_sar_mosaic",
            "band": "mask",
            "ignore_info_flags": [],
        },
    ],
    "native_crs": "EPSG:4326",
    "native_resolution": [
        0.000222222222222,
        -0.000222222222222,
    ],
    "styling": {
        "default_style": "hh",
        "styles": [style_jers_hh],
    },
}
