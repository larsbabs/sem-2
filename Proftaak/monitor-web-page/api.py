import flask
from requests.api import get
import mysql.connector
import configparser


app = flask.Flask(__name__)
app.config["DEBUG"] = True

def config_read():
    config = configparser.ConfigParser()
    config.read('./config.ini')
    return config

config = config_read()
def mysqlConnect():
    global mydb_tabel
    global mycursor_tabel
    mydb_tabel = mysql.connector.connect(
    host=config['mysql2']['host'],
    user=config['mysql2']['username'],
    password=config['mysql2']['password'],
    database=config['mysql2']['database'],
    port=config['mysql2']['port']
    )

    mycursor_tabel = mydb_tabel.cursor()

def get_data_tabel():
    count = 0
    location_list = []
    while True:
        point1 = mycursor_tabel.execute("SELECT * FROM `test` WHERE hostname = 'pte2scanner" + str((count + 1)) + "' ORDER BY `id` DESC LIMIT 1")
        myresult = mycursor_tabel.fetchall()
        count += 1
        location_list.append(myresult)
        if count == 5:
            break
    print("created database list")
    mycursor_tabel.close()
    return location_list

def htmlFormat():
    sqlData = get_data_tabel()
    scanner1Data = "babs"
    data = """
<table border=1>
<tr><td>Scanner-Name</td><td>CPU</td><td>RAM</td><td>Disk</td><td>last Online</td><td>12connect-IP</td></tr>
<tr><td>Scanner-1</td><td>""" + str(sqlData[0][0][2]) + """</td><td>""" + str(sqlData[0][0][6]) + """</td><td>""" + str(sqlData[0][0][3]) + """</td><td>""" + "UTC " + str(sqlData[0][0][1]) + """</td><td>""" + str(sqlData[0][0][5]) + """</td></tr>
<tr><td>Scanner-2</td><td>""" + str(sqlData[1][0][2]) + """</td><td>""" + str(sqlData[1][0][6]) + """</td><td>""" + str(sqlData[1][0][3]) + """</td><td>""" + "UTC " + str(sqlData[1][0][1]) + """</td><td>""" + str(sqlData[1][0][5]) + """</td></tr>
<tr><td>Scanner-3</td><td>""" + str(sqlData[2][0][2]) + """</td><td>""" + str(sqlData[2][0][6]) + """</td><td>""" + str(sqlData[2][0][3]) + """</td><td>""" + "UTC " + str(sqlData[2][0][1]) + """</td><td>""" + str(sqlData[2][0][5]) + """</td></tr>
<tr><td>Scanner-4</td><td>""" + str(sqlData[3][0][2]) + """</td><td>""" + str(sqlData[3][0][6]) + """</td><td>""" + str(sqlData[3][0][3]) + """</td><td>""" + "UTC " + str(sqlData[3][0][1]) + """</td><td>""" + str(sqlData[3][0][5]) + """</td></tr>
</table>
<button onClick="window.location.reload();">Refresh Page</button>
"""
    return data


@app.route('/ping/', methods=['GET'])
def ping_test():
    mysqlConnect()
    return htmlFormat()  
app.run(host="0.0.0.0", port="8080")