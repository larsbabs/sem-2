from io import StringIO
from flask import request
from flask import Response
from flask_cors import CORS
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
        return False
    try:
        status = server.status()
        status.players.online, status.latency
        return True, status
    except (ConnectionResetError, gaierror, socket.timeout, OSError) as e:
        return False

def serverPing(server):
    if server == False:
        return False
    try:
        latency = server.ping()
        return True, latency
    except (ConnectionResetError, gaierror, socket.timeout, OSError) as e:
        return False

def serverQuery(server):
    if server == False:
        return False
    try:
        query = server.query()
        print("The server has the following players online: {0}".format(", ".join(query.players.names)))
        return True, query
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

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

secretKey = "1fcbb0c4fc1f039f73aa6d697d2db9ba7f803f17"

def checksumChecker(request):
    if type(request.args.get('checksum')) != str:
        return False
    sha1Link = request.query_string.decode("utf-8").replace("&checksum=" + request.args.get('checksum'), "") + secretKey
    from hashlib import sha256
    checksumString = sha256(sha1Link.encode('utf-8')).hexdigest()
    if checksumString == request.args.get('checksum'):
        return True
    else:
        return False

def xmlMaker(url):
    minecraftInfo = mainStatusController(url)
    data = """<response>
<returncode>SUCCESS</returncode>
<serverurl>{0}</serverurl>
<playersonline>{1}</playersonline>
<serverlatency>{2}</serverlatency>
<version>1.0</version>
</response>""".format(url, minecraftInfo[0], minecraftInfo[1])
    return data

def errorXml():
    data = """<response>
<returncode>ERROR</returncode>
<error>MISSING 'url' VARIABLE</error>
<version>1.0</version>
</response>
    """
    return data

def checksumErrorXml():
    data = """<response>
<returncode>ERROR</returncode>
<error>BAD CHECKSUM</error>
<version>1.0</version>
</response>
    """
    return data

@app.route('/minecraft/')
def adhoc_test():
    url = request.args.get('url')
    if url == None:
        return Response(errorXml(), mimetype='   text/xml;charset=utf-8')
    else:
        if checksumChecker(request):
            return Response(xmlMaker(url), mimetype='text/xml;charset=utf-8')
        else:
            return Response(checksumErrorXml(), mimetype='text/xml;charset=utf-8')
app.run(host="0.0.0.0")