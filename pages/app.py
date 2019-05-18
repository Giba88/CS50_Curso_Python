from flask import Flask, jsonify, request, render_template
import time

app = Flask(__name__)

@app.route("/")
def Dinamico():
    return render_template("dinamico.html")

@app.route("/post", methods=["POST"])
def post():
    start = int(request.form.get("inicio") or 0)
    end = int(request.form.get("fim") or (start + 9))

    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    time.sleep(10)
    
    return jsonify(data)
