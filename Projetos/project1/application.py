import os
import requests
import hashlib
from flask import Flask, session, render_template, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
#if not os.getenv("DATABASE_URL"):
#    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine("postgres://zifcppbxexzolo:e3010b16e511b7eaa5ecf81c2f52b8e07582f937c8d50745d8a07054066f5a10@ec2-23-21-106-241.compute-1.amazonaws.com:5432/d72n20v43tptqd")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    books = db.execute("SELECT * FROM books").fetchall()

    return render_template("index.html", books=books)
    """
    res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": "yy2c9vgOvZYVssJeBcgBTg", "isbns": "9781632168146"})
    print(res.json())
    return "Project 1: TODO"
    """

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":        
        return render_template("login.html", message="")
    
    login = request.form.get("name")
    password = request.form.get("password")

    username = db.execute(f"SELECT username FROM users WHERE " +
                    f"password = '{password}'").fetchall()

    if len(username) == 1:
        session["username"] = username[0].username
        return render_template("index.html")
    else:
        return render_template("login.html", message="Invalid credentials")


@app.route("/logout")
def logout():
    session['username'] = ""
    return render_template("login.html", message="")

@app.route("/create", methods=["GET", "POST"])
def create1():
    if request.method == "GET":        
        return render_template("create.html", message="")
    
    username = request.form.get("username")
    password = request.form.get("password")
    confirm = request.form.get("Confirm")

    if password == confirm:
        try:
            db.execute("INSERT INTO users VALUES (':username', ':password')", {"username" :username, "password" :password})
            db.commit()
            session["username"] = username
            return render_template("index.html")
        except:
            return render_template("create.html", message="Error - try again")
