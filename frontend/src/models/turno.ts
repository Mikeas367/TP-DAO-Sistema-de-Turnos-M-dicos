import type { EstadoTurno } from "./estadoTurno";
import type { Medico } from "./medico";
import type { Paciente } from "./paciente";

export interface Turno {
  id: number;
  paciente: Paciente | null;
  medico: Medico;
  estado: EstadoTurno;
  fecha: string; // "2025-11-12 09:00"
}