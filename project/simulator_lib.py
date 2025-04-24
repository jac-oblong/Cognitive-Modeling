"""
Holds all classes and generating functions used by the simulator and model
"""

import numpy as np
from enum import IntEnum


GREEN_MU = 530
GREEN_SIGMA = 50
PERCENT_GREEN = 0.65

RED_MU = 600
RED_SIGMA = 50
PERCENT_RED = 0.33

BLUE_MU = 400
BLUE_SIGMA = 50
PERCENT_BLUE = 0.02

assert(PERCENT_GREEN + PERCENT_RED + PERCENT_BLUE == 1)


class ConeCell:
    """
    Simulates a cone cell that activates between lower and upper wavelength
    """
    def __init__(self, lower_wavelength: float, upper_wavelength: float):
        self.lower_wavelength = lower_wavelength
        self.upper_wavelength = upper_wavelength

    def plot_range(self, axis):
        axis.plot()


class Color(IntEnum):
    """
    Enum for colors
    """
    VIOLET = 0
    BLUE = 1
    GREEN = 2
    YELLOW = 3
    ORANGE = 4
    RED = 5


def generate_cone_cell(mu: float, sigma: float) -> ConeCell:
    """
    Generates a single cone cell

    :param mu: mean of normal distribution to sample from
    :param sigma: standard deviation of normal distribution to sample from
    :return: the generated cone cell with lower and upper wavelengths sampled 
             from normal distribution
    """
    f1 = np.random.normal(mu, sigma)
    f2 = np.random.normal(mu, sigma)
    lower = min(f1, f2)
    upper = max(f1, f2)
    return ConeCell(lower_wavelength=lower, upper_wavelength=upper)


def generate_cone_cells(num: int, mu: float, sigma: float) -> list[ConeCell]:
    """
    Generates multiple single cone cells

    :param num: number of cone cells to generate
    :param mu: mean of normal distribution to sample from
    :param sigma: standard deviation of normal distribution to sample from
    :return: list of cone cells
    """
    cells = []
    for _ in range(num):
        cells.append(generate_cone_cell(mu, sigma))
    return cells


def generate_plotting_data(cells: list[ConeCell], min_wavelength: float, max_wavelength: float, delta_wavelength: float):
    """
    Generates plotting data for the cells

    :param cells: list of cone cells to generate plotting data for
    :param min_wavelength: the minimum wavelength on the graph
    :param max_wavelength: the maximum wavelength on the graph
    :param delta_wavelength: step size between wavelengths
    :return: tuple containing two lists. First list contains the wavelengths and second
             list contains the number of cells that activate for that wavelength
    """
    num_wavelength = int((max_wavelength - min_wavelength) / delta_wavelength)
    wavelengths = np.ndarray(shape=num_wavelength)
    counts = np.ndarray(shape=num_wavelength)
    for i in range(num_wavelength):
        wavelength = min_wavelength + (i * delta_wavelength)
        count = 0
        wavelengths[i] = wavelength
        for cell in cells:
            if cell.lower_wavelength <= wavelength and cell.upper_wavelength >= wavelength:
                count += 1
        counts[i] = count
    return (wavelengths, counts)


def get_cell_responses(cells: list[ConeCell], wavelength: float):
    """
    Get the responses of all cells for wavelength

    :param cells: the cells to see if activate for wavelength
    :param wavelength: the wavelength to test
    :return: numpy array with 1 if cell activates and 0 if it doesn't
    """
    responses = np.zeros(shape=len(cells))
    i = 0
    for cell in cells:
        if cell.lower_wavelength <= wavelength and cell.upper_wavelength >= wavelength:
            responses[i] = 1
        else:
            responses[i] = 0
        i += 1
    return responses


def wavelength_to_color(wavelength: float) -> Color:
    """
    Convert wavelength of light into color using binning

    :param wavelength: wavelength of light
    :return: color associated with the wavelength
    """
    if wavelength < 450:
        return Color.VIOLET
    elif wavelength < 495:
        return Color.BLUE
    elif wavelength < 570:
        return Color.GREEN
    elif wavelength < 590:
        return Color.YELLOW
    elif wavelength < 620:
        return Color.ORANGE
    else:
        return Color.RED


def sample_wavelengths(num_data_points, cells, min_wl, max_wl):
    """
    Generates result of sampling cells at multiple wavelengths
    Wavelengths are randomly taken from a uniform distribution

    :param num_data_points: the number of wavelengths to sample at
    :param cells: the cells to use
    :param min_wl: the minimum wavelength to sample from
    :param max_wl: the maximum wavelength to sample at
    :return: a tuple where the first element is an array containing
             the results of each sample and the second element is an
             array containing the color corresponding with the wavelength
             used
    """
    data = np.ndarray(shape=(num_data_points, len(cells)))
    wavelengths = np.random.uniform(low=min_wl, high=max_wl, size=num_data_points)
    classified_wavelengths = []
    i = 0
    for wavelength in wavelengths:
        data[i] = get_cell_responses(cells, wavelength)
        classified_wavelengths.append(wavelength_to_color(wavelength))
        i += 1
    return data, classified_wavelengths