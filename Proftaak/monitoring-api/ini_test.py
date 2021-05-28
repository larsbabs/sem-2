import requests
#import json
import flask
import mysql.connector
import threading
import configparser
import dotenv


def config_read():
    config = configparser.ConfigParser()
    config.read(r'C:\Users\babs\Documents\sem-2\Proftaak\monitoring-api\config.ini')
    return config
config = config_read()
print(config['example']['poep'])