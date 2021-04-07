from tkinter import *
#import platform
#import subprocess
from pythonping import *
import string
from re import search
ip_1 = "8.8.8.8"
ip_2 = "10.10.10.10"
ip_3 = "192.168.1.1"
"""
def ping(host):

    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.


    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '2', host]

    return subprocess.call(command) == 0
"""

def pinger(ip, ping_count):
    ping_text = ""
    ping_text = ping(ip, verbose=True, timeout=0.8, count=ping_count, df=True)
    return ping_text

root = Tk()
root.title("Ping Machine")

'''
Button(root, text="babs", command = lambda: Label(text=pinger("google.nl")).pack()).pack()
'''
root.geometry("400x400")
canvas1 = Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = Entry (root) 
canvas1.create_window(200, 140, window=entry1)

entry2 = Entry (root) 
canvas1.create_window(200, 100, window=entry2)
l1 = Label(root, text="Aantal pings:")
l2 = Label(root, text="IP:")
canvas1.create_window(100, 100, window=l1)
canvas1.create_window(100, 140, window=l2)

def getPing ():
    x1 = entry1.get()
    x2 = entry2.get()
    if x2.strip().isdigit():
        x2 = x2
    else: x2 = 1
    x2 = int(x2)
    label1 = Label(root, text=pinger(x1, x2))
    canvas1.create_window(200, 300, window=label1)


button1 = Button(text='Ping host:', command=getPing)
canvas1.create_window(200, 180, window=button1)

root.mainloop()

'''
babs = str(ping("babs.nl"))
find_babs = babs.find("from")
if find_babs != -1:
    print("response")
else: print("werkt niet")
'''