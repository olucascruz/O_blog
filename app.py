from flask import Flask

app = Flask("Hello")

@app.route("/")
def hello():
    return "Hello world"

@app.route("/contatos")
def contatos():
    return "o contato"