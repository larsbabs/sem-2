import json
json_data = '{"hosts": [], "message": "got pings", "sucess": true}'
new_data = '{"external-router": {"ip": "10.10.1.1","online": true, "response_time": 0.26} }'
loaded_json = json.loads(json_data)
loaded_json.update(new_data)