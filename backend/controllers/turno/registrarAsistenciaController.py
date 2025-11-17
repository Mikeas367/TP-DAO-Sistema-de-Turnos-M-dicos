from interfaces.interfacePersistencia import IRepository
from schemas.turnoSchema import TurnoCreate
from models.turno import Turno
from fastapi import HTTPException, status

class RegistraAsistenciaController:
    def __init__(self, turno_repo: IRepository, estados_repo: IRepository):
        self.turno_repo = turno_repo
        self.estados_repo = estados_repo


    def registrarAsistencia(self, turno: TurnoCreate):
        turno_a_marcar = self.buscar_turno(turno.turno_id)
        estado_asistido = self.buscar_estado_asistido()

        turno_a_marcar.marcar_asistencia(estado_asistido)
        self.turno_repo.update(turno_a_marcar)



    def buscar_estado_asistido(self):
        estados = self.estados_repo.getAll()
        for estado in estados:
            if estado.es_asistido():
                return estado
    
    def buscar_turno(self, turno_id: int)-> Turno:
        p =  self.turno_repo.getById(turno_id)
        if not p:
            #error HTTP para el front
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No se encontró el turno con id {turno_id}"
            )
        return p