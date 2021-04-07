# API
hierin staan vooral bestanden waarmee ik ben gaan testen en oefenen met een api in Python. Ook probeer ik die api te combineren met een Database zodat andere mensen straks erbij kunnen om meer met de data te kunnen doen.

## Deze code heeft 4 onderdelen/taken
### 1. Het opvragen van de informatie
doormiddel van een GET request kan ik de FIND3 informatie uit de database halen. Er zijn **2** verschillende soorten requests, ik heb ze alletwee gebruikt en gekeken welke het makkelijkst is.


```Python
location_data_all = requests.get("https://pte2.duckdns.org/api/v1/locations/eersel") #JSON request
locoation_database = requests.get("https://pte2.duckdns.org/api/v1/database/eersel") #DataBase request
```

Het **database** request geeft in een SQLite format de SQL data door, deze moet je dus converteren naar het MySQL format.
Het **JSON** request geeft een JSON bestandje. Deze kan je dan strakts lezen en uit elkaar halen om de informatie te verdelen

### 2. Een bestand aanmaken:
Voor de JSON request is het handig om de response in een bestandje te zetten, dit is makkelijk te doen met **write**.
Voor de naam van het bestandje gebruik ik de **datetime** library, zo kan ik in elk bestandje de datum en tijd inzetten. Ik heb zelf daarvoorr een string gemaakt, je had ook al kant en klare dingen in de library maar deze werkte niet doordat hier aparte tekens instonden, dat vind windows niet zo leuk.
```Python
def bestand_maken(obj, file_name):

  datum = datetime.datetime.now()
  text = json.dumps(obj, sort_keys=True, indent=4)
  #datum in een str zetten
  date = str(datum.strftime("%d")) + "-" + str(datum.strftime("%m")) + "-" + str(datum.strftime("%Y")) + "_" + str(datum.strftime("%H")) + "-" + str(datum.strftime("%M")) + "-" + str(datum.strftime("%S"))

  f = open(file_name + "_" + date + ".json", "x")
  f.write(text)
```
Ik maar bij de SQL request geen bestandje aan omdat je het meteen in de database zet ipv een bestandje.

### 3. Converteren naar MySQL:
Om JSON te converten naar SQL moet je zelf de ERD opzet verzinnen en maken, daar heb ik niet zoveel werk ingestopt omdat dit alleen nog maar voor te oefenen is. Als ik dit straks met de proftaak samen met de mannen van de realtime viewer ga maken ga ik hier zeker langer overna denken.

Eerst maak ik connectie met de MySQL database, deze heb ik thuis op Docker draaien,
```Python
mydb = mysql.connector.connect(
  host="192.168.30.99",
  user="iraca",
  password="<SECRET>",
  port="3307",
  database="find3"
)
```
Daarna kijk ik of ik nog de tables erin moet zetten, ik check dus of ze al bestaan. Zo niet zet ik ze erin:
(Gevonden op internet: https://stackoverflow.com/questions/17044259/python-how-to-check-if-table-exists)
```Python
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
```

Nu kunnen we dus kiezen om gebruik te maken van de Database of het JSON bestandje.

#### 3.1 Database:
FIND3 maakt gebruik van een SQLite file, deze lijkt erg veel op die van MySQL maar het werkt niet samen.
Ik moet dus in die string een aantal dingen veranderen:

Elke regel in een list zetten:
```Python
f = locoation_database.text
all_sql_lines = f.splitlines()
```
Eerst moet ik alle lijnen waar geen INSERT instaan weghalen, ik kijk dus of er INSTERT in een regel staat en zet die regel in een andere list:
```Python
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
```
Daarna kan de bij de INSERT regels de string aanpassen: (dit is erg slechte code maar het werkt)
```Python
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
```
Het zet de regels elke keer in een nieuwe list omdat ik niet meerdere dingen tegelijkertijd kan replacen.
#### 3.2 JSON:
Om de JSON regels te splitten maak ik gebruik van de json library.
Ik ben hier veels te lang mee bezig geweest, ik ben er gelukkig wel uitgekomen. Toen ik erachter kwam dat de API ook een Database dump heeft ben ik meteen daarmee begonnen omdat dat veel tijd scheeld.

Met deze regel print hij wat 
```
print(data_file["locations"][0]["sensors"]["s"]["wifi"])
```
JSON:
```json
    "locations": [
        {
             "s": {
                    "bluetooth": {},
                    "wifi": {
                        "3e:94:ed:34:9b:e5": -94,
                            }
                   }
         }
```
Wat hij print:
```
"3e:94:ed:34:9b:e5": -94,
```
### 4. Het in de MySQL server zetten:
Als de de INSERT regels dan goed in de list's staan kan ik de regels in de MySQL server zetten:
```Python
while True:
  if counter == len(new_insert_list_4):
    break
  mycursor.execute(new_insert_list_4[counter])
  print(counter)
  counter += 1
```
Het gaat door elke regel en gebruikt ***mycursor.execute()*** voor de MySQL Query
