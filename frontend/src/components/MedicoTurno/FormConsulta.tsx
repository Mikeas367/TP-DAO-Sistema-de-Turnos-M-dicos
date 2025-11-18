import { useState } from "react";
import "./FormConsulta.css";

export const FormConsulta = ({ turno, onClose }: any) => {
  const [medicamento, setMedicamento] = useState("");
  const [tratamiento, setTratamiento] = useState("");

  const enviarConsulta = async () => {
    const body = {
      turno_id: turno.id,
      detalle_medicamento: medicamento,
      tratamiento: tratamiento,
    };

    await fetch("http://127.0.0.1:8000/api/registrar-consulta", {
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

        <p><b>Turno:</b> {turno.fecha}</p>
        <p><b>Paciente:</b> {turno.paciente.nombre} {turno.paciente.apellido}</p>

        <label>Medicamentos:</label>
        <textarea
          value={medicamento}
          onChange={(e) => setMedicamento(e.target.value)}
        />

        <label>Tratamiento:</label>
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