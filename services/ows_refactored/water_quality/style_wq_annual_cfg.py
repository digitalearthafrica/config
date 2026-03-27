"""
Water Quality Style Configuration for Digital Earth Africa OWS
================================================================

Style definitions for water quality parameters
Organized by parameter and sensor/source type.

"""
from ows_refactored.common.ows_legend_cfg import legend_mean_ndvi_ticks

# ============================================================================
# TOTAL SUSPENDED MATTER (TSM) STYLES
# ============================================================================
legend_tsm = {
    "show_legend": True,
    "title": "TSM(Index)",
    "begin": "0.0",
    "end": "500.0",
    "decimal_places": 0,
    "ticks_every": "100",
    "width": 5.5,
    "height": 2.1,
    "strip_location": [0.1, 0.4, 0.8, 0.2],
}

style_wq_annual_tsm = {
    "name": "wq_annual_tsm",
    "title": "TSM (Index)",
    "abstract": "Total suspended matter concentration (mg/L)",
    "legend": legend_tsm,
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "tsm"},
    },
    "needed_bands": ["tsm"],
    "include_in_feature_info": True,
    "color_ramp": [
        {"value": 0.0, "color": "#000004"},
        {"value": 10.0, "color": "#1b0c41"},
        {"value": 25.0, "color": "#3b0f70"},
        {"value": 50.0, "color": "#5c126e"},
        {"value": 75.0, "color": "#7a1f6a"},
        {"value": 100.0, "color": "#9a2a63"},
        {"value": 125.0, "color": "#ba3655"},
        {"value": 150.0, "color": "#d44842"},
        {"value": 175.0, "color": "#e8602d"},
        {"value": 200.0, "color": "#f57d15"},
        {"value": 225.0, "color": "#fca50a"},
        {"value": 250.0, "color": "#f6c141"},
        {"value": 275.0, "color": "#f1db6d"},
        {"value": 300.0, "color": "#fcf3a1"},
        {"value": 400.0, "color": "#fcfdbf"},
    ],
}

# ============================================================================
# TROPHIC STATE INDEX (TSI) STYLES
# ============================================================================
legend_tsi = {
    "show_legend": True,
    "title": "Trophic State Index",
    "units": "Index",
    "begin": "0.0",
    "end": "100.0",
    "decimal_places": 0,
    "ticks_every": "10",
    "width": 5.5,
    "height": 2.1,
    "strip_location": [0.1, 0.4, 0.8, 0.2],
}

style_wq_annual_tsi = {
    "name": "wq_annual_tsi",
    "title": "Trophic State Index",
    "abstract": "Biological productivity in surface water bodies",
    "legend": legend_tsi,
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "tsi"},
    },
    "needed_bands": ["tsi"],
    "include_in_feature_info": True,
    "color_ramp": [
        {"value": 0.0, "color": "#3f007d"},
        {"value": 10.0, "color": "#1a6faf"},
        {"value": 20.0, "color": "#1b9e77"},
        {"value": 30.0, "color": "#41ab5d"},
        {"value": 40.0, "color": "#78c679"},
        {"value": 50.0, "color": "#c8a800"},
        {"value": 60.0, "color": "#e07b00"},
        {"value": 70.0, "color": "#d94701"},
        {"value": 75.0, "color": "#c41a14"},
        {"value": 80.0, "color": "#a50026"},
        {"value": 90.0, "color": "#67001f"},
        {"value": 100.0, "color": "#40000f"},
        {"value": 110.0, "color": "#2a0009"},
    ],
}

# ============================================================================
# NDVI STYLES
# ============================================================================
color_ramp_ndvi = [
    {"value": 0.0, "color": "#a50026"},
    {"value": 0.1, "color": "#d73027"},
    {"value": 0.2, "color": "#f46d43"},
    {"value": 0.3, "color": "#fdae61"},
    {"value": 0.4, "color": "#fee090"},
    {"value": 0.5, "color": "#ffffbf"},
    {"value": 0.6, "color": "#d9ef8b"},
    {"value": 0.7, "color": "#a6d96a"},
    {"value": 0.8, "color": "#66bd63"},
    {"value": 0.9, "color": "#1a9850"},
    {"value": 1.0, "color": "#006837"},
]

