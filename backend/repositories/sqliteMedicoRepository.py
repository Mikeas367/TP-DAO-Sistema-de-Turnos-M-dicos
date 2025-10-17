from interfaces.interfacePersistencia import IRepository 
from models.medico import Medico
from database import Database


class SqliteMedicoRepository(IRepository):
    def __init__(self, db: Database):
        self.db = db

    def save(self, medico: Medico):
        query = "INSERT INTO medicos (nombre, apellido, email) VALUES (?, ?, ?)"
        self.db.execute(query, (medico.nombre, medico.apellido, medico.email))
