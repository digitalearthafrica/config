# import re

# Static config for the wms metadata.
# pylint: skip-file

response_cfg = {
    "Access-Control-Allow-Origin": "*",  # CORS header
}

service_cfg = {
    # Which web service(s) should be supported by this instance
    # Defaults: wms: True, wcs: False, wmts: False
    # Notes:
    #   WMTS support is implemented as a thin proxy to WMS. Some corners of the spec are interpreted
    #   somewhat loosely. In particular exception documents are directly translated from the underlying
    #   WMS error and are unlikely to be fully compliant with the WMTS standard.
    "wcs": True,
    "wms": True,
    "wmts": True,

    # Required config for WMS and/or WCS
    # Service title - appears e.g. in Terria catalog
    "title": "Digital Earth Africa - OGC Web Services",
    # Service URL.  Should a fully qualified URL or a list of fully qualified URLs that the service can return
    # in the GetCapabilities document based on the requesting url
    "url": ["https://ows.digitalearth.africa"],
    # URL that humans can visit to learn more about the WMS or organization
    # should be fully qualified
    "human_url": "https://digitalearth.africa",
    # Provide S3 data URL for data_links in GetFeatureinfo
    "s3_url": "https://data.digitalearth.africa",
    # Provide S3 bucket name for data_links in GetFeatureinfo    
    "s3_bucket": "deafrica-data",
    # Supported co-ordinate reference systems
    "published_CRSs": {
        "EPSG:3857": {  # Web Mercator
            "geographic": False,
            "horizontal_coord": "x",
            "vertical_coord": "y",
        },
        "EPSG:4326": {  # WGS-84
            "geographic": True,
            "vertical_coord_first": True
        },
        "EPSG:3577": {  # GDA-94, internal representation
            "geographic": False,
            "horizontal_coord": "x",
            "vertical_coord": "y",
        },
        "EPSG:102022": {
            "geographic": False,
            "horizontal_coord": "x",
            "vertical_coord": "y",
        },
        "EPSG:6933": { # Cylindrical equal area
            "geographic": False,
            "horizontal_coord": "x",
            "vertical_coord": "y",
        },
    },

    # Required config for WCS
    # Must be a geographic CRS in the published_CRSs list. EPSG:4326 is recommended, but any geographic CRS should work.
    "default_geographic_CRS": "EPSG:4326",

    # Supported WCS formats
    "wcs_formats": {
        # Key is the format name, as used in DescribeCoverage XML
        "GeoTIFF": {
            # Renderer is the FQN of a Python function that takes:
            #   * A WCSRequest object
            #   * Some ODC data to be rendered.
            "renderer": "datacube_wms.wcs_utils.get_tiff",
            # The MIME type of the image, as used in the Http Response.
            "mime": "image/geotiff",
            # The file extension to add to the filename.
            "extension": "tif",
            # Whether or not the file format supports multiple time slices.
            "multi-time": False
        },
        "netCDF": {
            "renderer": "datacube_wms.wcs_utils.get_netcdf",
            "mime": "application/x-netcdf",
            "extension": "nc",
            "multi-time": True,
        }
    },
    # The native wcs format must be declared in wcs_formats above.
    "native_wcs_format": "GeoTIFF",

    # Optional config for instances supporting WMS
    # Max tile height/width.  If not specified, default to 256x256
    "max_width": 512,
    "max_height": 512,

    # Optional config for all services (WMS and/or WCS) - may be set to blank/empty, no defaults
    "abstract": """Digital Earth Africa OGC Web Services""",
    "keywords": [
        "landsat",
        "africa",
        "WOfS",
        "fractional-cover",
        "time-series",
    ],
    "contact_info": {
        "person": "Digital Earth Africa",
        "organisation": "Geoscience Australia",
        "position": "",
        "address": {
            "type": "postal",
            "address": "GPO Box 378",
            "city": "Canberra",
            "state": "ACT",
            "postcode": "2609",
            "country": "Australia",
        },
        "telephone": "+61 2 6249 9111",
        "fax": "",
        "email": "earth.observation@ga.gov.au",
    },
    "fees": "",
    "access_constraints": "© Commonwealth of Australia (Geoscience Australia) 2018. "
                          "This product is released under the Creative Commons Attribution 4.0 International Licence. "
                          "http://creativecommons.org/licenses/by/4.0/legalcode",
    "preauthenticate_s3": True,
    # If True this will not calculate spatial extents
    # in update_ranges.py but will instead use a default
    # extent covering much of Africa for all
    # temporal extents
    # False by default (calculate spatial extents)
    "use_default_extent": True,
    # If using GeoTIFFs as storage
    # this will set the rasterio env
    # GDAL Config for GTiff Georeferencing
    # See https://www.gdal.org/frmt_gtiff.html#georeferencing
    "geotiff_georeference_source": "INTERNAL"
}

