from typing import Optional

class Paciente:
    def __init__(self, id: Optional[int], nombre: str, apellido:str, email:str):
        self.id = id
        self.nombre = nombre 
        self.apellido = apellido
        self.email = email