style_wq_annual_ndvi = {
    "name": "wq_annual_ndvi",
    "title": "Normalised Difference Vegeation Index (NDVI)",
    "abstract": "Presence of vegetation in surface water bodies",
    "legend": legend_mean_ndvi_ticks,
    "needed_bands": ["agm_ndvi"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "agm_ndvi"},
    },
    "color_ramp": color_ramp_ndvi,
}

# ============================================================================
# FAI STYLES
# ============================================================================

color_ramp_fai = [
    {"value": 0.05, "color": "#6baed6"},
    {"value": 0.1, "color": "#c7e9c0"},
    {"value": 0.2, "color": "#a1d99b"},
    {"value": 0.3, "color": "#fddd6a"},
    {"value": 0.4, "color": "#fd8d3c"},
    {"value": 0.5, "color": "#e31a1c"},
    {"value": 0.7, "color": "#800026"},
    {"value": 1.0, "color": "#3d0012"},
]

legend_fai = {
    "show_legend": True,
    "title": "Floating Algal Index",
    "units": "Index",
    "begin": "-0.05",
    "end": "1.0",
    "decimal_places": 2,
    "ticks_every": "0.1",
    "width": 5.5,
    "height": 2.1,
    "strip_location": [0.1, 0.4, 0.8, 0.2],
}

style_wq_annual_fai = {
    "name": "wq_annual_fai",
    "title": "Floating Algal Index (FAI)",
    "abstract": (
        "Presence and density of floating algal blooms in surface water bodies, "
        "derived from the Floating Algal Index. Negative values indicate open water; "
        "positive values indicate increasing algal or aquatic vegetation cover."
    ),
    "legend": legend_fai,
    "needed_bands": ["agm_fai"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "agm_fai"},
    },
    "include_in_feature_info": True,
    "color_ramp": color_ramp_fai,
}

# ============================================================================
# HUE STYLES
# ============================================================================
color_ramp_hue = [
    {"value": 0, "color": "#ff0000"},
    {"value": 30, "color": "#ff8000"},
    {"value": 60, "color": "#ffff00"},
    {"value": 90, "color": "#80ff00"},
    {"value": 120, "color": "#00ff00"},
    {"value": 150, "color": "#00ff80"},
    {"value": 180, "color": "#00ffff"},
    {"value": 210, "color": "#0080ff"},
    {"value": 240, "color": "#0000ff"},
    {"value": 270, "color": "#8000ff"},
    {"value": 300, "color": "#ff00ff"},
    {"value": 330, "color": "#ff0080"},
    {"value": 360, "color": "#ff0000"},
]

legend_hue = {
    "show_legend": True,
    "title": "Hue Angle",
    "units": "degrees",
    "begin": "0",
    "end": "360",
    "decimal_places": 0,
    "ticks_every": "30",
    "width": 4.5,
    "height": 2.1,
    "strip_location": [0.1, 0.4, 0.8, 0.2],
}

style_wq_annual_hue = {
    "name": "wq_annual_hue",
    "title": "Surface Water Body Colour (Hue Angle)",
    "abstract": "Surface water body colour",
    "legend": legend_hue,
    "needed_bands": ["agm_hue"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "agm_hue"},
    },
    "color_ramp": color_ramp_hue,
}

# ============================================================================
# OWT STYLES
# ============================================================================

legend_owt = {
    "type": "categorical",
    "items": [
        {"value": 1, "label": "OWT1 – Hypereutrophic, cyanobacterial scum"},
        {"value": 2, "label": "OWT2 – Common case waters"},
        {"value": 3, "label": "OWT3 – Clear waters"},
        {"value": 4, "label": "OWT4 – Turbid, organic-rich"},
        {"value": 5, "label": "OWT5 – Sediment-laden"},
        {"value": 6, "label": "OWT6 – Balanced optical constituents"},
        {"value": 7, "label": "OWT7 – Highly productive, cyanobacteria"},
        {"value": 8, "label": "OWT8 – Productive, cyano, Rrs peak ~700 nm"},
        {"value": 9, "label": "OWT9 – OWT2-like, high shortwave Rrs"},
        {"value": 10, "label": "OWT10 – CDOM-rich"},
        {"value": 11, "label": "OWT11 – CDOM + cyanobacteria + NAP"},
        {"value": 12, "label": "OWT12 – Turbid, moderately productive"},
        {"value": 13, "label": "OWT13 – Very clear blue waters"},
    ],
}

