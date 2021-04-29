import requests
import json
ping_response = requests.get('https://api.pte2.nl/ping/')
ping_data = ping_response.text

ping_json = json.loads(ping_data)

if ping_json['hosts'][0]['external-router']['online']:
    print("online")
else: print("offline")