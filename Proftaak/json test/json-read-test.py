import json
import requests

location_data = requests.get('https://find3.pte2.nl/api/v1/by_location/oil230')

data = location_data.json()
#print(data["locations"][0]["total"])
#print(data["locations"][1]["total"])
#print(len(data["locations"][0]["devices"]))
count_1 = 0
count_2 = 0
probability_sensor_1 = 0
probability_sensor_2 = 0
probability_sensor_3 = 0
while True:
    probability_sensor_1 += data["locations"][0]["devices"][count_1]["probability"]
    count_1 += 1
    if count_1 == len(data["locations"][0]["devices"]):
        break
while True:
    probability_sensor_2 += data["locations"][1]["devices"][count_2]["probability"]
    count_2 += 1
    if count_2 == len(data["locations"][1]["devices"]):
        break
if data["locations"][0]["location"] != "scanner-1":
    print("Probability sensor Locatie 1: ", probability_sensor_1)
    print("Probability sensor Locatie 2: ", probability_sensor_2)
else:
    print("Probability sensor Locatie 2: ", probability_sensor_2)
    print("Probability sensor Locatie 1: ", probability_sensor_1)

def percent(loc_1, loc_2):
    total_prob = 0
    total_prob = loc_1 + loc_2
    percent_1 = loc_1 / total_prob
    percent_2 = loc_2 / total_prob
    percent_1 *= 100
    percent_2 *= 100
    print(percent_1, percent_2)

percent(probability_sensor_1, probability_sensor_2)