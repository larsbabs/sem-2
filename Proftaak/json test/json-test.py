import json
data = {}

data['hosts'] = []
data['hosts'].append({
    'name': 'find-3-server',
    'ip': '10.10.1.10',
    'online': True,
    'response_time': 0.4
})
data['hosts'].append({
    'name': 'skie',
    'ip': '10.10.1.10',
    'online': True,
    'response_time': 0.4
})

with open('data_file.json', 'w') as write_file:
    json.dump(data, write_file)