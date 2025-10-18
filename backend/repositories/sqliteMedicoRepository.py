from interfaces.interfacePersistencia import IRepository 
from models.medico import Medico
from database import Database


class SqliteMedicoRepository(IRepository):
    def __init__(self, db: Database):
        self.db = db

    def save(self, medico: Medico):
        query = "INSERT INTO medicos (nombre, apellido, email) VALUES (?, ?, ?)"
        self.db.execute(query, (medico.nombre, medico.apellido, medico.email))

    def getAll(self):
        query = "SELECT id, nombre, apellido, email FROM medicos"
        cursor = self.db.execute(query)
        filas_medicos = cursor.fetchall()
        medicos = []
        # le doy como un formato Json 
        for fila in filas_medicos:
            medico = {
                "id": fila[0],
                "nombre": fila[1],
                "apellido": fila[2],
                "email": fila[3]
            }
            medicos.append(medico)
        return medicos

    def deleteById(self, id):
        query = "DELETE FROM medicos WHERE id = ?"
        self.db.execute(query, (id))
        
