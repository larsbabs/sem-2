import flask
from pythonping import *
import json
app = flask.Flask(__name__)
app.config["DEBUG"] = True

list_ip = ["10.10.1.1", "10.10.2.1", "10.10.2.152", "10.10.2.153", "10.10.2.154", "10.10.1.10"]
list_name = ["external-router", "internal-router", "scanner-1", "scanner-2", "scanner-3", "find3-server"]

def formatter_ping(name, ip):
    host_ping = ping(str(ip), verbose=False, timeout=0.2, count=4, df=False)
    formatted = '{"' + str(name) + '": {"ip": "' + str(ip) + '","online": ' + str(host_ping.success(1)).lower() + ', "response_time": ' + str(host_ping.rtt_avg_ms) + '} }'
    return formatted

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


test = "<h1>" + json.dumps(json.loads(formatter_json(list_formatter(list_ip, list_name))), sort_keys=False, indent=4) + "</h1>"

@app.route('/ping/', methods=['GET'])
def ping_test():
    if len(list_ip) == len(list_name):
        return formatter_json(list_formatter(list_ip, list_name))
    else: return "list length error"
@app.route('/ping-html/', methods=['GET'])
def ping_test_html():
    if len(list_ip) == len(list_name):
        return test
    else: return "list length error"
app.run(host="0.0.0.0")