from flask import Flask
from flask_cors import CORS

from routes.refill_routes import refill_bp
from routes.patient_routes import patient_bp

app = Flask(__name__)
CORS(app)

# Register routes
app.register_blueprint(refill_bp, url_prefix="/api")
app.register_blueprint(patient_bp, url_prefix="/api")

@app.get("/")
def home():
    return {"message": "Med Link API Working"}

if __name__ == "__main__":
    app.run(debug=True)