style_wq_annual_owt = {
    "name": "wq_annual_owt",
    "title": "Optical Water Types (OWT)",
    "abstract": (
        "Optical Water Types classification for inland waters following "
        "Spyrakos et al. (2018), based on dominant optical and biogeochemical properties."
    ),
    "legend": legend_owt,
    "needed_bands": ["agm_owt"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "agm_owt"},
    },
    "include_in_feature_info": True,
    "value_map": {                          # replaces color_ramp entirely
        "agm_owt": [
            {"title": "OWT1 – Hypereutrophic, cyanobacterial scum", "values": [1], "color": "#7a0177"},
            {"title": "OWT2 – Common case waters", "values": [2], "color": "#41b6c4"},
            {"title": "OWT3 – Clear waters", "values": [3], "color": "#2c7bb6"},
            {"title": "OWT4 – Turbid, organic-rich", "values": [4], "color": "#1a9850"},
            {"title": "OWT5 – Sediment-laden", "values": [5], "color": "#a6611a"},
            {"title": "OWT6 – Balanced optical constituents", "values": [6], "color": "#66c2a5"},
            {"title": "OWT7 – Highly productive, cyanobacteria", "values": [7], "color": "#d73027"},
            {"title": "OWT8 – Productive, cyano, Rrs peak ~700 nm", "values": [8], "color": "#fdae61"},
            {"title": "OWT9 – OWT2-like, high shortwave Rrs", "values": [9], "color": "#74add1"},
            {"title": "OWT10 – CDOM-rich", "values": [10], "color": "#542788"},
            {"title": "OWT11 – CDOM + cyanobacteria + NAP", "values": [11], "color": "#2d004b"},
            {"title": "OWT12 – Turbid, moderately productive", "values": [12], "color": "#fee08b"},
            {"title": "OWT13 – Very clear blue waters", "values": [13], "color": "#081d58"},
        ]
    },
}

# ============================================================================
# CHLA STYLES
# ============================================================================
color_ramp_chla = [
    {"value": 0.1, "color": "#081d58"},
    {"value": 0.5, "color": "#253494"},
    {"value": 1.0, "color": "#225ea8"},
    {"value": 2.0, "color": "#1d91c0"},
    {"value": 5.0, "color": "#41b6c4"},
    {"value": 10.0, "color": "#7fcdbb"},
    {"value": 20.0, "color": "#c7e9b4"},
    {"value": 40.0, "color": "#ffffcc"},
    {"value": 60.0, "color": "#fed976"},
    {"value": 100.0, "color": "#feb24c"},
    {"value": 150.0, "color": "#fd8d3c"},
    {"value": 200.0, "color": "#f03b20"},
    {"value": 300.0, "color": "#560b1a"},
]

legend_chla = {
    "show_legend": True,
    "title": "Chl-A (Index)",
    "begin": "0.1",
    "end": "300",
    "scale": "log",
    "ticks": [0.1, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 300],
    "decimal_places": 1,
    "width": 5.5,
    "height": 2.1,
    "strip_location": [0.1, 0.4, 0.8, 0.2],
}

style_wq_annual_chla = {
    "name": "wq_annual_chla",
    "title": "Chl-A (Index)",
    "abstract": (
        "Chlorophyll-a concentration (mg/m³) as an indicator of phytoplankton "
        "biomass and water productivity."
    ),
    "legend": legend_chla,
    "needed_bands": ["chla"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "chla"},
    },
    "include_in_feature_info": True,
    "color_ramp": color_ramp_chla,
}

