import numpy as np
import matplotlib.pyplot as plt
from python_tsp.exact import solve_tsp_dynamic_programming, solve_tsp_brute_force
from tsp_plot import plotTSP


# Get the list of nodes
nodes = [
    (42, 21), (32, 32), (6, 6),
    (4, 5), (32, 52), (23, 64),
    (65, 76), (45, 6), (76, 7),
    (23, 42), (76, 32), (23, 76),
    (32, 23), (65, 32), (32, 65),]

# Create the distance matrix
distances = np.zeros((len(nodes), len(nodes)))

# Get the distance between all nodes
for row in range(0, len(nodes)):
    for col in range(0, len(nodes)):
        distances[row, col] = np.linalg.norm(np.array(nodes[row]) - np.array(nodes[col]))


# Compute the optimal path and the total distance
# Source to the solver algorithm: https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm#cite_note-5
# Paper about dynamic programming: https://core.ac.uk/download/pdf/154419746.pdf
# TODO: define a maxsize value
permutation, distance = solve_tsp_dynamic_programming(distances)

# Plot the result
plotTSP([permutation], nodes)



