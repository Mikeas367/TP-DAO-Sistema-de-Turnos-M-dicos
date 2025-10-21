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
        query = "SELECT id, nombre, descripcion FROM especialidades"
        cursor = self.db.execute(query)
        filas_especialidades = cursor.fetchall()
        especialidades = []
        # le doy como un formato Json 
        for fila in filas_especialidades:
            especialidad = {
                "id": fila[0],
                "nombre": fila[1],
                "descripcion": fila[2],
            }
            especialidades.append(especialidad)
        return especialidades

    def deleteById(self, id):
        pass