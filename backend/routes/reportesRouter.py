from fastapi import APIRouter
from database import Database
from repositories.sqliteTurnoRepository import SqliteTurnoRepository
from repositories.sqliteEspecialidadRepository import SqliteEspecialidadRepository
from controllers.reportortes.asistenciaVsinasistenciaController import ReporteAsistencia
from controllers.reportortes.turnosXEspecialidadController import ReporteTurnosXEspecialidad


router = APIRouter() 

db = Database()
turno_repo = SqliteTurnoRepository(db)
especialidad_repo = SqliteEspecialidadRepository(db)

reporte_asistencia = ReporteAsistencia(turno_repo=turno_repo)


reporte_turno_especialidad = ReporteTurnosXEspecialidad(turno_repo=turno_repo, especialidad_repo=especialidad_repo)

@router.get("/asistencia-vs-inacistencias")
def generar_reporte_asistencia_vs_inasistencias():
    reporte_asistencia.generarReporteAsistencia()

@router.get("/turno_x_especialidad")
def generar_reporte_turno_x_especialidad():
    reporte_turno_especialidad.generarReporte()