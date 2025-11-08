import { useEffect, useState } from "react";
import { listarMedicos, eliminarMedico } from "../../services";
import type { Medico } from "../../models";
import { MedicoForm } from "../../components";

export const MedicoList = () => {
  const [medicos, setMedicos] = useState<Medico[]>([]);
  const [editingMedicoId, setEditingMedicoId] = useState<number | null>(null);
  const [showForm, setShowForm] = useState(false); // estado para mostrar el form de editar o crear Medico
  const [loading, setLoading] = useState(true)
  

  const getMedicos = async () => {
    try { 
      const response = await listarMedicos();
      setMedicos(response);
      setLoading(false)
    } catch (error: any) {
      console.error("Error al listar médicos", error);
      window.alert("Error al cargar los medicos: " + error.message)
    }
  };

  useEffect(() => {
    getMedicos();
  }, []);

  const handleEliminar = async (id: number) => {
    if (window.confirm("¿Está seguro de eliminar el médico?")) {
      try {
        await eliminarMedico(id);
        setMedicos((prev) => prev.filter((m) => m.id !== id));
      } catch (error: any) {
        console.error("Error al eliminar médico", error.message);
      }
    }
  };

  if (loading) {
    return(
      <h1>Cargando Doctores...</h1>
    )
  }

  return (
    <>
      {/* Boton Para Crear el Medico */}
      <button
        className="btn btn-primary mb-3"
        onClick={() => {
          setShowForm(true);
          setEditingMedicoId(null);}}>
        Nuevo Médico
      </button>

      {/* Muestra el formulario si se selecciono para editar un medico */}
      {showForm && (
        <MedicoForm
          medicoId={editingMedicoId ?? undefined}
          onSuccess={() => {
            getMedicos();
            setShowForm(false);
            setEditingMedicoId(null);
          }}
          onCancel={() => {
            setShowForm(false);
            setEditingMedicoId(null);
          }}
        />
      )}
      {/* Tabla con los medicos */}

      <table className="table table-striped table-hover shadow-sm">
        <thead className="table-primary">
          <tr>
            <th>Id</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Email</th>
            <th>Especialidad</th>
            <th className="text-center">Acciones</th>
          </tr>
        </thead>
        <tbody>
          {medicos.map((medico) => (
            <tr key={medico.id}>
              <td>{medico.id}</td>
              <td>{medico.nombre}</td>
              <td>{medico.apellido}</td>
              <td>{medico.email}</td>
              <td>{medico.especialidad.nombre}</td>
              <td className="text-center">
                <button
                  className="btn btn-warning me-2"
                  onClick={() => {
                    setEditingMedicoId(medico.id);
                    setShowForm(true);
                  }}
                >
                  Editar
                </button>
                <button
                  className="btn btn-danger"
                  onClick={() => handleEliminar(medico.id)}
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