from prod.ows_reslim_cfg import reslim_srtm

# bands


bands_usgs_wofs_summary = {"count_wet": [], "count_dry": [], "frequency": []}


bands_elevation = {
    "elevation": [],
}


bands_jers = {"hh": [], "mask": [], "date": [], "linci": []}

# Style


style_jers_hh = {
    "name": "hh",
    "title": "HH",
    "abstract": "HH band",
    "needed_bands": ["hh"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "hh",
        },
    },
    "color_ramp": [
        {"value": 0, "color": "#f7fcf5"},
        {"value": 908, "color": "#e2f4dd"},  # 750 * 1.21
        {"value": 1210, "color": "#c0e6b9"},
        {"value": 1815, "color": "#94d390"},
        {"value": 3025, "color": "#60ba6c"},
        {"value": 4840, "color": "#329b51"},
        {"value": 7260, "color": "#0c7835"},
        {"value": 9680, "color": "#00441b"},  # 8000 * 1.21
    ],
    "legend": {
        "begin": 0,
        "end": 9680,
        "ticks": ["0", "2420", "4840", "7260", "9680"],
        "tick_labels": {
            "0": {"label": "0"},
            "2420": {"label": "2420"},
            "4840": {"label": "4840"},
            "7260": {"label": "7260"},
            "9680": {"prefix": ">"},
        },
    },
}


style_greyscale = {
    "name": "greyscale",
    "title": "Greyscale",
    "abstract": "Greyscale elevation",
    "needed_bands": ["elevation"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "elevation",
        },
    },
    "color_ramp": [
        {"value": -0, "color": "#383838", "alpha": 0.0},
        {"value": 0.1, "color": "#383838"},
        {"value": 250, "color": "#5e5e5e"},
        {"value": 500, "color": "#858585"},
        {"value": 1000, "color": "#adadad"},
        {"value": 2000, "color": "#d4d4d4"},
        {"value": 4000, "color": "#fafafa"},
    ],
    "legend": {
        "title": "Elevation ",
        "begin": "0",
        "end": "4000",
        "ticks_every": 100,
        "units": "m",
        "tick_labels": {
            "4000": {"prefix": ">"},
        },
    },
}

style_colours = {
    "name": "colours",
    "title": "Coloured",
    "abstract": "Coloured elevation",
    "needed_bands": ["elevation"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "elevation",
        },
    },
    "color_ramp": [
        {"value": -0, "color": "#e1f2ff", "alpha": 0.0},
        {"value": 0.1, "color": "#41c23c"},
        {"value": 150, "color": "#f9a80e"},
        {"value": 300, "color": "#cb5f3e"},
        {"value": 400, "color": "#9d387d"},
        {"value": 500, "color": "#ba6daa"},
        {"value": 900, "color": "#d7a2d6"},
        {"value": 1200, "color": "#e6c8e6"},
        {"value": 4000, "color": "#ffecf9"},
    ],
    "legend": {
        "title": "Elevation ",
        "begin": "0",
        "end": "4000",
        "ticks_every": 400,
        "units": "m",
        "tick_labels": {
            "4000": {"prefix": ">"},
        },
    },
}


# Actual Configuration

