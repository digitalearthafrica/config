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
            "EPSG:4326": {"geographic": True, "vertical_coord_first": True},  # WGS-84
            "EPSG:6933": {  # Cylindrical equal area
                "geographic": False,
                "horizontal_coord": "x",
                "vertical_coord": "y",
            },
        },
        "allowed_urls": [
            "https://ows.dev.digitalearth.africa",
            "https://ows-latest.dev.digitalearth.africa",
        ],
        # Metadata to go straight into GetCapabilities documents
        "title": "Digital Earth Africa - OGC Web Services",
        "abstract": """Digital Earth Africa OGC Web Services""",
        "info_url": "digitalearthafrica.org/",
        "keywords": [
            "landsat",
            "africa",
            "WOfS",
            "fractional-cover",
            "time-series",
        ],
        "contact_info": {
            "person": "Digital Earth Africa",
            "organisation": "Digital Earth Africa",
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
            "email": "info@digitalearthafrica.org",
        },
        "fees": "",
        "access_constraints": "© Commonwealth of Australia (Geoscience Australia) 2018. "
        "This product is released under the Creative Commons Attribution 4.0 International Licence. "
        "http://creativecommons.org/licenses/by/4.0/legalcode",
        "translations_directory": "/env/config/ows_refactored/translations",
        "supported_languages": [
            "en",  # English  - the default language, the language used in the untranslated metadata.
            "fr",  # French
        ],
    },  # END OF global SECTION
    "wms": {
        # Config for WMS service, for all products/layers
        "s3_aws_zone": "af-south-1",
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
                # Hierarchical list of layers.  May be a combination of unnamed/unmappable
                # folder-layers or named mappable layers.
                {
                    "title": "Satellite images",
                    "abstract": """Satellite images""",
                    "layers": [
                        {
                            "title": "Surface reflectance",
                            "abstract": """Surface reflectance""",
                            "layers": [
                                {
                                    "title": "Daily surface reflectance",
                                    "abstract": """Daily surface reflectance""",
                                    "layers": [
                                        {
                                            "include": "ows_refactored.surface_reflectance.ows_s2_cfg.layer",
                                            "type": "python",
                                        },
                                        {
                                            "include": "ows_refactored.surface_reflectance.ows_lsc2_sr_cfg.layer_ls9",
                                            "type": "python",
                                        },
                                        {
                                            "include": "ows_refactored.surface_reflectance.ows_lsc2_sr_cfg.layer_ls8",
                                            "type": "python",
                                        },
                                        {
                                            "include": "ows_refactored.surface_reflectance.ows_lsc2_sr_cfg.layer_ls7",
                                            "type": "python",
                                        },
                                        {
                                            "include": "ows_refactored.surface_reflectance.ows_lsc2_sr_cfg.layer_ls5",
                                            "type": "python",
                                        },
                                    ],
                                },
                                {
                                    "title": "Annual surface reflectance",
                                    "abstract": """Annual surface reflectance""",
                                    "layers": [
                                        {
                                            "include": "ows_refactored.surface_reflectance.ows_gm_s2_annual_cfg.layer",
                                            "type": "python",
                                        },
                                        {
                                            "include": "ows_refactored.surface_reflectance.ows_gm_ls8_annual_cfg.layer",
                                            "type": "python",
                                        },
                                        {
                                            "include": "ows_refactored.surface_reflectance.ows_gm_ls8_ls9_annual_cfg.layer",
                                            "type": "python",
                                        },
                                        {
                                            "include": "ows_refactored.surface_reflectance.ows_gm_ls5_ls7_annual_cfg.layer",
                                            "type": "python",
                                        },
                                    ],
                                },
                                {
                                    "title": "Semiannual surface reflectance",
                                    "abstract": """Semiannual surface reflectance""",
                                    "layers": [
                                        {
                                            "include": "ows_refactored.surface_reflectance.ows_gm_s2_semiannual_cfg.layer",
                                            "type": "python",
                                        },
                                    ],
                                },
                                {
                                    "title": "Rolling surface reflectance",
                                    "abstract": """Monthly rolling surface reflectance values are provided, calculated using a moving window of three months.""",
                                    "layers": [
                                        {
                                            "include": "ows_refactored.surface_reflectance.ows_gm_s2_rolling_cfg.layer",
                                            "type": "python",
                                        },
                                    ],
                                }
                            ],
                        },
                        {
                            "title": "Surface temperature",
                            "abstract": """Surface temperature""",
                            "layers": [
                                {
                                    "title": "Daily surface temperature",
                                    "abstract": """Daily surface temperature""",
                                    "layers": [
                                        {
                                            "include": "ows_refactored.surface_temperature.ows_lsc2_st_cfg.layer_ls9",
                                            "type": "python",
                                        },
                                        {
                                            "include": "ows_refactored.surface_temperature.ows_lsc2_st_cfg.layer_ls8",
                                            "type": "python",
                                        },
                                        {
                                            "include": "ows_refactored.surface_temperature.ows_lsc2_st_cfg.layer_ls7",
                                            "type": "python",
                                        },
                                        {
                                            "include": "ows_refactored.surface_temperature.ows_lsc2_st_cfg.layer_ls5",
                                            "type": "python",
                                        },
                                    ],
                                },
                            ],
                        },
                        {
                            "title": "Radar backscatter",
                            "abstract": """Radar backscatter""",
                            "layers": [
                                {
                                    "title": "Daily radar backscatter",
                                    "abstract": """Daily radar backscatter""",
                                    "layers": [
                                        {
                                            "include": "ows_refactored.radar_backscatter.ows_sentinel1_cfg.layer",
                                            "type": "python",
                                        },
                                    ],
                                },
                                {
                                    "title": "Annual radar backscatter",
                                    "abstract": """Annual radar backscatter""",
                                    "layers": [
                                        {
                                            "include": "ows_refactored.radar_backscatter.ows_alos_cfg.layer",
                                            "type": "python",
                                        },
                                        {
                                            "include": "ows_refactored.radar_backscatter.ows_jers_cfg.layer",
                                            "type": "python",
                                        },
                                    ],
                                },
                            ],
                        },
                    ],
                },
                {
                    "title": "Surface water",
                    "abstract": """Surface water""",
                    "layers": [
                        {
                            "title": "Daily water",
                            "abstract": """Daily water""",
                            "layers": [
                                {
                                    "include": "ows_refactored.wofs.ows_wofs_ls_cfg.layer",
                                    "type": "python",
                                },
                            ],
                        },
                        {
                            "title": "Annual water",
                            "abstract": """Annual water""",
                            "layers": [
                                {
                                    "include": "ows_refactored.wofs.ows_wofs_ls_annual_cfg.layer",
                                    "type": "python",
                                }
                            ],
                        },
                        {
                            "title": "All-time water",
                            "abstract": """All-time water""",
                            "layers": [
                                {
                                    "include": "ows_refactored.wofs.ows_wofs_ls_alltime_cfg.layer",
                                    "type": "python",
                                }
                            ],
                        },
                    ],
                },
                {
                    "title": "Agriculture",
                    "abstract": """Agriculture""",
                    "layers": [
                        {
                            "include": "ows_refactored.agriculture.ows_crop_mask_cfg.layers",
                            "type": "python",
                        },
                    ],
                },
                {
                    "title": "Elevation and topography",
                    "abstract": """Digital elevation models and topographic indices""",
                    "layers": [
                        {
                            "include": "ows_refactored.elevation.ows_elevation_cfg.layer_srtm",
                            "type": "python",
                        },
                        {
                            "include": "ows_refactored.elevation.ows_elevation_cfg.layer_nasadem",
                            "type": "python",
                        },
                        {
                            "include": "ows_refactored.elevation.ows_elevation_cfg.layer_cop_30",
                            "type": "python",
                        },
                        {
                            "include": "ows_refactored.elevation.ows_srtm_deriv_cfg.layer_srtm_deriv",
                            "type": "python",
                        },
                    ],
                },
                {
                    "title": "Vegetation",
                    "abstract": """Vegetation""",
                    "layers": [
                        {
                            "title": "Daily vegetation",
                            "abstract": """Daily vegetation""",
                            "layers": [
                                {
                                    "include": "ows_refactored.vegetation.ows_fc_cfg.layer",
                                    "type": "python",
                                },
                            ],
                        },
                        {
                            "title": "Monthly vegetation",
                            "abstract": """Monthly vegetation""",
                            "layers": [
                                {
                                    "include": "ows_refactored.vegetation.ows_ndvi_anom_cfg.layer",
                                    "type": "python",
                                },
                            ],
                        },
                        {
                            "title": "Annual vegetation",
                            "abstract": """Annual vegetation""",
                            "layers": [
                                {
                                    "include": "ows_refactored.vegetation.ows_fc_summary_annual_cfg.layer",
                                    "type": "python",
                                },
                                {
                                    "include": "ows_refactored.vegetation.ows_gmw_cfg.layer",
                                    "type": "python",
                                },
                            ],
                        },
                        {
                            "title": "Vegetation climatology",
                            "abstract": """Vegetation climatology""",
                            "layers": [
                                {
                                    "include": "ows_refactored.vegetation.ows_ndvi_clim_cfg.layer",
                                    "type": "python",
                                },
                            ],
                        },
                    ],
                },
                {
                    "title": "Pixel count",
                    "abstract": """Pixel Count""",
                    "layers": [
                        {
                            "include": "ows_refactored.pixel_count.ows_pc_s2_annual_cfg.layer",
                            "type": "python",
                        },
                    ],
                },
                {
                    "title": "Land cover",
                    "abstract": """Land Cover""",
                    "layers": [
                        {
                            "title": "ESA datasets",
                            "abstract": """ESA datasets""",
                            "layers": [
                                {
                                    "include": "ows_refactored.land_cover.ows_cci_landcover_cfg.layer",
                                    "type": "python",
                                },
                                {
                                    "include": "ows_refactored.land_cover.ows_esa_worldcover_cfg_2020.layer",
                                    "type": "python",
                                },
                                {
                                    "include": "ows_refactored.land_cover.ows_esa_worldcover_cfg_2021.layer",
                                    "type": "python",
                                },
                            ],
                        },
                        {
                            "title": "World Settlement Footprint",
                            "abstract": """World Settlement Footprint and Evolution""",
                            "layers": [
                                {
                                    "include": "ows_refactored.land_cover.ows_wsf_cfg_2015.layer",
                                    "type": "python",
                                },
                                {
                                    "include": "ows_refactored.land_cover.ows_wsf_cfg_2019.layer",
                                    "type": "python",
                                },
                                {
                                    "include": "ows_refactored.land_cover.ows_wsf_evolution_cfg.layer",
                                    "type": "python",
                                },
                            ],
                        },
                        {
                            "include": "ows_refactored.land_cover.ows_io_lulc_cfg.layer",
                            "type": "python",
                        },
                    ],
                },
                {
                    "title": "Meteorology",
                    "abstract": """Meteorology""",
                    "layers": [
                        {
                            "include": "ows_refactored.meteorology.ows_rainfall.layer",
                            "type": "python",
                        }
                    ],
                },
            ],
        }
    ],
}
