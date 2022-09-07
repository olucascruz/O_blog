from flask import Flask, render_template
from datetime import datetime
import wikipedia

app = Flask("Hello")



posts = [
    {
        "title" : wikipedia.page("Mouse").title,
        "body": "Este post certamente é outro um post",
        "content":wikipedia.page("Mouse").content,
        "author": "cara que escreve posts",
        "created": datetime(2022,8,17),
        "id": 0
    },
    {
        "title" : "Outro post vey",
        "body": "Este post certamente é outro um post",
        "content":wikipedia.page("Instagram").content,
        "author": "cara que escreve posts as vezes",
        "created": datetime(2022,8,17),
        "id": 1
    },
    {
        "title" : "Como ser heroi sem ter poderes.",
        "body": "Não tem como.",
        "content":wikipedia.page("Batman").content,
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


