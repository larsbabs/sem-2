from pythonping import *
import string
ip = "1.1.1.1"
babs = ping(ip)
#print(babs)
#print(babs.success)
print(babs.verbose)
#print(babs.append)
print(babs.packets_lost)
print(babs._responses)