import { useEffect, useState } from "react";
import type { Turno } from "../../models/turno";
import { FormOcuparTurno } from "./FormOcuparTurno";
import { CalendarTurnos } from "./CalendarioTurnos";



export const TurnosForm = ()=>{
  const [turnos, setTurnos] = useState<Turno[]>([]);
  const [fechaFiltro, setFechaFiltro] = useState<string>("");
  const [espFiltro, setEspFiltro] = useState<number | "">("");
  const [turnoSeleccionado, setTurnoSeleccionado] = useState<Turno | null>(null);

  const cargarTurnos = () => {
    fetch("http://127.0.0.1:8000/api/turnos")
      .then((res) => res.json())
      .then((data) => setTurnos(data));
  };

  useEffect(() => {
    cargarTurnos();
  }, []);

  // ESPECIALIDADES ÚNICAS
  const especialidades = Array.from(
    new Map(
      turnos.map((t) => [t.medico.especialidad.id, t.medico.especialidad.nombre])
    ).entries()
  );

  // FILTRO DE TURNOS
  const turnosFiltrados = turnos.filter((t) => {
    const coincideFecha = fechaFiltro
      ? new Date(t.fecha.replace(" ", "T")) >= new Date(fechaFiltro)
      : true;

    const coincideEsp = espFiltro
      ? t.medico.especialidad.id === espFiltro
      : true;

    return coincideFecha && coincideEsp;
  });

  return (
    <div style={{ padding: 20 }}>
      <h1>Calendario de Turnos</h1>

      {/* FILTROS */}
      <div style={{ display: "flex", gap: "20px", marginBottom: "20px" }}>
        <div>
          <label>Filtrar por fecha:</label><br />
          <input
            type="date"
            value={fechaFiltro}
            onChange={(e) => setFechaFiltro(e.target.value)}
          />
        </div>

        <div>
          <label>Filtrar por especialidad:</label><br />
          <select
            value={espFiltro}
            onChange={(e) =>
              setEspFiltro(e.target.value ? Number(e.target.value) : "")
            }
          >
            <option value="">Todas</option>
            {especialidades.map(([id, nombre]) => (
              <option key={id} value={id}>{nombre}</option>
            ))}
          </select>
        </div>
      </div>

      {/* CALENDARIO */}
      <CalendarTurnos
        turnos={turnosFiltrados}
        onSeleccionar={(t) => setTurnoSeleccionado(t)}
      />

      {/* MODAL */}
      {turnoSeleccionado && (
        <FormOcuparTurno
          turno={turnoSeleccionado}
          onClose={() => setTurnoSeleccionado(null)}
          onConfirm={() => cargarTurnos()}
        />
      )}
    </div>
  );
}

