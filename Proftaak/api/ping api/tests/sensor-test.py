import requests
import json




ping_response = requests.get('https://api.pte2.nl/ping/')
ping_data = ping_response.text

ping_json = json.loads(ping_data)
print(ping_json['hosts'])
