import numpy  # pylint: disable=import-error


def mask_by_nan(data, band):
    return ~numpy.isnan(data[band])


def mask_by_emad_nan(data, band, band_mapper=None):
    if band_mapper:
        emad = band_mapper("EMAD")
    else:
        emad = "EMAD"
    return ~numpy.isnan(data[emad])

# Copied from commit 66c808b version of datacube-ows.time_utils.rolling_window_ndays.
# to solve error in ESA WorldCereal layers where the mosaic_date_func is not
# working as expected for datacube-ows version 1.8.42.
# TODO: Remove and use the official datacube-ows implementation when datacube-ows
# is upgraded to ghcr.io/opendatacube/ows:1.9.11 or later.
def rolling_window_ndays(
    available_dates,
    layer_cfg,
    ndays: int = 6,
) :
    if ndays > len(available_dates):
        days = available_dates
        idx = -len(available_dates)
    else:
        idx = -ndays
        days = available_dates[idx:]
    start, _ = layer_cfg.search_times(days[idx])
    _, end = layer_cfg.search_times(days[-1])
    return start, end
