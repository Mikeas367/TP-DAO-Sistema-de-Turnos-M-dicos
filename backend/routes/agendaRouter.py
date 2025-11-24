from fastapi import APIRouter
from controllers.agenda.generadorTurnosController import GeneradorTurnosController
from controllers.agenda.nuevaAgendaController import NuevaAgendaController
from controllers.agenda.obtenerAgendasController import ObtenerAgendaController
from database import Database
from repositories.sqliteAgendaRepository import SqliteAgendaRepository
from repositories.sqliteEstadoRepository import SqliteEstadoRepository
from repositories.sqliteMedicoRepository import SqliteMedicoRepository
from repositories.sqliteTurnoRepository import SqliteTurnoRepository
from schemas.agenda import AgendaCreate


router = APIRouter()

db = Database()
medico_repo = SqliteMedicoRepository(db)
agenda_repo = SqliteAgendaRepository(db)

turno_repo = SqliteTurnoRepository(db)
estado_repo = SqliteEstadoRepository(db)

nueva_agenda_controller = NuevaAgendaController(medico_repo=medico_repo, agenda_repo=agenda_repo)
consultor_agendas_controller = ObtenerAgendaController(agenda_repo)
generador_agendas_controller = GeneradorTurnosController(agenda_repo=agenda_repo, turnos_repo=turno_repo, estado_repo=estado_repo)

@router.post("/agendas")
def nuevaAgenda(agenda: AgendaCreate):
    nueva_agenda_controller.nuevaAgenda(agenda)

@router.get("/agendas")
def obtenerAgendas():
    return consultor_agendas_controller.obtener_agendas()

@router.post("/agendas/{agendaId}/generar-turnos")
def generarTurnos(agendaId: int):
    print("POST")
    generador_agendas_controller.generar_turnos_de_agenda(agendaId)

