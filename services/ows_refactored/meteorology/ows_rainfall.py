from ows_refactored.common.ows_reslim_cfg import reslim_smart5


style_rainfall = {
    "name": "rainfall",
    "title": "Chirps Monthly Rainfall",
    "abstract": "I see the rain, down in Africa",
    "needed_bands": ["rainfall"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "rainfall",
        },
    },
    "color_ramp": [
        {"value": -1, "color": "#000000", "alpha": 0.0},
        {"value": 0.0, "color": "#ffffcc", "alpha": 1.0},
        {
            "value": 40.0,
            "color": "#c0e6bc",
        },
        {
            "value": 80.0,
            "color": "#81ceb9",
        },
        {
            "value": 120.0,
            "color": "#41b6c4",
        },
        {
            "value": 160.0,
            "color": "#3391bc",
        },
        {
            "value": 250.0,
            "color": "#2a66ac",
        },
        {
            "value": 500.0,
            "color": "#253494",
        },
    ],
    "legend": {"width": 3.0, "height": 3.0},
}

layer = {
    "title": "Rainfall (Monthly)",
    "name": "rainfall_chirps_monthly",
    "abstract": """
Climate Hazards Group InfraRed Precipitation with Station data (CHIRPS) is a 35+ year quasi-global rainfall data set.

Spanning 50°S-50°N (and all longitudes) and ranging from 1981 to near-present, CHIRPS incorporates our in-house climatology, CHPclim, 0.05° resolution satellite imagery, and in-situ station data to create gridded rainfall time series for trend analysis and seasonal drought monitoring.
""",
    "product_name": "rainfall_chirps_monthly",
    "time_resolution": "month",
    "bands": {
        "rainfall": [],
    },
    "resource_limits": reslim_smart5,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [
        0.05000000074505806,
        -0.050000000745058060,
    ],
    "wcs": {
        "default_bands": ["rainfall"],
    },
    "styling": {
        "default_style": "rainfall",
        "styles": [style_rainfall],
    },
}
