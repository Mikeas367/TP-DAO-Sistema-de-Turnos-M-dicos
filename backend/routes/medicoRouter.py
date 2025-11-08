from fastapi import APIRouter, HTTPException
from schemas.medicoSchema import Medico
from database import Database
from repositories.sqliteMedicoRepository import SqliteMedicoRepository
from repositories.sqliteEspecialidadRepository import SqliteEspecialidadRepository
from controllers.medicoController import MedicoController
from controllers.medico.nuevoMedicoController import NuevoMedicoController
from controllers.medico.consultarMedicos import ConsultarMedicosController
from controllers.medico.modificarMedicoController import ModificarMedicosController
router = APIRouter() 

db = Database()
medico_repo = SqliteMedicoRepository(db)
especialidad_repo = SqliteEspecialidadRepository(db)
medico_controller = MedicoController(medico_repo, especialidad_repo)
nuevo_medico_controller = NuevoMedicoController(medico_repo, especialidad_repo)
consultar_medicos_controller = ConsultarMedicosController(medico_repo)
modificarMedicosController = ModificarMedicosController(medico_repo)


@router.post("/medicos")
def alta_medico(medico: Medico):
    return nuevo_medico_controller.nuevo_medico(
        nombre=medico.nombre,
        apellido=medico.apellido,
        email=medico.email,
        especialidad_id=medico.especialidad_id
    )

@router.get("/medicos")
def listar_medicos():
    return consultar_medicos_controller.obtener_medicos()

#Buscar un solo medico
@router.get("/medicos/{id}")
def obtener_medico(id: int):
    return consultar_medicos_controller.obtener_medico_por_id(id)

@router.put("/medicos/{id}")
def actualizar_medico(id: int, medico: Medico):
    modificarMedicosController.modificar_medico(id=id, nombre=medico.nombre, apellido=medico.apellido, email=medico.email, especialidad_id=medico.especialidad_id)

@router.delete("/medicos/{id}")
def eliminar_medico(id: int):
    eliminado = medico_controller.eliminar_medico_por_id(id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Médico no encontrado")
    return {"mensaje": "Médico eliminado"}
