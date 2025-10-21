import { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import { crearMedico, obtenerMedicoPorId, actualizarMedico } from "../../services";
import type { MedicoBase } from "../../models";
import type { Especialidad } from "../../models/especialidad";
import { listarEspecialidad } from "../../services/especialidad.service";

interface MedicoFormProps {
  medicoId?: number;
  onSuccess?: () => void;
  onCancel?: () => void;
}

export const MedicoForm = ({ medicoId, onSuccess, onCancel }: MedicoFormProps) => {
  const { register, handleSubmit, reset } = useForm<MedicoBase>();
  const [error, setError] = useState("");

  const [especialidades, setEspecialidades] = useState<Especialidad[]>()

  // Si hay medicoId, cargamos los datos para editar

  const getEspecialidades = async () => {
    try {
      const response = await listarEspecialidad();
      setEspecialidades(response);
    } catch (err) {
      console.error(err);
      setError("Error al cargar especialidades");
    }
  };

  useEffect(() => {
    const fetchData = async () => {
      await getEspecialidades();

      if (medicoId) {
        try {
          const medico = await obtenerMedicoPorId(medicoId);
          reset({
            nombre: medico.nombre,
            apellido: medico.apellido,
            email: medico.email,
            especialidad_id: medico.especialidad_id,
          });
        } catch (err) {
          console.error(err);
          setError("Error al cargar el médico");
        }
      } else {
        reset({ nombre: "", apellido: "", email: "", especialidad_id: undefined });
      }
    };
    fetchData();
  }, [medicoId, reset]);

  const onSubmit = async (data: MedicoBase) => {
    try {
      setError("");
      if (medicoId) {
        await actualizarMedico(medicoId, data);
        window.alert("Medico Actualizado con exito")
      } else {
        await crearMedico(data);
        window.alert("Medico Creado con exito")
      }
      reset();
      if (onSuccess) onSuccess(); // desde la lista defino la logica.
    } catch (err) {
      console.error(err);
      window.alert("Error al guardar el medico")
      setError("Error al guardar el médico");
    }
  };

  return (
    <div className="card p-3 mb-3 shadow-sm">
      <h3>{medicoId ? "Editar Médico" : "Registrar Nuevo Médico"}</h3>
      <form onSubmit={handleSubmit(onSubmit)}>
        <label>Nombre</label>
        <input {...register("nombre")} className="form-control mb-2" required />

        <label>Apellido</label>
        <input {...register("apellido")} className="form-control mb-2" required />

        <label>Email</label>
        <input {...register("email")} className="form-control mb-2" required />

        <label>Especialidad</label>
        <select {...register("especialidad_id")} className="form-control mb-2" required>
          <option value="">Seleccione una especialidad</option>
          {especialidades?.map((esp) => (
            <option key={esp.id} value={esp.id}>
              {esp.nombre}
            </option>
          ))}
        </select>


        <div className="mt-3">
          <button type="submit" className="btn btn-success me-2">
            {medicoId ? "Actualizar" : "Crear"}
          </button>
          {onCancel && (
            <button
              type="button"
              className="btn btn-secondary"
              onClick={onCancel}>
              Cancelar
            </button>
          )}
        </div>
        {error && <p className="text-danger mt-2">{error}</p>}
      </form>
    </div>
  );
};