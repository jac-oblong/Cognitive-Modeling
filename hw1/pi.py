import numpy as np


def estimate_pi(num_points: int) -> float:
    points = np.random.uniform(low=-1.0, high=1.0, size=(num_points, 2))
    inside = np.array([point[0] ** 2 + point[1] ** 2 <= 1 for point in points])
    num_inside = inside.sum()
    pi = 4 * (num_inside / len(inside))
    return pi


numbers = [1, 10, 100, 1000, 10000, 50000, 100000, 500000, 1000000]
padding = len(str(max(numbers)))
for i in numbers:
    print(f"[{str(i).rjust(padding)}] pi = {estimate_pi(i)}")
