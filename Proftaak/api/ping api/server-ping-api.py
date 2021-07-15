import flask
from pythonping import *
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

# Nieuwe manier van het maken van JSON bestanden:
def json_maker(name_list, ip_list):
    data = {}
    data['hosts'] = []
    data['online-hosts'] = {}
    data['offline-hosts'] = {}
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