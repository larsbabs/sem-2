import requests
import json
import datetime
import mysql.connector
import pyodbc

location_data_all = requests.get('https://pte2.duckdns.org/api/v1/locations/eersel')
locoation_database = requests.get("https://pte2.duckdns.org/api/v1/database/eersel")
file_name_pre = "response"
date = datetime.datetime.now()
date_format = str(date.strftime("%d")) + "-" + str(date.strftime("%m")) + "-" + str(date.strftime("%Y")) + "_" + str(date.strftime("%H")) + "-" + str(date.strftime("%M")) + "-" + str(date.strftime("%S"))

#aanmaken van het .json bestand met de API request:
def jprint(obj, file_name):

  datum = datetime.datetime.now()
  text = json.dumps(obj, sort_keys=True, indent=4)
  #datum in een str zetten
  date = str(datum.strftime("%d")) + "-" + str(datum.strftime("%m")) + "-" + str(datum.strftime("%Y")) + "_" + str(datum.strftime("%H")) + "-" + str(datum.strftime("%M")) + "-" + str(datum.strftime("%S"))

  f = open(file_name + "_" + date + ".json", "x")
  f.write(text)
#  print(text)


#aanvragen van de functie:
jprint(location_data_all.json(), file_name_pre)


#Connectie maken met de database
mydb = mysql.connector.connect(
  host="192.168.30.99",
  user="iraca",
  password="RALT_Ir@ca_60",
  port="3307",
  database="find3"
)
#cursor instellen:
mycursor = mydb.cursor()
print(locoation_database.text)
#Het openen van het net opgeslagen .json bestand:
#with open(file_name_pre + "_" + date_format + ".json") as f:
#  data_file = json.load(f)

#print(data_file["locations"][0]["sensors"]["s"]["wifi"])

## Kijken of de tabellen al bestaan:
def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True
    dbcur.close()
    mycursor.execute("CREATE TABLE find3_test (time INT(10) NULL DEFAULT NULL, mac INT(10) NULL DEFAULT NULL, strenth INT(10) NULL DEFAULT NULL, device INT(10) NULL DEFAULT NULL, family INT(10) NULL DEFAULT NULL)")
    return False

#print(checkTableExists(mydb, "devices"))
#mycursor.execute("SHOW TABLES")

#De bestaande tabellen printen:
#for x in mycursor:
#  print(x)

#Regels sorteren als ze beginnen met INSERT:
#with open(locoation_database.text) as a_file:
#  for line in a_file:
#    stripped_line = line.strip()
#    if stripped_line.startswith("INSERT"):

f = locoation_database.text
all_sql_lines = f.splitlines()


i = 0
insert_lines = []
sql_counter = 0


while True:
  if "INSERT" in all_sql_lines[i]:
    print('success')
    insert_lines.append(all_sql_lines[i])
    #sql_counter = sql_counter + 1
    #print(sql_counter) 
  else:
    print("Er zit geen INSERT in")
  i = i + 1
  if i == len(all_sql_lines):
    break

counter_pounter = 0
#print(insert_lines[4])
#while True: 
  #mycursor.execute(insert_lines[counter_pounter])
#  if counter_pounter == len(insert_lines):
#    break
#  counter_pounter =+1

new_insert_list = []
new_insert_list_2 = []
new_insert_list_3 = []
new_insert_list_4 = []
count = 0

while True:
  new_insert_list.append(insert_lines[count].replace('"gps"', 'gps'))
  new_insert_list_2.append(new_insert_list[count].replace('"devices"', 'devices'))
  new_insert_list_3.append(new_insert_list_2[count].replace('"keystore"', 'keystore'))
  new_insert_list_4.append(new_insert_list_3[count].replace('"sensors"', 'sensors'))
  count += 1
#  print(count)
  if count == len(insert_lines):
    break


#new_insert_list_4.pop(0)

#print(new_insert_list_4[12])
counter = 0
print(len(new_insert_list_4))

#new_insert_list_4.pop(0)

