

import numpy as np


data = {
   "destination_addresses" : 
   [
      "Bou Ismaïl, Algeria",
      "Bourkika, Algeria",
      "Chaiba, Algeria",
      "Cherchell, Algeria",
      "Damous, Algeria"
   ],
   "origin_addresses" : 
   [
      "Bou Ismaïl, Algeria",
      "Bourkika, Algeria",
      "Chaiba, Algeria",
      "Cherchell, Algeria",
      "Damous, Algeria"
   ],
   "rows" : 
   [
      {
         "elements" : 
         [
            {
               "distance" : 
               {
                  "text" : "1 m",
                  "value" : 0
               },
               "duration" : 
               {
                  "text" : "1 min",
                  "value" : 0
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "36.1 km",
                  "value" : 36133
               },
               "duration" : 
               {
                  "text" : "37 mins",
                  "value" : 2204
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "4.6 km",
                  "value" : 4605
               },
               "duration" : 
               {
                  "text" : "12 mins",
                  "value" : 720
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "56.2 km",
                  "value" : 56190
               },
               "duration" : 
               {
                  "text" : "50 mins",
                  "value" : 2978
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "107 km",
                  "value" : 106908
               },
               "duration" : 
               {
                  "text" : "1 hour 48 mins",
                  "value" : 6509
               },
               "status" : "OK"
            }
         ]
      },
      {
         "elements" : 
         [
            {
               "distance" : 
               {
                  "text" : "35.6 km",
                  "value" : 35576
               },
               "duration" : 
               {
                  "text" : "37 mins",
                  "value" : 2206
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "1 m",
                  "value" : 0
               },
               "duration" : 
               {
                  "text" : "1 min",
                  "value" : 0
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "37.1 km",
                  "value" : 37061
               },
               "duration" : 
               {
                  "text" : "39 mins",
                  "value" : 2349
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "35.1 km",
                  "value" : 35078
               },
               "duration" : 
               {
                  "text" : "41 mins",
                  "value" : 2461
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "85.8 km",
                  "value" : 85796
               },
               "duration" : 
               {
                  "text" : "1 hour 40 mins",
                  "value" : 5992
               },
               "status" : "OK"
            }
         ]
      },
      {
         "elements" : 
         [
            {
               "distance" : 
               {
                  "text" : "4.6 km",
                  "value" : 4596
               },
               "duration" : 
               {
                  "text" : "12 mins",
                  "value" : 705
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "33.9 km",
                  "value" : 33853
               },
               "duration" : 
               {
                  "text" : "36 mins",
                  "value" : 2135
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "1 m",
                  "value" : 0
               },
               "duration" : 
               {
                  "text" : "1 min",
                  "value" : 0
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "53.9 km",
                  "value" : 53910
               },
               "duration" : 
               {
                  "text" : "48 mins",
                  "value" : 2909
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "105 km",
                  "value" : 104629
               },
               "duration" : 
               {
                  "text" : "1 hour 47 mins",
                  "value" : 6440
               },
               "status" : "OK"
            }
         ]
      },
      {
         "elements" : 
         [
            {
               "distance" : 
               {
                  "text" : "57.0 km",
                  "value" : 57039
               },
               "duration" : 
               {
                  "text" : "51 mins",
                  "value" : 3074
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "36.2 km",
                  "value" : 36182
               },
               "duration" : 
               {
                  "text" : "42 mins",
                  "value" : 2540
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "58.5 km",
                  "value" : 58524
               },
               "duration" : 
               {
                  "text" : "54 mins",
                  "value" : 3217
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "1 m",
                  "value" : 0
               },
               "duration" : 
               {
                  "text" : "1 min",
                  "value" : 0
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "50.1 km",
                  "value" : 50114
               },
               "duration" : 
               {
                  "text" : "1 hour 15 mins",
                  "value" : 4506
               },
               "status" : "OK"
            }
         ]
      },
      {
         "elements" : 
         [
            {
               "distance" : 
               {
                  "text" : "107 km",
                  "value" : 106928
               },
               "duration" : 
               {
                  "text" : "1 hour 47 mins",
                  "value" : 6446
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "86.1 km",
                  "value" : 86071
               },
               "duration" : 
               {
                  "text" : "1 hour 39 mins",
                  "value" : 5912
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "108 km",
                  "value" : 108414
               },
               "duration" : 
               {
                  "text" : "1 hour 50 mins",
                  "value" : 6589
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "50.1 km",
                  "value" : 50124
               },
               "duration" : 
               {
                  "text" : "1 hour 13 mins",
                  "value" : 4382
               },
               "status" : "OK"
            },
            {
               "distance" : 
               {
                  "text" : "1 m",
                  "value" : 0
               },
               "duration" : 
               {
                  "text" : "1 min",
                  "value" : 0
               },
               "status" : "OK"
            }
         ]
      }
   ],
   "status" : "OK"
}



