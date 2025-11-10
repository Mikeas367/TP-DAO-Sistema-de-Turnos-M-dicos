from interfaces.interfacePersistencia import IRepository 
from models.turno import Turno

class SolicitarTurnoController:
    def __init__(self, turno_repo: IRepository):
        self.turno_repo = turno_repo
        


    def buscarTurnos(self):
        turnos = self.turno_repo.getAll()
        return turnos