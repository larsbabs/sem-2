from flask import Flask
from flask import request
from psutil import cpu_percent
import mysql.connector
import configparser
from datetime import datetime
def config_read():
    config = configparser.ConfigParser()
    config.read(r'C:\Users\larsi\Documents\github\Proftaak\monitoring-api\config.ini')
    return config
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
config = config_read()

app = Flask(__name__)

@app.route('/monitor')
def query_example():

    cpu = request.args.get('cpu')
    disk = request.args.get('disk')
    memory = request.args.get('memory')
    hostname = request.args.get('hostname')
    ip = request.args.get('ip')
    print(cpu, disk, memory, hostname, ip)

    def mysql_inserter():
        mydb = mysql.connector.connect(
        host=config['mysql']['host'],
        user=config['mysql']['username'],
        password=config['mysql']['password'],
        database=config['mysql']['database'],
        port=config['mysql']['port']
        )

        mycursor = mydb.cursor()
        sql = "INSERT INTO test (cpu, disk, hostname, ip, memory) VALUES (%s, %s, %s, %s, %s)"
        val = (cpu, disk, hostname, ip, memory)
        mycursor.execute(sql, val)

        mydb.commit()

    mysql_inserter()
    return '200'
app.run(host="0.0.0.0", port="8080")