while True:
  if counter == len(new_insert_list_4):
    break
  mycursor.execute(new_insert_list_4[counter])
  print(counter)
  counter += 1









#print(locoation_database.text)

#for line in locoation_database.text:
#    rec = line.strip()
#    if rec.startswith('IN'):# or rec.startswith('Referer'):
#       print(line)
##mycursor.execute(
"""CREATE TABLE devices (id TEXT PRIMARY KEY, name TEXT);
INSERT INTO "devices" VALUES ('b','thinkpad');
CREATE TABLE gps (id INTEGER PRIMARY KEY, timestamp INTEGER, mac TEXT, loc TEXT, lat REAL, lon REAL, alt REAL);
INSERT INTO "gps" VALUES(1,1616953331489,'wifi-ba:95:75:30:88:bc','',12.1,10.1,54.0);
INSERT INTO "gps" VALUES(2,1616953331489,'wifi-e2:63:da:19:f1:c4','',12.1,10.1,54.0);
INSERT INTO "gps" VALUES(3,1616953331489,'wifi-e2:63:da:29:f1:c5','',12.1,10.1,54.0);
INSERT INTO "gps" VALUES(4,1616953331489,'wifi-e4:57:40:18:62:a6','',12.1,10.1,54.0);
INSERT INTO "gps" VALUES(5,1616953331489,'wifi-3e:94:ed:34:9b:e5','',12.1,10.1,54.0);
INSERT INTO "gps" VALUES(6,1616953331489,'wifi-68:02:b8:49:4c:68','',12.1,10.1,54.0);
INSERT INTO "gps" VALUES(7,1616953331489,'wifi-6a:02:98:49:4c:6d','',12.1,10.1,54.0);
INSERT INTO "gps" VALUES(8,1616953331489,'wifi-e2:63:da:19:f1:c5','',12.1,10.1,54.0);
INSERT INTO "gps" VALUES(9,1616953331489,'wifi-68:02:b8:49:4c:6d','',12.1,10.1,54.0);
INSERT INTO "gps" VALUES(10,1616953331489,'wifi-80:2a:a8:94:eb:94','',12.1,10.1,54.0);
INSERT INTO "gps" VALUES(11,1616953331489,'wifi-82:2a:a8:94:eb:94','',12.1,10.1,54.0);
CREATE TABLE keystore (key text not null primary key, value text);
INSERT INTO "keystore" VALUES('sensorDataStringSizer','"{\"encoding\":{\"3e:94:ed:34:9b:e5\":\"e\",\"68:02:b8:49:4c:68\":\"f\",\"68:02:b8:49:4c:6d\":\"a\",\"6a:02:98:49:4c:6d\":\"g\",\"80:2a:a8:94:eb:94\":\"b\",\"82:2a:a8:94:eb:94\":\"c\",\"ba:95:75:30:88:bc\":\"h\",\"e2:63:da:19:f1:c4\":\"i\",\"e2:63:da:19:f1:c5\":\"d\",\"e2:63:da:29:f1:c5\":\"j\",\"e4:57:40:18:62:a6\":\"k\"},\"current\":11}"');
CREATE TABLE location_predictions (timestamp integer NOT NULL PRIMARY KEY, prediction TEXT, UNIQUE(timestamp));
CREATE TABLE locations (id TEXT PRIMARY KEY, name TEXT);
CREATE TABLE sensors (timestamp integer not null primary key, deviceid text, locationid text, bluetooth text, wifi text, unique(timestamp));
INSERT INTO "sensors" VALUES(1616953331489,'b','','','"a":-77,"b":-94,"c":-93,"d":-79,"e":-94,"f":-95,"g":-77,"h":-96,"i":-74,"j":-79,"k":-95');
CREATE INDEX keystore_idx on keystore(key);
CREATE INDEX devices_name on devices (name);
CREATE INDEX sensors_devices ON sensors (deviceid);
COMMIT;"""
#)
#print(locoation_database.text)
babsbabsbabsssssskie
#print("git commit/clone test pc")