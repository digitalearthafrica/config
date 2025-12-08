"""
Water Quality Style Configuration for Digital Earth Africa OWS
================================================================

Style definitions for water quality parameters
Organized by parameter and sensor/source type.


"""

from ows_refactored.common.ows_legend_cfg import legend_idx_0_1_1ticks

# ============================================================================
# TOTAL SUSPENDED MATTER (TSM) STYLES
# ============================================================================
color_ramp_tsm = [
    {"value": 0.0, "color": "#084594", "alpha": 1.0},  # 0 mg/L - Navy
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

style_wq_annual_tsm = {
    "name": "style_wq_annual_tsm",
    "title": "concentration of particulate material in the surface water",
    "abstract": "Total suspended matter concentration (mg/L)",
    "needed_bands": ["tsm"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "tsm",
        },
    },
    "color_ramp": color_ramp_tsm,
    "legend": legend_idx_0_1_1ticks,
}
