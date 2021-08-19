from ows_refactored.common.ows_reslim_cfg import reslim_sentinel2, reslim_srtm
from ows_refactored.surface_reflectance.band_sr_cfg import (bands_ls8c,
                                                            bands_s2_gm)
from ows_refactored.surface_reflectance.style_sr_cfg import (styles_gm_list,
                                                             styles_ls8c_list)

layers = {
    "title": "Annual Geometric Median",
    "abstract": "Landsat Geomedian based on USGS Provisional Collection 2 Level 2 Scenes",
    "layers": [
        {
            "title": "Surface Reflectance Annual Geomedian Landsat 8 (Beta)",
            "name": "ga_ls8c_gm_2_annual",
            "abstract": """
Individual remote sensing images can be affected by noisy data, including clouds, cloud shadows, and haze. To produce cleaner images that can be compared more easily across time, we can create 'summary' images or 'composites' that combine multiple images into one image to reveal the median or 'typical' appearance of the landscape for a certain time period. One approach is to create a geomedian. A geomedian is based on a high-dimensional statistic called the 'geometric median' (Small 1990), which effectively trades a temporal stack of poor-quality observations for a single high-quality pixel composite with reduced spatial noise (Roberts et al. 2017).

In contrast to a standard median, a geomedian maintains the relationship between spectral bands. This allows for conducting further analysis on the composite images just as we would on the original satellite images (e.g. by allowing the calculation of common band indices like NDVI). An annual median image is calculated from the surface reflectance values drawn from a calendar year.

This product has a spatial resolution of 30 m and a temporal coverage of 2018. The surface reflectance values are scaled to be between 0 and 65,455.

It is derived from Landsat 8 satellite observations as part of a provisional Landsat Collection 2 surface reflectance product.

Annual geomedian images enable easy visual and algorithmic interpretation, e.g. understanding urban expansion, at annual intervals. They are also useful for characterising permanent landscape features such as woody vegetation.

For more information on the algorithm, see https://doi.org/10.1109/TGRS.2017.2723896

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "ga_ls8c_gm_2_annual",
            "time_resolution": "year",
            "bands": bands_ls8c,
            "resource_limits": reslim_srtm,
            "image_processing": {
                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": [],
                "manual_merge": False,
            },
            "native_crs": "EPSG:6933",
            "native_resolution": [30.0, -30.0],
            "wcs": {
                "default_bands": ["red", "green", "blue"],
            },
            "styling": {
                "default_style": "simple_rgb",
                "styles": styles_ls8c_list,
            },
        },
        {
            "title": "Surface Reflectance Annual Geomedian Sentinel-2 (Beta)",
            "name": "ga_s2_gm",
            "abstract": """
Individual remote sensing images can be affected by noisy data, including clouds, cloud shadows, and haze. To produce cleaner images that can be compared more easily across time, we can create 'summary' images or 'composites' that combine multiple images into one image to reveal the median or 'typical' appearance of the landscape for a certain time period. One approach is to create a geomedian. A geomedian is based on a high-dimensional statistic called the 'geometric median' (Small 1990), which effectively trades a temporal stack of poor-quality observations for a single high-quality pixel composite with reduced spatial noise (Roberts et al. 2017).

In contrast to a standard median, a geomedian maintains the relationship between spectral bands. This allows for conducting further analysis on the composite images just as we would on the original satellite images (e.g. by allowing the calculation of common band indices like NDVI). An annual median image is calculated from the surface reflectance values drawn from a calendar year.

This product has a spatial resolution of 10 m and a temporal coverage of 2019.

It is derived from Surface Reflectance Sentinel-2 data. This product contains modified Copernicus Sentinel data 2019.

Annual geomedian images enable easy visual and algorithmic interpretation, e.g. understanding urban expansion, at annual intervals. They are also useful for characterising permanent landscape features such as woody vegetation.

For more information on the algorithm, see https://doi.org/10.1109/TGRS.2017.2723896

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
 """,
            "product_name": "ga_s2_gm",
            # Low product name
            #
            # Leave commented until we have an appropriate summary product.
            # (Packaged like the main product, but with much much lower
            # resolution and much much higher area covered in each dataset.
            #
            "low_res_product_name": "ga_s2_gm_lowres",
            "bands": bands_s2_gm,
            "dynamic": False,
            "resource_limits": reslim_sentinel2,
            "time_resolution": "year",
            "image_processing": {
                "extent_mask_func": "ows_refactored.common.ows_util_tools.mask_by_emad_nan",
                # "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                "always_fetch_bands": ["EMAD"],
                "manual_merge": False,  # True
                "apply_solar_corrections": False,
            },
            "native_crs": "EPSG:6933",
            "native_resolution": [10.0, -10.0],
            "wcs": {
                "default_bands": ["red", "green", "blue"],
            },
            "styling": {
                "default_style": "simple_rgb",
                "styles": styles_gm_list,
            },
        }
    ],
}
