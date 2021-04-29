import flask
from pythonping import *
import json
#ip = "1.1.1.1"
#host_ping = ping(str(ip), verbose=False, timeout=0.8, count=4, df=False)
#babs = host_ping.rtt_avg_ms
def json_editor():

#    print(json_result_dict)
    print(json_result_dict['hosts'][0]['scanner_1']['ip'])
    print(json_result_dict['hosts'][0]['scanner_1']['online'])
    print(json_result_dict['hosts'][0]['scanner_1']['response_time'])

#    print(test)
    json_result = '{"hosts": [], "message": "got pings", "sucess": true}'
    json_result_dict = json.loads(json_result)
    test = json.dumps(json_result_dict, sort_keys=True, indent=4)
    f = open("data.json", "x")
    f.write(test)
    json_editor()


def json_adder(name, ip_ping):
    host_ping = ping(str(ip_ping), verbose=False, timeout=0.8, count=4, df=False)
    return '{"' + str(name) + '": {"ip": "' + ip_ping + '","online": ' + str(host_ping.success(1)).lower() + ', "response_time": ' + str(host_ping.rtt_avg_ms) + '} }'

def write_json(data, filename='data.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)
    with open('data.json') as json_file:
        data = json.load(json_file)
        
        temp = data['hosts']
        y = json_adder("scanner_2", "1.1.1.1")
#print(json_adder("scanner_2", "1.1.1.1"))
#write_json(json_adder("scanner_2", "1.1.1.1"))


#json_result = '{"hosts": [{"scanner_1": {"ip": "' + ip + '","online": ' + str(host_ping.success(1)).lower() + ', "response_time": ' + str(host_ping.rtt_avg_ms) + '} }], "message": "got pings", "sucess": true}'
test_list_ip = ["1.1.1.1", "8.8.8.8", "192.168.1.1", "2.2.2.2"]
test_list_name = ["babs", "google", "router", "test"]

def formatter_ping(name, ip):
    host_ping = ping(str(ip), verbose=False, timeout=0.8, count=4, df=False)
    formatted = '{"' + str(name) + '": {"ip": "' + str(ip) + '","online": ' + str(host_ping.success(1)).lower() + ', "response_time": ' + str(host_ping.rtt_avg_ms) + '} }'
    return formatted
#print(formatter("babs", "1.1.1.1"))

def list_formatter(ip_list, name_list):
    count = 0
    formatted_list = ""
    while True:
        formatted_list = formatted_list + formatter_ping(name_list[count], ip_list[count]) + ", "
        count += 1
        if count == len(ip_list):
            break
    formatted_list = formatted_list[:-2]
    return formatted_list

def formatter_json(text):
    before = '{"hosts": ['
    after = '], "message": "got pings", "sucess": true}'
    formatted_json = before + text + after
    return formatted_json
print(formatter_json(list_formatter(test_list_ip, test_list_name)))