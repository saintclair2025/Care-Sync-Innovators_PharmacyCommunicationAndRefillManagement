import React, { useState } from "react";

export default function RefillRequest() {
  const [medicine, setMedicine] = useState("");

  function submitRequest() {
    fetch("http://localhost:5000/api/refill", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ patient_id: 1, medicine })
    })
      .then(res => res.json())
      .then(data => alert("Request submitted: " + data.message));
  }

  return (
    <div style={{ padding: "20px" }}>
      <h2>Request a Refill</h2>

      <input
        type="text"
        placeholder="Medicine name"
        value={medicine}
        onChange={(e) => setMedicine(e.target.value)}
      />
      <br /><br />
      
      <button onClick={submitRequest}>Submit</button>
    </div>
  );
}
