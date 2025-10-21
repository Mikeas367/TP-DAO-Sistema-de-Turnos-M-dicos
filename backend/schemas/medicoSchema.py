from pydantic import BaseModel,Field, EmailStr

class Medico(BaseModel):
    nombre: str = Field(..., min_length=2)
    apellido: str = Field(..., min_length=2)
    email: EmailStr
    especialidad_id: int = Field(...)
