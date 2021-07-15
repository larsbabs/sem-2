import json
import requests
#import json
import flask
import mysql.connector
import threading
import configparser
from requests.api import get
from flask_cors import CORS


def config_read():
    config = configparser.ConfigParser()
    config.read(r'C:\Users\larsi\Documents\github\Proftaak\monitoring-api\config.ini')
    return config

config = config_read()

mydb = mysql.connector.connect(
host=config['mysql']['host'],
user="locations",
password=config['mysql']['password'],
database="locations",
port=config['mysql']['port']
)

mycursor = mydb.cursor()



def get_data():
    count = 0
    location_list = []
    while True:
        point1 = mycursor.execute("SELECT * FROM `locations` WHERE locations = 'point" + str((count + 1)) + "' ORDER BY `id` DESC LIMIT 1")
        myresult = mycursor.fetchall()
        count += 1
        location_list.append(myresult)
        if count == 5:
            break
    return location_list

while True:
    print('vul iets in, press 3 to terminate te program')
    babs = input()
    if babs == '1':
        print('you entered 1')
        continue
    elif babs == '2':
        print('you entered 2')
        print(get_data())
    elif babs == '3':
        break
print('program has stopped')