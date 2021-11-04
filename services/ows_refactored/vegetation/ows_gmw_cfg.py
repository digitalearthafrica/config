from ows_refactored.common.ows_reslim_cfg import reslim_continental

mangrove = {
    "name": "mangrove",
    "title": "Mangroves",
    "abstract": "Global mangrove watch mangroves",
    "value_map": {
        "mask": [
            {
                "title": "Mangroves",
                "color": "#00CED1",
                "values": [1],
            }
        ]
    },
}


layer = {
    "title": "Global Mangrove Watch",
    "name": "gmw",
    "abstract": """
The GMW aims to provide geospatial information about mangrove extent and changes to the Ramsar Convention, national wetland practitioners, decision makers and NGOs. It is part of the Ramsar Science and Technical Review Panel (STRP) work plan for 2016-2018 and a Pilot Project to the Ramsar Global Wetlands Observation System (GWOS), which is implemented under the GEO-Wetlands Initiative. The primary objective of the GMW has been to provide countries lacking a national mangrove monitoring system with first cut mangrove extent and change maps, to help safeguard against further mangrove forest loss and degradation.

The GMW has generated a global baseline map of mangroves for 2010 using ALOS PALSAR and Landsat (optical) data, and changes from this baseline for six epochs between 1996 and 2016 derived from JERS-1 SAR, ALOS PALSAR and ALOS-2 PALSAR-2. Annual maps are planned from 2018 and onwards.

For more information, see https://data.unep-wcmc.org/datasets/45.
""",
    "product_name": "gmw",
    "bands": {
        "mangrove": [],
    },
    "resource_limits": reslim_continental,
    "dynamic": True,
    "image_processing": {
        "extent_mask_func": "datacube_ows.ogc_utils.mask_by_val",
        "always_fetch_bands": [],
        "manual_merge": False,
    },
    "native_crs": "EPSG:4326",
    "native_resolution": [0.0002, -0.0002],
    "styling": {
        "default_style": "mangrove",
        "styles": [
            mangrove
        ],
    },
}
