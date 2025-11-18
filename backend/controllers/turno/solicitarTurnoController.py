from http.client import HTTPException
from interfaces.interfacePersistencia import IRepository 
from models.turno import Turno
from schemas.turnoSchema import TurnoConsulta
from fastapi import HTTPException, status

class SolicitarTurnoController:
    def __init__(self, turno_repo: IRepository, paciente_repo: IRepository, estados_repo: IRepository):
        self.turno_repo = turno_repo
        self.paciente_repo = paciente_repo
        self.estados_repo = estados_repo


    def buscarTurnos(self):
        turnos = self.turno_repo.getAll()
        turnos_a_mostrar = []
        for turno in turnos:
            if turno.esta_libre() or turno.esta_ocupado():
                turnos_a_mostrar.append(turno)
        return turnos_a_mostrar
    

    def solicitar_turno(self, turno: TurnoConsulta):
        paciente = self.buscar_paciente(turno.paciente_id)
        turno_a_ocupar = self.buscar_turno(turno.turno_id)
        estado_ocupado = self.buscar_estado_ocupado()


        turno_a_ocupar.solicitar_turno(estado_ocupado, paciente)
        self.turno_repo.update(turno_a_ocupar)
 

    def buscar_estado_ocupado(self):
        estados = self.estados_repo.getAll()
        for estado in estados:
            if estado.es_ocupado():
                return estado
            

    def buscar_paciente(self, paciente_id: int):
        p =  self.paciente_repo.getById(paciente_id)
        if not p:
            #error HTTP para el front
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No se encontró el paciente con id {p}"
            )
        return p
    

    def buscar_turno(self, turno_id: int):
        p =  self.turno_repo.getById(turno_id)
        if not p:
            #error HTTP para el front
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No se encontró el turno con id {turno_id}"
            )
        return p