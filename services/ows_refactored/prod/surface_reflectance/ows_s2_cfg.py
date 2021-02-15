from prod.surface_reflectance.style_sr_cfg import styles_s2_list
from prod.ows_reslim_cfg import reslim_srtm
from prod.surface_reflectance.band_sr_cfg import bands_sentinel

layers = {
    "title": "Sentinel",
    "abstract": """Sentinel""",
    "layers": [
        {
            "title": "Surface Reflectance Sentinel-2",
            "name": "s2_l2a",
            "abstract": """
Surface reflectance is the fraction of incoming solar radiation that is reflected from Earth's surface. Variations in satellite measured radiance due to atmospheric properties have been corrected for, so images acquired over the same area at different times are comparable and can be used readily to detect changes on Earth’s surface.

DE Africa provides Sentinel 2 Level-2A surface reflectance data from European Commission's Copernicus Programme. Sentinel-2 is an Earth observation mission that systematically acquires optical imagery at up to 10 m spatial resolution. The mission is based on a constellation of two identical satellites in the same orbit, 180° apart for optimal coverage and data delivery. Together, they cover all Earth's land surfaces, large islands, inland and coastal waters every 3-5 days. Each of the Sentinel-2 satellites carries a wide swath high-resolution multispectral imager with 13 spectral bands.

This product has a temporal coverage of 2017 to current and is updated as new images are acquired. Images in different spectral bands are provided at spatial resolutions of 10, 20 or 60 m. The surface reflectance values are scaled to be between 0 and 10,000.

Sentinel-2 Level-2A data are provided by the European Space Agency (ESA).  Data prior to 2017 are processed from Level-1C to Level-2A with ESA's Sen2Cor software by Sinergise. All images are converted to Cloud Optimised GeoTIFF format by Element 84, Inc.

For more information on the Sentinel-2 Level-2A surface reflectance product, see https://earth.esa.int/web/sentinel/technical-guides/sentinel-2-msi/level-2a/algorithm

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "s2_l2a",
            "bands": bands_sentinel,
            "dynamic": True,
            "resource_limits": reslim_srtm,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,  # True
                "apply_solar_corrections": False,
            },
            "wcs": {
                "native_crs": "EPSG:4326",
                "native_resolution": [30.0, -30.0],
                "default_bands": ["red", "green", "blue"],
            },
            "styling": {
                "default_style": "simple_rgb",
                "styles": styles_s2_list,
            },
        },
    ],
}
