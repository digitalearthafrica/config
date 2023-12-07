from ows_refactored.common.ows_reslim_cfg import reslim_land_cover

style_wsf_evolution = {
    "name": "wsf_evolution",
    "title": "World Settlement Footprint Evolution",
    "abstract": "World Settlement Footprint Evolution colours",
    "needed_bands": ["wsfevolution"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "wsfevolution",
        },
    },
    "color_ramp": [
        {"value": -0, "color": "#000000"},
        {"value": 1985, "color": "#f6bb97"},
        {"value": 1990, "color": "#f4865e"},
        {"value": 1995, "color": "#ec4a3e"},
        {"value": 2000, "color": "#ca1a50"},
        {"value": 2005, "color": "#951c5b"},
        {"value": 2010, "color": "#601f52"},
        {"value": 2015, "color": "#2e1739"},
    ],
    "legend": {
        "title": "Year",
        "begin": "1985",
        "end": "2015",
        "ticks_every": 5,
    },
}

style_wsf_idc = {
    "name": "wsf_evolution_idc",
    "title": "IDC Score",
    "abstract": "World Settlement Footprint Evolution IDC colours",
    "needed_bands": ["idc_score"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "idc_score",
        },
    },
    "color_ramp": [
        {"value": -0, "color": "#000000"},
        {"value": 1, "color": "#db5f57"},
        {"value": 2, "color": "#d3db57"},
        {"value": 3, "color": "#57db5f"},
        {"value": 4, "color": "#57d3db"},
        {"value": 5, "color": "#5f57db"},
        {"value": 6, "color": "#db57d3"},
    ],
    "legend": {
        "title": "IDC Score",
        "begin": "1",
        "end": "6",
        "ticks_every": 1,
    },
}

layer = {
    "title": "World Settlement Footprint Evolution",
    "name": "wsf_evolution",
    "abstract": """
The World Settlement Footprint (WSF) Evolution is a 30m resolution dataset derived from Landsat-5/7 outlining the global settlement extent on a yearly basis from 1985 to 2015.

For more information, see https://austriaca.at/?arp=0x003c9b4c.
""",
    "product_name": "wsf_evolution",
    "time_resolution": "summary",
    "bands": {"wsfevolution": [], "idc_score": []},
    "resource_limits": reslim_land_cover,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [0.00026949458523585647, -0.00026949458523585647],
    "styling": {
        "default_style": "wsf_evolution",
        "styles": [style_wsf_evolution, style_wsf_idc],
    },
}
