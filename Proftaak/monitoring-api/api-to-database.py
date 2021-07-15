import requests
#import json
#import flask
import mysql.connector
import threading
import configparser
def config_read():
    config = configparser.ConfigParser()
    config.read(r'C:\Users\larsi\Documents\github\Proftaak\monitoring-api\config.ini')
    return config

config = config_read()

mydb = mysql.connector.connect(
host=config['mysql']['host'],
user=config['mysql']['username'],
password=config['mysql']['password'],
database=config['mysql']['database'],
port=config['mysql']['port']
)

mycursor = mydb.cursor()

def nameList(ini_name):
    config = config_read()
    name_list = []
    for key in config[ini_name]:
        name_list.append(key)
    return name_list

print(nameList("scanner_names"))
print(nameList("scanner_urls"))

# het lezen van de config file, dit doe ik in een functie zodat ie vanzelf wordt bijgewerkt zonder de API opnieuw op de starten
def json_maker_unreachable(device_name):
    data = {}
    data['device-info'] = []
    data['device-info'].append({
        'hostname': str(device_name),
        'ip': '0',
        'cpu': '0',
        'disk': '0',
        'memory': '0'
    })
    return data

def mysql_inserter(data):
    sql = "INSERT INTO test (cpu, disk, hostname, ip, memory) VALUES (%s, %s, %s, %s, %s)"
    val = (data["device-info"][0]["cpu"], data["device-info"][0]["disk"], data["device-info"][0]["hostname"], data["device-info"][0]["ip"], data["device-info"][0]["memory"])
    mycursor.execute(sql, val)

    mydb.commit()

def get_request():
    count = 0
    url_list = ['http://10.10.3.10:8080/sys-info/', 'http://10.10.3.11:8080/sys-info/', 'http://10.10.3.12:8080/sys-info/', 'http://10.10.3.13:8080/sys-info/']
    device_list = ['pte2scanner1', 'pte2scanner2', 'pte2scanner3', 'pte2scanner4']
    while True:
        print(count)
        try:
            response = requests.get(url_list[count])
        except requests.ConnectionError:
            mysql_inserter(json_maker_unreachable(device_list[count]))
            print(device_list[count], " is not reachable")
        else:
            mysql_inserter(response.json())
            print(response.text)
        count += 1
        if count == len(url_list):
            break


#get_request()


def poep():

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




    mysql_inserter(scanner1_json)
    mysql_inserter(scanner2_json)
    mysql_inserter(scanner3_json)
    mysql_inserter(scanner4_json)
    #whole_program()