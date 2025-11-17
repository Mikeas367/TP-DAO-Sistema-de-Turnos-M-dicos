from typing import Optional
class Estado:
    def __init__(self,id: Optional[int], nombre:str, descripcion:str):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def es_libre(self):
        return self.nombre == "Libre"
    
    def es_ocupado(self):
        return self.nombre == "Ocupado"
    
    def es_asistido(self):
        return self.nombre == "Asistido"
    
    def es_no_asistido(self):
        return self.nombre == "No Asistido"