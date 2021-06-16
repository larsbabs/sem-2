#importeren van de Library's
import flask
import mysql.connector
import configparser
from requests.api import get
from flask_cors import CORS

# Start de API app en zorg dat de CORS goed is
app = flask.Flask(__name__)
app.config["DEBUG"] = False
CORS(app)

# Het lezen van de config file voor de MySQL database
def config_read():
    config = configparser.ConfigParser()
    config.read('./config.ini')
    return config

# Maak er een globale var van
config = config_read()

# Maak connectie met de MySQL database
def connector():
    global mydb
    mydb = mysql.connector.connect(
    host=config['mysql']['host'],
    user="locations",
    password=config['mysql']['password'],
    database="locations",
    port=config['mysql']['port']
    )
    global mycursor
    mycursor = mydb.cursor()

# Haal de laatste data uit de MySQL database
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
    print("created database list")
    mycursor.close()
    return location_list

# Maak van de datalist een globale variabele en zorg dat hij elke kaar nieuwe data heeft
def createDataPoint():
    global data_list
    print("getting data from database")
    data_list = get_data()

# Reken het percentatge uit per learning point
def total_percent():
    count2 = 0
    total = 0
    while True:
        total = total + data_list[count2][0][3]
        count2 += 1
        if count2 == len(data_list):
            break
    print("calculating percent")
    return total

# Maak er een JSON formaat van voor de API
def json_maker():
    data = {}
    data['locations'] = []
    data['total'] = []
    data['total'].append({
        'total': total_percent()
    })
    count = 0
    percent = 0
    while True:
        percent_skeer = data_list[count][0][3] / total_percent() * 100
        percent = round(percent_skeer, 2)
        data['locations'].append({
            'location': data_list[count][0][2],
            'devices': data_list[count][0][3],
            'per_cent': percent,
            'date': data_list[count][0][0]
        })
        count += 1
        if count == len(data_list):
            break
    print("created json from data")
    return data

# Start de API op: /heatmap/
@app.route('/heatmap/', methods=['GET'])
def heatmap():
    createDataPoint()
    connector()
    return json_maker()
app.run(host="0.0.0.0", port="888")