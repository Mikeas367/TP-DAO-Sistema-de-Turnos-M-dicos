from models.medico import Medico
from interfaces.interfacePersistencia import IRepository
from fastapi import HTTPException, status

class ConsultarMedicosController:
    def __init__(self, medico_repo: IRepository):
        self.medico_repo = medico_repo

    def obtener_medicos(self):
        try:
            medicos = self.medico_repo.getAll()
            return medicos
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"No se encontraron Medicos"
            )

    def obtener_medico_por_id(self, id: int):
        return self.medico_repo.getById(id)