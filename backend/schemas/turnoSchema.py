from pydantic import BaseModel

class TurnoConsulta(BaseModel):
    turno_id: int
    paciente_id: int

class TurnoCreate(BaseModel):
    fecha: str
    medico_id: int


