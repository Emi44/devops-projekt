from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/hello")
def hello():
    return "Hello from Flask!"

@app.get("/version")
def version():
    return jsonify(app="devops-projekt", version="0.1.0")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)