import json
from pythonping import *
ip = "1.1.1.1"
host_ping = ping(str(ip), verbose=False, timeout=0.8, count=4, df=False)
babs = '{"scanner_1": {"ip": "' + ip + '","online": ' + str(host_ping.success(1)).lower() + ', "response_time": ' + str(host_ping.rtt_avg_ms) + '} }'


with open('data.json', 'w') as data:
    json.dump(data['hosts'].append(babs), outfile)