from typing import Optional
from models.paciente import Paciente
from models.medico import Medico


class HistoriaClinica():
    def __init__(self, id: Optional[int], medico: Medico, fecha: str, paciente: Paciente, diagnostico:str, tratamiento:str):
        self.id = id
        self.medico = medico
        self.fecha = fecha
        self.paciente = paciente
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
    