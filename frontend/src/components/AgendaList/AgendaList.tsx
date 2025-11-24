import React, { useEffect, useState } from "react";
import axios from "axios";

interface Medico {
  id: number;
  nombre: string;
  apellido: string;
}

interface DiaLaboral {
  dia_semana: number;
  hora_inicio: string;
  hora_fin: string;
  duracion_turno_min: number;
}

interface Agenda {
  id: number;
  medico: Medico;
  dias_trabajo: DiaLaboral[];
}

export const AgendaList: React.FC = () => {
  const [agendas, setAgendas] = useState<Agenda[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/agendas")
      .then(r => {
        setAgendas(r.data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  const generarTurnos = async (agendaId: number) => {
    try {
      await axios.post(`http://127.0.0.1:8000/api/agendas/${agendaId}/generar-turnos`);
      alert("Turnos generados correctamente");
    } catch (error) {
      console.error(error);
      alert("Error generando turnos");
    }
  };

  if (loading) return <p className="text-center mt-5">Cargando agendas...</p>;

  return (
    <div className="container mt-4">

      <h2 className="mb-4">Listado de Agendas</h2>

      <table className="table table-bordered table-striped">
        <thead className="table-dark">
          <tr>
            <th>#</th>
            <th>Médico</th>
            <th>Días laborales</th>
            <th>Acciones</th>
          </tr>
        </thead>

        <tbody>
          {agendas.map(a => (
            <tr key={a.id}>
              <td>{a.id}</td>
              <td>
                {a.medico.nombre} {a.medico.apellido}
              </td>
              <td>
                {a.dias_trabajo.map((d, idx) => (
                  <div key={idx}>
                    {["Lun","Mar","Mié","Jue","Vie","Sáb","Dom"][d.dia_semana]} → 
                    {d.hora_inicio} - {d.hora_fin} 
                    ({d.duracion_turno_min} min)
                  </div>
                ))}
              </td>

              <td>
                <button
                  className="btn btn-success"
                  onClick={() => generarTurnos(a.id)}
                >
                  Generar turnos
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>

    </div>
  );
};