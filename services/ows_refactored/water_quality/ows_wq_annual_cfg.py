from ows_refactored.water_quality.style_wq_annual_cfg import style_wq_annual_tsm

bands_wq = {"tsm_lym_msi_agm": []}

layer = {
    "title": "Water quality variables",
    "name": "wq_annual",
    "abstract": """Water quality variables at 10m resolution \
This service provides water quality data derived from satellite imagery, \
specifically from the MSI sensor on Sentinel-2 satellites, at a spatial \
resolution of 10 meters. The data is available from June 2015 to the \
present.
This service is accessible through OGC Web Service \
(https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox \
JupyterLab and for direct download click on a tile in the explorer page \
(https://explorer.dev.digitalearth.africa/products/wq_annual)
""",
    "product_name": "wq_annual",
    "time_resolution": "annual",
    "bands": bands_wq,
    "resource_limits": {},
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:6933",
    "native_resolution": [10, -10],
    "styling": {
        # The default_style must match the style's "name" field.
        "default_style": "style_wq_annual_tsm",
        "styles": [
            style_wq_annual_tsm,
        ],
    },
}
