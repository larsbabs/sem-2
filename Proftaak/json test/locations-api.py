import requests
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def data_request():
    location_data = requests.get('https://find3.pte2.nl/api/v1/by_location/oil231')
    data = location_data.json()
    return data


def infoFormatter():
    count = 0
    total_list = []
    data = data_request()
    while True:
        total = data["locations"][count]["total"]
        name = data["locations"][count]["location"]
        percent = (data["locations"][count]["total"] / totalCalculator() * 100)
        name_and_total_list = [str(name), total, round(percent, 2)]
        total_list.append(name_and_total_list)
        count += 1
        if count == len(data["locations"]):
            break
    return total_list

def totalCalculator():
    total_devices = 0
    data = data_request()
    count = 0
    while True:
        total_devices += data["locations"][count]["total"]
        count += 1
        if count == len(data["locations"]):
            break
    return total_devices

def jsonMaker():
    data = {}
    data['locations'] = []
    count = 0
    list = infoFormatter()
    while True:
        data['locations'].append({
            'location': list[count][0],
            'devices': list[count][1],
            'per_cent': list[count][2]
        })
        count += 1
        if count == len(list):
            break
    return data

@app.route('/ping/', methods=['GET'])
def ping_test():
    return jsonMaker()
app.run(host="0.0.0.0", port="8080")