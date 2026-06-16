from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/status")
def status():
    with open("output.json", "r") as f:
        data = json.load(f)
    return jsonify(data)

app.run(debug=True)