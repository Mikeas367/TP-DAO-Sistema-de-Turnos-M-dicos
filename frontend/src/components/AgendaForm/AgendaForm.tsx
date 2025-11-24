import React, { useEffect, useState } from "react";
import { useForm, useFieldArray } from "react-hook-form";
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

interface AgendaFormData {
  medico_id: number;
  dias_trabajo: DiaLaboral[];
}

export const AgendaForm: React.FC = () => {
  const [medicos, setMedicos] = useState<Medico[]>([]);

  // React Hook Form
  const { control, register, handleSubmit, reset, watch } = useForm<AgendaFormData>({
    defaultValues: {
      medico_id: 0,
      dias_trabajo: []
    }
  });

  // Manejo dinámico de campos (días)
  const { fields, append, remove } = useFieldArray({
    control,
    name: "dias_trabajo"
  });

  // Obtener médicos
  useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/medicos")
      .then(r => setMedicos(r.data))
      .catch(console.error);
  }, []);

  const diasSemana = [
    "Lunes", "Martes", "Miércoles", "Jueves",
    "Viernes", "Sábado", "Domingo"
  ];

  const onSubmit = async (data: AgendaFormData) => {
    try {
      await axios.post("http://127.0.0.1:8000/api/agendas", data);
      alert("Agenda creada correctamente");

      reset({
        medico_id: 0,
        dias_trabajo: []
      });

    } catch (error) {
      console.error(error);
      alert("Error al crear agenda");
    }
  };

  return (
    <div className="container mt-4">

      <h2 className="mb-4">Crear Agenda Médica</h2>

      <form onSubmit={handleSubmit(onSubmit)}>

        {/* ---------- MÉDICO ---------- */}
        <div className="mb-3">
          <label className="form-label">Médico</label>
          <select
            className="form-control"
            {...register("medico_id", { required: true })}
          >
            <option value={0}>Seleccione un médico...</option>
            {medicos.map(m => (
              <option key={m.id} value={m.id}>
                {m.nombre} {m.apellido}
              </option>
            ))}
          </select>
        </div>

        <hr />

        {/* ---------- DÍAS LABORALES ---------- */}
        <h4>Días laborales</h4>

        {fields.map((field, index) => (
          <div key={field.id} className="card shadow-sm p-3 mb-3">

            <div className="row">

              {/* Día de semana */}
              <div className="col-md-3">
                <label className="form-label">Día semana</label>
                <select
                  className="form-control"
                  {...register(`dias_trabajo.${index}.dia_semana` as const, { required: true })}
                >
                  <option value="">Seleccione...</option>
                  {diasSemana.map((d, i) => (
                    <option key={i} value={i}>{d}</option>
                  ))}
                </select>
              </div>

              {/* Hora Inicio */}
              <div className="col-md-3">
                <label className="form-label">Hora inicio</label>
                <input
                  type="time"
                  className="form-control"
                  {...register(`dias_trabajo.${index}.hora_inicio` as const, { required: true })}
                />
              </div>

              {/* Hora Fin */}
              <div className="col-md-3">
                <label className="form-label">Hora fin</label>
                <input
                  type="time"
                  className="form-control"
                  {...register(`dias_trabajo.${index}.hora_fin` as const, { required: true })}
                />
              </div>

              {/* Duración */}
              <div className="col-md-2">
                <label className="form-label">Duración (min)</label>
                <input
                  type="number"
                  className="form-control"
                  defaultValue={30}
                  {...register(`dias_trabajo.${index}.duracion_turno_min` as const, {
                    required: true,
                    min: 5
                  })}
                />
              </div>

              {/* Botón eliminar */}
              <div className="col-md-1 d-flex align-items-end">
                <button
                  type="button"
                  className="btn btn-danger"
                  onClick={() => remove(index)}
                >
                  X
                </button>
              </div>
            </div>
          </div>
        ))}

        {/* BOTÓN AGREGAR */}
        <button
          type="button"
          className="btn btn-primary mb-3"
          onClick={() =>
            append({
              dia_semana: 0,
              hora_inicio: "",
              hora_fin: "",
              duracion_turno_min: 30
            })
          }
        >
          + Agregar día laboral
        </button>

        <hr />

        {/* SUBMIT */}
        <button
          type="submit"
          className="btn btn-success btn-lg"
          disabled={watch("medico_id") === 0 || fields.length === 0}
        >
          Crear Agenda
        </button>

      </form>
    </div>
  );
};