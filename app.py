from flask import Flask, render_template
from datetime import datetime
import wikipedia
import math

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
    },
    {
        "title" : "Como ser heroi sem ter poderes.",
        "body": "Não tem como.",
        "content":wikipedia.page("Batman").content,
        "author": "Batman",
        "created": datetime(2022,8,17),
        "id": 3
    },
    {
        "title" : "Como ser heroi sem ter poderes.",
        "body": "Não tem como.",
        "content":wikipedia.page("Batman").content,
        "author": "Batman",
        "created": datetime(2022,8,17),
        "id": 4
    },
    {
        "title" : "Como ser heroi sem ter poderes.",
        "body": "Não tem como.",
        "content":wikipedia.page("Batman").content,
        "author": "Batman",
        "created": datetime(2022,8,17),
        "id": 5
    },
    {
        "title" : "Como ser heroi sem ter poderes.",
        "body": "Não tem como.",
        "content":wikipedia.page("Batman").content,
        "author": "Batman",
        "created": datetime(2022,8,17),
        "id": 6
    },
    {
        "title" : "Como ser heroi sem ter poderes.",
        "body": "Não tem como.",
        "content":wikipedia.page("Batman").content,
        "author": "Batman",
        "created": datetime(2022,8,17),
        "id": 7
    },
    {
        "title" : "Como ser heroi sem ter poderes.",
        "body": "Não tem como.",
        "content":wikipedia.page("Batman").content,
        "author": "Batman",
        "created": datetime(2022,8,17),
        "id": 8
    },
]

@app.route("/")
@app.route("/<int:page>")
def index(page=1):
    n_post = math.ceil(len(posts)/4)
    show_posts = [posts[x:x+4] for x in range(0, len(posts), 4)]
    return render_template("index.html", page=page, posts=show_posts[page-1], n_posts=n_post, )

@app.route("/posts/<int:id>")
def post(id):
    post = posts[id]
    return render_template("post.html", post=post)

app.run(threaded=True)