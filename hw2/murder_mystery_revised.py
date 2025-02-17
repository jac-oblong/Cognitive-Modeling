import numpy as np

# number of simulation runs
N = 10000
# student names
STUDENTS = ["Bob", "Brandon", "Billy", "Bart", "Ben"]


def choose_hat():
    return np.random.choice(["A", "B"], p=(0.5, 0.5))


def observation_model(hat: str):
    if hat == "A":
        return np.random.choice(STUDENTS, p=(0.25, 0.25, 0.5, 0, 0))
    return np.random.choice(STUDENTS, p=(0.2, 0.2, 0, 0.4, 0.2))


def run_simulation():
    hat = choose_hat()
    student = observation_model(hat)
    return f"{hat}-{student}"


# running simulation and calculating probabilities
gen_simulations = np.frompyfunc(run_simulation, 0, 1)
simulations = gen_simulations(np.empty(N, dtype=object))
unique, counts = np.unique(simulations, return_counts=True)
probs = counts / N

# printing table
print("|         |  Hat A |  Hat B |")
for s in STUDENTS:
    a = np.where(unique == f"A-{s}")[0]
    b = np.where(unique == f"B-{s}")[0]
    probA = probs[a[0]] if len(a) == 1 else 0
    probB = probs[b[0]] if len(b) == 1 else 0
    print(f"| {s:<7} | {probA:.4f} | {probB:.4f} |")
