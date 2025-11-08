from models.medico import Medico
from interfaces.interfacePersistencia import IRepository
from fastapi import HTTPException, status


class ModificarMedicosController:
    def __init__(self, medico_repo: IRepository):
        self.medico_repo = medico_repo

    def modificar_medico(self, id: int, nombre: str, apellido: str, email: str, especialidad_id: int):
        medico = self.buscar_medico(id)
        medico.nombre = nombre
        medico.apellido = apellido
        medico.email = email
        medico.especialidad.id = especialidad_id

        self.medico_repo.update(medico)



    def buscar_medico(self, id: int):
        medico = self.medico_repo.getById(id)
        if not medico:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No se encontró el medico con id {id}"
            )
        return medico