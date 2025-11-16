from interfaces.interfacePersistencia import IRepository 
from database import Database
from models.estado import Estado

class SqliteEstadoRepository(IRepository):
    def __init__(self, db: Database):
        self.db = db

    def getAll(self):
        query = """
            SELECT e.id, e.nombre, e.descripcion
            FROM estados e
        """
        cursor = self.db.execute(query)
        filas = cursor.fetchall()

        estados = []
        for f in filas:
            estado = Estado(f[0], f[1], f[2])
            estados.append(estado)

        return estados
    
    def getById(self, id):
        return super().getById(id)
    
    def save(self, entity):
        return super().save(entity)
    
    def update(self, entity):
        return super().update(entity)
    
    def deleteById(self, id):
        return super().deleteById(id)
    