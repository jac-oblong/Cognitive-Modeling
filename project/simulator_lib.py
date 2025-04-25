"""
Holds all classes and generating functions used by the simulator and model
"""

import numpy as np
from enum import Enum

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
    Simulates a cone cell that activates between lower and upper wavelength
    """
    def __init__(self, lower_wavelength: float, upper_wavelength: float, living: bool=True):
        self.lower_wavelength = lower_wavelength  # lowest wavelength of light that activates this cell
        self.upper_wavelength = upper_wavelength  # highest wavelength of light that actvates this cell
        self.living = living                    # if the cell is alive (i.e. can activate)

    def kill_cell(self):
        """
        Kills the cell by setting living to false, cell will no longer activate
        """
        self.living = False

    def plot_range(self, axis):
        axis.plot()


class Color(Enum):
    """
    Enum for colors
    """
    VIOLET = {"min": 380, "max": 450, "val": 0}
    BLUE = {"min": 450, "max": 495, "val": 1}
    GREEN = {"min": 495, "max": 570, "val": 2}
    YELLOW = {"min": 570, "max": 590, "val": 3}
    ORANGE = {"min": 590, "max": 620, "val": 4}
    RED = {"min": 620, "max": 750, "val": 5}


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
    return ConeCell(lower_wavelength=lower, upper_wavelength=upper, living=living)


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
        cells.append(generate_cone_cell(mu, sigma, chance_dead))
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
    for i, cell in enumerate(cells):
        if not cell.living:
            responses[i] = 0
        elif cell.lower_wavelength <= wavelength and cell.upper_wavelength >= wavelength:
            responses[i] = 1
        else:
            responses[i] = 0
    return responses


def wavelength_to_color(wavelength: float) -> Color:
    """
    Convert wavelength of light into color using binning

    :param wavelength: wavelength of light
    :return: color associated with the wavelength
    """
    for color in Color:
        if color["min"] <= wavelength and wavelength <= color["max"]:
            return color


def sample_wavelengths(num_data_points, cells):
    """
    Generates result of sampling cells at multiple wavelengths
    Wavelengths are randomly taken from a uniform distribution

    :param num_data_points: the number of wavelengths to sample at
    :param cells: the cells to use
    :return: a tuple where the first element is an array containing
             the results of each sample and the second element is an
             array containing the color corresponding with the wavelength
             used
    """
    data = np.ndarray(shape=(num_data_points, len(cells)))
    colors = np.random.choice(Color, size=num_data_points)
    for i, color in enumerate(colors):
        wavelength = np.random.uniform(low=color.value["min"], high=color.value["max"])
        data[i] = get_cell_responses(cells, wavelength)
    return data, [c.value["val"] for c in colors]