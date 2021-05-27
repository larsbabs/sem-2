from platform import platform
import flask
import psutil
import socket

app = flask.Flask(__name__)
app.config["DEBUG"] = True

partitions = psutil.disk_partitions()
svmem = psutil.virtual_memory()
interfaces = psutil.net_if_addrs()
ip = interfaces["wlan0"][0][1]

for partition in partitions:
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue

def json_maker(name, ip, disk, cpu, memory):
    data = {}
    data['device-info'] = []
    data['device-info'].append({
        'hostname': str(name),
        'ip': str(ip),
        'cpu': str(cpu),
        'disk': str(disk),
        'memory': str(memory)
    })
    return data

for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    continue

#print(psutil.cpu_percent())
#print(f"{partition_usage.percent}")
#print(f"{svmem.percent}")
#json_maker(device_name, "10.10.3.1", (f"{partition_usage.percent}"), psutil.cpu_percent(), psutil.virtual_memory().percent)

@app.route('/sys-info/', methods=['GET'])
def ping_test_html():
    return json_maker(socket.gethostname(), ip, partition_usage.percent, psutil.cpu_percent(), svmem.percent)
app.run(host="0.0.0.0", port="8080")