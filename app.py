from flask import Flask, render_template

app = Flask("Hello")

@app.route("/")
def hello():
    return "Hello world"

@app.route("/contatos")
def contatos():
    usuario = [1, "O user", "CaraQueUsaSite"]
    nomeAula = "Aula python para web"
    return render_template("index.html", nome = nomeAula, usuario = usuario)