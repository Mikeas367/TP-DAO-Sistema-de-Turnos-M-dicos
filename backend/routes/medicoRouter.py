from fastapi import APIRouter, HTTPException
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

#Buscar un solo medico
@router.get("/medicos/{id}")
def obtener_medico(id: int):
    medico = medico_controller.obtener_medico(id)
    if not medico:
        raise HTTPException(status_code=404, detail="Médico no encontrado")
    return medico

@router.put("/medicos/{id}")
def actualizar_medico(id: int, medico: Medico):
    actualizado = medico_controller.actualizar_medico(
        id=id,
        nombre=medico.nombre,
        apellido=medico.apellido,
        email=medico.email
    )
    if not actualizado:
        raise HTTPException(status_code=404, detail="Médico no encontrado")
    return {"mensaje": "Médico actualizado"}

@router.delete("/medicos/{id}")
def eliminar_medico(id: int):
    eliminado = medico_controller.eliminar_medico_por_id(id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Médico no encontrado")
    return {"mensaje": "Médico eliminado"}
