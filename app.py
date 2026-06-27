from flask import Flask, jsonify, render_template
from api.linux import get_linux_stats

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/api/linux")
def linux():
    return jsonify(get_linux_stats())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
