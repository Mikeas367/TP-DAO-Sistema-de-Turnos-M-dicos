from models.especialidad import Especialidad
from typing import Optional

class Medico:
    def __init__(self,id: Optional[int] ,nombre: str, apellido: str, email: str, especialidad: Especialidad):
        self.id = id
        self.nombre = nombre 
        self.apellido = apellido
        self.email = email
        self.especialidad = especialidad 
    