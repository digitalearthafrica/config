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
color_ramp_tsm = [
    {"value": 0.0, "color": "#084594"},  # 0 mg/L - Navy
    {"value": 10.0, "color": "#2171b5"},  # 10 mg/L - Blue
    {"value": 25.0, "color": "#4292c6"},  # 25 mg/L - Light blue
    {"value": 50.0, "color": "#6baed6"},  # 50 mg/L - Pale blue
    {"value": 75.0, "color": "#9ecae1"},  # 75 mg/L - Very pale blue
    {"value": 100.0, "color": "#deebf7"},  # 100 mg/L - Almost white blue
    {"value": 125.0, "color": "#ffffcc"},  # 125 mg/L - Pale yellow
    {"value": 150.0, "color": "#ffeda0"},  # 150 mg/L - Light yellow
    {"value": 175.0, "color": "#fed976"},  # 175 mg/L - Yellow
    {"value": 200.0, "color": "#feb24c"},  # 200 mg/L - Orange
    {"value": 225.0, "color": "#fd8d3c"},  # 225 mg/L - Dark orange
    {"value": 250.0, "color": "#fc4e2a"},  # 250 mg/L - Red-orange
    {"value": 275.0, "color": "#e31a1c"},  # 275 mg/L - Red
    {"value": 300.0, "color": "#bd0026"},  # 300 mg/L - Dark red
    {"value": 400.0, "color": "#800026"},  # 400+ mg/L - Very dark red
]

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
    "title": "Total Suspended Matter (TSM)",
    "abstract": "Total suspended matter concentration (mg/L) in surface water bodies",
    "legend": legend_tsm,
    "needed_bands": ["tsm"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "tsm"},
    },
    "color_ramp": color_ramp_tsm,
}


# ============================================================================
# TROPHIC STATE INDEX (TSI) STYLES
# ============================================================================
color_ramp_tsi = [
    {"value": 0.0, "color": "#440154"},    # 0 - Deep purple/navy (oligotrophic)
    {"value": 10.0, "color": "#31688e"},   # 10 - Blue (oligotrophic)
    {"value": 20.0, "color": "#35b779"},   # 20 - Cyan-blue (oligotrophic)
    {"value": 30.0, "color": "#1f9e89"},   # 30 - Teal (oligo-mesotrophic)
    {"value": 40.0, "color": "#26828e"},   # 40 - Dark cyan (mesotrophic)
    {"value": 50.0, "color": "#3fbc73"},   # 50 - Green-cyan (mesotrophic)
    {"value": 60.0, "color": "#6ece58"},   # 60 - Light green (eutrophic)
    {"value": 70.0, "color": "#b5de2b"},   # 70 - Yellow-green (eutrophic)
    {"value": 75.0, "color": "#fde725"},   # 75 - Yellow (eutrophic-hypereutrophic)
    {"value": 80.0, "color": "#fca636"},   # 80 - Orange-yellow (hypereutrophic)
    {"value": 85.0, "color": "#f1605d"},   # 85 - Orange-red (hypereutrophic)
    {"value": 90.0, "color": "#e8576b"},   # 90 - Red (hypereutrophic)
    {"value": 95.0, "color": "#d84c6f"},   # 95 - Red-pink (hypereutrophic)
    {"value": 100.0, "color": "#b73779"},  # 100 - Magenta (hypereutrophic)
    {"value": 110.0, "color": "#8c2981"},  # 110+ - Purple-magenta (hypereutrophic)
]

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
    "title": "Trophic State Index (TSI)",
    "abstract": "Biological productivity in surface water bodies",
    "legend": legend_tsi,
    "needed_bands": ["tsi"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {"band": "tsi"},
    },
    "color_ramp": color_ramp_tsi,
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
