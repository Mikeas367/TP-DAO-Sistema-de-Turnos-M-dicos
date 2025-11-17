from interfaces.interfacePersistencia import IRepository
from schemas.turnoSchema import TurnoCreate
from models.turno import Turno
from fastapi import HTTPException, status

class ReporteAsistencia:
    def __init__(self, turno_repo: IRepository):
        self.turno_repo = turno_repo
    

    def generarReporteAsistencia(self):
        turnos = self.turno_repo.getAll()

        turnosAsistidos = []
        turnosNoAsistidos = []

        for turno in turnos:
            if turno.es_asistido():
                turnosAsistidos.append(turno)
            elif turno.es_no_asistido:
                turnosNoAsistidos.append(turno)
        
