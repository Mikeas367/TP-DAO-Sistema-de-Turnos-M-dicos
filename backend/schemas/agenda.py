from pydantic import BaseModel
from typing import List

class DiaLaboralCreate(BaseModel):
    dia_semana: int
    hora_inicio: str      # "08:00"
    hora_fin: str         # "12:00"
    duracion_turno_min: int

class AgendaCreate(BaseModel):
    medico_id: int
    dias_trabajo: List[DiaLaboralCreate]