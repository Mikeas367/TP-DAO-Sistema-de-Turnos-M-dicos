from database import Database
from fastapi import APIRouter
from repositories.sqliteEspecialidadRepository import SqliteEspecialidadRepository
from controllers.especialidadController import especialidadController
from schemas.especialidadSchema import Especialidad
router = APIRouter()

db = Database()
especialidad_repo = SqliteEspecialidadRepository(db)
especialidad_controller = especialidadController(especialidad_repo)

@router.post("/especialidad")
def alta_especialidad(especialidad: Especialidad):
    especialidad_controller.crear_especialidad(especialidad.nombre, especialidad.descripcion)
    return {"mensaje" : "Especialidad creada"}