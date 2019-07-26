import re

# Static config for the wms metadata.
# pylint: skip-file

response_cfg = {
    "Access-Control-Allow-Origin": "*",  # CORS header
}


service_cfg = {
    ## Which web service(s) should be supported by this instance
    # Defaults: wms: True, wcs: False, wmts: False
    # Notes:
    #   WMTS support is implemented as a thin proxy to WMS. Some corners of the spec are interpreted
    #   somewhat loosely. In particular exception documents are directly translated from the underlying
    #   WMS error and are unlikely to be fully compliant with the WMTS standard.
    "wcs": True,
    "wms": True,
    "wmts": True,

    ## Required config for WMS and/or WCS
    # Service title - appears e.g. in Terria catalog
    "title": "Digital Earth Africa - OGC Web Services",
    # Service URL.  Should a fully qualified URL or a list of fully qualified URLs that the service can return
    # in the GetCapabilities document based on the requesting url
    "url": [ "https://ows.digitalearth.africa" ],
    # URL that humans can visit to learn more about the WMS or organization
    # should be fully qualified
    "human_url": "https://digitalearth.africa",
    # Provide S3 data URL for data_links in GetFeatureinfo
    "s3_url": "http://data.digitalearth.africa",
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
    },

    ## Required config for WCS
    # Must be a geographic CRS in the published_CRSs list.  EPSG:4326 is recommended, but any geographic CRS should work.
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

    ## Optional config for instances supporting WMS
    # Max tile height/width.  If not specified, default to 256x256
    "max_width": 512,
    "max_height": 512,

    # Optional config for all services (WMS and/or WCS) - may be set to blank/empty, no defaults
    "abstract": """Digital Earth Africa OGC Web Services""",
    "keywords": [
        "landsat",
        "africa",
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
    # extent covering much of Australia for all
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
        "name": "LANDSAT_8",
        "title": "Landsat 8",
        "abstract": "Images from the Landsat 8 satellite",
        "products": [
            {
                # Included as a keyword  for the layer
                "label": "USGS",
                # Included as a keyword  for the layer
                "type": "Surface Reflectance",
                # Included as a keyword  for the layer
                "variant": "",
                # The WMS name for the layer
                "name": "ls8_usgs_sr_scene",
                # The Datacube name for the associated data product
                "product_name": "ls8_usgs_sr_scene",
                "bands": {
                    "red": ["crimson"],
                    "green": [],
                    "blue": [ "azure" ],
                    "nir": [ "near_infrared" ],
                    "swir1": [ "shortwave_infrared_1", "near_shortwave_infrared" ],
                    "swir2": [ "shortwave_infrared_2", "far_shortwave_infrared" ],
                    "coastal_aerosol": [ "far_blue" ],
                },
                "pq_dataset": "ls8_usgs_sr_scene",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                "pq_band": "pixel_qa",
                # Min zoom factor - sets the zoom level where the cutover from indicative polygons
                # to actual imagery occurs.
                "min_zoom_factor": 500.0,
                "max_datasets_wms": 6,
                # max_datasets_wcs is the WCS equivalent of max_datasets_wms.  The main requirement for setting this
                # value is to avoid gateway timeouts on overly large WCS requests (and reduce server load).
                "max_datasets_wcs": 16,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                #
                "extent_mask_func": "datacube_wms.ogc_utils.mask_by_val",
                "ignore_info_flags": [],
                # Include an additional list of utc dates in the WMS Get Feature Info
                # HACK: only used for GSKY non-solar day lookup
                "feature_info_include_utc_dates": True,
                # Set to true if the band product dataset extents include nodata regions.
                "data_manual_merge": False,
                # Set to true if the pq product dataset extents include nodata regions.
                "pq_manual_merge": False,
                # Bands to always fetch from the Datacube, even if it is not used by the active style.
                # Useful for when a particular band is always needed for the extent_mask_func,
                "always_fetch_bands": [ ],
                # Apply corrections for solar angle, for "Level 1" products.
                # (Defaults to false - should not be used for NBAR/NBAR-T or other Analysis Ready products
                "apply_solar_corrections": False,
                # If this value is set then WCS works exclusively with the configured
                # date and advertises no time dimension in GetCapabilities.
                # Intended mostly for WCS debugging.
                "wcs_sole_time": "2017-01-01",
                "native_wcs_crs": "EPSG:3577",
                # The resolution (x,y) for WCS.
                # This is the number of CRS units (e.g. degrees, metres) per pixel in the horizontal and vertical
                # directions for the native resolution.  E.g. for a EPSG:3577  (25.0,25.0) for Landsat-8 and (10.0,10.0 for Sentinel-2)
                "native_wcs_resolution": [ 25.0, 25.0 ],
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
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
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
                        "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water (McFeeters 1996)",
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
                                "legend": { }
                            },
                            {
                                "value": 0.3,
                                "color": "#3e8ec4"
                            },
                            {
                                "value": 0.4,
                                "color": "#1563aa",
                                "legend": { }
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
                        "abstract": "Modified Normalised Difference Water Index - a derived index that correlates well with the existence of water (Xu 2006)",
                        "index_function": lambda data: (data["green"] - data["swir1"]) / (data["green"] + data["swir1"]),
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
            }
        ]
    },
    {
        # Name and title of the platform layer.
        # Platform layers are not mappable. The name is for internal server use only.
        "name": "LANDSAT_7",
        "title": "Landsat 7",
        "abstract": "Images from the Landsat 7 satellite",
        "products": [
            {
                # Included as a keyword  for the layer
                "label": "USGS",
                # Included as a keyword  for the layer
                "type": "Surface Reflectance",
                # Included as a keyword  for the layer
                "variant": "",
                # The WMS name for the layer
                "name": "ls7_usgs_sr_scene",
                # The Datacube name for the associated data product
                "product_name": "ls7_usgs_sr_scene",
                "bands": {
                    "red": ["crimson"],
                    "green": [],
                    "blue": [ "azure" ],
                    "nir": [ "near_infrared" ],
                    "swir1": [ "shortwave_infrared_1", "near_shortwave_infrared" ],
                    "swir2": [ "shortwave_infrared_2", "far_shortwave_infrared" ]
                },
                "pq_dataset": "ls7_usgs_sr_scene",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                "pq_band": "pixel_qa",
"min_zoom_factor": 35.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
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
                # A function that extracts the "sub-product" id (e.g. path number) from a dataset. Function should return a (small) integer
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
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
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
                        "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water (McFeeters 1996)",
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
                                "legend": { }
                            },
                            {
                                "value": 0.3,
                                "color": "#3e8ec4"
                            },
                            {
                                "value": 0.4,
                                "color": "#1563aa",
                                "legend": { }
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
                        "abstract": "Modified Normalised Difference Water Index - a derived index that correlates well with the existence of water (Xu 2006)",
                        "index_function": lambda data: (data["green"] - data["swir1"]) / (data["green"] + data["swir1"]),
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
        "name": "LANDSAT_5",
        "title": "Landsat 5",
        "abstract": "Images from the Landsat 5 satellite",
        "products": [
            {
                # Included as a keyword  for the layer
                "label": "USGS",
                # Included as a keyword  for the layer
                "type": "Surface Reflectance",
                # Included as a keyword  for the layer
                "variant": "",
                # The WMS name for the layer
                "name": "ls5_usgs_sr_scene",
                # The Datacube name for the associated data product
                "product_name": "ls5_usgs_sr_scene",
                "bands": {
                    "red": ["crimson"],
                    "green": [],
                    "blue": [ "azure" ],
                    "nir": [ "near_infrared" ],
                    "swir1": [ "shortwave_infrared_1", "near_shortwave_infrared" ],
                    "swir2": [ "shortwave_infrared_2", "far_shortwave_infrared" ]
                },
                "pq_dataset": "ls5_usgs_sr_scene",
                # The name of the measurement band for the pixel-quality product
                # (Only required if pq_dataset is set)
                "pq_band": "pixel_qa",
                "min_zoom_factor": 35.0,
                # The fill-colour of the indicative polygons when zoomed out.
                # Triplets (rgb) or quadruplets (rgba) of integers 0-255.
                "zoomed_out_fill_colour": [150, 180, 200, 160],
                # Time Zone.  In hours added to UTC (maybe negative)
                # Used for rounding off scene times to a date.
                # 9 is good value for imagery of Australia.
                "time_zone": 9,
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
                # A function that extracts the "sub-product" id (e.g. path number) from a dataset. Function should return a (small) integer
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
                        "abstract": "Normalised Difference Vegetation Index - a derived index that correlates well with the existence of vegetation",
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
                        "abstract": "Normalised Difference Water Index - a derived index that correlates well with the existence of water (McFeeters 1996)",
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
                                "legend": { }
                            },
                            {
                                "value": 0.3,
                                "color": "#3e8ec4"
                            },
                            {
                                "value": 0.4,
                                "color": "#1563aa",
                                "legend": { }
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
                        "abstract": "Modified Normalised Difference Water Index - a derived index that correlates well with the existence of water (Xu 2006)",
                        "index_function": lambda data: (data["green"] - data["swir1"]) / (data["green"] + data["swir1"]),
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
    }
]
