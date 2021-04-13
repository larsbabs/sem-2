#In deze code moet je een SQlite bestandje downloaden en of inladen.
#Daarna kan ik die door een library halen om het te converteren naar een MySQL formaat.
#Eventueel kan ik ook nog kijken naar het Json gedeelte
import threading
import os
import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.30.99",
  user="iraca",
  password="RALT_Ir@ca_60",
  database="find3",
  port="3307"
)
mycursor = mydb.cursor()
sql = ["devices", "gps", "keystore", "locations", "location_predictions", "sensors"]


#os.system('docker cp find3_find3_1:/data/data/xUq8pGzb.sqlite3.db /home/pte2/sqlite3/oil230-data.sqlite3.db')
#os.system('sqlite3mysql -f /home/pte2/sqlite3/oil230-data.sqlite3.db -d "find3" -u "find3" -p "Lekkerhoor12@" -h "10.10.1.12"')


def printit():
  threading.Timer(5.0, printit).start()
  print("Hello, World!")

#printit()
counter = 0
mycursor.execute("SHOW TABLES")
tables = mycursor.fetchall() 
print(tables)
print(sql)
list_len = len(sql)

print("yoooo dababy", sql[4])
while True:
#    print(sql[counter])
#    print(counter)
#    sql_ding = ""
#    sql_ding = "DROP TABLE " + sql[counter]
#    print(sql_ding)
    mycursor.execute("DROP TABLE IF EXISTS " + sql[counter])
    counter += 1
    if counter  == list_len:
        break
