from models.medico import Medico
from interfaces.interfacePersistencia import IRepository

class MedicoController:
    def __init__(self, repository: IRepository):
        self.repository = repository # repositorio del medico

    def crear_medico(self, nombre: str, apellido: str, email: str):
        medico = Medico(nombre, apellido, email)
        self.repository.save(medico)
        return medico
