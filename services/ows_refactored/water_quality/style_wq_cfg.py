"""
Water Quality Style Configuration for Digital Earth Africa OWS
================================================================

Style definitions for water quality parameters 
Organized by parameter and sensor/source type.


"""

from ows_refactored.common.ows_legend_cfg import legend_idx_0_1_1ticks, legend_mean_ndvi_ticks


# ============================================================================
# TOTAL SUSPENDED SOLIDS STYLES
# ============================================================================
color_ramp_tss_oli = [
    {"value": 0.0, "color": "#001050", "alpha": 0.0},
    {"value": 0.1, "color": "#001050"},
    {"value": 0.2, "color": "#103070"},
    {"value": 0.3, "color": "#205090"},
    {"value": 0.4, "color": "#4080b0"},
    {"value": 0.4, "color": "#80b0d0"},
    {"value": 0.5, "color": "#c0d080"},
    {"value": 0.6, "color": "#d0a040"},
    {"value": 0.7, "color": "#a05020"},
    {"value": 0.8, "color": "#703010"},
    {"value": 0.9, "color": "#401000"},
]

color_ramp_tss_msi= [
    {"value": 0.0, "color": "#001050", "alpha": 0.0},
    {"value": 1.0, "color": "#001050"},
    {"value": 2.0, "color": "#103070"},
    {"value": 3.0, "color": "#205090"},
    {"value": 4.0, "color": "#4080b0"},
    {"value": 5.0, "color": "#80b0d0"},
    {"value": 6.0, "color": "#c0d080"},
    {"value": 7.0, "color": "#d0a040"},
    {"value": 8.0, "color": "#a05020"},
    {"value": 9.0, "color": "#703010"},
    
]

# tss styles------------------------------------------------------
style_tss_oli = {
    "name": "tss",
    "title": "Total Suspended Solids",
    "abstract": "Total suspended solids concentration (mg/L)",
    "needed_bands": ["tss_zhang_oli_agm"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "tss_zhang_oli_agm",
        },
    },
    "color_ramp": color_ramp_tss_oli,
    "legend": legend_mean_ndvi_ticks,
}

style_tss_msi= {
    "name": "tss",
    "title": "Total Suspended Solids",
    "abstract": "Total suspended solids concentration (mg/L)",
    "needed_bands": ["tss_zhang_msi_agm"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "tss_zhang_msi_agm",
        },
    },
    "color_ramp": color_ramp_tss_msi,
    "legend": legend_idx_0_1_1ticks,
}
    
   

