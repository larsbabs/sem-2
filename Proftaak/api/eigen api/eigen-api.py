import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True
books = open("./books.json")

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"
@app.route('/api/v1/books/test/', methods=['GET'])
def babs():
    return books.read()
@app.route('/babs/', methods=['GET'])
def test():
    return "1"
@app.route('/api/v1/antwoord1/', methods=['GET'])
def antwoord_test():
    return 'Jullie hebben het goed: <a href="https://groep3.eersel.duckdns.org/qrcode3.png">link</a>'
app.run(host="0.0.0.0")