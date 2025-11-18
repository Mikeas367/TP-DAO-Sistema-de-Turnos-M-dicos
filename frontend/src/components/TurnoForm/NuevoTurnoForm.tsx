import { useEffect, useState } from "react";
import axios from "axios";

interface TurnoCreate {
  fecha: string;
  medico_id: number;
}

export const NuevoTurnoForm = () => {
  const [medicos, setMedicos] = useState<any[]>([]);
  const [fecha, setFecha] = useState("");
  const [medicoId, setMedicoId] = useState<number | "">("");
  const [loading, setLoading] = useState(false);
  const [mensaje, setMensaje] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/medicos").then((res) => {
      setMedicos(res.data);
    });
  }, []);

  const crearTurno = async () => {
    setError(null);
    setMensaje(null);

    if (!fecha || !medicoId) {
      setError("Debe completar todos los campos.");
      return;
    }

    const data: TurnoCreate = {
      fecha,
      medico_id: Number(medicoId),
    };

    try {
      setLoading(true);
      await axios.post("http://127.0.0.1:8000/api/nuevo-turno", data);

      setMensaje("Turno creado correctamente.");
      setFecha("");
      setMedicoId("");
    } catch (error) {
      setError("Error al crear el turno.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mt-4">
      <div className="card shadow-sm">
        <div className="card-body">
          <h2 className="card-title mb-4 text-center fw-bold">
            Crear Nuevo Turno
          </h2>

          {error && (
            <div className="alert alert-danger text-center">{error}</div>
          )}

          {mensaje && (
            <div className="alert alert-success text-center">{mensaje}</div>
          )}

          <div className="mb-3">
            <label className="form-label fw-semibold">Fecha del turno</label>
            <input
              type="datetime-local"
              value={fecha}
              onChange={(e) => setFecha(e.target.value)}
              className="form-control"
            />
          </div>

          <div className="mb-3">
            <label className="form-label fw-semibold">Médico</label>
            <select
              value={medicoId}
              onChange={(e) => setMedicoId(Number(e.target.value))}
              className="form-select"
            >
              <option value="">Seleccione un médico</option>
              {medicos.map((m) => (
                <option key={m.id} value={m.id}>
                  {m.nombre} {m.apellido}
                </option>
              ))}
            </select>
          </div>

          <button
            onClick={crearTurno}
            disabled={loading}
            className="btn btn-primary w-100 py-2"
          >
            {loading ? (
              <>
                <span
                  className="spinner-border spinner-border-sm me-2"
                  role="status"
                ></span>
                Creando...
              </>
            ) : (
              "Crear turno"
            )}
          </button>
        </div>
      </div>
    </div>
  );
};