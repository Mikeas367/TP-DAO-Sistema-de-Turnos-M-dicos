from models.medico import Medico
from models.especialidad import Especialidad
from interfaces.interfacePersistencia import IRepository

class MedicoController:
    def __init__(self, medico_repo: IRepository, especialidad_repo: IRepository):
        self.medico_repo = medico_repo # repositorio del medico
        self.especialidad_repo = especialidad_repo

    def crear_medico(self, nombre: str, apellido: str, email: str, especialidad_id: int):
        #print(nombre, apellido, email, especialidad_id)
        esp = self.especialidad_repo.getById(especialidad_id) # valido que exista por id
        
        if not esp:
            print("No se encontro la especialidad con id: "  + especialidad_id)
        especialidad = Especialidad(None, nombre= esp["nombre"], descripcion=esp["descripcion"])
        
        medico = Medico(None, nombre, apellido, email, especialidad)
        self.medico_repo.save(medico)
        return medico

    def listar_medicos(self):
        medicos = self.medico_repo.getAll()
        return medicos
    
    def obtener_medico(self, id: int):
        medicos = self.medico_repo.getAll()
        for medico in medicos:
            if medico["id"] == id:
                return medico
        return None
    
    def eliminar_medico_por_id(self, id: int) -> bool:
        try:
            eliminado = self.medico_repo.deleteById(id)
            return eliminado
        except Exception:
            return False
        

    def actualizar_medico(self, id: int, nombre: str, apellido: str, email: str) -> bool:
        medico_existente = self.medico_repo.getById(id)

        #medico_con_nuevos_datos = Medico(id, nombre, apellido, ema)
        if not medico_existente:
            return False
        self.medico_repo.update(id, nombre, apellido, email)
        return True

