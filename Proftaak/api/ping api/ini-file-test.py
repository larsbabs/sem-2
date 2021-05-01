import flask
from pythonping import *
import json
import configparser

# lezen van config file:
config = configparser.ConfigParser()
config.read("ip-config.ini")

# Maak een list van de namen in de .ini file
def nameList():
    name_list = []
    for key in config['ping-ip']:
        name_list.append(key)
    return name_list

# Maak een list van de IP's
def ipList():
    count = 0
    ip_list = []
    while True:
        ip_list.append(config['ping-ip'][nameList()[count]])
        count += 1
        if count == len(nameList()):
            break
    return ip_list
print(nameList)
print(ipList())