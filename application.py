import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    agora = datetime.datetime.now()
    ano_novo = agora.month == 1 and agora.day == 1
    text = "Sim" if ano_novo else "Não"

    adicional = " 22"
    headline = "Hello Variavel" + adicional
    return render_template("index.html", headline=headline, ano_novo=ano_novo)

@app.route("/Giba")
def Giba():
    nomes = ["Giba", "Gil", "Gilberto"]
    return render_template("repeticao.html", nomes=nomes)

@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}!"

'''
if __name__ == "__main__":
    app.run(debug=True)
'''