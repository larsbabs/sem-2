import flask
from pythonping import *
import json
import configparser

# lezen van config file:
config = configparser.ConfigParser()
config.read(r"C:\Users\larsi\Documents\github\Proftaak\api\ping api\ip-config.ini")

#print(config['ping-ip'].items)

for key in config['ping-ip']:  
    print(key)