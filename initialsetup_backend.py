from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({
        "message": "Med Link API is running",
        "status": "OK"
    })

if __name__ == "__main__":
    app.run(debug=True)
