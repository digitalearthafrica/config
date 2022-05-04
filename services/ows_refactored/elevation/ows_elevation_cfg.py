from ows_refactored.common.ows_reslim_cfg import reslim_continental


style_greyscale = {
    "name": "greyscale",
    "title": "Greyscale",
    "abstract": "Greyscale elevation",
    "needed_bands": ["elevation"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "elevation",
        },
    },
    "color_ramp": [
        {"value": -0, "color": "#383838", "alpha": 0.0},
        {"value": 0.1, "color": "#383838"},
        {"value": 250, "color": "#5e5e5e"},
        {"value": 500, "color": "#858585"},
        {"value": 1000, "color": "#adadad"},
        {"value": 2000, "color": "#d4d4d4"},
        {"value": 4000, "color": "#fafafa"},
    ],
    "legend": {
        "title": "Elevation ",
        "begin": "0",
        "end": "4000",
        "ticks_every": 400,
        "units": "m",
        "tick_labels": {
            "4000": {"prefix": ">"},
        },
    },
}

style_colours = {
    "name": "colours",
    "title": "Coloured",
    "abstract": "Coloured elevation",
    "needed_bands": ["elevation"],
    "index_function": {
        "function": "datacube_ows.band_utils.single_band",
        "mapped_bands": True,
        "kwargs": {
            "band": "elevation",
        },
    },
    "color_ramp": [
        {"value": -0, "color": "#e1f2ff", "alpha": 0.0},
        {"value": 0.1, "color": "#41c23c"},
        {"value": 150, "color": "#f9a80e"},
        {"value": 300, "color": "#cb5f3e"},
        {"value": 400, "color": "#9d387d"},
        {"value": 500, "color": "#ba6daa"},
        {"value": 900, "color": "#d7a2d6"},
        {"value": 1200, "color": "#e6c8e6"},
        {"value": 4000, "color": "#ffecf9"},
    ],
    "legend": {
        "title": "Elevation ",
        "begin": "0",
        "end": "4000",
        "ticks_every": 400,
        "units": "m",
        "tick_labels": {
            "4000": {"prefix": ">"},
        },
    },
}

layer_srtm = {
    "title": "Shuttle Radar Topography Mission Digital Elevation Model (30 m)",
    "name": "dem_srtm",
    "abstract": """
A Digital Elevation Model (DEM) is a digital representation of Earth’s topography. It helps to understand the land surface characteristics in the height dimension. It is also used as an ancillary dataset to calculate illumination and viewing geometry of a satellite imagery. DE Africa provides access to the Shuttle Radar Topography Mission (SRTM) v 3.0 (SRTMGL1) product.

This elevation model has a spatial resolution of 30 m and is derived from data collected by NASA's Shuttle Radar Topography Mission in 2000.

It is provided by NASA's Land Processes Distributed Active Archive Center (LP DAAC).

For more information, see https://lpdaac.usgs.gov/products/srtmgl1v003/

This product is accessible through OGC Web Service (https://ows.digitalearth.africa/), for analysis in DE Africa Sandbox JupyterLab (https://github.com/digitalearthafrica/deafrica-sandbox-notebooks/wiki).
""",
    "product_name": "dem_srtm",
    "time_resolution": "year",
    "bands": {
        "elevation": []
    },
    "resource_limits": reslim_continental,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [
        0.00027777777778,
        -0.00027777777778,
    ],
    "styling": {
        "default_style": "greyscale",
        "styles": [style_greyscale, style_colours],
    },
}

layer_nasadem = {
    "title": "NASA Digital Elevation Model (30 m)",
    "name": "nasadem",
    "abstract": """
NASADEM provides global topographic data at 1 arc-second (~30m) horizontal resolution, derived primarily from data captured via the Shuttle Radar Topography Mission (SRTM).

The product is indexed directly from Microsoft's Planetary Computer, for more information, see https://planetarycomputer.microsoft.com/dataset/nasadem
""",
    "product_name": "nasadem",
    "time_resolution": "year",
    "bands": {
        "elevation": []
    },
    "resource_limits": reslim_continental,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [
        0.00027777777778,
        -0.00027777777778,
    ],
    "styling": {
        "default_style": "greyscale",
        "styles": [style_greyscale, style_colours],
    },
}

layer_cop_30 = {
    "title": "Copernicus Digital Elevation Model (30 m)",
    "name": "dem_cop_30",
    "abstract": """
The Copernicus DEM is a Digital Surface Model (DSM) which represents the surface of the Earth including buildings, infrastructure and vegetation. This DSM is derived from an edited DSM named WorldDEM, where flattening of water bodies and consistent flow of rivers has been included. In addition, editing of shore- and coastlines, special features such as airports, and implausible terrain structures has also been applied.

he WorldDEM product is based on the radar satellite data acquired during the TanDEM-X Mission, which is funded by a Public Private Partnership between the German State, represented by the German Aerospace Centre (DLR) and Airbus Defence and Space. OpenTopography is providing access to the global 30m (GLO-30) DSM through the public AWS S3 bucket established by Sinergise.

This data is indexed directly from Open Topography, for more information, see https://portal.opentopography.org/raster?opentopoID=OTSDEM.032021.4326.3
""",
    "product_name": "dem_cop_30",
    "time_resolution": "year",
    "bands": {
        "elevation": []
    },
    "resource_limits": reslim_continental,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [
        0.00027777777778,
        -0.00027777777778,
    ],
    "styling": {
        "default_style": "greyscale",
        "styles": [style_greyscale, style_colours],
    },
}
