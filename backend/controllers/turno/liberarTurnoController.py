from interfaces.interfacePersistencia import IRepository 
from models.turno import Turno
from schemas.turnoSchema import TurnoConsulta
from fastapi import HTTPException, status


class LiberarTurnoController:
    def __init__(self, turno_repo: IRepository, estados_repo: IRepository):
        self.turno_repo = turno_repo
        self.estados_repo = estados_repo


    def buscarTurnos(self):
        turnos = self.turno_repo.getAll()
        return turnos
    

    def liberar_turno(self, turno: TurnoConsulta):
        turno_a_liberar = self.buscar_turno(turno.turno_id)
        estado_libre = self.buscar_estado_libre()
        turno_a_liberar.liberar_turno(estado_libre)
        print(f"Estado del turno: {turno_a_liberar.estado} + Paciente: {turno_a_liberar.paciente}")
        self.turno_repo.update(turno_a_liberar)
 

    def buscar_estado_libre(self):
        estados = self.estados_repo.getAll()
        for estado in estados:
            if estado.es_libre():
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