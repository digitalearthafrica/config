# Sentinel-1 ows styles

style_s1_vv = {
    "name": "vv",
    "title": "VV",
    "abstract": "VV band",
    "additional_bands": [],
    "components": {
        "red": {"vv": 1.0, "scale_range": [0.0, 0.28]},
        "green": {"vv": 1.0, "scale_range": [0.0, 0.28]},
        "blue": {"vv": 1.0, "scale_range": [0.0, 0.28]},
    },
    "pq_masks": [
        {
            "band": "mask",
            "values": [1],
        },
    ],
}

style_s1_vh = {
    "name": "vh",
    "title": "VH",
    "abstract": "VH band",
    "additional_bands": [],
    "components": {
        "red": {"vh": 1.0, "scale_range": [0.0, 0.06]},
        "green": {"vh": 1.0, "scale_range": [0.0, 0.06]},
        "blue": {"vh": 1.0, "scale_range": [0.0, 0.06]},
    },
    "pq_masks": [
        {
            "band": "mask",
            "values": [1],
        },
    ],
}

style_s1_vh_over_vv = {
    "name": "vv_vh_vh_over_vv",
    "title": "VV, VH and VH/VV",
    "abstract": "False colour representation of VV, VH and VH/VV for R, G and B respectively",
    "additional_bands": [],
    "components": {
        "red": {"vv": 1.0, "scale_range": [0.0, 0.28]},
        "green": {"vh": 1.0, "scale_range": [0.0, 0.06]},
        "blue": {
            "function": "datacube_ows.band_utils.band_quotient",
            "mapped_bands": True,
            "kwargs": {"band1": "vh", "band2": "vv", "scale_from": [0.0, 0.49]},
        },
    },
    "pq_masks": [
        {
            "band": "mask",
            "values": [1],
        },
    ],
}

style_s1_rvi = {
    "name": "rvi",
    "title": "Radar Vegetation Index",
    "abstract": "Dual-pol radar vegetation index for Sentinel-1",
    "index_expression": "4*vh/(vv + vh)",
    "mpl_ramp": "YlGnBu_r",
    "range": [0.0, 1.0],
    "legend": {
        "begin": "0.0",
        "end": "1.0",
        "decimal_places": 1,
        "ticks": ["0.0", "0.2", "0.4", "0.6", "0.8", "1.0"],
    },
    "pq_masks": [
        {
            "band": "mask",
            "values": [1],
        },
    ],
}

styles_s1_list = [
    style_s1_vh_over_vv,
    style_s1_vv,
    style_s1_vh,
    style_s1_rvi
]
