from fastapi import APIRouter
from database import Database
from repositories.sqlitePacienteRepository import SqlitePacienteRepository
from controllers.pacientes.consultarPacientesController import ConsultarPacientesController
router = APIRouter() 

db = Database()
paciente_repo = SqlitePacienteRepository(db)
pacienteController = ConsultarPacientesController(paciente_repo)



@router.get("/pacientes")
def listar_pacientes():
    return pacienteController.obtener_pacientes()
