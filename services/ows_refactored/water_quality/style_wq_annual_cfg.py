"""
Water Quality Style Configuration for Digital Earth Africa OWS
================================================================

Style definitions for water quality parameters
Organized by parameter and sensor/source type.

"""

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

