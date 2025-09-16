bands_ls8c = {
    "red": [],
    "green": [],
    "blue": [],
    "nir": [],
    "swir_1": [],
    "swir_2": [],
}

bands_sentinel = {
    "B01": ["coastal_aerosol"],
    "B02": ["blue"],
    "B03": ["green"],
    "B04": ["red"],
    "B05": ["red_edge_1"],
    "B06": ["red_edge_2"],
    "B07": ["red_edge_3"],
    "B08": ["nir", "nir_1"],
    "B8A": ["nir_narrow", "nir_2"],
    "B09": ["water_vapour"],
    "B11": ["swir_1", "swir_16"],
    "B12": ["swir_2", "swir_22"],
    "AOT": ["aerosol_optical_thickness"],
    "WVP": ["scene_average_water_vapour"],
    "SCL": ["mask", "qa"],
}

bands_s2_gm = {
    "B02": ["blue"],
    "B03": ["green"],
    "B04": ["red"],
    "B05": ["red_edge_1"],
    "B06": ["red_edge_2"],
    "B07": ["red_edge_3"],
    "B08": ["nir", "nir_1"],
    "B8A": ["nir_narrow", "nir_2"],
    "B11": ["swir_1", "swir_16"],
    "B12": ["swir_2", "swir_22"],
    "SMAD": ["smad", "sdev"],
    "EMAD": ["emad", "edev"],
    "BCMAD": ["bcmad", "bcdev", "BCDEV"],
    "COUNT": ["count"],
}

bands_ls8_gm = {
    "SR_B2": ["blue", "band_2"],
    "SR_B3": ["green", "band_3"],
    "SR_B4": ["red", "band_4"],
    "SR_B5": ["nir", "band_5"],
    "SR_B6": ["swir_1", "band_6"],
    "SR_B7": ["swir_2", "band_7"],
    "SMAD": ["smad", "sdev", "SDEV"],
    "EMAD": ["emad", "edev", "EDEV"],
    "BCMAD": ["bcmad", "bcdev", "BCDEV"],
    "COUNT": ["count"],
}

bands_ls8_ls9_gm = bands_ls8_gm

bands_ls5_ls7_gm = {
    "SR_B1": ["blue", "band_2"],
    "SR_B2": ["green", "band_3"],
    "SR_B3": ["red", "band_4"],
    "SR_B4": ["nir", "band_5"],
    "SR_B5": ["swir_1", "band_6"],
    "SR_B7": ["swir_2", "band_7"],
    "SMAD": ["smad", "sdev", "SDEV"],
    "EMAD": ["emad", "edev", "EDEV"],
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
    "QA_PIXEL": ["pq"],
    "SR_ATMOS_OPACITY": ["atmospheric_opacity"],
}

bands_ls7_sr = {
    "SR_B1": ["blue"],
    "SR_B2": ["green"],
    "SR_B3": ["red"],
    "SR_B4": ["nir"],
    "SR_B5": ["swir_1"],
    "SR_B7": ["swir_2"],
    "QA_PIXEL": ["pq"],
    "SR_ATMOS_OPACITY": ["atmospheric_opacity"],
}

bands_ls8_sr = {
    "SR_B2": ["blue"],
    "SR_B3": ["green"],
    "SR_B4": ["red"],
    "SR_B5": ["nir"],
    "SR_B6": ["swir_1"],
    "SR_B7": ["swir_2"],
    "QA_PIXEL": ["pq"],
    "SR_QA_AEROSOL": ["aerosol_level"],
}

bands_s3_olci_l2_land = {
    "GIFAPAR": ["GI-FAPAR"],
    "IWV_L": ["water_vapour"],
    "OTCI": ["chlorophyll"],
    "RC681": [],
    "RC865": [],
    "LQSF": [],
    "dataMask": ["mask"],
}
