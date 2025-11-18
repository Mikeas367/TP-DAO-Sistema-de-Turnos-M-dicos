import { useEffect, useState } from "react";
import axios from "axios";

interface TurnoCreate {
  fecha: string;
  medico_id: number;
}

export const NuevoTurnoForm = ()=> {
  const [medicos, setMedicos] = useState<any[]>([]);
  const [fecha, setFecha] = useState("");
  const [medicoId, setMedicoId] = useState<number | "">("");
  const [loading, setLoading] = useState(false);
  const [mensaje, setMensaje] = useState<string | null>(null);

  // Cargar médicos
  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/medicos").then((res) => {
      setMedicos(res.data);
    });
  }, []);

  const crearTurno = async () => {
    if (!fecha || !medicoId) {
      setMensaje("Debe completar todos los campos");
      return;
    }

    const data: TurnoCreate = {
      fecha,
      medico_id: Number(medicoId),
    };

    try {
      setLoading(true);
      setMensaje(null);
      console.log(data.fecha)
      await axios.post("http://127.0.0.1:8000/api/nuevo-turno", data);

      setMensaje("Turno creado correctamente");
      setFecha("");
      setMedicoId("");
    } catch (error) {
      setMensaje("Error al crear el turno");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 max-w-md mx-auto">
      <h2 className="text-xl font-bold mb-4">Crear nuevo turno</h2>

      <label className="block font-medium mt-2">Fecha del turno</label>
      <input
        type="datetime-local"
        value={fecha}
        onChange={(e) => setFecha(e.target.value)}
        className="border p-2 w-full rounded"
      />

      <label className="block font-medium mt-2">Médico</label>
      <select
        value={medicoId}
        onChange={(e) => setMedicoId(Number(e.target.value))}
        className="border p-2 w-full rounded"
      >
        <option value="">Seleccione un médico</option>
        {medicos.map((m) => (
          <option key={m.id} value={m.id}>
            {m.nombre} {m.apellido}
          </option>
        ))}
      </select>

      <button
        onClick={crearTurno}
        disabled={loading}
        className="bg-blue-600 text-white px-4 py-2 rounded mt-4 w-full"
      >
        {loading ? "Creando..." : "Crear turno"}
      </button>

      {mensaje && (
        <p className="mt-3 text-center font-semibold">
          {mensaje}
        </p>
      )}
    </div>
  );
}
