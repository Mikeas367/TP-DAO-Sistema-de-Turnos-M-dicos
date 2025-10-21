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
    
    def obtener_medico(self, id: int):
        medicos = self.repository.getAll()
        for medico in medicos:
            if medico["id"] == id:
                return medico
        return None
    
    def eliminar_medico_por_id(self, id: int) -> bool:
        try:
            eliminado = self.repository.deleteById(id)
            return eliminado
        except Exception:
            return False
        

    def actualizar_medico(self, id: int, nombre: str, apellido: str, email: str) -> bool:
        medico_existente = self.repository.getById(id)
        if not medico_existente:
            return False
        self.repository.update(id, nombre, apellido, email)
        return True