layer_cfg = [
    # Layer Config is a list of platform configs
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "Surface Reflectance",
        "title": "Landsat",
        "abstract": """Landsat represents a collection of space-based land remote sensing data. Surface reflectance 
        measures incoming solar radiation reflected from the Earth to the Landsat sensor, which improves comparison 
        between multiple images over the same region. This helps us detect Earth surface changes. This dataset 
        includes Landsat 8 US Geological Survey Collection 1 Higher Level SR scene processed using LaSRC. 30m UTM 
        based projection.""",
        "products": [
            {
                # Included as a keyword  for the layer
                "label": "Landsat 8",
                # Included as a keyword  for the layer
                "type": "Surface Reflectance",
                # Included as a keyword  for the layer
                "variant": "",
                # The WMS name for the layer
                "abstract": """ Landsat 8 Surface Reflectance""",
                "name": "ls8_usgs_sr_scene",
                # The Datacube name for the associated data product
                "product_name": "ls8_usgs_sr_scene",
                # "bands": {
                #    "red": ["crimson"],
                #    "green": [],
                #    "blue": ["azure"],
                #    "nir": ["near_infrared"],
                #    "swir1": ["shortwave_infrared_1", "near_shortwave_infrared"],
                #    "swir2": ["shortwave_infrared_2", "far_shortwave_infrared"],
                #    "coastal_aerosol": ["far_blue"],
                # },
                # "pq_dataset": "ls8_usgs_sr_scene",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_qa",
                "min_zoom_factor": 35.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # Central Africa Timezone (UTC+2).
                "time_zone": 2,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: data[band] != data[band].attrs['nodata'],

                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "data_manual_merge": True,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                # Define layer wide legend graphic if no style is passed
                # to GetLegendGraphic
                "legend": {
                    # "url": ""
                    "styles": ["ndvi", "ndwi", "mndwi"]
                },
                "wcs_default_bands": ["red", "green", "blue"],
                # A function that extracts the "sub-product" id (e.g. path number) from a dataset.
                # Function should return a (small) integer
                # If None or not specified, the product has no sub-layers.
                # "sub_product_extractor": lambda ds: int(s3_path_pattern.search(ds.uris[0]).group("path")),
                # A prefix used to describe the sub-layer in the GetCapabilities response.
                # E.g. sub-layer 109 will be described as "Landsat Path 109"
                # "sub_product_label": "Landsat Path",

                # Bands to include in time-dimension "pixel drill".
                # Don't activate in production unless you really know what you're doing.
                # "band_drill": ["nir", "red", "green", "blue"],

                # Styles.
                #
                # See band_mapper.py
                #
                # The various available spectral bands, and ways to combine them
                # into a single rgb image.
                # The examples here are ad hoc
                #
                "styles": [
                    # Examples of styles which are linear combinations of the available spectral bands.
                    #
                    {
                        "name": "simple_rgb",
                        "title": "Simple RGB",
                        "abstract": "Simple true-colour image, using the red, green and blue bands",
                        "components": {
                            "red": {
                                "red": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        # The raw band value range to be compressed to an 8 bit range for the output image tiles.
                        # Band values outside this range are clipped to 0 or 255 as appropriate.
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "infrared_green",
                        "title": "False colour - Green, SWIR, NIR",
                        "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
                        "components": {
                            "red": {
                                "swir1": 1.0
                            },
                            "green": {
                                "nir": 1.0
                            },
                            "blue": {
                                "green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    #
                    # Examples of non-linear heat-mapped styles.
                    {
                        "name": "ndvi",
                        "title": "NDVI - Red, NIR",
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well "
                                    "with the existence of vegetation",
                        "index_function": lambda data: (data["nir"] - data["red"]) / (data["nir"] + data["red"]),
                        "needed_bands": ["red", "nir"],
                        "color_ramp": [
                            {
                                "value": -0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 1.0
                            },
                            {
                                "value": 0.1,
                                "color": "#A35F18"
                            },
                            {
                                "value": 0.2,
                                "color": "#B88512"
                            },
                            {
                                "value": 0.3,
                                "color": "#CEAC0E"
                            },
                            {
                                "value": 0.4,
                                "color": "#E5D609"
                            },
                            {
                                "value": 0.5,
                                "color": "#FFFF0C"
                            },
                            {
                                "value": 0.6,
                                "color": "#C3DE09"
                            },
                            {
                                "value": 0.7,
                                "color": "#88B808"
                            },
                            {
                                "value": 0.8,
                                "color": "#529400"
                            },
                            {
                                "value": 0.9,
                                "color": "#237100"
                            },
                            {
                                "value": 1.0,
                                "color": "#114D04"
                            }
                        ]
                    },
                    {
                        "name": "ndwi",
                        "title": "NDWI - Green, NIR",
                        "abstract": "Normalised Difference Water Index - a derived index that correlates well with "
                                    "the existence of water (McFeeters 1996)",
                        "index_function": lambda data: (data["green"] - data["nir"]) / (data["nir"] + data["green"]),
                        "needed_bands": ["green", "nir"],
                        "color_ramp": [
                            {
                                "value": -0.1,
                                "color": "#f7fbff",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.0,
                                "color": "#d8e7f5",
                                "legend": {
                                    "prefix": "<"
                                }
                            },
                            {
                                "value": 0.1,
                                "color": "#b0d2e8"
                            },
                            {
                                "value": 0.2,
                                "color": "#73b3d8",
                                "legend": {}
                            },
                            {
                                "value": 0.3,
                                "color": "#3e8ec4"
                            },
                            {
                                "value": 0.4,
                                "color": "#1563aa",
                                "legend": {}
                            },
                            {
                                "value": 0.5,
                                "color": "#08306b",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ],
                    },
                    {
                        "name": "mndwi",
                        "title": "MNDWI - Green, SWIR",
                        "abstract": "Modified Normalised Difference Water Index - a derived index that correlates "
                                    "well with the existence of water (Xu 2006)",
                        "index_function": lambda data: (data["green"] - data["swir1"]) / (
                                data["green"] + data["swir1"]),
                        "needed_bands": ["green", "swir1"],
                        "color_ramp": [
                            {
                                "value": -0.1,
                                "color": "#f7fbff",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.0,
                                "color": "#d8e7f5"
                            },
                            {
                                "value": 0.2,
                                "color": "#b0d2e8"
                            },
                            {
                                "value": 0.4,
                                "color": "#73b3d8"
                            },
                            {
                                "value": 0.6,
                                "color": "#3e8ec4"
                            },
                            {
                                "value": 0.8,
                                "color": "#1563aa"
                            },
                            {
                                "value": 1.0,
                                "color": "#08306b"
                            }
                        ]
                    },
                    {
                        "name": "blue",
                        "title": "Blue - 480",
                        "abstract": "Blue band, centered on 480nm",
                        "components": {
                            "red": {
                                "blue": 1.0
                            },
                            "green": {
                                "blue": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "green",
                        "title": "Green - 560",
                        "abstract": "Green band, centered on 560nm",
                        "components": {
                            "red": {
                                "green": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red",
                        "title": "Red - 660",
                        "abstract": "Red band, centered on 660nm",
                        "components": {
                            "red": {
                                "red": 1.0
                            },
                            "green": {
                                "red": 1.0
                            },
                            "blue": {
                                "red": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "nir",
                        "title": "Near Infrared (NIR) - 870",
                        "abstract": "Near infra-red band, centered on 870nm",
                        "components": {
                            "red": {
                                "nir": 1.0
                            },
                            "green": {
                                "nir": 1.0
                            },
                            "blue": {
                                "nir": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir1",
                        "title": "Shortwave Infrared (SWIR) - 1610",
                        "abstract": "Short wave infra-red band 1, centered on 1610nm",
                        "components": {
                            "red": {
                                "swir1": 1.0
                            },
                            "green": {
                                "swir1": 1.0
                            },
                            "blue": {
                                "swir1": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir2",
                        "title": "Shortwave Infrared (SWIR) - 2200",
                        "abstract": "Short wave infra-red band 2, centered on 2200nm",
                        "components": {
                            "red": {
                                "swir2": 1.0
                            },
                            "green": {
                                "swir2": 1.0
                            },
                            "blue": {
                                "swir2": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            },
            {
                # Included as a keyword  for the layer
                "label": "Landsat 7",
                # Included as a keyword  for the layer
                "type": "Surface Reflectance",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """ Landsat 7 Surface Reflectance""",
                # The WMS name for the layer
                "name": "ls7_usgs_sr_scene",
                # The Datacube name for the associated data product
                "product_name": "ls7_usgs_sr_scene",
                # "bands": {
                #    "red": ["crimson"],
                #    "green": [],
                #    "blue": ["azure"],
                #    "nir": ["near_infrared"],
                #    "swir1": ["shortwave_infrared_1", "near_shortwave_infrared"],
                #    "swir2": ["shortwave_infrared_2", "far_shortwave_infrared"]
                # },
                # "pq_dataset": "ls7_usgs_sr_scene",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_qa",
                "min_zoom_factor": 35.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # Central Africa Timezone (UTC+2).
                "time_zone": 2,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: data[band] != data[band].attrs['nodata'],

                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "data_manual_merge": True,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                # Define layer wide legend graphic if no style is passed
                # to GetLegendGraphic
                "legend": {
                    # "url": ""
                    "styles": ["ndvi", "ndwi", "mndwi"]
                },
                "wcs_default_bands": ["red", "green", "blue"],
                # A function that extracts the "sub-product" id (e.g. path number) from a dataset.
                # Function should return a (small) integer
                # If None or not specified, the product has no sub-layers.
                # "sub_product_extractor": lambda ds: int(s3_path_pattern.search(ds.uris[0]).group("path")),
                # A prefix used to describe the sub-layer in the GetCapabilities response.
                # E.g. sub-layer 109 will be described as "Landsat Path 109"
                # "sub_product_label": "Landsat Path",

                # Bands to include in time-dimension "pixel drill".
                # Don't activate in production unless you really know what you're doing.
                # "band_drill": ["nir", "red", "green", "blue"],

                # Styles.
                #
                # See band_mapper.py
                #
                # The various available spectral bands, and ways to combine them
                # into a single rgb image.
                # The examples here are ad hoc
                #
                "styles": [
                    # Examples of styles which are linear combinations of the available spectral bands.
                    #
                    {
                        "name": "simple_rgb",
                        "title": "Simple RGB",
                        "abstract": "Simple true-colour image, using the red, green and blue bands",
                        "components": {
                            "red": {
                                "red": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        # The raw band value range to be compressed to an 8 bit range for the output image tiles.
                        # Band values outside this range are clipped to 0 or 255 as appropriate.
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "infrared_green",
                        "title": "False colour - Green, SWIR, NIR",
                        "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
                        "components": {
                            "red": {
                                "swir1": 1.0
                            },
                            "green": {
                                "nir": 1.0
                            },
                            "blue": {
                                "green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    #
                    # Examples of non-linear heat-mapped styles.
                    {
                        "name": "ndvi",
                        "title": "NDVI - Red, NIR",
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well "
                                    "with the existence of vegetation",
                        "index_function": lambda data: (data["nir"] - data["red"]) / (data["nir"] + data["red"]),
                        "needed_bands": ["red", "nir"],
                        "color_ramp": [
                            {
                                "value": -0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 1.0
                            },
                            {
                                "value": 0.1,
                                "color": "#A35F18"
                            },
                            {
                                "value": 0.2,
                                "color": "#B88512"
                            },
                            {
                                "value": 0.3,
                                "color": "#CEAC0E"
                            },
                            {
                                "value": 0.4,
                                "color": "#E5D609"
                            },
                            {
                                "value": 0.5,
                                "color": "#FFFF0C"
                            },
                            {
                                "value": 0.6,
                                "color": "#C3DE09"
                            },
                            {
                                "value": 0.7,
                                "color": "#88B808"
                            },
                            {
                                "value": 0.8,
                                "color": "#529400"
                            },
                            {
                                "value": 0.9,
                                "color": "#237100"
                            },
                            {
                                "value": 1.0,
                                "color": "#114D04"
                            }
                        ]
                    },
                    {
                        "name": "ndwi",
                        "title": "NDWI - Green, NIR",
                        "abstract": "Normalised Difference Water Index - a derived index that correlates well with "
                                    "the existence of water (McFeeters 1996)",
                        "index_function": lambda data: (data["green"] - data["nir"]) / (data["nir"] + data["green"]),
                        "needed_bands": ["green", "nir"],
                        "color_ramp": [
                            {
                                "value": -0.1,
                                "color": "#f7fbff",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.0,
                                "color": "#d8e7f5",
                                "legend": {
                                    "prefix": "<"
                                }
                            },
                            {
                                "value": 0.1,
                                "color": "#b0d2e8"
                            },
                            {
                                "value": 0.2,
                                "color": "#73b3d8",
                                "legend": {}
                            },
                            {
                                "value": 0.3,
                                "color": "#3e8ec4"
                            },
                            {
                                "value": 0.4,
                                "color": "#1563aa",
                                "legend": {}
                            },
                            {
                                "value": 0.5,
                                "color": "#08306b",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ],
                    },
                    {
                        "name": "mndwi",
                        "title": "MNDWI - Green, SWIR",
                        "abstract": "Modified Normalised Difference Water Index - a derived index that correlates "
                                    "well with the existence of water (Xu 2006)",
                        "index_function": lambda data: (data["green"] - data["swir1"]) / (
                                data["green"] + data["swir1"]),
                        "needed_bands": ["green", "swir1"],
                        "color_ramp": [
                            {
                                "value": -0.1,
                                "color": "#f7fbff",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.0,
                                "color": "#d8e7f5"
                            },
                            {
                                "value": 0.2,
                                "color": "#b0d2e8"
                            },
                            {
                                "value": 0.4,
                                "color": "#73b3d8"
                            },
                            {
                                "value": 0.6,
                                "color": "#3e8ec4"
                            },
                            {
                                "value": 0.8,
                                "color": "#1563aa"
                            },
                            {
                                "value": 1.0,
                                "color": "#08306b"
                            }
                        ]
                    },
                    {
                        "name": "blue",
                        "title": "Blue - 490",
                        "abstract": "Blue band, centered on 490nm",
                        "components": {
                            "red": {
                                "blue": 1.0
                            },
                            "green": {
                                "blue": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "green",
                        "title": "Green - 560",
                        "abstract": "Green band, centered on 560nm",
                        "components": {
                            "red": {
                                "green": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red",
                        "title": "Red - 660",
                        "abstract": "Red band, centered on 660nm",
                        "components": {
                            "red": {
                                "red": 1.0
                            },
                            "green": {
                                "red": 1.0
                            },
                            "blue": {
                                "red": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "nir",
                        "title": "Near Infrared (NIR) - 840",
                        "abstract": "Near infra-red band, centered on 840nm",
                        "components": {
                            "red": {
                                "nir": 1.0
                            },
                            "green": {
                                "nir": 1.0
                            },
                            "blue": {
                                "nir": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir1",
                        "title": "Shortwave Infrared (SWIR) - 1650",
                        "abstract": "Short wave infra-red band 1, centered on 1650nm",
                        "components": {
                            "red": {
                                "swir1": 1.0
                            },
                            "green": {
                                "swir1": 1.0
                            },
                            "blue": {
                                "swir1": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir2",
                        "title": "Shortwave Infrared (SWIR) - 2220",
                        "abstract": "Short wave infra-red band 2, centered on 2220nm",
                        "components": {
                            "red": {
                                "swir2": 1.0
                            },
                            "green": {
                                "swir2": 1.0
                            },
                            "blue": {
                                "swir2": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            },
            {
                # Included as a keyword  for the layer
                "label": "Landsat 5",
                # Included as a keyword  for the layer
                "type": "Surface Reflectance",
                # Included as a keyword  for the layer
                "variant": "",
                # The WMS name for the layer
                "name": "ls5_usgs_sr_scene",
                # The Datacube name for the associated data product
                "product_name": "ls5_usgs_sr_scene",
                # "bands": {
                #   "red": ["crimson"],
                #    "green": [],
                #    "blue": ["azure"],
                #    "nir": ["near_infrared"],
                #    "swir1": ["shortwave_infrared_1", "near_shortwave_infrared"],
                #    "swir2": ["shortwave_infrared_2", "far_shortwave_infrared"]
                # },
                # "pq_dataset": "ls5_usgs_sr_scene",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "pixel_qa",
                "min_zoom_factor": 35.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # Central Africa Timezone (UTC+2).
                "time_zone": 2,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: data[band] != data[band].attrs['nodata'],

                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "data_manual_merge": True,
                "always_fetch_bands": [],
                "apply_solar_corrections": False,
                # Define layer wide legend graphic if no style is passed
                # to GetLegendGraphic
                "legend": {
                    # "url": ""
                    "styles": ["ndvi", "ndwi", "mndwi"]
                },
                "wcs_default_bands": ["red", "green", "blue"],
                # A function that extracts the "sub-product" id (e.g. path number) from a dataset.
                # Function should return a (small) integer
                # If None or not specified, the product has no sub-layers.
                # "sub_product_extractor": lambda ds: int(s3_path_pattern.search(ds.uris[0]).group("path")),
                # A prefix used to describe the sub-layer in the GetCapabilities response.
                # E.g. sub-layer 109 will be described as "Landsat Path 109"
                # "sub_product_label": "Landsat Path",

                # Bands to include in time-dimension "pixel drill".
                # Don't activate in production unless you really know what you're doing.
                # "band_drill": ["nir", "red", "green", "blue"],

                # Styles.
                #
                # See band_mapper.py
                #
                # The various available spectral bands, and ways to combine them
                # into a single rgb image.
                # The examples here are ad hoc
                #
                "styles": [
                    # Examples of styles which are linear combinations of the available spectral bands.
                    #
                    {
                        "name": "simple_rgb",
                        "title": "Simple RGB",
                        "abstract": "Simple true-colour image, using the red, green and blue bands",
                        "components": {
                            "red": {
                                "red": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        # The raw band value range to be compressed to an 8 bit range for the output image tiles.
                        # Band values outside this range are clipped to 0 or 255 as appropriate.
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "infrared_green",
                        "title": "False colour - Green, SWIR, NIR",
                        "abstract": "False Colour image with SWIR1->Red, NIR->Green, and Green->Blue",
                        "components": {
                            "red": {
                                "swir1": 1.0
                            },
                            "green": {
                                "nir": 1.0
                            },
                            "blue": {
                                "green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    #
                    # Examples of non-linear heat-mapped styles.
                    {
                        "name": "ndvi",
                        "title": "NDVI - Red, NIR",
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well "
                                    "with the existence of vegetation",
                        "index_function": lambda data: (data["nir"] - data["red"]) / (data["nir"] + data["red"]),
                        "needed_bands": ["red", "nir"],
                        "color_ramp": [
                            {
                                "value": -0.0,
                                "color": "#8F3F20",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.0,
                                "color": "#8F3F20",
                                "alpha": 1.0
                            },
                            {
                                "value": 0.1,
                                "color": "#A35F18"
                            },
                            {
                                "value": 0.2,
                                "color": "#B88512"
                            },
                            {
                                "value": 0.3,
                                "color": "#CEAC0E"
                            },
                            {
                                "value": 0.4,
                                "color": "#E5D609"
                            },
                            {
                                "value": 0.5,
                                "color": "#FFFF0C"
                            },
                            {
                                "value": 0.6,
                                "color": "#C3DE09"
                            },
                            {
                                "value": 0.7,
                                "color": "#88B808"
                            },
                            {
                                "value": 0.8,
                                "color": "#529400"
                            },
                            {
                                "value": 0.9,
                                "color": "#237100"
                            },
                            {
                                "value": 1.0,
                                "color": "#114D04"
                            }
                        ]
                    },
                    {
                        "name": "ndwi",
                        "title": "NDWI - Green, NIR",
                        "abstract": "Normalised Difference Water Index - a derived index that correlates well with "
                                    "the existence of water (McFeeters 1996)",
                        "index_function": lambda data: (data["green"] - data["nir"]) / (data["nir"] + data["green"]),
                        "needed_bands": ["green", "nir"],
                        "color_ramp": [
                            {
                                "value": -0.1,
                                "color": "#f7fbff",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.0,
                                "color": "#d8e7f5",
                                "legend": {
                                    "prefix": "<"
                                }
                            },
                            {
                                "value": 0.1,
                                "color": "#b0d2e8"
                            },
                            {
                                "value": 0.2,
                                "color": "#73b3d8",
                                "legend": {}
                            },
                            {
                                "value": 0.3,
                                "color": "#3e8ec4"
                            },
                            {
                                "value": 0.4,
                                "color": "#1563aa",
                                "legend": {}
                            },
                            {
                                "value": 0.5,
                                "color": "#08306b",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ],
                    },
                    {
                        "name": "mndwi",
                        "title": "MNDWI - Green, SWIR",
                        "abstract": "Modified Normalised Difference Water Index - a derived index that correlates "
                                    "well with the existence of water (Xu 2006)",
                        "index_function": lambda data: (data["green"] - data["swir1"]) / (
                                data["green"] + data["swir1"]),
                        "needed_bands": ["green", "swir1"],
                        "color_ramp": [
                            {
                                "value": -0.1,
                                "color": "#f7fbff",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.0,
                                "color": "#d8e7f5"
                            },
                            {
                                "value": 0.2,
                                "color": "#b0d2e8"
                            },
                            {
                                "value": 0.4,
                                "color": "#73b3d8"
                            },
                            {
                                "value": 0.6,
                                "color": "#3e8ec4"
                            },
                            {
                                "value": 0.8,
                                "color": "#1563aa"
                            },
                            {
                                "value": 1.0,
                                "color": "#08306b"
                            }
                        ]
                    },
                    {
                        "name": "blue",
                        "title": "Blue - 490",
                        "abstract": "Blue band, centered on 490nm",
                        "components": {
                            "red": {
                                "blue": 1.0
                            },
                            "green": {
                                "blue": 1.0
                            },
                            "blue": {
                                "blue": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "green",
                        "title": "Green - 560",
                        "abstract": "Green band, centered on 560nm",
                        "components": {
                            "red": {
                                "green": 1.0
                            },
                            "green": {
                                "green": 1.0
                            },
                            "blue": {
                                "green": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "red",
                        "title": "Red - 660",
                        "abstract": "Red band, centered on 660nm",
                        "components": {
                            "red": {
                                "red": 1.0
                            },
                            "green": {
                                "red": 1.0
                            },
                            "blue": {
                                "red": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "nir",
                        "title": "Near Infrared (NIR) - 840",
                        "abstract": "Near infra-red band, centered on 840nm",
                        "components": {
                            "red": {
                                "nir": 1.0
                            },
                            "green": {
                                "nir": 1.0
                            },
                            "blue": {
                                "nir": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir1",
                        "title": "Shortwave Infrared (SWIR) - 1650",
                        "abstract": "Short wave infra-red band 1, centered on 1650nm",
                        "components": {
                            "red": {
                                "swir1": 1.0
                            },
                            "green": {
                                "swir1": 1.0
                            },
                            "blue": {
                                "swir1": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    },
                    {
                        "name": "swir2",
                        "title": "Shortwave Infrared (SWIR) - 2220",
                        "abstract": "Short wave infra-red band 2, centered on 2220nm",
                        "components": {
                            "red": {
                                "swir2": 1.0
                            },
                            "green": {
                                "swir2": 1.0
                            },
                            "blue": {
                                "swir2": 1.0
                            }
                        },
                        "scale_range": [0.0, 3000.0]
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "simple_rgb",
            }
        ]
    },
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "WOfS",
        "title": "Water Observations from Space",
        "abstract": "WOfS",
        # Products available for this platform.
        # For each product, the "name" is the Datacube name, and the label is used
        # to describe the label to end-users.
        "products": [
            {
                # Included as a keyword  for the layer
                "label": "USGS WOfS Daily Observations",
                # Included as a keyword  for the layer
                "type": "wofls",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """Historic Flood Mapping Water Observations from Space""",
                # The WMS name for the layer
                "name": "ls_usgs_wofs_scene",
                # The Datacube name for the associated data product
                "product_name": "ls_usgs_wofs_scene",
                "fuse_func": "datacube_wms.wms_utils.wofls_fuser",
                # "pq_fuse_func": "datacube_wms.wms_utils.wofls_fuser",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                # "pq_dataset": "ls_usgs_wofs_scene",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                # "pq_band": "water",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 35.0,
                "max_datasets_wms": 6,
                # max_datasets_wcs is the WCS equivalent of max_datasets_wms.  The main requirement for setting this
                # value is to avoid gateway timeouts on overly large WCS requests (and reduce server load).
                "max_datasets_wcs": 16,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [200, 180, 180, 160],
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": "datacube_wms.ogc_utils.mask_by_bitflag",
                # (Defaults to false)
                "pq_manual_merge": False,
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_flags_info": [
                    "nodata",
                    # "noncontiguous",
                ],
                "wcs_default_bands": ["water"],
                "styles": [
                    {
                        "name": "observations",
                        "title": "Observations",
                        "abstract": "Classified as water by the decision tree",
                        "value_map": {
                            "water": [
                                {
                                    "title": "Invalid",
                                    "abstract": "Slope or Cloud",
                                    "flags": {
                                        "or": {
                                            "cloud_shadow": True,
                                            "cloud": True
                                        }
                                    },
                                    "color": "#707070"
                                },
                                {
                                    # Possible Sea Glint, also mark as invalid
                                    "title": "Invalid_Dry",
                                    "abstract": "Possible Sea Glint, also mark as invalid",
                                    "flags": {
                                        "dry": True,
                                        "sea": True,
                                        "cloud_shadow": False,
                                        "cloud": False,
                                        "nodata": False
                                    },
                                    "color": "#707070"
                                },
                                {
                                    "title": "Dry",
                                    "abstract": "Dry",
                                    "flags": {
                                        "dry": True,
                                        "sea": False,
                                        "cloud_shadow": False,
                                        "cloud": False,
                                        "nodata": False
                                    },
                                    "color": "#D99694"
                                },
                                {
                                    "title": "Wet",
                                    "abstract": "Wet or Sea",
                                    "flags": {
                                        "or": {
                                            "wet": True,
                                            "sea": True
                                        }
                                    },
                                    "color": "#4F81BD"
                                }
                            ]
                        }
                    },
                    {
                        "name": "wet",
                        "title": "Wet Only",
                        "abstract": "Clear and Wet",
                        "value_map": {
                            "water": [
                                {
                                    "title": "Invalid",
                                    "abstract": "Slope or Cloud",
                                    "flags": {
                                        "or": {
                                            "cloud_shadow": True,
                                            "cloud": True,
                                            "nodata": True,
                                        }
                                    },
                                    "color": "#707070",
                                    "mask": True
                                },
                                {
                                    # Possible Sea Glint, also mark as invalid
                                    "title": "Invalid_Dry",
                                    "abstract": "Possible Sea Glint, also mark as invalid",
                                    "flags": {
                                        "dry": True,
                                        "sea": True
                                    },
                                    "color": "#707070",
                                    "mask": True
                                },
                                {
                                    "title": "Dry",
                                    "abstract": "Dry",
                                    "flags": {
                                        "dry": True,
                                        "sea": False,
                                    },
                                    "color": "#D99694",
                                    "mask": True
                                },
                                {
                                    "title": "Wet",
                                    "abstract": "Wet or Sea",
                                    "flags": {
                                        "or": {
                                            "wet": True,
                                            "sea": True
                                        }
                                    },
                                    "color": "#4F81BD"
                                }
                            ]
                        }
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is not required
                # by the standard.)
                "default_style": "observations",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS Statistics",
                # Included as a keyword  for the layer
                "type": "Water Summary",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_annual_summary_statistics",
                # The Datacube name for the associated data product
                "product_name": "ls_usgs_wofs_summary",
                "abstract": """Water Observations from Space (WOfS) Statistics is a set of statistical summaries of 
                the WOfS product which combines WOfS observations into summary products that help the understanding 
                of surface water across Africa. WOfS Statistics is calculated from the full depth time series (1984 ? 
                2018). The water detected for each location is summed through time and then compared to the number of 
                clear observations of that location. The result is a percentage value of the number of times water 
                was observed at the location. The layers available are: the count of dry observations; the count of 
                wet observations; the percentage of wet observations over time (water summary). 

                This layer contains the Water Summary: the percentage of clear observations which were detected as 
                wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to 
                appear transparent, few clear observations of water correlate with red and yellow colours, 
                deep blue and purple correspond to an area being wet through 90%-100% of clear observations. 

                As no confidence filtering is applied to this product, it is affected by noise where 
                mis-classifications have occurred in the WOfS water classifications, and hence can be difficult to 
                interpret on its own. The confidence layer and filtered summary are contained in the Water 
                Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of 
                the water summary.""",
                "min_zoom_factor": 15.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # Central Africa Timezone (UTC+2).
                "time_zone": 2,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: (data[band] != data[band].attrs['nodata']),
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "legend": {
                    # "url": ""
                    "styles": ["WOfS_frequency", "WOfS_frequency_blues_transparent"]
                },
                "wcs_default_bands": ["frequency"],
                "styles": [
                    {
                        "name": "WOfS_frequency",
                        "title": " Water Summary",
                        "abstract": "WOfS summary showing the frequency of Wetness",
                        "needed_bands": ["frequency"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#000000",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.002,
                                "color": "#000000",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.005,
                                "color": "#8e0101",
                                "alpha": 0.25
                            },
                            {
                                "value": 0.01,
                                "color": "#cf2200",
                                "alpha": 0.75
                            },
                            {
                                "value": 0.02,
                                "color": "#e38400"
                            },
                            {
                                "value": 0.05,
                                "color": "#e3df00"
                            },
                            {
                                "value": 0.1,
                                "color": "#a6e300"
                            },
                            {
                                "value": 0.2,
                                "color": "#62e300"
                            },
                            {
                                "value": 0.3,
                                "color": "#00e32d"
                            },
                            {
                                "value": 0.4,
                                "color": "#00e384"
                            },
                            {
                                "value": 0.5,
                                "color": "#00e3c8"
                            },
                            {
                                "value": 0.6,
                                "color": "#00c5e3"
                            },
                            {
                                "value": 0.7,
                                "color": "#0097e3"
                            },
                            {
                                "value": 0.8,
                                "color": "#005fe3"
                            },
                            {
                                "value": 0.9,
                                "color": "#000fe3"
                            },
                            {
                                "value": 1.0,
                                "color": "#5700e3"
                            }
                        ],
                        "legend": {
                            "url": "https://data.dea.ga.gov.au/WOfS/filtered_summary/v2.1.0/wofs_full_summary_legend"
                                   ".png",
                        }
                    },
                    {
                        "name": "WOfS_frequency_blues_transparent",
                        "title": "Water Summary (Blue)",
                        "abstract": "WOfS summary showing the frequency of Wetness",
                        "needed_bands": ["frequency"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#ffffff",
                                "alpha": 0.0,
                            },
                            {
                                "value": 0.001,
                                "color": "#d5fef9",
                                "alpha": 0.0,
                            },
                            {
                                "value": 0.02,
                                "color": "#d5fef9",
                            },
                            {
                                "value": 0.2,
                                "color": "#71e3ff"
                            },
                            {
                                "value": 0.4,
                                "color": "#01ccff"
                            },
                            {
                                "value": 0.6,
                                "color": "#0178ff"
                            },
                            {
                                "value": 0.8,
                                "color": "#2701ff"
                            },
                            {
                                "value": 1.0,
                                "color": "#5700e3"
                            }
                        ],
                        "legend": {
                            "units": "%",
                            "radix_point": 0,
                            "scale_by": 100.0,
                            "major_ticks": 0.1
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "WOfS_frequency",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS Statistics",
                # Included as a keyword  for the layer
                "type": "Wet Count",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_annual_summary_wet",
                # The Datacube name for the associated data product
                "product_name": "ls_usgs_wofs_summary",
                "abstract": """Water Observations from Space (WOfS) Statistics is a set of statistical summaries of 
                the WOfS product that combines the many years of WOfS observations into summary products which help 
                the understanding of surface water across Africa.  The layers available are: the count of dry 
                observations; the count of wet observations; the percentage of wet observations over time. 

            This layer contains Wet Count: how many times water was detected in observations that were clear. No 
            clear observations of water causes an area to appear transparent, 1-50 total clear observations of water 
            correlate with red and yellow colours, 100 clear observations of water correlate with green, 
            200 clear observations of water correlates with light blue, 300 clear observations of water correlates to 
            deep blue and 400 and over observations of clear water correlate to purple. 

            As no confidence filtering is applied to this product, it is affected by noise where mis-classifications 
            have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The 
            confidence layer and filtered summary are contained in the Water Observations from Space Statistics 
            Filtered Summary product, which provide a noise-reduced view of the water summary.""",
                "min_zoom_factor": 15.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # Central Africa Timezone (UTC+2).
                "time_zone": 2,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: (data[band] != data[band].attrs['nodata']),
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "legend": {
                    # "url": ""
                    "styles": ["water_observations"]
                },
                "wcs_default_bands": ["count_wet"],
                "styles": [
                    {
                        "name": "water_observations",
                        "title": "Count Wet",
                        "abstract": "WOfS summary showing the count of water observations",
                        "needed_bands": ["count_wet"],
                        "color_ramp": [
                            {
                                "value": 0,
                                "color": "#666666",
                                "alpha": 0
                            },
                            {
                                "value": 2,
                                "color": "#890000"
                            },
                            {
                                "value": 5,
                                "color": "#990000"
                            },
                            {
                                "value": 10,
                                "color": "#E38400"
                            },
                            {
                                "value": 25,
                                "color": "#E3DF00"
                            },
                            {
                                "value": 50,
                                "color": "#A6E300"
                            },
                            {
                                "value": 100,
                                "color": "#00E32D"
                            },
                            {
                                "value": 150,
                                "color": "#00E3C8"
                            },
                            {
                                "value": 200,
                                "color": "#0097E3"
                            },
                            {
                                "value": 250,
                                "color": "#005FE3"
                            },
                            {
                                "value": 300,
                                "color": "#000FE3"
                            },
                            {
                                "value": 350,
                                "color": "#000EA9"
                            },
                            {
                                "value": 400,
                                "color": "#5700E3",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ],
                        "legend": {
                            "radix_point": 0,
                            "scale_by": 1,
                            "major_ticks": 100
                        }
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "water_observations",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS Statistics",
                # Included as a keyword  for the layer
                "type": "Dry Count",
                # Included as a keyword  for the layer
                "variant": "25m",
                # The WMS name for the layer
                "name": "wofs_annual_summary_dry",
                # The Datacube name for the associated data product
                "product_name": "ls_usgs_wofs_summary",
                "abstract": """Water Observations from Space (WOfS) Statistics is a set of statistical summaries of 
                the WOfS product that combines the many years of WOfS observations into summary products which help 
                the understanding of surface water across Africa.  The layers available are: the count of dry 
                observations; the count of wet observations; the percentage of wet observations over time. 

            This layer contains Dry Count: how many times an area could be seen Dry (ie. not affected by clouds, 
            shadows or other satellite observation problems). 

            As no confidence filtering is applied to this product, it is affected by noise where mis-classifications 
            have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The 
            confidence layer and filtered summary are contained in the Water Observations from Space Statistics 
            Filtered Summary product, which provide a noise-reduced view of the water summary.""",
                "min_zoom_factor": 15.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # Central Africa Timezone (UTC+2).
                "time_zone": 2,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: (data[band] != data[band].attrs['nodata']),
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "legend": {
                    # "url": ""
                    "styles": ["dry_observations"]
                },
                "wcs_default_bands": ["count_dry"],
                "styles": [
                    {
                        "name": "dry_observations",
                        "title": "Count Dry",
                        "abstract": "WOfS summary showing the count of dry observations",
                        "needed_bands": ["count_dry"],
                        "color_ramp": [
                            {
                                "value": 0,
                                "color": "#FFFFFF",
                                "alpha": 0
                            },
                            {
                                # purely for legend display
                                # we should not get fractional
                                # values in this styles
                                "value": 10,
                                "color": "#b21800",
                                "alpha": 1
                            },
                            {
                                "value": 100,
                                "color": "#ef8500"
                            },
                            {
                                "value": 200,
                                "color": "#ffb800"
                            },
                            {
                                "value": 300,
                                "color": "#ffd300"
                            },
                            {
                                "value": 400,
                                "color": "#ffe300"
                            },
                            {
                                "value": 500,
                                "color": "#fff300"
                            },
                            {
                                "value": 600,
                                "color": "#d0f800"
                            },
                            {
                                "value": 700,
                                "color": "#a0fd00"
                            },
                            {
                                "value": 800,
                                "color": "#6ee100"
                            },
                            {
                                "value": 901,
                                "color": "#39a500"
                            },
                            {
                                "value": 1000,
                                "color": "#026900",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ],
                        "legend": {
                            "radix_point": 0,
                            "scale_by": 1,
                            "major_ticks": 100,
                            "axes_position": [0.05, 0.5, 0.89, 0.15]
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "dry_observations",
            }
        ]
    },
        {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "WOfS Collection2",
        "title": "Water Observations from Space c2",
        "abstract": "WOfS",
        # Products available for this platform.
        # For each product, the "name" is the Datacube name, and the label is used
        # to describe the label to end-users.
        "products": [
            {
                # Included as a keyword  for the layer
                "label": "WOfS C2 Annual Statistics",
                # Included as a keyword  for the layer
                "type": "Water Summary",
                # Included as a keyword  for the layer
                "variant": "30m",
                # The WMS name for the layer
                "name": "wofs_2_annual_summary_statistics",
                # The Datacube name for the associated data product
                "product_name": "ga_ls8c_wofs_2_annual_summary",
                "abstract": """Water Observations from Space (WOfS) Statistics is a set of statistical summaries of 
                the WOfS product which combines WOfS observations into summary products that help the understanding 
                of surface water across Africa. The water detected for each location is summed through time and then 
                compared to the number of clear observations of that location. 
                The result is a percentage value of the number of times water 
                was observed at the location. The layers available are: the count of 
                wet observations; the percentage of wet observations over time (water summary). 

                This layer contains the Water Summary: the percentage of clear observations which were detected as 
                wet (ie. the ratio of wet to clear as a percentage). No clear observations of water causes an area to 
                appear transparent, few clear observations of water correlate with red and yellow colours, 
                deep blue and purple correspond to an area being wet through 90%-100% of clear observations. 

                As no confidence filtering is applied to this product, it is affected by noise where 
                mis-classifications have occurred in the WOfS water classifications, and hence can be difficult to 
                interpret on its own. The confidence layer and filtered summary are contained in the Water 
                Observations from Space Statistics Filtered Summary product, which provide a noise-reduced view of 
                the water summary.""",
                "min_zoom_factor": 0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # Central Africa Timezone (UTC+2).
                "time_zone": 2,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: (data[band] != data[band].attrs['nodata']),
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "legend": {
                    # "url": ""
                    "styles": ["WOfS_frequency", "WOfS_frequency_blues_transparent"]
                },
                "wcs_default_bands": ["frequency"],
                "styles": [
                    {
                        "name": "WOfS_frequency",
                        "title": " Water Summary",
                        "abstract": "WOfS summary showing the frequency of Wetness",
                        "needed_bands": ["frequency"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#000000",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.002,
                                "color": "#000000",
                                "alpha": 0.0
                            },
                            {
                                "value": 0.005,
                                "color": "#8e0101",
                                "alpha": 0.25
                            },
                            {
                                "value": 0.01,
                                "color": "#cf2200",
                                "alpha": 0.75
                            },
                            {
                                "value": 0.02,
                                "color": "#e38400"
                            },
                            {
                                "value": 0.05,
                                "color": "#e3df00"
                            },
                            {
                                "value": 0.1,
                                "color": "#a6e300"
                            },
                            {
                                "value": 0.2,
                                "color": "#62e300"
                            },
                            {
                                "value": 0.3,
                                "color": "#00e32d"
                            },
                            {
                                "value": 0.4,
                                "color": "#00e384"
                            },
                            {
                                "value": 0.5,
                                "color": "#00e3c8"
                            },
                            {
                                "value": 0.6,
                                "color": "#00c5e3"
                            },
                            {
                                "value": 0.7,
                                "color": "#0097e3"
                            },
                            {
                                "value": 0.8,
                                "color": "#005fe3"
                            },
                            {
                                "value": 0.9,
                                "color": "#000fe3"
                            },
                            {
                                "value": 1.0,
                                "color": "#5700e3"
                            }
                        ],
                        "legend": {
                            "url": "https://data.dea.ga.gov.au/WOfS/filtered_summary/v2.1.0/wofs_full_summary_legend"
                                   ".png",
                        }
                    },
                    {
                        "name": "WOfS_frequency_blues_transparent",
                        "title": "Water Summary (Blue)",
                        "abstract": "WOfS summary showing the frequency of Wetness",
                        "needed_bands": ["frequency"],
                        "color_ramp": [
                            {
                                "value": 0.0,
                                "color": "#ffffff",
                                "alpha": 0.0,
                            },
                            {
                                "value": 0.001,
                                "color": "#d5fef9",
                                "alpha": 0.0,
                            },
                            {
                                "value": 0.02,
                                "color": "#d5fef9",
                            },
                            {
                                "value": 0.2,
                                "color": "#71e3ff"
                            },
                            {
                                "value": 0.4,
                                "color": "#01ccff"
                            },
                            {
                                "value": 0.6,
                                "color": "#0178ff"
                            },
                            {
                                "value": 0.8,
                                "color": "#2701ff"
                            },
                            {
                                "value": 1.0,
                                "color": "#5700e3"
                            }
                        ],
                        "legend": {
                            "units": "%",
                            "radix_point": 0,
                            "scale_by": 100.0,
                            "major_ticks": 0.1
                        }
                    },
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "WOfS_frequency",
            },
            {
                # Included as a keyword  for the layer
                "label": "WOfS C2 Annual Statistics",
                # Included as a keyword  for the layer
                "type": "Wet Count",
                # Included as a keyword  for the layer
                "variant": "30m",
                # The WMS name for the layer
                "name": "wofs_2_annual_summary_wet",
                # The Datacube name for the associated data product
                "product_name": "ga_ls8c_wofs_2_annual_summary",
                "abstract": """Water Observations from Space (WOfS) Statistics is a set of statistical summaries of 
                the WOfS product that combines the many years of WOfS observations into summary products which help 
                the understanding of surface water across Africa.  The layers available are: 
                the count of wet observations; the percentage of wet observations over time. 

            This layer contains Wet Count: how many times water was detected in observations that were clear. No 
            clear observations of water causes an area to appear transparent, 1-50 total clear observations of water 
            correlate with red and yellow colours, 100 clear observations of water correlate with green, 
            200 clear observations of water correlates with light blue, 300 clear observations of water correlates to 
            deep blue and 400 and over observations of clear water correlate to purple. 

            As no confidence filtering is applied to this product, it is affected by noise where mis-classifications 
            have occurred in the WOfS water classifications, and hence can be difficult to interpret on its own. The 
            confidence layer and filtered summary are contained in the Water Observations from Space Statistics 
            Filtered Summary product, which provide a noise-reduced view of the water summary.""",
                "min_zoom_factor": 0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # Central Africa Timezone (UTC+2).
                "time_zone": 2,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: (data[band] != data[band].attrs['nodata']),
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "legend": {
                    # "url": ""
                    "styles": ["water_observations"]
                },
                "wcs_default_bands": ["count_wet"],
                "styles": [
                    {
                        "name": "water_observations",
                        "title": "Count Wet",
                        "abstract": "WOfS summary showing the count of water observations",
                        "needed_bands": ["count_wet"],
                        "color_ramp": [
                            {
                                "value": 0,
                                "color": "#666666",
                                "alpha": 0
                            },
                            {
                                "value": 2,
                                "color": "#890000"
                            },
                            {
                                "value": 5,
                                "color": "#990000"
                            },
                            {
                                "value": 10,
                                "color": "#E38400"
                            },
                            {
                                "value": 25,
                                "color": "#E3DF00"
                            },
                            {
                                "value": 50,
                                "color": "#A6E300"
                            },
                            {
                                "value": 100,
                                "color": "#00E32D"
                            },
                            {
                                "value": 150,
                                "color": "#00E3C8"
                            },
                            {
                                "value": 200,
                                "color": "#0097E3"
                            },
                            {
                                "value": 250,
                                "color": "#005FE3"
                            },
                            {
                                "value": 300,
                                "color": "#000FE3"
                            },
                            {
                                "value": 350,
                                "color": "#000EA9"
                            },
                            {
                                "value": 400,
                                "color": "#5700E3",
                                "legend": {
                                    "prefix": ">"
                                }
                            }
                        ],
                        "legend": {
                            "radix_point": 0,
                            "scale_by": 1,
                            "major_ticks": 100
                        }
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.

                # (Looks like Terria assumes this is the first style in the list, but this is
                #  not required by the standard.)
                "default_style": "water_observations",
            }
        ]
    },
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "Fractional Cover",
        "title": "Landsat",
        "abstract": "Landsat Fractional Cover based on USGS Level 2 Scenes",

        # Products available for this platform.
        # For each product, the "name" is the Datacube name, and the label is used
        # to describe the label to end-users.
        "products": [
            {
                # Included as a keyword  for the layer
                "label": "USGS",
                # Included as a keyword  for the layer
                "type": "Fractional Cover",
                # Included as a keyword  for the layer
                "variant": "",
                "abstract": """Landsat Fractional Cover based on USGS Level 2 Scenes. Data is only visible at higher 
                resolutions; when zoomed-out the available area will be displayed as a shaded region. Fractional 
                cover provides information about the the proportions of green vegetation, non-green vegetation (
                including deciduous trees during autumn, dry grass, etc.), and bare areas. Fractional cover provides 
                insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over 
                time. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program, 
                for more information please see 
                data.auscover.org.au/xwiki/bin/view/Product+pages/Landsat+Fractional+Cover Fractional Cover products 
                use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. This 
                product contains Fractional Cover derived from Landsat 5, Landsat 7, and Landsat 8 US Geological 
                Survey Collection 1 Level2 Surface Reflectance USARD, 30m UTM based projection.""",
                # The WMS name for the layer
                "name": "ls_usgs_fc_scene",
                # The Datacube name for the associated data product
                # "multi_product": False,
                "product_name": "ls_usgs_fc_scene",
                # The Datacube name for the associated pixel-quality product (optional)
                # The name of the associated Datacube pixel-quality product
                "pq_dataset": "ls_usgs_wofs_scene",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                "pq_band": "water",
                # Fuse function for pq data
                "pq_fuse_func": "datacube_wms.wms_utils.wofls_fuser",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 10.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # Central Africa Timezone (UTC+2).
                "time_zone": 2,
                # Extent mask function
                # Determines what portions of dataset is potentially meaningful data.
                "extent_mask_func": lambda data, band: (data[band] != data[band].attrs['nodata']),
                # Flags listed here are ignored in GetFeatureInfo requests.
                # (defaults to empty list)
                "ignore_info_flags": [],
                "legend": {
                    "url": "https://data.dea.ga.gov.au/fractional-cover/fc-percentile/annual/v2.1.0/fcp_legend.png",
                },
                "wcs_default_bands": ["BS", "PV", "NPV"],
                "styles": [
                    {
                        "name": "simple_fc",
                        "title": "Fractional Cover",
                        "abstract": "Fractional cover representation, with green vegetation in green, dead vegetation "
                                    "in blue, and bare soil in red",
                        "components": {
                            "red": {
                                "BS": 1.0
                            },
                            "green": {
                                "PV": 1.0
                            },
                            "blue": {
                                "NPV": 1.0
                            }
                        },
                        "scale_range": [0.0, 100.0],
                        "pq_masks": [
                            {
                                "flags": {
                                    'dry': True
                                },
                            },
                            {
                                "flags": {
                                    "cloud_shadow": False,
                                    "cloud": False,
                                    "sea": False
                                }
                            },
                        ]
                    }
                ],
                # Default style (if request does not specify style)
                # MUST be defined in the styles list above.
                # (Looks like Terria assumes this is the first style in the list, but this is not required
                # by the standard.)
                "default_style": "simple_fc",
            }
        ]
    },
]
