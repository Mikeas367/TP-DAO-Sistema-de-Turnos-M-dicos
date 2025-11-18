from interfaces.interfacePersistencia import IRepository
from models.especialidad import Especialidad
from database import Database

class SqliteEspecialidadRepository(IRepository):
    def __init__(self, db: Database):
        self.db = db
    
    def save(self, especialidad: Especialidad):
        query = "INSERT INTO especialidades (nombre, descripcion) VALUES (?,?)"
        self.db.execute(query, (especialidad.nombre, especialidad.descripcion))

    def getAll(self):
        query = "SELECT id, nombre, descripcion FROM especialidades"
        cursor = self.db.execute(query)
        filas_especialidades = cursor.fetchall()
        especialidades = []
        # le doy como un formato Json 
        for fila in filas_especialidades:
            # Creamos una instancia de la clase Especialidad
            especialidad_objeto = Especialidad(
                id=fila[0],
                nombre=fila[1],
                descripcion=fila[2],
            )
            especialidades.append(especialidad_objeto)
        return especialidades

    def deleteById(self, id):
        pass

    def getById(self, id):
        query = "SELECT id, nombre, descripcion FROM especialidades WHERE id = ?"
        cursor = self.db.execute(query, (id,))
        fila = cursor.fetchone()
        if not fila:
            return None
    
        return Especialidad(fila[0], fila[1], fila[2])
    
    def update(self, especialidad: Especialidad):
        pass