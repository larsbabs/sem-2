from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route('/user')
def query_example():
    username = request.args.get('username')
    password = request.args.get('password')
    if isinstance(username, str) == True and isinstance(password, str) == True:
        os.system("docker exec -d prosody prosodyctl --config /config/prosody.cfg.lua register " + username + " meet.jitsi " + password + "")
        return 'OK'
    else:
        return 'FAILED, no user was created, please enter the username and password'
app.run(host="0.0.0.0", port="8080")