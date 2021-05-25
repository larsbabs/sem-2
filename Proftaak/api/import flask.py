import flask
from pythonping import *
import json
import configparser


# het lezen van de config file, dit doe ik in een functie zodat ie vanzelf wordt bijgewerkt zonder de API opnieuw op de starten
def config_read():
    config = configparser.ConfigParser()
    config.read(r'C:\Users\larsi\Documents\github\Proftaak\api\ping api\ip-config.ini')
    return config

# Maak een list van de IP's
def ipList():
    config = config_read()
    count = 0
    ip_list = []
    while True:
        ip_list.append(config['ping-ip'][nameList()[count]])
        count += 1
        if count == len(nameList()):
            break
    return ip_list

# Maak een list van de namen in de .ini file
def nameList():
    config = config_read()
    name_list = []
    for key in config['ping-ip']:
        name_list.append(key)
    return name_list

#starten van de API
app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Het maken van de apparte JSON stukjes per IP
def formatter_ping(name, ip):
    host_ping = ping(str(ip), verbose=False, timeout=0.2, count=4, df=False)
    formatted = '{"' + str(name) + '": {"ip": "' + str(ip) + '","online": ' + str(host_ping.success(1)).lower() + ', "response_time": ' + str(host_ping.rtt_avg_ms) + '} }'
    return formatted

# het achterelkaar zetten van de json stukjes per IP
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

# het afmaken van de JSON text
def formatter_json(text):
    before = '{"hosts": ['
    after = '], "message": "got pings", "sucess": true}'
    formatted_json = before + text + after
    return formatted_json


# Nieuwe manier van het maken van JSON bestanden:
def json_maker(name_list, ip_list):
    data = {}
    data['hosts'] = []
    count = 0
    while True:
        host_ping = ping(str(ip_list[count]), verbose=False, timeout=0.2, count=4, df=False)
        if host_ping.success(1):
            data['hosts'].append({
                'name': str(name_list[count]),
                'ip': str(ip_list[count]),
                'online': str(host_ping.success(1)),
                'response_time': str(host_ping.rtt_avg_ms)
            })
        else:
            data['hosts'].append({
                'name': str(name_list[count]),
                'ip': str(ip_list[count]),
                'online': str(host_ping.success(1)),
                'response_time': '-'
            })
        count += 1
        if count == len(ip_list):
            break
    return data

#print(json_maker(nameList(), ipList()))

# De http aanvraag voor de ping API
@app.route('/ping/', methods=['GET'])
def ping_test():
    return json_maker(nameList(), ipList())

# Dit is een test om het JSON format beter te laten zien in html format, nog niet gelukt
@app.route('/ping-html/', methods=['GET'])
def ping_test_html():
    if len(list_ip) == len(list_name):
        return test
    else: return "list length error"
app.run(host="0.0.0.0")