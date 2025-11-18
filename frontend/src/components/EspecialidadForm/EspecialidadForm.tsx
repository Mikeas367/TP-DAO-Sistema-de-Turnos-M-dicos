import { useEffect, useState } from "react";
import { useForm } from "react-hook-form";
import {
  crearEspecialidad,
  obtenerEspecialidadPorId,
  actualizarEspecialidad,
} from "../../services/especialidad.service";
import type { EspecialidadBase } from "../../models/especialidad";
import { useNavigate } from "react-router-dom"; // 👈 NUEVO

interface Props {
  especialidadId?: number;
  onSuccess?: () => void;
  onCancel?: () => void;
}

export const EspecialidadForm = ({
  especialidadId,
  onSuccess,
  onCancel,
}: Props) => {
  const { register, handleSubmit, reset } = useForm<EspecialidadBase>();
  const [error, setError] = useState("");
  const navigate = useNavigate(); 

  const esEdicion = Boolean(especialidadId);

  useEffect(() => {
    const fetchData = async () => {
      if (especialidadId) {
        try {
          const esp = await obtenerEspecialidadPorId(especialidadId);
          reset({
            nombre: esp.nombre,
            descripcion: esp.descripcion,
          });
        } catch (err) {
          setError("Error al cargar la especialidad");
        }
      } else {
        reset({ nombre: "", descripcion: "" });
      }
    };
    fetchData();
  }, [especialidadId, reset]);

  const onSubmit = async (data: EspecialidadBase) => {
    try {
      setError("");

      if (especialidadId) {
        await actualizarEspecialidad(especialidadId, data);
        window.alert("Especialidad actualizada correctamente");

      } else {

        await crearEspecialidad(data);
        window.alert("Especialidad creada correctamente");

        navigate("/especialidades");
      }

      reset();
      if (onSuccess) onSuccess();

    } catch (err) {
      console.error(err);
      setError("Error al guardar especialidad");
      window.alert("Ocurrió un error al guardar");
    }
  };

  return (
    <div className="card p-3 mb-3 shadow-sm">
      <h3>{esEdicion ? "Editar Especialidad" : "Registrar Especialidad"}</h3>

      <form onSubmit={handleSubmit(onSubmit)}>
        <label>Nombre</label>
        <input
          {...register("nombre")}
          className="form-control mb-2"
          required
        />

        <label>Descripción</label>
        <input
          {...register("descripcion")}
          className="form-control mb-2"
          required
        />

        <div className="mt-3">
          <button type="submit" className="btn btn-success me-2">
            {esEdicion ? "Actualizar" : "Crear"}
          </button>

          {onCancel && (
            <button type="button" className="btn btn-secondary" onClick={onCancel}>
              Cancelar
            </button>
          )}
        </div>

        {error && <p className="text-danger mt-2">{error}</p>}
      </form>
    </div>
  );
};