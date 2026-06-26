from flask import Flask, jsonify
from api.linux import get_linux_stats

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Enterprise Infrastructure Monitoring Platform</h1><p>API Running...</p>"

@app.route("/api/linux")
def linux():
    return jsonify(get_linux_stats())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
