from prod_af.ows_reslim_cfg import reslim_landsat
from prod_af.surface_reflectance.band_sr_cfg import bands_ls
from prod_af.surface_reflectance.style_sr_cfg import styles_sr_list

layers = {
    "title": "Landsat",
    "abstract": """Landsat represents a collection of space-based land remote sensing data. Surface reflectance
                        measures incoming solar radiation reflected from the Earth to the Landsat sensor, which improves comparison
                        between multiple images over the same region. This helps us detect Earth surface changes. This dataset
                        includes Landsat 8 US Geological Survey Collection 1 Higher Level SR scene processed using LaSRC. 30m UTM
                        based projection.""",
    "layers": [
        {
            "title": "Surface Reflectance Landsat 8 (USGS Collection 1)",
            "name": "ls8_usgs_sr_scene",
            "abstract": """
Surface reflectance is the fraction of incoming solar radiation that is reflected from Earth's surface. Variations in satellite measured radiance due to atmospheric properties have been corrected for, so images acquired over the same area at different times are comparable and can be used readily to detect changes on Earth’s surface.

DE Africa contains Landsat Collection 1, Level 2 surface reflectance products over five countries (Tanzania, Senegal, Sierra Leone, Ghana, and Kenya). Landsat Collection 1 consists of products generated from the Landsat 8 Operational Land Imager (OLI) / Thermal Infrared Sensor (TIRS), Landsat 7 Enhanced Thematic Mapper Plus (ETM+), Landsat 4-5 Thematic Mapper (TM), and Landsat 1-5 Multispectral Scanner (MSS) instruments. The implementation of collections ensures consistent and known radiometric and geometric quality through time and across instruments and improves control in the calibration and processing parameters.

This product has a spatial resolution of 30 m and a temporal coverage of 2013 to 2019. The surface reflectance values are scaled to be between 0 and 10,000.

It is provided by United States Geological Survey (USGS).

For more information on the Landsat surface reflectance product, see https://www.usgs.gov/land-resources/nli/landsat/landsat-surface-reflectance

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "ls8_usgs_sr_scene",
            "bands": bands_ls,
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
                "styles": styles_sr_list,
            },
        },
        {
            "title": "Surface Reflectance Landsat 7 (USGS Collection 1)",
            "name": "ls7_usgs_sr_scene",
            "abstract": """
Surface reflectance is the fraction of incoming solar radiation that is reflected from Earth's surface. Variations in satellite measured radiance due to atmospheric properties have been corrected for so images acquired over the same area at different times are comparable and can be used readily to detect changes on Earth’s surface.

DE Africa contains Landsat Collection 1, Level 2 surface reflectance products over five countries (Tanzania, Senegal, Sierra Leone, Ghana, and Kenya). Landsat Collection 1 consists of products generated from the Landsat 8 Operational Land Imager (OLI) / Thermal Infrared Sensor (TIRS), Landsat 7 Enhanced Thematic Mapper Plus (ETM+), Landsat 4-5 Thematic Mapper (TM), and Landsat 1-5 Multispectral Scanner (MSS) instruments. The implementation of collections ensures consistent and known radiometric and geometric quality through time and across instruments and improves control in the calibration and processing parameters.

This product has a spatial resolution of 30 m and a temporal coverage of 1999 to 2019. The surface reflectance values are scaled to be between 0 and 10,000.

It is provided by United States Geological Survey (USGS).

For more information on the Landsat surface reflectance product, see https://www.usgs.gov/land-resources/nli/landsat/landsat-surface-reflectance

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "ls7_usgs_sr_scene",
            "bands": bands_ls,
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
                "styles": styles_sr_list,
            },
        },
        {
            "title": "Surface Reflectance Landsat 5 (USGS Collection 1)",
            "name": "ls5_usgs_sr_scene",
            "abstract": """
Surface reflectance is the fraction of incoming solar radiation that is reflected from Earth's surface. Variations in satellite measured radiance due to atmospheric properties have been corrected for so images acquired over the same area at different times are comparable and can be used readily to detect changes on Earth’s surface.

DE Africa contains Landsat Collection 1, Level 2 surface reflectance products over five countries (Tanzania, Senegal, Sierra Leone, Ghana, and Kenya). Landsat Collection 1 consists of products generated from the Landsat 8 Operational Land Imager (OLI) / Thermal Infrared Sensor (TIRS), Landsat 7 Enhanced Thematic Mapper Plus (ETM+), Landsat 4-5 Thematic Mapper (TM), and Landsat 1-5 Multispectral Scanner (MSS) instruments. The implementation of collections ensures consistent and known radiometric and geometric quality through time and across instruments and improves control in the calibration and processing parameters.

This product has a spatial resolution of 30 m and a temporal coverage of 1984 to 2011. The surface reflectance values are scaled to be between 0 and 10,000.

It is provided by United States Geological Survey (USGS).

For more information on the Landsat surface reflectance product, see https://www.usgs.gov/land-resources/nli/landsat/landsat-surface-reflectance

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
            "product_name": "ls5_usgs_sr_scene",
            "bands": bands_ls,
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
                "styles": styles_sr_list,
            },
        },
    ],
}
