from fastapi import APIRouter
from schemas.medicoSchema import Medico
from database import Database
from repositories.sqliteMedicoRepository import SqliteMedicoRepository
from controllers.medicoController import MedicoController

router = APIRouter()  # Usar APIRouter en lugar de FastAPI()

# Instancias globales (únicas)
db = Database()
medico_repo = SqliteMedicoRepository(db)
medico_controller = MedicoController(medico_repo)

@router.post("/medicos")
def alta_medico(medico: Medico):
    creado = medico_controller.crear_medico(
        nombre=medico.nombre,
        apellido=medico.apellido,
        email=medico.email
    )
    return {"mensaje": "Médico creado", "nombre": creado.nombre}

@router.get("/medicos")
def listar_medicos():
    medicos = medico_controller.listar_medicos()
    return {"medicos": medicos}