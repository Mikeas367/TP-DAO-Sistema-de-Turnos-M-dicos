from fastapi import APIRouter
from database import Database
from controllers.turno.solicitarTurnoController import SolicitarTurnoController
from repositories.sqliteTurnoRepository import SqliteTurnoRepository


router = APIRouter() 

db = Database()
turno_repo = SqliteTurnoRepository(db)
turnoController = SolicitarTurnoController(turno_repo)


@router.get("/turnos")
def listar_turnos_libres():
    return turnoController.buscarTurnos()