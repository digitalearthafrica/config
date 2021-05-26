bands_ls8c = {
    "red": [],
    "green": [],
    "blue": [],
    "nir": [],
    "swir_1": [],
    "swir_2": [],
}

bands_sentinel = {
    "B01": ["band_01", "coastal_aerosol"],
    "B02": ["band_02", "blue"],
    "B03": ["band_03", "green"],
    "B04": ["band_04", "red"],
    "B05": ["band_05", "red_edge_1"],
    "B06": ["band_06", "red_edge_2"],
    "B07": ["band_07", "red_edge_3"],
    "B08": ["band_08", "nir", "nir_1"],
    "B8A": ["band_8a", "nir_narrow", "nir_2"],
    "B09": ["band_09", "water_vapour"],
    "B11": ["band_11", "swir_1", "swir_16"],
    "B12": ["band_12", "swir_2", "swir_22"],
    "AOT": ["aerosol_optical_thickness"],
    "WVP": ["scene_average_water_vapour"],
    "SCL": ["mask", "qa"],
}

bands_s2_gm = {
    "B02": ["band_02", "blue"],
    "B03": ["band_03", "green"],
    "B04": ["band_04", "red"],
    "B05": ["band_05", "red_edge_1"],
    "B06": ["band_06", "red_edge_2"],
    "B07": ["band_07", "red_edge_3"],
    "B08": ["band_08", "nir", "nir_1"],
    "B8A": ["band_8a", "nir_narrow", "nir_2"],
    "B11": ["band_11", "swir_1", "swir_16"],
    "B12": ["band_12", "swir_2", "swir_22"],
    "SMAD": ["smad", "sdev"],
    "EMAD": ["emad", "edev"],
    "BCMAD": ["bcmad", "bcdev", "BCDEV"],
    "COUNT": ["count"],
}

bands_ls = {
    "red": [],
    "green": [],
    "blue": [],
    "nir": ["near_infrared"],
    "swir1": ["shortwave_infrared_1", "near_shortwave_infrared"],
    "swir2": ["shortwave_infrared_2", "far_shortwave_infrared"],
}

# new styles for C2 Landsat

bands_ls5_sr = {
    "SR_B1": ["blue"],
    "SR_B2": ["green"],
    "SR_B3": ["red"],
    "SR_B4": ["nir"],
    "SR_B5": ["swir_1"],
    "SR_B7": ["swir_2"],
}

bands_ls7_sr = {
    "SR_B1": ["blue"],
    "SR_B2": ["green"],
    "SR_B3": ["red"],
    "SR_B4": ["nir"],
    "SR_B5": ["swir_1"],
    "SR_B7": ["swir_2"],
}

bands_ls8_sr = {
    "SR_B2": ["blue"],
    "SR_B3": ["green"],
    "SR_B4": ["red"],
    "SR_B5": ["nir"],
    "SR_B6": ["swir_1"],
    "SR_B7": ["swir_2"],
}
