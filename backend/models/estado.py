from typing import Optional
class Estado:
    def __init__(self,id: Optional[int], nombre:str, descripcion:str):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def es_libre(self):
        return self.nombre == "Libre"
    