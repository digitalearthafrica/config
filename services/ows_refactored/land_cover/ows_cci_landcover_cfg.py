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
            {"title": "no data", "abstract": "", "values": [0], "color": "#1e1e1f"},
            {
                "title": "Cropland, rainfed",
                "abstract": "",
                "values": [10],
                "color": "#f7fa48",
            },
            {
                "title": "Cropland, irrigated or post-flooding",
                "abstract": "",
                "values": [20],
                "color": "#99e3f7",
            },
            {
                "title": "Mosaic cropland/natural vegetation",
                "abstract": "",
                "values": [30],
                "color": "#c1e371",
            },
            {
                "title": "Mosaic natural vegetation/cropland",
                "abstract": "",
                "values": [40],
                "color": "#b9cc64",
            },
            {
                "title": "Tree cover, broadleaved, evergreen, closed to open",
                "abstract": "",
                "values": [50],
                "color": "#007a0e",
            },
            {
                "title": "Tree cover, broadleaved, deciduous, closed to open",
                "abstract": "",
                "values": [60],
                "color": "#148c22",
            },
            {
                "title": "Tree cover, needleleaved, evergreen, closed to open",
                "abstract": "",
                "values": [70],
                "color": "#0b3810",
            },
            {
                "title": "Tree cover, needleleaved, deciduous, closed to open",
                "abstract": "",
                "values": [80],
                "color": "##1a5c21",
            },
            {
                "title": "Tree cover, mixed leaf type",
                "abstract": "",
                "values": [90],
                "color": "#70660c",
            },
            {
                "title": "Mosaic tree and shrub/herbaceous cover",
                "abstract": "",
                "values": [100],
                "color": "#707d1b",
            },
            {
                "title": "Mosaic herbaceous cover/tree and shrub",
                "abstract": "",
                "values": [110],
                "color": "#a88220",
            },
            {
                "title": "Shrubland",
                "abstract": "",
                "values": [120],
                "color": "#a16312"},
            {
                "title": "Grassland",
                "abstract": "",
                "values": [130],
                "color": "#e08b1b"},
            {
                "title": "Lichens and mosses",
                "abstract": "",
                "values": [140],
                "color": "#e8bcdd",
            },
            {
                "title": "Sparse vegetation",
                "abstract": "",
                "values": [150],
                "color": "#f7e6a1",
            },
            {
                "title": "Tree cover, flooded, fresh or brakish water",
                "abstract": "",
                "values": [160],
                "color": "#1d7837",
            },
            {
                "title": "Tree cover, flooded, saline water",
                "abstract": "",
                "values": [170],
                "color": "#44bd86",
            },
            {
                "title": "Shrub or herbaceous cover, flooded, fresh/saline/brakish water",
                "abstract": "",
                "values": [180],
                "color": "#66dea8",
            },
            {
                "title": "Urban areas",
                "abstract": "",
                "values": [190],
                "color": "#b31010"
            },
            {
                "title": "Bare areas",
                "abstract": "",
                "values": [200],
                "color": "#d9d4d4"
            },
            {
                "title": "Water bodies",
                "abstract": "",
                "values": [210],
                "color": "#3330e6"
            },
            {
                "title": "Permanent snow and ice",
                "abstract": "",
                "values": [220],
                "color": "#ffffff",
            },
        ]
    },
    "legend": {"width": 3.0, "height": 4.0},
}

layer = {
    "title": "ESA CCI Landcover",
    "name": "cci_landcover",
    "abstract": """
As part of the ESA Climate Change Initiative (CCI), the Land Cover project is concerned with the generation of the land cover ECV. Land cover is defined as the physical material at the surface of the earth. Land covers include grass, asphalt, trees, bare ground, water, etc.

The project's objective is to critically revisit all algorithms required for the generation of a global land product in the light of GCOS requirements, and to design and demonstrate a prototype system delivering in a consistent way over years and from various EO instruments global land cover information matching the needs of key users' belonging to the climate change community. The focus is placed on the ESA and Member States missions providing near daily global surface reflectance observation at moderate spatial resolution (MERIS FR & RR, SPOT VEGETATION) but the contribution of ESA SAR sensors will also be investigated to tackle specific land cover discrimination issue.

For more information, see https://climate.esa.int/en/projects/land-cover/about/
""",
    "product_name": "cci_landcover",
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
        0.0027777777777777783,
        -0.0027777777777777783,
    ],
    "styling": {
        "default_style": "style_colours",
        "styles": [style_colours],
    },
}
