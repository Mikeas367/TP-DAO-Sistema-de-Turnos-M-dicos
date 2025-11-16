import React from "react";
import type { Turno } from "../../models/turno";
import "./Calendario.css"

interface Props {
  turnos: Turno[];
}

interface Props {
  turnos: Turno[];
  onSeleccionar: (turno: Turno) => void;
}

export const CalendarTurnos: React.FC<Props> = ({ turnos, onSeleccionar }) => {
  return (
    <div className="calendar-container">
      {turnos.map((turno) => {
        const fecha = new Date(turno.fecha);
        const esOcupado = turno.estado.nombre === "Ocupado";

        return (
          <div
            key={turno.id}
            className={`turno-card ${esOcupado ? "ocupado" : "libre"}`}
            onClick={() => !esOcupado && onSeleccionar(turno)}
            style={{ cursor: esOcupado ? "not-allowed" : "pointer" }}
          >
            <strong>
              {fecha.toLocaleDateString()} - {fecha.getHours()}:00
            </strong>

            <p>
              <b>Médico:</b> {turno.medico.nombre} {turno.medico.apellido}
            </p>

            <p>
              <b>Especialidad:</b> {turno.medico.especialidad.nombre}
            </p>

            {turno.paciente ? (
              <p>
                <b>Paciente:</b> {turno.paciente.nombre} {turno.paciente.apellido}
              </p>
            ) : (
              <p className="sin-paciente">Sin paciente</p>
            )}
          </div>
        );
      })}
    </div>
  );
};
