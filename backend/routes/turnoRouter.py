from fastapi import APIRouter
from database import Database
from controllers.turno.solicitarTurnoController import SolicitarTurnoController
from repositories.sqliteTurnoRepository import SqliteTurnoRepository
from repositories.sqlitePacienteRepository import SqlitePacienteRepository
from repositories.sqliteEstadoRepository import SqliteEstadoRepository
from schemas.turnoSchema import TurnoCreate

router = APIRouter() 

db = Database()
turno_repo = SqliteTurnoRepository(db)
estado_repo = SqliteEstadoRepository(db)
paciente_repo = SqlitePacienteRepository(db)

turnoController = SolicitarTurnoController(turno_repo, estados_repo=estado_repo, paciente_repo=paciente_repo)


@router.get("/turnos")
def listar_turnos_libres():
    return turnoController.buscarTurnos()


@router.post("/solicitar-turno")
def solicitar_turno(turno: TurnoCreate):
    turnoController.solicitar_turno(turno)
