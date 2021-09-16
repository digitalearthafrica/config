from ows_refactored.common.ows_reslim_cfg import reslim_smart9s2, reslim_zoom9
from ows_refactored.surface_reflectance.band_sr_cfg import bands_s2_gm
from ows_refactored.surface_reflectance.style_sr_cfg import styles_gm_list


layer = {
    "title": "Surface Reflectance Annual GeoMAD Sentinel-2",
    "name": "gm_s2_annual",
    "abstract": """
Individual remote sensing images can be affected by noisy data, such as clouds, cloud shadows, and haze. To produce cleaner images that can be compared more easily across time, we can create 'summary' images or 'composites' that combine multiple images into one image to reveal the median or 'typical' appearance of the landscape for a certain time period.

One approach is to create a geomedian. A geomedian is based on a high-dimensional statistic called the 'geometric median' (Small 1990), which effectively trades a temporal stack of poor-quality observations for a single high-quality pixel composite with reduced spatial noise (Roberts et al. 2017). In contrast to a standard median, a geomedian maintains the relationship between spectral bands. This allows further analysis on the composite images, just as we would on the original satellite images (e.g. by allowing the calculation of common band indices like NDVI). An annual geomedian image is calculated from the surface reflectance values drawn from a calendar year.

In addition, surface reflectance varabilities within the same time period can be measured to support characterization of the land surfaces. The median absolute deviation (MAD) is a robust measure (resilient to outliers) of the variability within a dataset. For multi-spectral Earth observation, deviation can be measured against the geomedian using a number of distance metrics.  Three of these metrics are adopted to highlight different types of changes in the landscape:
- Euclidean distance (EMAD), which is more sensitive to changes in target brightness.
- Cosine (spectral) distance (SMAD), which is more sensitive to changes in target spectral response.
- Bray Curtis dissimilarity (BCMAD), which is more sensitive to the distribution of the observation values through time.

More techincal information about the GeoMAD product can be found in the User Guide (https://docs.digitalearthafrica.org/en/latest/data_specs/GeoMAD_specs.html)

This product has a spatial resolution of 10 m and is available annually for 2017 to 2020.

It is derived from Surface Reflectance Sentinel-2 data. This product contains modified Copernicus Sentinel data 2017-2020.

Annual geomedian images enable easy visual and algorithmic interpretation, e.g. understanding urban expansion, at annual intervals. They are also useful for characterising permanent landscape features such as woody vegetation. The MADs can be used on their own or together with geomedian to gain insights about the land surface, e.g. for land cover classificiation and for change detection from year to year.

For more information on the algorithm, see https://doi.org/10.1109/TGRS.2017.2723896 and https://doi.org/10.1109/IGARSS.2018.8518312

""",
    "product_name": "gm_s2_annual",
    # Low product name
    #
    # Leave commented until we have an appropriate summary product.
    # (Packaged like the main product, but with much much lower
    # resolution and much much higher area covered in each dataset.
    #
    "low_res_product_name": "gm_s2_annual_lowres",
    "bands": bands_s2_gm,
    "dynamic": False,
    "resource_limits": reslim_smart9s2,
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
    }
}
