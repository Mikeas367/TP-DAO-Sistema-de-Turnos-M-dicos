from models.medico import Medico
from interfaces.interfacePersistencia import IRepository
from fastapi import HTTPException, status

class NuevoMedicoController:
    def __init__(self, medico_repo: IRepository, especialidad_repo: IRepository):
        self.medico_repo = medico_repo # repositorio del medico
        self.especialidad_repo = especialidad_repo

    def nuevo_medico(self, nombre: str, apellido: str, email:str , especialidad_id: int):
        especialidad = self.buscar_especialidad(especialidad_id)
        medico = Medico(None, nombre=nombre, apellido=apellido,email=email, especialidad=especialidad)
        self.medico_repo.save(medico)
    
    def buscar_especialidad(self, esp_id: int):
        esp =  self.especialidad_repo.getById(esp_id)
        if not esp:
            #error HTTP para el front
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No se encontró la especialidad con id {esp_id}"
            )
        return esp


