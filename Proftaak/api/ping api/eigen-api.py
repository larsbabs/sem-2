import flask
from pythonping import *
import json
app = flask.Flask(__name__)
app.config["DEBUG"] = True
#books = open("./books.json")
scanner1_ip = "2.2.2.2"

ip_list = ["1.1.1.1", "8.8.8.8", "192.168.1.1", "2.2.2.2"]
def online_tester(ip):
    host_ping = ping(str(ip), verbose=False, timeout=0.8, count=4, df=True)
    if host_ping.success(1):
        result = "Host " + str(ip) + " is online "
    else:
        result = "Host " + str(ip) + " is offline"
    return result

def json_editor():
    json_result = '{hosts:}'
    json_result_dict = json.loads(json_result)


test_list_ip = ["1.1.1.1", "8.8.8.8", "192.168.1.1", "2.2.2.2"]
test_list_name = ["babs", "google", "router", "test"]

def formatter_ping(name, ip):
    host_ping = ping(str(ip), verbose=False, timeout=0.2, count=4, df=False)
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

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
@app.route('/api/v1/books/test/', methods=['GET'])
def babs():
    return books.read()
@app.route('/babs/', methods=['GET'])
def test():
    return "1"
@app.route('/api/v1/antwoord1/', methods=['GET'])
def antwoord_test():
    return 'Jullie hebben het goed: <a href="https://groep3.eersel.duckdns.org/qrcode3.png">link</a>'
@app.route('/ping/', methods=['GET'])
def pinger():
    count = 0
    skie = ""
    while True:
        skie = skie + "\n" + str((online_tester(ip_list[count]))) + "\n"
        count += 1
        if count == len(ip_list):
            break
    return skie
@app.route('/kanker/', methods=['GET'])
def ping_test():
    return formatter_json(list_formatter(test_list_ip, test_list_name))
app.run(host="0.0.0.0")

#    scanner1_ping = ping(scanner1_ip, verbose=True, timeout=0.8, count=4, df=True)
#    if scanner1_ping.success(1):
#        ping_return = "scanner 1 is online"
##    else:
 #       ping_return = "scanner 1 is offline"