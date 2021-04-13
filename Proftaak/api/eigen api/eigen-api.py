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

pull test ubuntu

app.run(host="0.0.0.0")