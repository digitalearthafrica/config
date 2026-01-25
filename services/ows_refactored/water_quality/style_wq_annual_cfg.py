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
    "title": "Total Suspended Matter",
    "units": "mg/L",
    "begin": "0.0",
    "end": "500.0",
    "decimal_places": 1,
    "ticks_every": "100",
    "width": 4.5,
    "height": 2.1,
    "strip_location": [0.1, 0.4, 0.8, 0.2],
}

style_wq_annual_tsm = {
    "name": "wq_annual_tsm",
    "title": "Total Suspended Matter",
    "abstract": "Total suspended matter concentration (mg/L)",
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "tsm"},
    },
    "needed_bands": ["tsm"],
    "include_in_feature_info": True,
    "color_ramp": [
        {"value": 0.0, "color": "#000004", "alpha":0.3},
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
    "units": "unitless",
    "begin": "0.0",
    "end": "100.0",
    "decimal_places": 1,
    "ticks_every": "5",
    "width": 4.5,
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
        {"value": 0.0, "color": "#5e4fa2"},    # 0 - Purple (oligotrophic)
        {"value": 10.0, "color": "#3288bd"},   # 10 - Blue
        {"value": 20.0, "color": "#66c2a5"},   # 20 - Cyan
        {"value": 30.0, "color": "#abdda4"},   # 30 - Light cyan-green
        {"value": 40.0, "color": "#e6f598"},   # 40 - Pale green-yellow (mesotrophic)
        {"value": 50.0, "color": "#ffffbf"},   # 50 - Pale yellow
        {"value": 60.0, "color": "#fee08b"},   # 60 - Light yellow
        {"value": 70.0, "color": "#fdae61"},   # 70 - Orange-yellow (eutrophic)
        {"value": 75.0, "color": "#f46d43"},   # 75 - Orange
        {"value": 80.0, "color": "#d53e4f"},   # 80 - Red-orange
        {"value": 90.0, "color": "#9e0142"},   # 90 - Dark red (hypereutrophic)
        {"value": 100.0, "color": "#67001f"},  # 100 - Very dark red
        {"value": 110.0, "color": "#4d0013"},  # 110+ - Extremely dark red
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
    "needed_bands": [
        "agm_ndvi",
        "msi_agm_ndvi",
        "oli_agm_ndvi",
        "tm_agm_ndvi"
    ],
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
    {"value": -0.1, "color": "#00004d"},
    {"value": 0.0, "color": "#00ffff"},
    {"value": 0.1, "color": "#00ff00"},
    {"value": 0.2, "color": "#ffff00"},
    {"value": 0.3, "color": "#ff8000"},
    {"value": 0.4, "color": "#ff0000"},
    {"value": 0.5, "color": "#8b0000"},
]

legend_fai = {
    "show_legend": True,
    "title": "Floating Algal Index",
    "units": "unitless",
    "begin": "-0.05",
    "end": "1.0",
    "decimal_places": 2,
    "ticks_every": "5",
    "width": 4.5,
    "height": 2.1,
    "strip_location": [0.1, 0.4, 0.8, 0.2],
}

style_wq_annual_fai = {
    "name": "wq_annual_fai",
    "title": "Floating Algal Index (FAI)",
    "abstract": "Presence of algal blooms in surface water bodies",
    "legend": legend_fai,
    "needed_bands": [
        "agm_fai",
        "msi_agm_fai",
        "oli_agm_fai",
        "tm_agm_fai"
    ],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "agm_fai"},
    },
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
    "title": "Floating Algal Index (FAI)",
    "abstract": "Surface water body colour",
    "legend": legend_hue,
    "needed_bands": [
        "agm_hue",
        "msi_agm_hue",
        "oli_agm_hue",
        "tm_agm_hue"
    ],
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
color_ramp_owt = [
    {"value": 1, "color": "#7a0177"},
    {"value": 2, "color": "#41b6c4"},
    {"value": 3, "color": "#2c7bb6"},
    {"value": 4, "color": "#1a9850"},
    {"value": 5, "color": "#a6611a"},
    {"value": 6, "color": "#66c2a5"},
    {"value": 7, "color": "#d73027"},
    {"value": 8, "color": "#fdae61"},
    {"value": 9, "color": "#74add1"},
    {"value": 10, "color": "#542788"},
    {"value": 11, "color": "#2d004b"},
    {"value": 12, "color": "#fee08b"},
    {"value": 13, "color": "#081d58"},
]

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
    "needed_bands": [
        "agm_owt",
        "msi_agm_owt",
        "oli_agm_owt",
        "tm_agm_owt"
    ],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "agm_owt"},
    },
    "include_in_feature_info": True,
    "color_ramp": color_ramp_owt,
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
    "begin": "0.1",
    "end": "300",
    "ticks_every": "20",
    "units": "mg/m³",
    "decimal_places": 0,
    "width": 4.5,
    "height": 2.1,
    "strip_location": [0.1, 0.4, 0.8, 0.2],
}

style_wq_annual_chla = {
    "name": "wq_annual_chla",
    "title": "Chlorophyll-a Concentration",
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
    "begin": "-5",
    "end": "40",
    "ticks_every": "5",
    "units": "°C",
    "decimal_places": 0,
    "width": 4.5,
    "height": 2.1,
    "strip_location": [0.1, 0.4, 0.8, 0.2],
}

style_wq_annual_tirs = {
    "name": "wq_annual_temp_mean",
    "title": "Mean Water Temperature",
    "abstract": "Annual mean surface water temperature",
    "legend": legend_tirs,
    "needed_bands": [
        "tirs_st_ann_max",
        "tirs_st_ann_med",
        "tirs_st_ann_min"
    ],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "tirs_st_ann_max"},
    },
    "include_in_feature_info": True,
    "color_ramp": color_ramp_tirs,
}
