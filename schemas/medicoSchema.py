from pydantic import BaseModel

class Medico(BaseModel):
    nombre: str 
    apellido: str
    email: str