from fastapi import APIRouter
from schemas.medicoSchema import Medico
from database import Database
from repositories.sqliteMedicoRepository import SqliteMedicoRepository
from controllers.medicoController import MedicoController

router = APIRouter() 

db = Database()
medico_repo = SqliteMedicoRepository(db)
medico_controller = MedicoController(medico_repo)

@router.post("/medicos")
def alta_medico(medico: Medico):
    print(medico)
    medico_controller.crear_medico(
        nombre=medico.nombre,
        apellido=medico.apellido,
        email=medico.email
    )
    return {"mensaje": "Médico creado"}

@router.get("/medicos")
def listar_medicos():
    medicos = medico_controller.listar_medicos()
    return medicos

@router.delete("/medicos/{id}")
def eliminar_medico_por_id(id):
    print("El id es" + id)
    medico_controller.eliminar_medico_por_id(id)
    return {"mensaje": "Médico eliminado"}