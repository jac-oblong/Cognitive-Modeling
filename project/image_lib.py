import matplotlib.pyplot as plt
from simulator_lib import *

def color_to_rgb(color):
    match color:
        case 0: # violet
            return (72, 5, 118)
        case 1: # blue
            return (11, 17, 212)
        case 2: # green
            return (11, 212, 45)
        case 3: # yellow
            return (251, 247, 2)
        case 4: # orange
            return (251, 138, 2)
        case 5: # red
            return (251, 2, 2)


def array_to_image(in_arr):
    image = []
    for i in range(100):
        arr = []
        for j in range(100):
            pixel = color_to_rgb(in_arr[i][j])
            arr.append(pixel)
        image.append(arr)
    return image