from math import ceil

import matplotlib.pyplot as plt
from PIL import Image

from simulator_lib import *

flower = [
    [Color.VIOLET.value["val"], Color.VIOLET.value["val"], Color.VIOLET.value["val"], Color.VIOLET.value["val"], Color.VIOLET.value["val"], Color.VIOLET.value["val"], Color.VIOLET.value["val"], Color.VIOLET.value["val"], Color.VIOLET.value["val"], Color.VIOLET.value["val"]],
    [Color.VIOLET.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.VIOLET.value["val"]],
    [Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.ORANGE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"]],
    [Color.BLUE.value["val"], Color.BLUE.value["val"], Color.RED.value["val"], Color.BLUE.value["val"], Color.ORANGE.value["val"], Color.ORANGE.value["val"], Color.ORANGE.value["val"], Color.BLUE.value["val"], Color.YELLOW.value["val"], Color.BLUE.value["val"]],
    [Color.BLUE.value["val"], Color.RED.value["val"], Color.RED.value["val"], Color.RED.value["val"], Color.BLUE.value["val"], Color.GREEN.value["val"], Color.BLUE.value["val"], Color.YELLOW.value["val"], Color.YELLOW.value["val"], Color.YELLOW.value["val"]],
    [Color.BLUE.value["val"], Color.BLUE.value["val"], Color.GREEN.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.GREEN.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.GREEN.value["val"], Color.BLUE.value["val"]],
    [Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.GREEN.value["val"], Color.GREEN.value["val"], Color.GREEN.value["val"], Color.BLUE.value["val"], Color.GREEN.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"]],
    [Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.GREEN.value["val"], Color.GREEN.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"]],
    [Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.GREEN.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"], Color.BLUE.value["val"]],
    [Color.GREEN.value["val"], Color.GREEN.value["val"], Color.GREEN.value["val"], Color.GREEN.value["val"], Color.GREEN.value["val"], Color.GREEN.value["val"], Color.GREEN.value["val"], Color.GREEN.value["val"], Color.GREEN.value["val"], Color.GREEN.value["val"]]
]

def color_to_rgb(color: Color) -> np.array:
    """
    Converts a color to the associated pixel value

    :param color: color to convert to RGB
    :return: numpy array with rgb value
    """

    if color == Color.VIOLET.value["val"]:
        return np.array([72, 5, 118], dtype=np.uint8)
    if color == Color.BLUE.value["val"]:
        return np.array([11, 17, 212], dtype=np.uint8)
    if color == Color.GREEN.value["val"]:
        return np.array([11, 212, 45], dtype=np.uint8)
    if color == Color.YELLOW.value["val"]:
        return np.array([251, 247, 2], dtype=np.uint8)
    if color == Color.ORANGE.value["val"]:
        return np.array([251, 138, 2], dtype=np.uint8)
    return np.array([251, 2, 2], dtype=np.uint8)


def array_to_image(colors: np.array) -> Image:
    """
    Converts input array of ints to an Image

    :param colors: array of ints corresponding to Color enums
    :return: image from colors
    """

    # each color is put in a 10x10 box of pixels
    # maximum of 200 pixels across (20 colors)

    num_cols = min(200, colors.shape[0]*10)
    num_rows = ceil(colors.shape[0] / 20) * 10

    pixels = np.zeros(shape=(num_rows, num_cols, 3), dtype=np.uint8)
    for ind, color in enumerate(colors):
        pixel = color_to_rgb(color)
        x = int(ind / 20) * 10
        y = int(ind % 20) * 10
        for i in range(10):
            for j in range(10):
                pixels[x + i][y + j] = pixel
    return Image.fromarray(pixels)
