from fastapi import APIRouter
from database import Database
from controllers.turno.solicitarTurnoController import SolicitarTurnoController
from repositories.sqliteTurnoRepository import SqliteTurnoRepository
from repositories.sqlitePacienteRepository import SqlitePacienteRepository
from repositories.sqliteEstadoRepository import SqliteEstadoRepository
from repositories.sqliteMedicoRepository import SqliteMedicoRepository
from repositories.sqliteHistoriaClinicaRepository import SqliteHistoriaClinicaRepository
from controllers.turno.liberarTurnoController import LiberarTurnoController
from controllers.turno.registrarAsistenciaController import RegistraAsistenciaController
from controllers.turno.turnoMedicoController import TurnoMedicoController
from controllers.turno.registrarInasistenciaController import RegistraInAsistenciaController
from controllers.turno.registrarNuevoTurnoController import RegistrarNuevoTurnoController
from schemas.turnoSchema import TurnoConsulta
from schemas.turnoSchema import TurnoCreate, TurnoAsistencia

router = APIRouter() 

db = Database()
turno_repo = SqliteTurnoRepository(db)
estado_repo = SqliteEstadoRepository(db)
paciente_repo = SqlitePacienteRepository(db)
medico_repo = SqliteMedicoRepository(db)
historia_clinica_repo = SqliteHistoriaClinicaRepository(db)


solicitar_turno_controller = SolicitarTurnoController(turno_repo, estados_repo=estado_repo, paciente_repo=paciente_repo)
turnos_medico_controller = TurnoMedicoController(repo_medico=medico_repo, repoturnos=turno_repo)
liberar_turno_controller = LiberarTurnoController(turno_repo=turno_repo, estados_repo=estado_repo)
marcar_inasistencia_controller = RegistraInAsistenciaController(turno_repo= turno_repo, estados_repo=estado_repo)
registrar_nuevo_turno_controller = RegistrarNuevoTurnoController(turno_repo=turno_repo, estado_repo=estado_repo, medico_repo=medico_repo)
marcar_asistencia_controller = RegistraAsistenciaController(turno_repo=turno_repo, estados_repo=estado_repo, historia_clinica_repo= historia_clinica_repo)

@router.get("/turnos")
def listar_turnos_libres():
    return solicitar_turno_controller.buscarTurnos()


@router.post("/solicitar-turno")
def solicitar_turno(turno: TurnoConsulta):
    solicitar_turno_controller.solicitar_turno(turno)

@router.post("/nuevo-turno")
def nuevo_turno(turno: TurnoCreate):
    registrar_nuevo_turno_controller.registrar_nuevo_turno(turno)

@router.post("/liberar-turno")
def liberar_turno(turno: TurnoConsulta):
    liberar_turno_controller.liberar_turno(turno)

@router.post("/marcar-asistencia")
def marcar_asistencia(turno: TurnoAsistencia):
    marcar_asistencia_controller.registrarAsistencia(turno)

@router.post("/marcar-inasistencia")
def marcar_asistencia(turno: TurnoConsulta):
    marcar_inasistencia_controller.registrarInAsistencia(turno)

@router.get("/turnos-medico/{id}")
def turnos_medico(id: int):
    return turnos_medico_controller.buscar_turnos_medico(id)