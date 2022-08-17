from flask import Flask, render_template
from datetime import datetime

app = Flask("Hello")



posts = [
    {
        "title" : "O post vey",
        "body": "Este post certamente é um post",
        "author": "cara que escreve posts",
        "created": datetime(2022,8,17)
    },
    {
        "title" : "Outro post vey",
        "body": "Este post certamente é outro um post",
        "author": "cara que escreve posts as vezes",
        "created": datetime(2022,8,17)
    },
    {
        "title" : "Como ser heroi sem ter poderes.",
        "body": "Se vista estranho e saia batendo em pessoas na rua",
        "author": "Batman",
        "created": datetime(2022,8,17)
    }
]
@app.route("/")
def index():
    return render_template("index.html", posts=posts)