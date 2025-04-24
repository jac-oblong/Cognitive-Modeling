"""
Holds all classes and generating functions used by the simulator and model
"""

import numpy as np
from enum import IntEnum

# Peak (mu) values vary person to person,
#   use a uniform distribution to get a mu for a particular person
#   (or use the standard (mean of high and low))

# M (Medium - green) cone cells: 534-545 nm peak
GREEN_MU_LOWER = 534
GREEN_MU_UPPER = 545
GREEN_MU_STANDARD = 540
GREEN_SIGMA = 50
PERCENT_GREEN = 0.33

# L (Long - red) cone cells: 564-580 nm peak
RED_MU_LOWER = 564
RED_MU_UPPER = 580
RED_MU_STANDARD = 573
RED_SIGMA = 50
PERCENT_RED = 0.65

# S (Short - blue) cone cells: 420-440 nm peak
BLUE_MU_LOWER = 420
BLUE_MU_UPPER = 440
BLUE_MU_STANDARD = 430
BLUE_SIGMA = 50
PERCENT_BLUE = 0.02

# colorblind individuals (dichromatic)
RED_GREEN_MU = (RED_MU_STANDARD + GREEN_MU_STANDARD) / 2
RED_GREEN_SIGMA = 70

# 4th celled individuals (tetrachromatic)
TETRA_MU_LOWER = 550
TETRA_MU_UPPER = 560
TETRA_MU_STANDARD = 555
TETRA_SIGMA = 50
# was unable to find statistical breakdown, estimation based on biological reasoning for tetrachromacy
# (father's M(green) cone shifts toward L(red), where mother's stays, so child gets both (i.e. half of M cones become PRIME cones))
TETRA_RED = PERCENT_RED
TETRA_GREEN = 0.5 * PERCENT_GREEN
TETRA_PRIME = TETRA_GREEN
TETRA_BLUE = PERCENT_BLUE

assert(PERCENT_GREEN + PERCENT_RED + PERCENT_BLUE == 1)
assert(TETRA_GREEN + TETRA_RED + TETRA_BLUE + TETRA_PRIME == 1)


class ConeCell:
    """
    Simulates a cone cell that activates between lower and upper frequency
    """
    def __init__(self, lower_frequency: float, upper_frequency: float, living: bool=True):
        self.lower_frequency = lower_frequency  # lowest frequency of light that activates this cell
        self.upper_frequency = upper_frequency  # highest frequency of light that actvates this cell
        self.living = living                    # if the cell is alive (i.e. can activate)

    def kill_cell(self):
        """
        Kills the cell by setting living to false, cell will no longer activate
        """
        self.living = False

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


def generate_cone_cell(mu: float, sigma: float, chance_dead: float=0) -> ConeCell:
    """
    Generates a single cone cell

    :param mu: mean of normal distribution to sample from
    :param sigma: standard deviation of normal distribution to sample from
    :param chance_dead: probability [0, 1] the generated cell is dead on creation
    :return: the generated cone cell with lower and upper frequencies sampled 
             from normal distribution
    """
    f1 = np.random.normal(mu, sigma)
    f2 = np.random.normal(mu, sigma)
    lower = min(f1, f2)
    upper = max(f1, f2)
    living = np.random.random() > chance_dead
    return ConeCell(lower_frequency=lower, upper_frequency=upper, living=living)


def generate_cone_cells(num: int, mu: float, sigma: float, chance_dead: float=0) -> list[ConeCell]:
    """
    Generates multiple single cone cells

    :param num: number of cone cells to generate
    :param mu: mean of normal distribution to sample from
    :param sigma: standard deviation of normal distribution to sample from
    :param chance_dead: probability [0, 1] the generated cell is dead on creation
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