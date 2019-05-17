import os
import requests

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

votos = {"sim": 0, "nao": 0, "talvez": 0}


@app.route("/")
def index():
    return render_template("index.html", votos=votos)

@socketio.on("FuncVoto")
def voto(data):
    selecionado = data["selecionado"]
    votos[selecionado] += 1
    emit("Func_Voto", votos, broadcast="true")
    print(votos)

@app.route("/Teste")
def Teste():
    return "Teste";