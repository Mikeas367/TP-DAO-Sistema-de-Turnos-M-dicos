import { useEffect, useState } from "react"
import { listarMedicos, eliminarMedico } from "../../services"
import type { Medico } from "../../models"
 
export const MedicoList = () => {
    const [medicos, setMedicos] = useState<Medico[]>()
    useEffect(()=>{
        const getMedicos = async() => {
            try {
                const response = await listarMedicos()
                setMedicos(response)
            } catch (error) {
                
            }
        }
        getMedicos()
    }, [])

    const handleEliminar = async (id: number) => {
      if(window.confirm("esta seguro de eliminar el medico?")){
        try {
            await eliminarMedico(id)
            // Actualizamos la lista filtrando el médico eliminado
            setMedicos(prev => prev?.filter(m => m.id !== id))
        } catch (error) {
            console.error("Error al eliminar médico", error)
        }
      }
    }

    return(
        <>
        <table className="table table-striped table-hover shadow-sm">
        <thead className="table-primary">
          <tr>
            <th>Id</th>
            <th>Nombre</th>
            <th>Apellido</th>
            <th>Email</th>
            <th className="text-center">Acciones</th>
          </tr>
        </thead>
        <tbody>
          {medicos?.map((medico) => (
            <tr key={medico.id}>
              <td>{medico.id}</td>
              <td>{medico.nombre}</td>
              <td>{medico.apellido}</td>
              <td>{medico.email}</td>
              <td className="text-center">
                <button type="button" className="btn btn-danger me-2" onClick={() => handleEliminar(medico.id)}>
                   Eliminar
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
        </>
    )
}