# ============================================================================
# TIRS STYLES
# ============================================================================
color_ramp_tirs = [
    {"value": -5.0, "color": "#313695"},
    {"value": 0.0, "color": "#4575b4"},
    {"value": 5.0, "color": "#74add1"},
    {"value": 10.0, "color": "#abd9e9"},
    {"value": 15.0, "color": "#e0f3f8"},
    {"value": 20.0, "color": "#ffffbf"},
    {"value": 25.0, "color": "#fee090"},
    {"value": 30.0, "color": "#fdae61"},
    {"value": 35.0, "color": "#f46d43"},
    {"value": 40.0, "color": "#d73027"},
]

legend_tirs = {
    "show_legend": True,
    "title": "Surface Water Temperature",
    "begin": "-5",
    "end": "40",
    "ticks_every": "5",
    "units": " Deg C",
    "decimal_places": 0,
    "width": 4.5,
    "height": 2.1,
    "strip_location": [0.1, 0.4, 0.8, 0.2],
}

style_wq_annual_tirs_max = {
    "name": "wq_annual_tirs_max",
    "title": "Water Temperature - Annual Maximum",
    "abstract": "Annual maximum surface water temperature",
    "legend": legend_tirs,
    "needed_bands": ["tirs_st_ann_max"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "tirs_st_ann_max"},
    },
    "include_in_feature_info": True,
    "color_ramp": color_ramp_tirs,
}

style_wq_annual_tirs_med = {
    "name": "wq_annual_tirs_med",
    "title": "Water Temperature - Annual Median",
    "abstract": "Annual median surface water temperature",
    "legend": legend_tirs,
    "needed_bands": ["tirs_st_ann_med"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "tirs_st_ann_med"},
    },
    "include_in_feature_info": True,
    "color_ramp": color_ramp_tirs,
}

style_wq_annual_tirs_min = {
    "name": "wq_annual_tirs_min",
    "title": "Water Temperature - Annual Minimum",
    "abstract": "Annual minimum surface water temperature",
    "legend": legend_tirs,
    "needed_bands": ["tirs_st_ann_min"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "tirs_st_ann_min"},
    },
    "include_in_feature_info": True,
    "color_ramp": color_ramp_tirs,
}
# ============================================================================
# WATER MASK STYLES
# ============================================================================
color_ramp_mask = [
    {"value": 0.0, "color": "#000000", "alpha": 0.0},
    {"value": 1.0, "color": "#4393c3"},
]

legend_water_mask = {
    "show_legend": True,
    "title": "Water Mask",
    "begin": "0.0",
    "end": "1.0",
    "ticks_every": "1.0",
    "decimal_places": 0,
    "width": 4.5,
    "height": 2.1,
    "strip_location": [0.1, 0.4, 0.8, 0.2],
}

style_wq_annual_water_mask = {
    "name": "wq_annual_water_mask",
    "title": "Water Mask",
    "abstract": "Binary water presence mask derived from WOfS",
    "legend": legend_water_mask,
    "needed_bands": ["water_mask"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "water_mask"},
    },
    "include_in_feature_info": True,
    "color_ramp": color_ramp_mask,
}

# ============================================================================
# CLEAR WATER STYLES
# ============================================================================
color_ramp_clear_water = [
    {"value": 0.0, "color": "#000000", "alpha": 0.0},
    {"value": 1.0, "color": "#4393c3"},
]

legend_clear_water = {
    "show_legend": True,
    "title": "Clear Water Mask",
    "begin": "0.0",
    "end": "1.0",
    "ticks_every": "1.0",
    "decimal_places": 0,
    "width": 4.5,
    "height": 2.1,
    "strip_location": [0.1, 0.4, 0.8, 0.2],
}

style_wq_annual_clear_water = {
    "name": "wq_annual_clear_water",
    "title": "Clear Water",
    "abstract": "Observations classified as clear (non-turbid) water",
    "legend": legend_clear_water,
    "needed_bands": ["clear_water"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "clear_water"},
    },
    "include_in_feature_info": True,
    "color_ramp": color_ramp_clear_water,
}
