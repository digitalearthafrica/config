# reslim

reslim_smart = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_level": 6.0,
        # "max_datasets": 16, # Defaults to no dataset limit
    },
    "wcs": {
        "max_datasets": 64
    }, 
}

reslim_landsat = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 35.0,
        # "max_datasets": 16, # Defaults to no dataset limit
    },
    "wcs": {
        # "max_datasets": 16, # Defaults to no dataset limit
    },
}

reslim_sentinel2 = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 20.0,  # defaults to 300!
        "max_datasets": 64,  # Defaults to no dataset limit
    },
    "wcs": {
        "max_datasets": 64,  # Defaults to no dataset limit
    },
}

reslim_zoom9 = {
    "zoomed_out_fill_colour": [150, 180, 200, 160],
    "min_zoom_factor": 2000.0,
    "max_datasets": 64,  # Defaults to no dataset limit
    "wcs": {
        "max_datasets": 64,  # Defaults to no dataset limit
    },
}

reslim_srtm = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 10.0,
        # "max_datasets": 16, # Defaults to no dataset limit
    },
    "wcs": {
        # "max_datasets": 16, # Defaults to no dataset limit
    },
}

reslim_wofs = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 0.0,
        # "max_datasets": 16, # Defaults to no dataset limit
    },
    "wcs": {
        # "max_datasets": 16, # Defaults to no dataset limit
    },
}
reslim_wofs_daily = {
    "wms": {
        "zoomed_out_fill_colour": [200, 180, 180, 160],
        "min_zoom_factor": 35.0,
        "max_datasets_wms": 6,
    },
    "wcs": {
        "max_datasets": 16,  # Defaults to no dataset limit
    },
}

reslim_wofs_dry = {
    "wms": {
        "zoomed_out_fill_colour": [150, 180, 200, 160],
        "min_zoom_factor": 15.0,
        # "max_datasets": 16, # Defaults to no dataset limit
    },
    "wcs": {
        # "max_datasets": 16, # Defaults to no dataset limit
    },
}
reslim_alos_palsar = reslim_srtm
