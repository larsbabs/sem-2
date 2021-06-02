from platform import platform
import psutil
import socket
import requests
import threading
from datetime import datetime

def whole_program():
    threading.Timer(300.0, whole_program).start()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    partitions = psutil.disk_partitions()
    svmem = psutil.virtual_memory()
    interfaces = psutil.net_if_addrs()
    ip = interfaces["wlan0"][0][1]

    for partition in partitions:
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue

    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        continue
    try:
        requests.get('http://10.10.2.14:8080/monitor?cpu=' + str(psutil.cpu_percent()) + '&disk=' + str(partition_usage.percent) + '&memory=' + str(svmem.percent) + '&ip=' + ip + '&hostname=' + str(socket.gethostname()) + '')
        print(str(now) + ", Request made to 10.10.2.14")
    except requests.ConnectionError:
        print(str(now) + ", No Request made to 10.10.2.14, no connection")
whole_program()