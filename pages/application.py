from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

texto = ["Lorem ipsum sit amet, consectetur adipiscing elemnte of torotr",
        "venenatis. Cras consequat temperation incidunt. Proin ulnss cererus mauris",
        "Morbi imperdiet nunc ac quam hendrerit facucib"]

@app.route("/primeiro")
def primeiro():
    return texto[0]

@app.route("/segundo")
def segundo():
    return texto[1]

@app.route("/terceiro")
def terceiro():
    return texto[2]

@app.route("/posts", methods=["POST"])
def posts():
    start = int(request.form.get("inicio") or 0)
    end = int(request.form.get("fim") or (start + 9))

    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    time.sleep(100)

    return jsonify(data)
    