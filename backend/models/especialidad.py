from typing import Optional

class Especialidad:
    def __init__(self, id: Optional[int], nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion


    def __str__(self):
        return f"Especialidad -> Id: {self.id}, Nombre: {self.nombre}, Descripcion: {self.descripcion}"