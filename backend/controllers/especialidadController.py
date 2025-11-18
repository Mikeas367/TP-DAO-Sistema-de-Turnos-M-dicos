from models.especialidad import Especialidad
from interfaces.interfacePersistencia import IRepository
from schemas.especialidadSchema import EspecialidadCreate, EspecialidadUpdate

class especialidadController:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def crear_especialidad(self, nombre:str, descripcion: str):
        especialidad = Especialidad(None, nombre=nombre, descripcion=descripcion)
        self.repository.save(especialidad)
        return especialidad
    
    def listar_especialidades(self):
        especialidades = self.repository.getAll()
        return especialidades
    
    def crear(self, data: EspecialidadCreate):
        esp = Especialidad(None, data.nombre, data.descripcion)
        self.repo.save(esp)
        return esp 
    
    def obtener(self, id: int):
        return self.repo.getById(id)

    def actualizar(self, id: int, data: EspecialidadUpdate):
        esp = self.repo.getById(id)
        if not esp:
            return None
        esp.nombre = data.nombre
        esp.descripcion = data.descripcion
        self.repo.update(esp)
        return esp

    def eliminar(self, id: int):
        return self.repo.deleteById(id)