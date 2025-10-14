from ows_refactored.common.ows_reslim_cfg import reslim_land_cover

# ----------------------------
# Helper function to create styles
# ----------------------------
def create_style(name, title, value_map):
    return {
        "name": name,
        "title": title,
        "needed_bands": ["classification"],
        "index_function": {
            "function": "datacube_ows.band_utils.single_band",
            "mapped_bands": True,
            "kwargs": {"band": "classification"},
        },
        "value_map": {"classification": value_map},
    }

# ----------------------------
# Define styles
# ----------------------------
style_activecropland = create_style(
    "style_activecropland",
    "Active cropland",
    [
        {"title": "Inactive cropland", "abstract": "", "values": [0], "color": "#f50707"},
        {"title": "Active cropland", "abstract": "", "values": [100], "color": "#004f01"},
    ],
)

style_irrigated = create_style(
    "style_irrigated",
    "Irrigated",
    [
        {"title": "Rainfed", "abstract": "", "values": [0], "color": "#ff7096"},
        {"title": "Irrigated", "abstract": "", "values": [100], "color": "#367a9c"},
    ],
)

style_maize = create_style(
    "style_maize",
    "Maize",
    [
        {"title": "Maize", "abstract": "", "values": [100], "color": "#fcfc44"},
    ],
)

style_temporarycrops = create_style(
    "style_temporarycrops",
    "Temporary crops",
    [
        {"title": "Temporary crops", "abstract": "", "values": [100], "color": "#f50707"},
    ],
)

style_wintercereals = create_style(
    "style_wintercereals",
    "Winter cereals",
    [
        {"title": "Winter cereals", "abstract": "", "values": [100], "color": "#f7882d"},
    ],
)

# ----------------------------
# Helper function to create ESA WorldCereal layers
# ----------------------------
def create_esa_layer(product_name, title, default_style, abstract=None, single_time="2021-01-01"):
    """
    Creates a Datacube OWS layer for ESA WorldCereal with a single time for all regional tiles.
    """
    if abstract is None:
        abstract = f"ESA WorldCereal 10m 2021 v1.0.0 layer {product_name}. For more info see https://esa-worldcereal.org/en/products/global-maps"
    
    return {
        "title": title,
        "name": product_name,
        "abstract": abstract,
        "product_name": product_name,
        "time": single_time,  # Force single date for all regions
        "time_resolution": "year",
        "bands": {"classification": []},
        "resource_limits": reslim_land_cover,
        "image_processing": {
            "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
            "always_fetch_bands": [],
            "manual_merge": False,
            "fuse_func": "datacube_ows.utils.fuse.first",  # merge overlapping tiles
        },
        "native_crs": "EPSG:4326",
        "native_resolution": [0.000083333333333, -0.000083333333333],
        "styling": {
            "default_style": default_style["name"],
            "styles": [default_style],
        },
    }

# ----------------------------
# Create all layers
# ----------------------------
activecropland_layer = create_esa_layer("esa_worldcereal_activecropland", "ESA WorldCereal Active Cropland", style_activecropland)

maize_active_layer = create_esa_layer("esa_worldcereal_maize_active", "ESA WorldCereal Active Maize Cropland", style_activecropland)

maize_irrigation_layer = create_esa_layer("esa_worldcereal_maize_irrigation", "ESA WorldCereal Irrigated Maize", style_irrigated)

wintercereals_irrigation_layer = create_esa_layer("esa_worldcereal_wintercereals_irrigation", "ESA WorldCereal Winter Cereals – Irrigation", style_irrigated)

maize_main_layer = create_esa_layer("esa_worldcereal_maize_main", "ESA WorldCereal Main-Season Maize", style_maize)

temporarycrops_layer = create_esa_layer("esa_worldcereal_temporarycrops", "ESA WorldCereal Temporary Cropland Extent", style_temporarycrops)

wintercereals_layer = create_esa_layer("esa_worldcereal_wintercereals", "ESA WorldCereal Winter Cereals", style_wintercereals)
