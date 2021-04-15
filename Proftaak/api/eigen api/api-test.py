import requests
import json
import datetime
import mysql.connector
import pyodbc

test = requests.get('http://192.168.30.99:5000/babs/')
print(test.text)