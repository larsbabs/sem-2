from pythonping import *
import string
import ctypes
from tkinter import *
import socket




ping_count = 4
ip = "192.168.30.1"
babs = ping(ip)

# Test prints
"""
print(babs)
print(babs.success)
print(babs.verbose)
print(babs.append)
print(babs.packets_lost)
print(babs._responses)
print(babs.success)
print(babs.rtt_avg_ms)
"""

# Het maken van een popup box
def popup(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def hostname_resolves(hostname):
    try:
        socket.gethostbyname(hostname)
        return 1
    except socket.error:
        return 0

# Functie die input leest en dan pingt
def pingPopup():
    ip_input = entry1.get()

    if hostname_resolves(ip_input) == 0:
        popup('ping tester', 'De host: "' + str(ip_input) + '" is niet bekent.\nControleer op spelfouten.', 0)

    else:
        geping = ping(ip_input, verbose=True, timeout=0.8, count=ping_count, df=True)
        if geping.success(1):
            if socket.gethostbyname(ip_input) == str(ip_input):
                popup('ping tester', 'De host: "' + str(ip_input) + '" is bereikbaar!\nDe gemiddelde reactietijd is ' + str(geping.rtt_avg_ms) + " ms", 0)
            else:
                popup('ping tester', 'De host: "' + str(ip_input) + '" is bereikbaar!\nDe gemiddelde reactietijd is ' + str(geping.rtt_avg_ms) + " ms\nIP: " + socket.gethostbyname(ip_input), 0)

        else:
            popup('ping tester', 'De host: "' + str(ip_input) +'" is niet bereikbaar.', 0)


root = Tk()
root.title("Ping Machine")

root.geometry("200x200")
canvas1 = Canvas(root, width = 200, height = 200)
canvas1.pack()

entry1 = Entry (root) 
canvas1.create_window(100, 80, window=entry1)

l1 = Label(root, text="IP:")
canvas1.create_window(100, 50, window=l1)
button1 = Button(text='Ping host:', command=pingPopup)
canvas1.create_window(100, 130, window=button1)

root.mainloop()


