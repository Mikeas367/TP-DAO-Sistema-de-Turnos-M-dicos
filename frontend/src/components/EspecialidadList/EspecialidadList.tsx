import { useEffect, useState } from "react";
import {
  listarEspecialidad,
  eliminarEspecialidad,
} from "../../services/especialidad.service";
import type { Especialidad } from "../../models/especialidad";
import { EspecialidadForm } from "../../components/EspecialidadForm/EspecialidadForm";

export const EspecialidadList = () => {
  const [especialidades, setEspecialidades] = useState<Especialidad[]>([]);
  const [editingId, setEditingId] = useState<number | null>(null);
  const [showForm, setShowForm] = useState(false);
  const [loading, setLoading] = useState(true);

  const getEspecialidades = async () => {
    try {
      const response = await listarEspecialidad();
      setEspecialidades(response);
      setLoading(false);
    } catch (error: any) {
      console.error("Error al listar especialidades", error);
      window.alert("Error al cargar las especialidades: " + error.message);
    }
  };

  useEffect(() => {
    getEspecialidades();
  }, []);

  const handleEliminar = async (id: number) => {
    if (window.confirm("¿Está seguro de eliminar la especialidad?")) {
      try {
        await eliminarEspecialidad(id);
        setEspecialidades((prev) => prev.filter((e) => e.id !== id));
      } catch (error: any) {
        console.error("Error al eliminar especialidad", error.message);
      }
    }
  };

  if (loading) {
    return <h1>Cargando Especialidades...</h1>;
  }

  return (
    <>
      <button
        className="btn btn-primary mb-3"
        onClick={() => {
          setShowForm(true);
          setEditingId(null);
        }}
      >
        Nueva Especialidad
      </button>

      {showForm && (
        <EspecialidadForm
          especialidadId={editingId ?? undefined}
          onSuccess={() => {
            getEspecialidades();
            setShowForm(false);
            setEditingId(null);
          }}
          onCancel={() => {
            setShowForm(false);
            setEditingId(null);
          }}
        />
      )}

      <table className="table table-striped table-hover shadow-sm">
        <thead className="table-primary">
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Descripción</th>
            <th className="text-center">Acciones</th>
          </tr>
        </thead>
        <tbody>
          {especialidades.map((esp) => (
            <tr key={esp.id}>
              <td>{esp.id}</td>
              <td>{esp.nombre}</td>
              <td>{esp.descripcion}</td>
              <td className="text-center">
                <button
                  className="btn btn-warning me-2"
                  onClick={() => {
                    setEditingId(esp.id);
                    setShowForm(true);
                  }}
                >
                  Editar
                </button>

                <button
                  className="btn btn-danger"
                  onClick={() => handleEliminar(esp.id)}
                >
                  Eliminar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
};