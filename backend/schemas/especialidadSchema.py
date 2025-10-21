from pydantic import BaseModel,Field

class Especialidad(BaseModel):
    nombre: str = Field(..., min_length=2)
    descripcion: str = Field(..., min_length=2)
