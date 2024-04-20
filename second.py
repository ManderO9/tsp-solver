import datetime
import json
import math
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming, solve_tsp_brute_force
from tsp_plot import plotTSP
import time
import csv
import requests


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
    # we need to specify if the destination should be the last node or not, if it should, we will change
    # the distance between the first and last node to be the minimum distance possible

    # File format is : WILAYA, Baladia, latitude, longitude
    with open('wilayas.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        lines = list(readCSV)

        # filtered = []
        # np.random.seed(1)

        # count = 10

        # for i in range(0, count):
        #     new_line = lines[np.random.randint(0, len(lines))]
        #     if filtered.__contains__(new_line):
        #         i -= 1
        #     else:
        #         filtered.append(new_line)

        filtered = [line for line in lines if line[0] == "Tipaza"]
        filtered = filtered[:9]

        nodes = [(float(line[2]), float(line[3]), line[0] + "_" + line[1]) for line in filtered]

    return nodes


app_id = "a2f023b2"
app_key = "b6e2714b3a274fa4236870001d6dfe44"

old_data = {
    "locations": [
        {
            "id": "source",
            "coords": {
                "lat": 51.51198245486377,
                "lng": -0.1278277598563
            }
        },
        {
            "id": "destination",
            "coords": {
                "lat": 51.51198245486377,
                "lng": -1.1278277598563
            }
        },
    ],
    "departure_searches": [
        {
            "id": "source-results",
            "departure_location_id": "source",
            "arrival_location_ids": ["source", "destination"],
            "departure_time": datetime.datetime.now().isoformat(sep="T", timespec="auto"),
            "travel_time": 9800,
            "properties": [
                "travel_time",
                "distance"
            ],
            "transportation": {
                "type": "driving"
            }
        }
    ]
}

nodes = get_nodes()

data = {
    "locations": [
        {
            "id": node[2],
            "coords": {
                "lat": node[0],
                "lng": node[1]
            }
        }
        for node in nodes
    ],
    "departure_searches": [
        {
            "id": f"{destination_node[2]}-results",
            "departure_location_id": destination_node[2],
            "arrival_location_ids": [node[2] for node in nodes],
            "departure_time": datetime.datetime.now().isoformat(sep="T", timespec="auto"),
            "travel_time": 11800,
            "properties": [
                "travel_time",
                "distance"
            ],
            "transportation": {
                "type": "driving"
            }
        }

        for destination_node in nodes
    ]
}


response = requests.post(
    'https://api.traveltimeapp.com/v4/time-filter',
    headers={
        'Content-Type': 'application/json',
        'X-Application-Id': app_id,
        'X-Api-Key': app_key
    },
    data=json.dumps(data)
)


print(response.status_code)

print(json.dumps(response.json(), indent=2))

exit(0)


start = time.time()

nodes = get_nodes()
distances = get_distances_for_nodes(nodes)

print(f"finished solving in {time.time() - start}s")

# permutation, distance = solve_tsp_dynamic_programming(distances)

# display_solution(nodes, permutation)
