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
    
    def getById(self, id):
        query = "SELECT id, nombre, apellido, email FROM medicos WHERE id = ?"
        cursor = self.db.execute(query, (id,))
        fila = cursor.fetchone()
        if fila:
            return {
                "id": fila[0],
                "nombre": fila[1],
                "apellido": fila[2],
                "email": fila[3]
            }
        return None

    def update(self, id, nombre, apellido, email):
        query = "UPDATE medicos SET nombre = ?, apellido = ?, email = ? WHERE id = ?"
        self.db.execute(query, (nombre, apellido, email, id))

    def deleteById(self, id):
        query = "DELETE FROM medicos WHERE id = ?"
        cursor = self.db.execute(query, (id,))
        return cursor.rowcount > 0

        
