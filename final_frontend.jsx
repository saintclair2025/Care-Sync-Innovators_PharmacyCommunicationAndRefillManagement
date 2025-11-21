import React, { useState } from "react";
import InputField from "../components/InputField";

export default function RefillRequest() {
  const [medicine, setMedicine] = useState("");

  async function handleSubmit() {
    const res = await fetch("http://localhost:5000/api/refill", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ patient_id: 1, medicine })
    });

    const data = await res.json();
    alert(data.message);
  }

  return (
    <div style={{ padding: "20px" }}>
      <h2>Request a Refill</h2>

      <InputField 
        label="Medicine Name"
        value={medicine}
        setValue={setMedicine}
      />

      <button onClick={handleSubmit} style={{ padding: "10px" }}>
        Submit Request
      </button>
    </div>
  );
}
