from pydantic import BaseModel
from datetime import datetime

class TurnoCreate(BaseModel):
    turno_id: int
    paciente_id: int
