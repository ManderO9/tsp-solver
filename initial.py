import math
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming, solve_tsp_brute_force
from tsp_plot import plotTSP
import time
import csv


def get_distances_for_nodes(nodes):
    # nodes is a list of tuples (latitude, longitude)

    distances = np.zeros((len(nodes), len(nodes)))

    for row in range(0, len(nodes)):
        for col in range(0, len(nodes)):
            (latitude1, longitude1) = (nodes[row][0], nodes[row][1])
            (latitude2, longitude2) = (nodes[col][0], nodes[col][1])
            distance = math.acos(math.sin(latitude1) * math.sin(latitude2) +
                                 math.cos(latitude1) * math.cos(latitude2) * math.cos(longitude2-longitude1)
                                 ) * 6371
            distances[row, col] = distance

    return distances


def display_solution(nodes, permutation):
    # nodes is a list of tuples (latitude, longitude)
    # permutation is a list of indexes of nodes

    # Latitude is specified in degrees within the range [-90, 90].
    # Longitude is specified in degrees within the range [-180, 180].

    # Normalize the nodes values
    max_latitude = np.max([node[0] for node in nodes])
    max_longitude = np.max([node[1] for node in nodes])

    # Calculate min longitude and latitude
    min_latitude = np.min([node[0] for node in nodes])
    min_longitude = np.min([node[1] for node in nodes])

    # Normalize the nodes values
    nodes = [((node[0] - min_latitude) / (max_latitude-min_latitude),
              (node[1] - min_longitude) / (max_longitude-min_longitude)
              ) for node in nodes]

    # Plot the result
    plotTSP([permutation], nodes)


def get_nodes():
    # From the returned result, we will assume that the source is the first node in the list
    # and the destination is the last node in the list

    # File format is : WILAYA, Baladia, latitude, longitude
    with open('wilayas.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        lines = list(readCSV)

        filtered = []
        np.random.seed(1)

        count = 10

        for i in range(0, count):
            new_line = lines[np.random.randint(0, len(lines))]
            if filtered.__contains__(new_line):
                i -= 1
            else:
                filtered.append(new_line)

        nodes = [(float(line[2]), float(line[3])) for line in filtered]

    return nodes


start = time.time()

nodes = get_nodes()
distances = get_distances_for_nodes(nodes)
permutation, distance = solve_tsp_dynamic_programming(distances)

print(f"finished solving in {time.time() - start}s")

display_solution(nodes, permutation)