ows_cfg = {
    "global": {
        # Master config for all services and products.
        "response_headers": {
            "Access-Control-Allow-Origin": "*",  # CORS header
        },
        "services": {
            "wms": True,
            "wcs": True,
            "wmts": True,
        },
        "published_CRSs": {
            "EPSG:3857": {  # Web Mercator
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:3577": {  # GDA-94, Australian Albers. Not sure why, but it's required!
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "EPSG:4326": {"geographic": True, "vertical_coord_first": True},  # WGS-84
            "EPSG:6933": {  # Cylindrical equal area
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
            "ESRI:102022": {
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
        },
        "allowed_urls": [
            "https://ows.digitalearth.africa",
            "https://ows-latest.digitalearth.africa",
        ],
        # Metadata to go straight into GetCapabilities documents
        "title": "Digital Earth Africa - OGC Web Services",
        "abstract": """Digital Earth Africa OGC Web Services""",
        "info_url": "dea.ga.gov.au/",
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
    },  # END OF global SECTION
    "wms": {
        # Config for WMS service, for all products/layers
        "s3_url": "https://data.digitalearth.africa",
        "s3_bucket": "deafrica-data",
        "s3_aws_zone": "ap-southeast-2",
        "max_width": 512,
        "max_height": 512,
    },  # END OF wms SECTION
    "wcs": {
        # Config for WCS service, for all products/coverages
        "default_geographic_CRS": "EPSG:4326",
        "formats": {
            "GeoTIFF": {
                # "renderer": "datacube_ows.wcs_utils.get_tiff",
                "renderers": {
                    "1": "datacube_ows.wcs1_utils.get_tiff",
                    "2": "datacube_ows.wcs2_utils.get_tiff",
                },
                "mime": "image/geotiff",
                "extension": "tif",
                "multi-time": False,
            },
            "netCDF": {
                # "renderer": "datacube_ows.wcs_utils.get_netcdf",
                "renderers": {
                    "1": "datacube_ows.wcs1_utils.get_netcdf",
                    "2": "datacube_ows.wcs2_utils.get_netcdf",
                },
                "mime": "application/x-netcdf",
                "extension": "nc",
                "multi-time": True,
            },
        },
        "native_format": "GeoTIFF",
    },  # END OF wcs SECTION
    "layers": [
        {
            "title": "Digital Earth Africa - OGC Web Services",
            "abstract": "Digital Earth Africa OGC Web Services",
            "layers": [
                # Hierarchical list of layers.  May be a combination of unnamed/unmappable folder-layers or named mappable layers.
                {
                    "include": "prod.landsat.ows_sr_cfg.layers",
                    "type": "python",
                },
                {
                    "include": "prod.landsat.ows_s2_cfg.layers",
                    "type": "python",
                },
                {
                    "include": "prod.wofs.ows_wofs_cfg.layers",
                    "type": "python",
                },
                {
                    "include": "prod.wofs.ows_wofsc2_cfg.layers",
                    "type": "python",
                },
                {
                    "include": "prod.fc.ows_fc_cfg.layers",
                    "type": "python",
                },
                {
                    "include": "prod.landsat.ows_geomedian_cfg.layers",
                    "type": "python",
                },
                {
                    "title": "ALOS/PALSAR",
                    "abstract": """Annual mosaic of ALOS/PALSAR and ALOS-2/PALSAR-2 data""",
                    "layers": [
                        {
                            "include": "prod.alos.ows_alos_cfg.layer",
                            "type": "python",
                        },
                        {
                            "title": "Radar Backscatter Annual Mosaic (JERS)",
                            "name": "jers_mosaic",
                            "abstract": """
Synthetic Aperture Radar (SAR) data have been shown to provide different and complementary information to the more common optical remote sensing data. Radar backscatter response is a function of topography, land cover structure, orientation, and moisture characteristics—including vegetation biomass—and the radar signal can penetrate clouds, providing information about the earth’s surface where optical sensors cannot. Digital Earth Africa provides access to Normalized Radar Backscatter data, for which Radiometric Terrain Correction (RTC) has been applied so data acquired with different imaging geometries over the same region can be compared.
The JERS annual mosaic is generated from images acquired by the SAR sensor on the Japanese Earth Resources Satellite-1 (JERS-1) satellite.

This product contains radar measurement in L-band and HH polarization. It has a spatial resolution of 25 m and is available for 1996. Data is provided as digital number (DN), which can be converted to backscatter in decibel unit using 10*log10(𝐷𝑁^2)-84.66.

It is part of a global dataset provided by the Japan Aerospace Exploration Agency (JAXA) Earth Observation Research Center.

For more information on the product, see https://www.eorc.jaxa.jp/ALOS/en/palsar_fnf/fnf_index.htm

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
                            "product_name": "jers_sar_tile",
                            "time_resolution": "year",
                            "bands": bands_jers,
                            "resource_limits": reslim_alos_palsar,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": False,
                            },
                            "flags": {
                                "product": "jers_sar_tile",
                                "band": "mask",
                                "ignore_info_flags": [],
                            },
                            "wcs": {
                                "native_crs": "EPSG:4326",
                                "native_resolution": [
                                    0.000222222222222,
                                    -0.000222222222222,
                                ],
                                "default_bands": ["hh", "mask"],
                            },
                            "styling": {
                                "default_style": "hh",
                                "styles": [style_jers_hh],
                            },
                        },
                    ],
                },
                {
                    "title": "Shuttle Radar Topography Mission",
                    "abstract": """Digital elevation model from NASA's SRTM<""",
                    "layers": [
                        {
                            "title": "Shuttle Radar Topography Mission Digital Elevation Model",
                            "name": "srtm",
                            "abstract": """
A Digital Elevation Model (DEM) is a digital representation of Earth’s topography. It helps to understand the land surface characteristics in the height dimension. It is also used as an ancillary dataset to calculate illumination and viewing geometry of a satellite imagery. DE Africa provides access to the Shuttle Radar Topography Mission (SRTM) v 3.0 (SRTMGL1) product.

This elevation model has a spatial resolution of 30 m and is derived from data collected by NASA's Shuttle Radar Topography Mission in 2000.

It is provided by NASA's Land Processes Distributed Active Archive Center (LP DAAC).

For more information, see https://lpdaac.usgs.gov/products/srtmgl1v003/

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki) and for direct download from AWS S3 (https://data.digitalearth.africa/).
""",
                            "product_name": "srtm",
                            "time_resolution": "year",
                            "bands": bands_elevation,
                            "resource_limits": reslim_srtm,
                            "image_processing": {
                                "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
                                "always_fetch_bands": [],
                                "manual_merge": False,
                            },
                            "wcs": {
                                "native_crs": "EPSG:4326",
                                "native_resolution": [
                                    0.000277777777780,
                                    -0.000277777777780,
                                ],
                                "default_bands": ["elevation"],
                            },
                            "styling": {
                                "default_style": "greyscale",
                                "styles": [style_greyscale, style_colours],
                            },
                        },
                    ],
                },
            ],
        }
    ],
}
