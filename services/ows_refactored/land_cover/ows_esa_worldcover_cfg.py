from ows_refactored.common.ows_reslim_cfg import reslim_land_cover

style_colours = {
    "name": "style_colours",
    "title": "Coloured",
    "abstract": "Land cover colours",
    "needed_bands": ["classification"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "classification",
        },
    },
    "value_map": {
        "classification": [
            {
                "title": "",
                "abstract": "",
                "values": [0],
                "alpha": 0.0,
                "color": "#707070",
            },
            {
                "title": "Tree cover",
                "abstract": "",
                "values": [10],
                "color": "#006400",
            },
            {
                "title": "Shrubland",
                "abstract": "",
                "values": [20],
                "color": "#ffbd22",
            },
            {
                "title": "Grassland",
                "abstract": "",
                "values": [30],
                "color": "#ffff4c",
            },
            {
                "title": "Cropland",
                "abstract": "",
                "values": [40],
                "color": "#ef96ff",
            },
            {
                "title": "Built-up",
                "abstract": "",
                "values": [50],
                "color": "#fa0000",
            },
            {
                "title": "Bare/sparse vegetation",
                "abstract": "",
                "values": [60],
                "color": "#b4b4b4",
            },
            {
                "title": "Snow and ice",
                "abstract": "",
                "values": [70],
                "color": "#f0f0f0",
            },
            {
                "title": "Permanent water bodies",
                "abstract": "",
                "values": [80],
                "color": "#0064c8",
            },
            {
                "title": "Herbaceous wetland",
                "abstract": "",
                "values": [90],
                "color": "#0095a0",
            },
            {
                "title": "Mangroves",
                "abstract": "",
                "values": [95],
                "color": "#00cf75",
            },
            {
                "title": "Moss and lichen",
                "abstract": "",
                "values": [100],
                "color": "#fae6a0",
            },
        ]
    },
    "legend": {"width": 3.0, "height": 4.0},
}

layer = {
    "title": "ESA Worldcover",
    "name": "esa_worldcover",
    "abstract": """
The ESA WorldCover global land cover product builds further on the GlobCover and CCI Land Cover
experiences from the European Space Agency (Arino et al. 2008; ESA 2017).

The algorithm used to generate the ESA WorldCover product is based on the algorithm to produce the dynamic yearly
Copernicus Global Land Service Land Cover (CGLS-LC) map at 100 m resolution (Buchhorn et al.,
2020a). The CGLS-LC workflow uses 100 m, 5-day, Proba-V data as an input which were re-processed
to the Sentinel-2 UTM grid together with training data obtained at 10 m resolution.

For the generation of the WorldCover product however both Sentinel-2 multi-spectral image data and Sentinel-1 C-band
Synthetic Aperture Radar (SAR) data are used instead of Proba-V data.

For more information, see https://esa-worldcover.s3.amazonaws.com/v100/2020/docs/WorldCover_PUM_V1.0.pdf
""",
    "product_name": "esa_worldcover",
    "time_resolution": "year",
    "bands": {
        "classification": [],
    },
    "resource_limits": reslim_land_cover,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [
        0.000083333333333,
        -0.000083333333333,
    ],
    "styling": {
        "default_style": "style_colours",
        "styles": [style_colours],
    },
}
