from ows_refactored.common.ows_reslim_cfg import reslim_wms_min_zoom_15


legend_idx_0_100_pixel_fc_25ticks = {
    "begin": 0,
    "end": 100,
    "units": "% / pixel",
    "ticks_every": 25,
    "title": "Percentage of Pixel that is Green Vegetation",
    "rcParams": {"font.size": 9},
}

legend_idx_0_100_pixel_fc_ngv_25ticks = {
    "begin": 0,
    "end": 100,
    "units": "% / pixel",
    "ticks_every": 25,
    "title": "Percentage of Pixel that is Green Vegetation",
    "rcParams": {"font.size": 9},
}

legend_idx_0_100_pixel_fc_bs_25ticks = {
    "begin": 0,
    "end": 100,
    "ticks_every": 25,
    "units": "% / pixel",
    "title": "Percentage of Pixel that is Bare Soil",
    "rcParams": {"font.size": 9},
}


# fc_percentile_flags = [
#     {
#         "band": "land",
#         "product": "geodata_coast_100k",
#         "ignore_time": True,
#         "ignore_info_flags": [],
#     },
# ]

bands_fc_percentile = {
    "pv_pc_10": [],
    "pv_pc_50": [],
    "pv_pc_90": [],
    "npv_pc_10": [],
    "npv_pc_50": [],
    "npv_pc_90": [],
    "bs_pc_10": [],
    "bs_pc_50": [],
    "bs_pc_90": [],
    "count_valid": [],
}


green_veg_10 = {
    "name": "green_veg_10",
    "title": "Green Veg, 10th Percentile",
    "abstract": "10th Percentile of Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "pv_pc_10",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["pv_pc_10"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#ffffcc",
        },
        {
            "value": 25,
            "color": "#c2e699",
        },
        {
            "value": 50,
            "color": "#78c679",
        },
        {
            "value": 75,
            "color": "#31a354",
        },
        {
            "value": 100,
            "color": "#006837",
        },
    ],
    # "pq_masks": fc_pq_mask,
    "legend": legend_idx_0_100_pixel_fc_25ticks,
}

green_veg_50 = {
    "name": "green_veg_50",
    "title": "Green Veg, 50th Percentile",
    "abstract": "50th Percentile of Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "pv_pc_50",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["pv_pc_50"],
    "color_ramp": [
        {"value": 0, "color": "#ffffcc"},
        {"value": 25, "color": "#c2e699"},
        {"value": 50, "color": "#78c679"},
        {"value": 75, "color": "#31a354"},
        {"value": 100, "color": "#006837"},
    ],
    # old behaviour was wrong.  This is what Leo and Emma requested
    "legend": legend_idx_0_100_pixel_fc_25ticks,
    # "pq_masks": fc_pq_mask,
}

green_veg_90 = {
    "name": "green_veg_90",
    "title": "Green Veg, 90th Percentile",
    "abstract": "90th Percentile of Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "pv_pc_90",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["pv_pc_90"],
    "color_ramp": [
        {"value": 0, "color": "#ffffcc"},
        {"value": 25, "color": "#c2e699"},
        {"value": 50, "color": "#78c679"},
        {"value": 75, "color": "#31a354"},
        {"value": 100, "color": "#006837"},
    ],
    # old behaviour was wrong.  This is what Leo and Emma requested
    "legend": legend_idx_0_100_pixel_fc_25ticks,
    # "pq_masks": fc_pq_mask,
}

non_green_veg_10 = {
    "name": "non_green_veg_10",
    "title": "Non-green Veg, 10th Percentile",
    "abstract": "10th Percentile of Non Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "npv_pc_10",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["npv_pc_10"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#ffffd4",
        },
        {"value": 25, "color": "#fed98e"},
        {
            "value": 50,
            "color": "#fe9929",
        },
        {
            "value": 75,
            "color": "#d95f0e",
        },
        {
            "value": 100,
            "color": "#993404",
        },
    ],
    # Emulates what we had previously
    "legend": legend_idx_0_100_pixel_fc_ngv_25ticks,
    # "pq_masks": fc_pq_mask,
}

non_green_veg_50 = {
    "name": "non_green_veg_50",
    "title": "Non-Green Veg, 50th Percentile",
    "abstract": "50th Percentile of Non Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "npv_pc_50",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["npv_pc_50"],
    "color_ramp": [
        {"value": 0, "color": "#ffffd4"},
        {"value": 25, "color": "#fed98e"},
        {"value": 50, "color": "#fe9929"},
        {"value": 75, "color": "#d95f0e"},
        {"value": 100, "color": "#993404"},
    ],
    # old behaviour was wrong.  This is what Leo and Emma requested
    "legend": legend_idx_0_100_pixel_fc_ngv_25ticks,
    # "pq_masks": fc_pq_mask,
}

