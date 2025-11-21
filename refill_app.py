from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Temporary in-memory storage (to simulate DB)
patients = {
    1: {"id": 1, "name": "John Doe", "email": "john@example.com"}
}

refills = [
    {"id": 1, "patient_id": 1, "medicine": "Atorvastatin", "status": "Approved"},
    {"id": 2, "patient_id": 1, "medicine": "Metformin", "status": "Pending"}
]


@app.get("/api/patient/<int:id>")
def get_patient(id):
    return jsonify(patients.get(id))


@app.get("/api/patient/<int:id>/refills")
def get_refill_status(id):
    patient_refills = [r for r in refills if r["patient_id"] == id]
    return jsonify(patient_refills)


@app.post("/api/refill")
def create_refill():
    data = request.json
    new_refill = {
        "id": len(refills) + 1,
        "patient_id": data["patient_id"],
        "medicine": data["medicine"],
        "status": "Pending"
    }
    refills.append(new_refill)

    return jsonify({"message": "Refill request received", "refill": new_refill})


if __name__ == "__main__":
    app.run(debug=True)
