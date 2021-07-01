from mcstatus import MinecraftServer
from socket import gethostbyname, gaierror
import socket
import flask

def serverUrlMaker(url):
    if hostname_resolves(url):
        server = MinecraftServer.lookup(url)
        return server
    else:
        return False

def hostname_resolves(hostname):
    if hostname.find(":"):
        splitHost = hostname.split(":", 1)
        try:
            socket.gethostbyname(splitHost[0])
            return True
        except socket.error:
            return False
    else:
        try:
            socket.gethostbyname(hostname)
            return True
        except socket.error:
            return False


def serverStatus(server):
    if server == False:
        return "Host coult not be resolved", False
    try:
        status = server.status()
#        serverStatus.append(status.players.online)
#        serverStatus.append(status.latency)
        status.players.online, status.latency
        return True, status
    except (ConnectionResetError, gaierror, socket.timeout, OSError) as e:
        return False

def serverPing(server):
    try:
        latency = server.ping()
#        serverStatus.append(latency)
#        print("The server replied in {0} ms".format(latency))
        return True, latency
    except (ConnectionResetError, gaierror, socket.timeout, OSError) as e:
#        print("Server does not support 'server.ping'")
        return False

def serverQuery(server):
    try:
        query = server.query()
#        serverStatus.append(query.players.names)
        return query
    except (ConnectionResetError, gaierror, socket.timeout, OSError) as e:
        print("The server has 0 players online")
        return False

def mainStatusController(url):
    server = serverUrlMaker(url)
    status = serverStatus(server)
    ping = serverPing(server)
    if status:
        onlinePlayers = status[1].players.online
    else:
        onlinePlayers = "Host could not be resolved"
    if ping:
        latency = ping[1]
    else:
        latency = "Server Could not be pinged"
    return onlinePlayers, latency
    print(mainStatusController("iraca.duckdns.org:25565"))
print(serverQuery(serverUrlMaker("iraca.duckdns.org:25585")))
