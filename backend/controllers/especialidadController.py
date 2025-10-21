from models.especialidad import Especialidad
from interfaces.interfacePersistencia import IRepository

class especialidadController:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def crear_especialidad(self, nombre:str, descripcion: str):
        especialidad = Especialidad(nombre, descripcion)
        self.repository.save(especialidad)
        return especialidad
    
    def listar_especialidades(self):
        especialidades = self.repository.getAll()
        return especialidades