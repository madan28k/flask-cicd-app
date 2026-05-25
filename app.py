from flask import Flask, jsonify
import platform
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Flask CI/CD Pipeline — Deployed via Azure DevOps",
        "author": "Madankumar Perumalsamy",
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "python_version": platform.python_version()
    })

@app.route("/info")
def info():
    return jsonify({
        "app": "Flask CI/CD Demo",
        "version": "1.0.0",
        "pipeline": "Azure DevOps",
        "deployed_to": "Azure App Service (Free F1)"
    })

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8000)
