from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse
from database import Database
from repositories.sqliteTurnoRepository import SqliteTurnoRepository
from controllers.reportortes.asistenciaVsinasistenciaController import ReporteAsistencia
from controllers.reportortes.pacientesAtendidosController import ReportePacientesAtendidos

router = APIRouter() 

db = Database()
turno_repo = SqliteTurnoRepository(db)

reporte_asistencia = ReporteAsistencia(turno_repo=turno_repo)
reporte_pacientes_atendidos = ReportePacientesAtendidos(turno_repo=turno_repo)

@router.get("/asistencia-vs-inacistencias")
def generar_reporte_asistencia_vs_inasistencias():
    reporte_asistencia.generarReporteAsistencia()

from fastapi.responses import FileResponse

@router.get("/asistencia-vs-inasistencias-pdf")
def descargar_pdf():
    ruta_pdf = reporte_asistencia.generarReporteAsistencia()
    return FileResponse(ruta_pdf, media_type="application/pdf", filename="reporte_asistencias.pdf")


@router.get("/pacientes-atendidos")
def pacientes_atendidos(desde: str = Query(...), hasta: str = Query(...)):
    return reporte_pacientes_atendidos.generarReportePacientesAtendidos(desde, hasta)

@router.get("/pacientes-atendidos-pdf")
def descargar_pdf(desde: str, hasta: str):
    pdf_buffer = reporte_pacientes_atendidos.generar_pdf(desde, hasta)
    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={"Content-Disposition": f"attachment; filename=pacientes_{desde}_a_{hasta}.pdf"}
    )