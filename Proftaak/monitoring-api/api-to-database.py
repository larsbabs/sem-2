import requests
#import json
#import flask
import mysql.connector
import threading
import configparser
import dotenv

# het lezen van de config file, dit doe ik in een functie zodat ie vanzelf wordt bijgewerkt zonder de API opnieuw op de starten
def config_read():
    config = configparser.ConfigParser()
    config.read(r'C:\Users\babs\Documents\sem-2\Proftaak\monitoring-api\config.ini')
    return config
def whole_program():
    threading.Timer(5.0, whole_program).start()
    config = config_read()
    scanner_1_get = requests.get('http://10.10.3.10:8080/sys-info/')
    scanner_2_get = requests.get('http://10.10.3.11:8080/sys-info/')
    scanner_3_get = requests.get('http://10.10.3.12:8080/sys-info/')
    scanner_4_get = requests.get('http://10.10.3.13:8080/sys-info/')
    scanner1_json = scanner_1_get.json()
    scanner2_json = scanner_2_get.json()
    scanner3_json = scanner_3_get.json()
    scanner4_json = scanner_4_get.json()
    #print(scanner_1_get.text, scanner_2_get.text, scanner_3_get.text, scanner_4_get.text)
#    print(scanner1_json["device-info"][0]["cpu"])

    mydb = mysql.connector.connect(
    host=config['mysql']['host'],
    user=config['mysql']['username'],
    password=config['mysql']['password'],
    database=config['mysql']['database'],
    port=config['mysql']['port']
    )

    mycursor = mydb.cursor()

    def mysql_inserter(data):
        sql = "INSERT INTO test (cpu, disk, hostname, ip, memory) VALUES (%s, %s, %s, %s, %s)"
        val = (data["device-info"][0]["cpu"], data["device-info"][0]["disk"], data["device-info"][0]["hostname"], data["device-info"][0]["ip"], data["device-info"][0]["memory"])
        mycursor.execute(sql, val)

        mydb.commit()

    mysql_inserter(scanner1_json)
    mysql_inserter(scanner2_json)
    mysql_inserter(scanner3_json)
    mysql_inserter(scanner4_json)
whole_program()