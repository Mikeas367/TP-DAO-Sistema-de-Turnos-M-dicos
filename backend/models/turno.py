from typing import Optional
from models.paciente import Paciente
from models.medico import Medico
from models.estado import Estado

class Turno:
    def __init__(self, id: Optional[int], paciente: Optional[Paciente], medico: Medico, estado: Estado, fecha):
        self.id = id
        self.paciente = paciente
        self.medico = medico
        self.estado = estado
        self.fecha = fecha


    def esta_libre(self):
        return self.estado.es_libre()
    
    def solicitar_turno(self, estado: Estado):
        if self.esta_libre:
            self.estado = estado


    def __str__(self):
        return f"Turno ID: {self.id}, Estado: {self.estado}"