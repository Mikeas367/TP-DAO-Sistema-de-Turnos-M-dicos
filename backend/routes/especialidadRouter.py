from database import Database
from repositories.sqliteEspecialidadRepository import SqliteEspecialidadRepository
from controllers.especialidadController import especialidadController
from schemas.especialidadSchema import Especialidad, EspecialidadResponse
from fastapi import APIRouter, Depends
from database import Database
from schemas.especialidadSchema import (
    EspecialidadCreate,
    EspecialidadUpdate,
    EspecialidadResponse
)

router = APIRouter()

db = Database()
especialidad_repo = SqliteEspecialidadRepository(db)
especialidad_controller = especialidadController(especialidad_repo)

@router.post("/especialidad")
def alta_especialidad(especialidad: Especialidad):
    especialidad_controller.crear_especialidad(especialidad.nombre, especialidad.descripcion)

    return {"mensaje" : "Especialidad creada"}

@router.get("/especialidad")
def listar_especialidades():
    especialidades = especialidad_controller.listar_especialidades()
    return especialidades

@router.get("/especialidad/{id}")
def obtener(id: int):
    return especialidad_controller.obtener(id)

@router.put("/especialidad/{id}")
def actualizar(id: int, data: EspecialidadUpdate):
    return especialidadController.actualizar(id, data)

@router.delete("/especialidad/{id}")
def eliminar(id: int):
    especialidadController.eliminar(id)
    return {"mensaje": "Especialidad eliminada correctamente"}