non_green_veg_90 = {
    "name": "non_green_veg_90",
    "title": "Non-Green Veg, 90th Percentile",
    "abstract": "90th Percentile of Non Green Vegetation",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "npv_pc_90",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["npv_pc_90"],
    "color_ramp": [
        {"value": 0, "color": "#ffffd4"},
        {"value": 25, "color": "#fed98e"},
        {"value": 50, "color": "#fe9929"},
        {"value": 75, "color": "#d95f0e"},
        {"value": 100, "color": "#993404"},
    ],
    # old behaviour was wrong.  This is what Leo and Emma requested
    "legend": legend_idx_0_100_pixel_fc_ngv_25ticks,
    # "pq_masks": fc_pq_mask,
}

bare_ground_10 = {
    "name": "bare_ground_10",
    "title": "Bare Ground, 10th Percentile",
    "abstract": "10th Percentile of Bare Soil",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "bs_pc_10",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["bs_pc_10"],
    "color_ramp": [
        {
            "value": 0,
            "color": "#feebe2",
        },
        {
            "value": 25,
            "color": "#fbb4b9",
        },
        {
            "value": 50,
            "color": "#f768a1",
        },
        {
            "value": 75,
            "color": "#c51b8a",
        },
        {
            "value": 100,
            "color": "#7a0177",
        },
    ],
    # "pq_masks": fc_pq_mask,
    # Emulates what we had previously
    "legend": legend_idx_0_100_pixel_fc_bs_25ticks,
}

bare_ground_50 = {
    "name": "bare_ground_50",
    "title": "Bare Ground, 50th Percentile",
    "abstract": "50th Percentile of Bare Soil",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "bs_pc_50",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["bs_pc_50"],
    "color_ramp": [
        {"value": 0, "color": "#feebe2"},
        {"value": 25, "color": "#fbb4b9"},
        {"value": 50, "color": "#f768a1"},
        {"value": 75, "color": "#c51b8a"},
        {"value": 100, "color": "#7a0177"},
    ],
    # Old behaviour was wrong - this is what Leo and Emma have requested.
    "legend": legend_idx_0_100_pixel_fc_bs_25ticks,
    # "pq_masks": fc_pq_mask,
}

bare_ground_90 = {
    "name": "bare_ground_90",
    "title": "Bare Ground, 90th Percentile",
    "abstract": "90th Percentile of Bare Soil",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "bs_pc_90",
        },
    },
    "include_in_feature_info": False,
    "needed_bands": ["bs_pc_90"],
    "color_ramp": [
        {"value": 0, "color": "#feebe2"},
        {"value": 25, "color": "#fbb4b9"},
        {"value": 50, "color": "#f768a1"},
        {"value": 75, "color": "#c51b8a"},
        {"value": 100, "color": "#7a0177"},
    ],
    # Old behaviour was wrong - this is what Leo and Emma have requested.
    "legend": legend_idx_0_100_pixel_fc_bs_25ticks,
    # "pq_masks": fc_pq_mask,
}

fc_rgb = {
    "name": "fc_rgb",
    "title": "Three-band Fractional Cover 50th Percentile",
    "abstract": "Fractional cover medians - red is bare soil, green is green vegetation and blue is non-green vegetation",
    "components": {
        "red": {"bs_pc_50": 1.0},
        "green": {"pv_pc_50": 1.0},
        "blue": {"npv_pc_50": 1.0},
    },
    "scale_range": [0.0, 100.0],
    # "pq_masks": fc_pq_mask,
    "legend": {
        "show_legend": True,
        "url": "https://data.dea.ga.gov.au/fractional-cover/FC_legend.png",
    },
}

fc_percentiles_styles = [
    fc_rgb,
    green_veg_10,
    green_veg_50,
    green_veg_90,
    non_green_veg_10,
    non_green_veg_50,
    non_green_veg_90,
    bare_ground_10,
    bare_ground_50,
    bare_ground_90,
]

layer = {
    "title": "Fractional Cover annual summary",
    "name": "fc_ls_summary_annual",
    "abstract": """
Fractional cover provides information about the the proportions of green vegetation, non-green vegetation (including deciduous trees during autumn, dry grass, etc.), and bare areas for every 30 m x 30 m ground footprint. Fractional cover provides insight into how areas of dry vegetation and/or bare soil and green vegetation are changing over time. The percentile summaries are designed to make it easier to analyse and interpret fractional cover. Percentiles provide an indicator of where an observation sits, relative to the rest of the observations for the pixel. For example, the 90th percentile is the value below which 90% of the observations fall. The fractional cover algorithm was developed by the Joint Remote Sensing Research Program.

This product contains the 10th, 50th, and 90th percentiles estimated independently for the green vegetation, non-green vegetation, and bare fractions observed in each calendar year (1st of January - 31st December) from 1984 to the most recent full calendar year.

Fractional Cover products use Water Observations from Space (WOfS) to mask out areas of water, cloud and other phenomena. To be considered in the FCP product a pixel must have had at least 10 clear observations over the year.
""",
    "product_name": "fc_ls_summary_annual",
    "time_resolution": "year",
    "bands": bands_fc_percentile,
    "resource_limits": reslim_wms_min_zoom_15,
    # "flags": fc_percentile_flags,
    "native_crs": "EPSG:6933",
    "native_resolution": [30, -30],
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "styling": {
        "default_style": "fc_rgb",
        "styles": fc_percentiles_styles,
    },
}
