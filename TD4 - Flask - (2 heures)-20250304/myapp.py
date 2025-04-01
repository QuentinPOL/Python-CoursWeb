from flask import Flask, render_template, request
from db import *
import os

app = Flask(__name__)

app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'Chinook.db'),
) 

@app.get('/login')
def login_get():
 return "<h1>do_the_login()</h1>"

@app.post('/login')
def login_post():
 return "<h1>show_the_login_form()</h1>"

@app.get('/read_db')
def read_db():
    db = get_db()
    artists = db.execute("select * from artist limit 10").fetchall()
    return render_template('list_artists.html', artists=artists) 


#Q2Q3 non aucune différence, car sans précision flask réagit uniquement aux requêtes