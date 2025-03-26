from ows_refactored.common.ows_reslim_cfg import reslim_landsat
from ows_refactored.radar_backscatter.style_s1_cfg import styles_s1_list

bands_s1_mosaic = {"vv": [], "vh": []}


layer = {
    "title": "Monthly mosaic (Sentinel-1)",
    "name": "s1_monthly_mosaic",
    "abstract": """

Synthetic Aperture Radar (SAR) data have been shown to provide different and complementary information to the more common optical remote sensing data. Radar backscatter response is a function of topography, land cover structure, orientation, and moisture characteristics—including vegetation biomass—and the radar signal can penetrate clouds, providing information about the earth’s surface where optical sensors cannot. Digital Earth Africa provides access to Normalized Radar Backscatter data, for which Radiometric Terrain Correction (RTC) has been applied so data acquired with different imaging geometries over the same region can be compared.

The Sentinel-1 monthly mosaics are generated by combining RTC images acquired within each calendar month using a multitemporal compositing algorithm. This algorithm calculates a weighted average of valid pixels, assigning higher weights to pixels with higher local resolution (e.g., slopes facing away from the sensor). This local resolution weighting approach minimizes noise and improves spatial homogeneity in the composites. 

This product contains radar measurement in C-band and in VV and VH polarizations. It has a spatial resolution of 20 m, a temporal coverage of January 2020 to current and is updated as new mosaics are generated. Data is provided as Gamma0 in linear power, which can be converted to backscatter in decibel unit using 10*log10(DN).

This dataset is processed by Sinergise Sentinel Hub using the Sentinel-1 RTC product as input.

More techincal information about the Sentinel-1 Normalized Backscatter can be found in the User Guide (https://docs.digitalearthafrica.org/en/latest/data_specs/Sentinel-1_Monthly_Mosaic_specs.html)

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
    "product_name": "s1_monthly_mosaic",
    "bands": bands_s1_mosaic,
    "dynamic": True,
    "resource_limits": reslim_landsat,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [0.0002, -0.0002],
    "styling": {
        "default_style": "vv_vh_vh_over_vv",
        "styles": styles_s1_list,
    },
}
