from fastapi import APIRouter, HTTPException
from schemas.pacienteSchema import Paciente, PacienteUpdate
from database import Database
from repositories.sqlitePacienteRepository import SqlitePacienteRepository
from controllers.pacientes.pacientesController import PacienteController

router = APIRouter() 

db = Database()
paciente_repo = SqlitePacienteRepository(db)
paciente_controller = PacienteController(paciente_repo)

@router.post("/pacientes")
def alta_paciente(paciente: Paciente):
    paciente_controller.crear_paciente(
        nombre=paciente.nombre,
        apellido=paciente.apellido,
        email=paciente.email
    )
    return {"mensaje": "Paciente creado"}

@router.get("/pacientes")
def listar_pacientes():
    pacientes = paciente_controller.listar_pacientes()
    return pacientes

@router.get("/pacientes/{id}")
def obtener_paciente(id: int):
    paciente = paciente_controller.obtener_paciente(id)
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return paciente

@router.put("/pacientes/{id}")
def actualizar_paciente(id: int, paciente: PacienteUpdate):
    actualizado = paciente_controller.actualizar_paciente(
        id=id,
        nombre=paciente.nombre,
        apellido=paciente.apellido,
        email=paciente.email
    )
    if not actualizado:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return {"mensaje": "Paciente actualizado"}

@router.delete("/pacientes/{id}")
def eliminar_paciente(id: int):
    eliminado = paciente_controller.eliminar_paciente_por_id(id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    return {"mensaje": "Paciente eliminado"}