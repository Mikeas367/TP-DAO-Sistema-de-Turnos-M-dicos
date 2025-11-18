from fastapi import APIRouter
from database import Database
from controllers.turno.solicitarTurnoController import SolicitarTurnoController
from repositories.sqliteTurnoRepository import SqliteTurnoRepository
from repositories.sqlitePacienteRepository import SqlitePacienteRepository
from repositories.sqliteEstadoRepository import SqliteEstadoRepository
from repositories.sqliteMedicoRepository import SqliteMedicoRepository
from controllers.turno.liberarTurnoController import LiberarTurnoController
from controllers.turno.registrarAsistenciaController import RegistraAsistenciaController
from controllers.turno.turnoMedicoController import TurnoMedicoController
from controllers.turno.registrarInasistenciaController import RegistraInAsistenciaController
from schemas.turnoSchema import TurnoCreate

router = APIRouter() 

db = Database()
turno_repo = SqliteTurnoRepository(db)
estado_repo = SqliteEstadoRepository(db)
paciente_repo = SqlitePacienteRepository(db)
medico_repo = SqliteMedicoRepository(db)


solicitar_turno_controller = SolicitarTurnoController(turno_repo, estados_repo=estado_repo, paciente_repo=paciente_repo)
turnos_medico_controller = TurnoMedicoController(repo_medico=medico_repo, repoturnos=turno_repo)
liberar_turno_controller = LiberarTurnoController(turno_repo=turno_repo, estados_repo=estado_repo)
marcar_asistencia_controller = RegistraAsistenciaController(turno_repo=turno_repo, estados_repo=estado_repo)
marcar_inasistencia_controller = RegistraInAsistenciaController(turno_repo= turno_repo, estados_repo=estado_repo)


@router.get("/turnos")
def listar_turnos_libres():
    return solicitar_turno_controller.buscarTurnos()


@router.post("/solicitar-turno")
def solicitar_turno(turno: TurnoCreate):
    solicitar_turno_controller.solicitar_turno(turno)

@router.post("/liberar-turno")
def liberar_turno(turno: TurnoCreate):
    liberar_turno_controller.liberar_turno(turno)

@router.post("/marcar-asistencia")
def marcar_asistencia(turno: TurnoCreate):
    marcar_asistencia_controller.registrarAsistencia(turno)

@router.post("/marcar-inasistencia")
def marcar_asistencia(turno: TurnoCreate):
    marcar_inasistencia_controller.registrarInAsistencia(turno)

@router.get("/turnos-medico/{id}")
def turnos_medico(id: int):
    return turnos_medico_controller.buscar_turnos_medico(id)