count = len(data["destination_addresses"])

distances = np.zeros((count, count))

for row in range(0, count):
    for col in range(0, count):
        item = data['rows'][row]["elements"][col]
        time_seconds = item["duration"]["value"]
        # TODO: maybe should take distance also into consideration, not only time
        # distance_meters = item["distance"]["value"]

        distances[row, col] = time_seconds



for index_1 in range(count):
    for index_2 in range(count):
        item = data['rows'][index_1]["elements"][index_2]
        source =      data["origin_addresses"]     [index_1]
        destination = data["destination_addresses"][index_2]
        time = item["duration"]["value"]
        time_text= item["duration"]["text"]
        distance = item["distance"]["value"]
        # format floating piont in print to only have 2 numbers after the decimal point
        print(f"distance is: {distance/1000:.1f}km, time is: {time/60:.2f}m -- text: {time_text} from: {source} to {destination}")
        


# check if the response status is ok
# If not, return an error to the client.
# For each row that you read
# Check it's status,

# If one of them is not ok, return an error to the client, saying, that we cannot calculate the best route
# cuz route information is not available, and don't try to send a request again, if something else is missing
# and the user can request again, send an error with a try again message.






# -- it will be presumed that the order of the addresses in the response is the same as the order of
# the addresses in the request in all fields, unless proven otherwise.
# -- rows in the response have the same order as the origins in the request, proof:
# https://developers.google.com/maps/documentation/distance-matrix/distance-matrix#DistanceMatrixRow


# response status: DistanceMatrixStatus
# https://developers.google.com/maps/documentation/distance-matrix/distance-matrix#DistanceMatrixStatus
# OK indicates the response contains a valid result.
# INVALID_REQUEST indicates that the provided request was invalid.
# MAX_ELEMENTS_EXCEEDED indicates that the product of origins and destinations exceeds the per-query limit.
# MAX_DIMENSIONS_EXCEEDED indicates that the number of origins or destinations exceeds the per-query limit.
# OVER_DAILY_LIMIT indicates any of the following:
#     The API key is missing or invalid.
#     Billing has not been enabled on your account.
#     A self-imposed usage cap has been exceeded.
#     The provided method of payment is no longer valid (for example, a credit card has expired). 
# OVER_QUERY_LIMIT indicates the service has received too many requests from your application within the allowed time period.
# REQUEST_DENIED indicates that the service denied use of the Distance Matrix service by your application.
# UNKNOWN_ERROR indicates a Distance Matrix request could not be processed due to a server error. The request may succeed if you try again. 



# row element status: DistanceMatrixElementStatus
# https://developers.google.com/maps/documentation/distance-matrix/distance-matrix#DistanceMatrixElementStatus
# OK indicates the response contains a valid result.
# NOT_FOUND indicates that the origin and/or destination of this pairing could not be geocoded.
# ZERO_RESULTS indicates no route could be found between the origin and destination.
# MAX_ROUTE_LENGTH_EXCEEDED indicates the requested route is too long and cannot be processed. 