from models.medico import Medico
from interfaces.interfacePersistencia import IRepository

class MedicoController:
    def __init__(self, repository: IRepository):
        self.repository = repository # repositorio del medico

    def crear_medico(self, nombre: str, apellido: str, email: str):
        medico = Medico(nombre, apellido, email)
        self.repository.save(medico)
        return medico

    def listar_medicos(self):
        medicos = self.repository.getAll()
        return medicos
    
    def eliminar_medico_por_id(self, id):
        self.repository.deleteById(id)
