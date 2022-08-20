from flask import Flask, render_template
from datetime import datetime
import wikipedia

app = Flask("Hello")



posts = [
    {
        "title" : wikipedia.page("Mouse").title,
        "body": wikipedia.page("Mouse").summary,
        "content":wikipedia.page("Mouse").content,
        "author": "cara que escreve posts",
        "created": datetime(2022,8,17),
        "id": 0
    },
    {
        "title" : "Outro post vey",
        "body": "Este post certamente é outro um post",
        "author": "cara que escreve posts as vezes",
        "created": datetime(2022,8,17),
        "id": 1
    },
    {
        "title" : "Como ser heroi sem ter poderes.",
        "body": "Se vista estranho e saia batendo em pessoas na rua",
        "author": "Batman",
        "created": datetime(2022,8,17),
        "id": 2
    }
]
@app.route("/")
def index():
    return render_template("index.html", posts=posts)


@app.route("/posts/<int:id>")
def post(id):
    post = posts[id]
    return render_template("post.html", post=post)


