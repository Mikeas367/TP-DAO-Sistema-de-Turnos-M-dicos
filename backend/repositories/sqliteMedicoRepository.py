from interfaces.interfacePersistencia import IRepository 
from models.medico import Medico
from database import Database
from models.medico import Medico
from models.especialidad import Especialidad


class SqliteMedicoRepository(IRepository):
    def __init__(self, db: Database):
        self.db = db

    def save(self, medico: Medico):
        query = "INSERT INTO medicos (nombre, apellido, email, especialidad_id) VALUES (?, ?, ?, ?)"
        self.db.execute(query, (medico.nombre, medico.apellido, medico.email, medico.especialidad.id))

    def getAll(self):
        query = """
            SELECT m.id, m.nombre, m.apellido, m.email,
                e.id, e.nombre, e.descripcion
            FROM medicos m
            JOIN especialidades e ON m.especialidad_id = e.id
        """
        cursor = self.db.execute(query)
        filas = cursor.fetchall()

        medicos = []
        for f in filas:
            esp = Especialidad(f[4], f[5], f[6])
            medicos.append(Medico(f[0], f[1], f[2], f[3], esp))

        return medicos
    
    def getById(self, id):
        query = """
            SELECT m.id, m.nombre, m.apellido, m.email,
                e.id, e.nombre, e.descripcion
            FROM medicos m
            JOIN especialidades e ON m.especialidad_id = e.id
            WHERE m.id = ?
        """
        
        cursor = self.db.execute(query, (id,))
        fila = cursor.fetchone()

        if not fila:
            return None

        especialidad = Especialidad(fila[4], fila[5], fila[6])

        medico = Medico(
            id=fila[0],
            nombre=fila[1],
            apellido=fila[2],
            email=fila[3],
            especialidad=especialidad
        )

        return medico

    def update(self, medico: Medico):
        query = """
            UPDATE medicos
            SET nombre = ?, apellido = ?, email = ?, especialidad_id = ?
            WHERE id = ?
        """
        self.db.execute(query, (
            medico.nombre,
            medico.apellido,
            medico.email,
            medico.especialidad.id,
            medico.id
        ))
        

    def deleteById(self, id):
        query = "DELETE FROM medicos WHERE id = ?"
        cursor = self.db.execute(query, (id,))
        return cursor.rowcount > 0

        
