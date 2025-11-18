import React, { useState } from "react";

export const Reportes: React.FC = () => {
  const [desde, setDesde] = useState<string>("");
  const [hasta, setHasta] = useState<string>("");

  const descargarPDF = (endpoint: "pacientes" | "asistencias") => {
    if (endpoint === "pacientes") {
      if (!desde || !hasta) {
        alert("Seleccioná las fechas primero");
        return;
      }
      window.open(
        `http://127.0.0.1:8000/api/pacientes-atendidos-pdf?desde=${desde}&hasta=${hasta}`,
        "_blank"
      );
    } else if (endpoint === "asistencias") {
      window.open(
        "http://127.0.0.1:8000/api/asistencia-vs-inasistencias-pdf",
        "_blank"
      );
    }
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h2>Reportes</h2>

      <div style={{ marginBottom: "1rem" }}>
        <label>Desde: </label>
        <input
          type="date"
          value={desde}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            setDesde(e.target.value)
          }
        />
        <label style={{ marginLeft: "1rem" }}>Hasta: </label>
        <input
          type="date"
          value={hasta}
          onChange={(e: React.ChangeEvent<HTMLInputElement>) =>
            setHasta(e.target.value)
          }
        />
      </div>

      <div style={{ display: "flex", gap: "1rem" }}>
        <button onClick={() => descargarPDF("pacientes")}>
          Descargar PDF Pacientes Atendidos
        </button>
        <button onClick={() => descargarPDF("asistencias")}>
          Descargar PDF Asistencias/Inasistencias
        </button>
      </div>
    </div>
  );
};
