from fastapi import APIRouter
from database import Database
from repositories.sqliteTurnoRepository import SqliteTurnoRepository
from controllers.reportortes.asistenciaVsinasistenciaController import ReporteAsistencia


router = APIRouter() 

db = Database()
turno_repo = SqliteTurnoRepository(db)
reporte_asistencia = ReporteAsistencia(turno_repo=turno_repo)

@router.get("/asistencia-vs-inacistencias")
def generar_reporte_asistencia_vs_inasistencias():
    reporte_asistencia.generarReporteAsistencia()
