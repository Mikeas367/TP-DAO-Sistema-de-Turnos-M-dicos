import { useEffect, useState } from "react";
import { FormConsulta } from "./FormConsulta";
import axios from "axios";


export const MedicoTurnos = () => {
  const [medicos, setMedicos] = useState([]);
  const [medicoSeleccionado, setMedicoSeleccionado] = useState<number | null>(null);
  const [turnos, setTurnos] = useState([]);
  const [turnoConsulta, setTurnoConsulta] = useState(null);

  // ------------------------------
  // Cargar médicos
  // ------------------------------
  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/api/medicos")
      .then((res) => setMedicos(res.data))
      .catch((err) => console.error("Error cargando médicos", err));
  }, []);

  // ------------------------------
  // Cargar turnos del médico
  // ------------------------------
  useEffect(() => {
    if (!medicoSeleccionado) return;

    axios
      .get(`http://127.0.0.1:8000/api/turnos-medico/${medicoSeleccionado}`)
      .then((res) => setTurnos(res.data))
      .catch((err) => console.error("Error cargando turnos", err));
  }, [medicoSeleccionado]);

  // ------------------------------
  // MARCAR INASISTENCIA
  // ------------------------------
  const marcarInasistencia = async (turno: any) => {
    if (!turno.paciente) {
      alert("Este turno no tiene paciente asignado.");
      return;
    }

    try {
      await axios.post("http://127.0.0.1:8000/api/marcar-inasistencia", {
        turno_id: turno.id,
        paciente_id: turno.paciente.id,
      });

      alert("Inasistencia registrada");

      // Recargar turnos
      const res = await axios.get(
        `http://127.0.0.1:8000/api/turnos-medico/${medicoSeleccionado}`
      );
      setTurnos(res.data);

    } catch (error) {
      console.error(error);
      alert("Error al registrar inasistencia");
    }
  };

  return (
    <div style={{ padding: 20 }}>
      <h2>Turnos por Médico</h2>

      {/* Selección de médicos */}
      <label>Seleccionar médico:</label><br />
      <select
        value={medicoSeleccionado ?? ""}
        onChange={(e) => setMedicoSeleccionado(Number(e.target.value))}
      >
        <option value="">Seleccione...</option>
        {medicos.map((m: any) => (
          <option key={m.id} value={m.id}>
            {m.nombre} {m.apellido} — {m.especialidad.nombre}
          </option>
        ))}
      </select>

      <hr />

      {/* Lista de turnos */}
      {medicoSeleccionado && (
        <>
          <h3>Turnos del médico</h3>
          {console.log(turnos)}

          {turnos?.map((t: any) => (
            <div
              key={t.id}
              style={{
                border: "1px solid #ccc",
                padding: 15,
                marginBottom: 10,
                borderRadius: 8,
              }}
            >
              <p><b>Fecha:</b> {t.fecha}</p>
              <p><b>Estado:</b> {t.estado.nombre}</p>

              {t.paciente ? (
                <p><b>Paciente:</b> {t.paciente.nombre} {t.paciente.apellido}</p>
              ) : (
                <p style={{ color: "gray" }}>Sin paciente</p>
              )}

              {t.estado.nombre === "Ocupado" && (
                <>
                  <button
                    style={{ marginRight: 10 }}
                    onClick={() => marcarInasistencia(t)}
                  >
                    Marcar Inasistencia
                  </button>

                  <button onClick={() => setTurnoConsulta(t)}>
                    Registrar Consulta
                  </button>
                </>
              )}
            </div>
          ))}
        </>
      )}

      {/* Modal consulta */}
      {turnoConsulta && (
        <FormConsulta
          turno={turnoConsulta}
          onClose={() => setTurnoConsulta(null)}
        />
      )}
    </div>
  );
};