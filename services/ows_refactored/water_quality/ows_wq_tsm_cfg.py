from ows_refactored.water_quality.style_wq_cfg import style_tsm

bands_wq = {"tsm": [], "tsi": []}

layer = {
    "title": "Total Suspended Matter",
    "name": "water_quality_tsm",
    "abstract": """Total Suspended Matter (TSM) is a measure of the \
concentration of particulate material in the surface water such as mud,
silt, and other fine-scale debris. High concentrations of TSM can reduce \
water quality, affect aquatic life, and impact human health.
This service provides TSM data derived from satellite imagery, \
specifically from the MSI sensor on Sentinel-2 satellites, at a spatial \
resolution of 20 meters. The data is available from June 2015 to the \
present.
This service is accessible through OGC Web Service \
(https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox \
JupyterLab and for direct download click on a tile in the explorer page \
(https://explorer.digitalearth.africa/products/ndvi_anomaly)
""",
    "product_name": "water_quality_tsm",
    "time_resolution": "annual",
    "bands": bands_wq,
    "resource_limits": {},
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:6933",
    "native_resolution": [20, -20],
    "styling": {
        "default_style": "style_tsm",
        "styles": [
            style_tsm,
        ],
    },
}
