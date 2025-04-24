"""
Holds all classes and generating functions used by the simulator and model
"""

import numpy as np
from enum import IntEnum


class ConeCell:
    """
    Simulates a cone cell that activates between lower and upper frequency
    """
    def __init__(self, lower_frequency: float, upper_frequency: float):
        self.lower_frequency = lower_frequency
        self.upper_frequency = upper_frequency

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
    :return: the generated cone cell with lower and upper frequencies sampled 
             from normal distribution
    """
    f1 = np.random.normal(mu, sigma)
    f2 = np.random.normal(mu, sigma)
    lower = min(f1, f2)
    upper = max(f1, f2)
    return ConeCell(lower_frequency=lower, upper_frequency=upper)


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


def generate_plotting_data(cells: list[ConeCell], min_freq: float, max_freq: float, delta_freq: float):
    """
    Generates plotting data for the cells

    :param cells: list of cone cells to generate plotting data for
    :param min_freq: the minimum frequency on the graph
    :param max_freq: the maximum frequency on the graph
    :param delta_freq: step size between frequencies
    :return: tuple containing two lists. First list contains the frequencies and second
             list contains the number of cells that activate for that frequency
    """
    num_freq = int((max_freq - min_freq) / delta_freq)
    freqs = np.ndarray(shape=num_freq)
    counts = np.ndarray(shape=num_freq)
    for i in range(num_freq):
        freq = min_freq + (i * delta_freq)
        count = 0
        freqs[i] = freq
        for cell in cells:
            if cell.lower_frequency <= freq and cell.upper_frequency >= freq:
                count += 1
        counts[i] = count
    return (freqs, counts)


def get_cell_responses(cells: list[ConeCell], frequency: float):
    """
    Get the responses of all cells for frequency

    :param cells: the cells to see if activate for frequency
    :param frequency: the frequency to test
    :return: numpy array with 1 if cell activates and 0 if it doesn't
    """
    responses = np.zeros(shape=len(cells))
    i = 0
    for cell in cells:
        if cell.lower_frequency <= frequency and cell.upper_frequency >= frequency:
            responses[i] = 1
        else:
            responses[i] = 0
        i += 1
    return responses


def freq_to_color(freq: float) -> Color:
    """
    Convert frequency of light into color using binning

    :param freq: frequency of light
    :return: color associated with the frequency
    """
    if freq < 450:
        return Color.VIOLET
    elif freq < 495:
        return Color.BLUE
    elif freq < 570:
        return Color.GREEN
    elif freq < 590:
        return Color.YELLOW
    elif freq < 620:
        return Color.ORANGE
    else:
        return Color.RED


def sample_frequencies(num_data_points, cells, min_freq, max_freq):
    """
    Generates result of sampling cells at multiple frequencies
    Frequencies are randomly taken from a uniform distribution

    :param num_data_points: the number of frequencies to sample at
    :param cells: the cells to use
    :param min_freq: the minimum frequency to sample from
    :param max_freq: the maximum frequency to sample at
    :return: a tuple where the first element is an array containing
             the results of each sample and the second element is an
             array containing the color corresponding with the frequency
             used
    """
    data = np.ndarray(shape=(num_data_points, len(cells)))
    freqs = np.random.uniform(low=min_freq, high=max_freq, size=num_data_points)
    classified_freqs = []
    i = 0
    for freq in freqs:
        data[i] = get_cell_responses(cells, freq)
        classified_freqs.append(freq_to_color(freq))
        i += 1
    return data, classified_freqs