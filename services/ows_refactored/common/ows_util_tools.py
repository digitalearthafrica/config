import numpy


def mask_by_nan(data, band):
    return ~numpy.isnan(data[band])
