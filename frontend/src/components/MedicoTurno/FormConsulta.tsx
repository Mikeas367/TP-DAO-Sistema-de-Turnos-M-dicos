import { useState } from "react";
import "./FormConsulta.css";

export const FormConsulta = ({ turno, onClose }: any) => {
  const [diagnostico, setDiagnostico] = useState("");
  const [tratamiento, setTratamiento] = useState("");

  const enviarConsulta = async () => {
    const body = {
      turno_id: turno.id,
      detalle_diagnostico: diagnostico,
      tratamiento: tratamiento,
    };

    await fetch("http://127.0.0.1:8000/api/marcar-asistencia", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    alert("Consulta registrada correctamente.");
    onClose();
  };

  return (
    <div className="modal">
      <div className="modal-content">
        <h3>Registrar Consulta</h3>

        <p><b>Turno:</b> {turno.id} Fecha Turno:{turno.fecha}</p>
        <p><b>Paciente:</b> {turno.paciente.nombre} {turno.paciente.apellido}</p>

        <label>Diagnostico:</label>
        <textarea
          value={diagnostico}
          onChange={(e) => setDiagnostico(e.target.value)}
        />

        <label>tratamiento:</label>
        <textarea
          value={tratamiento}
          onChange={(e) => setTratamiento(e.target.value)}
        />

        <div style={{ marginTop: 15 }}>
          <button onClick={enviarConsulta}>Guardar</button>
          <button style={{ marginLeft: 10 }} onClick={onClose}>
            Cancelar
          </button>
        </div>
      </div>
    </div>
  );
};