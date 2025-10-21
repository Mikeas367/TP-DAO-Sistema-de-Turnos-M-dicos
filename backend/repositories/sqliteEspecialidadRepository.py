from interfaces.interfacePersistencia import IRepository
from models.especialidad import Especialidad
from database import Database

class SqliteEspecialidadRepository(IRepository):
    def __init__(self, db: Database):
        self.db = db
    
    def save(self, especialidad: Especialidad):
        query = "INSERT INTO especialidad (nombre, descripcion) VALUES (?,?)"
        self.db.execute(query, (especialidad.nombre, especialidad.descripcion))

    def getAll(self):
        pass

    def deleteById(self, id):
        pass