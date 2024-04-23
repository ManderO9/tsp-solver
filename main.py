import datetime
import json
import math
import numpy as np
from python_tsp.exact import solve_tsp_dynamic_programming, solve_tsp_brute_force
from tsp_plot import plotTSP
import time
import csv
import requests

from key import api_key


def get_distances_for_nodes(nodes):
    # nodes is a list of tuples (latitude, longitude)

    endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json?"

    addresses = ""

    # Set the source and destination addresses to the list of addresses that are passed in the nodes
    for node in nodes:
        addresses = addresses + node[2] + "|"
    addresses = addresses[:-1]

    url = endpoint + "destinations=" + addresses
    url = url + "&origins=" + addresses
    url = url + "&mode=driving&language=en-US"
    url = url + "&key=" + api_key

    response = requests.get(url)
    data = response.json()

    # data = {
    #     "destination_addresses":
    #     [
    #         "Bou Ismaïl, Algeria",
    #         "Bourkika, Algeria",
    #         "Chaiba, Algeria",
    #         "Cherchell, Algeria",
    #         "Damous, Algeria"
    #     ],
    #     "origin_addresses":
    #     [
    #         "Bou Ismaïl, Algeria",
    #         "Bourkika, Algeria",
    #         "Chaiba, Algeria",
    #         "Cherchell, Algeria",
    #         "Damous, Algeria"
    #     ],
    #     "rows":
    #     [
    #         {
    #             "elements":
    #             [
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "1 m",
    #                         "value": 0
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "1 min",
    #                         "value": 0
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "36.1 km",
    #                         "value": 36133
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "37 mins",
    #                         "value": 2201
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "4.6 km",
    #                         "value": 4605
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "12 mins",
    #                         "value": 720
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "56.2 km",
    #                         "value": 56190
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "50 mins",
    #                         "value": 2972
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "107 km",
    #                         "value": 106908
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "1 hour 48 mins",
    #                         "value": 6503
    #                     },
    #                     "status": "OK"
    #                 }
    #             ]
    #         },
    #         {
    #             "elements":
    #             [
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "36.1 km",
    #                         "value": 36071
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "38 mins",
    #                         "value": 2260
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "1 m",
    #                         "value": 0
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "1 min",
    #                         "value": 0
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "37.1 km",
    #                         "value": 37061
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "39 mins",
    #                         "value": 2363
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "35.1 km",
    #                         "value": 35078
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "41 mins",
    #                         "value": 2439
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "85.8 km",
    #                         "value": 85796
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "1 hour 40 mins",
    #                         "value": 5970
    #                     },
    #                     "status": "OK"
    #                 }
    #             ]
    #         },
    #         {
    #             "elements":
    #             [
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "4.6 km",
    #                         "value": 4596
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "12 mins",
    #                         "value": 705
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "33.9 km",
    #                         "value": 33853
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "35 mins",
    #                         "value": 2122
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "1 m",
    #                         "value": 0
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "1 min",
    #                         "value": 0
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "53.9 km",
    #                         "value": 53910
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "48 mins",
    #                         "value": 2894
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "105 km",
    #                         "value": 104629
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "1 hour 47 mins",
    #                         "value": 6424
    #                     },
    #                     "status": "OK"
    #                 }
    #             ]
    #         },
    #         {
    #             "elements":
    #             [
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "57.0 km",
    #                         "value": 57039
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "51 mins",
    #                         "value": 3074
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "36.2 km",
    #                         "value": 36182
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "42 mins",
    #                         "value": 2522
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "58.5 km",
    #                         "value": 58524
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "54 mins",
    #                         "value": 3210
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "1 m",
    #                         "value": 0
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "1 min",
    #                         "value": 0
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "50.1 km",
    #                         "value": 50114
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "1 hour 15 mins",
    #                         "value": 4506
    #                     },
    #                     "status": "OK"
    #                 }
    #             ]
    #         },
    #         {
    #             "elements":
    #             [
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "107 km",
    #                         "value": 106928
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "1 hour 47 mins",
    #                         "value": 6446
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "86.1 km",
    #                         "value": 86071
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "1 hour 38 mins",
    #                         "value": 5894
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "108 km",
    #                         "value": 108414
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "1 hour 50 mins",
    #                         "value": 6582
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "50.1 km",
    #                         "value": 50124
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "1 hour 13 mins",
    #                         "value": 4382
    #                     },
    #                     "status": "OK"
    #                 },
    #                 {
    #                     "distance":
    #                     {
    #                         "text": "1 m",
    #                         "value": 0
    #                     },
    #                     "duration":
    #                     {
    #                         "text": "1 min",
    #                         "value": 0
    #                     },
    #                     "status": "OK"
    #                 }
    #             ]
    #         }
    #     ],
    #     "status": "OK"
    # }

    count = len(data["destination_addresses"])

    distances = np.zeros((count, count))

    for row in range(0, count):
        for col in range(0, count):
            item = data['rows'][row]["elements"][col]
            time_seconds = item["duration"]["value"]
            # TODO: maybe should take distance also into consideration, not only time
            # distance_meters = item["distance"]["value"]

            distances[row, col] = time_seconds

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

    nodes = [
        (36.5718933, 1.9059603, "Gouraya, Tipaza, Algeria"),
        (36.642758, 2.6899362, "Bou Ismaïl, Tipaza, Algeria"),
        (36.4942993, 2.4775236, "Bourkika, Tipaza, Algeria"),
        (36.8276943, 7.7189892, "Chaiba, Tipaza, Algeria"),
        (36.6075021, 2.1901982, "Cherchell, Tipaza, Algeria"),
        (36.5487451, 1.705542, "Damous, Tipaza, Algeria"),
        (36.6737396, 2.7900902, "Douaouda, Tipaza, Algeria"),
        (36.6615638, 2.742117, "Fouka, Tipaza, Algeria"),
        (36.5121198, 2.4142888, "Hadjout, Tipaza, Algeria"),
        (36.5740991, 2.0537607, "Hadjret Ennous, Tipaza, Algeria"),
    ]
    return nodes



start = time.time()

nodes = get_nodes()

distances = get_distances_for_nodes(nodes)

permutation, distance = solve_tsp_dynamic_programming(distances)


print(f"finished solving in {time.time() - start}s")


print("solution is:")

for i in range(len(permutation)):
    print(nodes[permutation[i]][2])

display_solution(nodes, permutation)
