from flask import Flask, jsonify
from engine import get_status

app = Flask(__name__)

@app.get("/")
def home():
    return "Project is running"

@app.get("/status")
def status():
    return jsonify(get_status())

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
