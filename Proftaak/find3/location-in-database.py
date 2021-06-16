#Library's importeren
import mysql.connector
import requests
import configparser
from datetime import datetime
import threading


def whole_program():
    #Het herhalen van functie: "whole_program" zodat hij elke 2 minuten draait.
    threading.Timer(120.0, whole_program).start()
    now = datetime.now()

    #Het ophalen van de Find3 data
    def get_data():
        try:
            data = requests.get('https://find3.pte2.nl/api/v1/by_location/oil231')
            print(str(now) + ", Request made to the Find3 server")
        except requests.ConnectionError:
            print(str(now) + ", No Request made to the Find3 server, no connection to find3")
        return data.json()
    #Het lezen van de config file voor de MySQL inloggevens.
    def config_read():
        config = configparser.ConfigParser()
        config.read(r'C:\Users\larsi\Documents\github\Proftaak\find3\config.ini')
        return config
    config = config_read()

    #Connectie maken met de datbase en daarna de data erin zetten.
    def mysql_inserter():
        mydb = mysql.connector.connect(
        host=config['mysql']['host'],
        user=config['mysql']['username'],
        password=config['mysql']['password'],
        database=config['mysql']['database'],
        port=config['mysql']['port']
        )
        data = get_data()
        count = 0

        #loop voor de data insertion
        while True:
            devices = data["locations"][count]["total"]
            locations = data["locations"][count]["location"]
            mycursor = mydb.cursor()
            sql = "INSERT INTO locations (locations, devices) VALUES (%s, %s)"
            val = (locations, devices)
            mycursor.execute(sql, val)
            mydb.commit()
            count += 1
            if count == len(data["locations"]):
                break
    mysql_inserter()
whole_program()