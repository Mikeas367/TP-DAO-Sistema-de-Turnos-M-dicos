from pydantic import BaseModel,Field

class Especialidad(BaseModel):
    nombre: str = Field(..., min_length=2)
    descripcion: str = Field(..., min_length=2)

class EspecialidadBase(BaseModel):
    nombre: str
    descripcion: str

class EspecialidadCreate(EspecialidadBase):
    pass

class EspecialidadUpdate(EspecialidadBase):
    pass

class EspecialidadResponse(EspecialidadBase):
    id: int

    class Config:
        orm_mode = True