from ows_refactored.common.ows_reslim_cfg import reslim_landsat
from ows_refactored.surface_reflectance.band_sr_cfg import bands_lsc2_sr
from ows_refactored.surface_reflectance.style_sr_cfg import styles_lsc2_sr_list

layers = {
    "title": "Landsat",
    "abstract": """Landsat represents a collection of space-based land remote sensing data. Surface reflectance
                        measures incoming solar radiation reflected from the Earth to the Landsat sensor, which improves comparison
                        between multiple images over the same region. This helps us detect Earth surface changes. This dataset
                        includes Landsat 8 US Geological Survey Collection 1 Higher Level SR scene processed using LaSRC. 30m UTM
                        based projection.""",
    "layers": [
        {
            "title": "Surface Reflectance Landsat 8 (USGS Collection 2)",
            "name": "ls8_sr",
            "abstract": """
Surface reflectance is the fraction of incoming solar radiation that is reflected from Earth's surface. Variations in satellite measured radiance due to atmospheric properties have been corrected for, so images acquired over the same area at different times are comparable and can be used readily to detect changes on Earth’s surface. 

DE Africa provides access to Landsat Collection 2 Level-2 Surface Reflectance products over Africa. USGS Landsat Collection 2 offers improved processing, geometric accuracy, and radiometric calibration compared to previous Collection 1 products. The Level-2 products are endorsed by the Committee on Earth Observation Satellites (CEOS) to be Analysis Ready Data for Land (CARD4L)-compliant. 

More techincal information about the Landsat Surface Reflectance product can be found in the User Guide (https://docs.digitalearthafrica.org/en/latest/data_specs/Landsat_C2_SR_specs.html).

Landsat 8 product has a spatial resolution of 30 m and a temporal coverage of 2013 to present. 

Landsat Level- 2 Surface Reflectance Science Product courtesy of the U.S. Geological Survey.

For more information on Landsat products, see https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-level-2-science-products.

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "ls8_sr",
            "bands": bands_lsc2_sr,
            "resource_limits": reslim_landsat,
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
                "styles": styles_lsc2_sr_list,
            },
        },
        {
            "title": "Surface Reflectance Landsat 7 (USGS Collection 2)",
            "name": "ls7_sr",
            "abstract": """
Surface reflectance is the fraction of incoming solar radiation that is reflected from Earth's surface. Variations in satellite measured radiance due to atmospheric properties have been corrected for, so images acquired over the same area at different times are comparable and can be used readily to detect changes on Earth’s surface. 

DE Africa provides access to Landsat Collection 2 Level-2 Surface Reflectance products over Africa. USGS Landsat Collection 2 offers improved processing, geometric accuracy, and radiometric calibration compared to previous Collection 1 products. The Level-2 products are endorsed by the Committee on Earth Observation Satellites (CEOS) to be Analysis Ready Data for Land (CARD4L)-compliant. 

More techincal information about the Landsat Surface Reflectance product can be found in the User Guide (https://docs.digitalearthafrica.org/en/latest/data_specs/Landsat_C2_SR_specs.html).

Landsat 7 product has a spatial resolution of 30 m and a temporal coverage of 1999 to present.

Landsat Level- 2 Surface Reflectance Science Product courtesy of the U.S. Geological Survey.

For more information on Landsat products, see https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-level-2-science-products.

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "ls7_sr",
            "bands": bands_lsc2_sr,
            "resource_limits": reslim_landsat,
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
                "styles": styles_lsc2_sr_list,
            },
        },
        {
            "title": "Surface Reflectance Landsat 5 (USGS Collection 2)",
            "name": "ls5_sr",
            "abstract": """
Surface reflectance is the fraction of incoming solar radiation that is reflected from Earth's surface. Variations in satellite measured radiance due to atmospheric properties have been corrected for, so images acquired over the same area at different times are comparable and can be used readily to detect changes on Earth’s surface. 

DE Africa provides access to Landsat Collection 2 Level-2 Surface Reflectance products over Africa. USGS Landsat Collection 2 offers improved processing, geometric accuracy, and radiometric calibration compared to previous Collection 1 products. The Level-2 products are endorsed by the Committee on Earth Observation Satellites (CEOS) to be Analysis Ready Data for Land (CARD4L)-compliant. 

More techincal information about the Landsat Surface Reflectance product can be found in the User Guide (https://docs.digitalearthafrica.org/en/latest/data_specs/Landsat_C2_SR_specs.html).

Landsat 5 product has a spatial resolution of 30 m and a temporal coverage of 1984 to 2012.

Landsat Level- 2 Surface Reflectance Science Product courtesy of the U.S. Geological Survey.

For more information on Landsat products, see https://www.usgs.gov/core-science-systems/nli/landsat/landsat-collection-2-level-2-science-products.

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "ls5_sr",
            "bands": bands_lsc2_sr,
            "resource_limits": reslim_landsat,
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
                "styles": styles_lsc2_sr_list,
            },
        },
    ],
}
