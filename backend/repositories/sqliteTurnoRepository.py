from interfaces.interfacePersistencia import IRepository 
from models.medico import Medico
from database import Database
from models.medico import Medico
from models.especialidad import Especialidad
from models.turno import Turno
from models.paciente import Paciente
from models.estado import Estado

class SqliteTurnoRepository(IRepository):
    def __init__(self, db: Database):
        self.db = db

    def save(self, turno: Turno):
        #query = "INSERT INTO medicos (nombre, apellido, email, especialidad_id) VALUES (?, ?, ?, ?)"
        #self.db.execute(query, (medico.nombre, medico.apellido, medico.email, medico.especialidad.id))
        pass

    def getAll(self):
        query = """
        SELECT 
            t.id, t.fecha,

            -- Paciente (puede ser NULL)
            p.id, p.nombre, p.apellido, p.email,

            -- Médico
            m.id, m.nombre, m.apellido, m.email,

            -- Especialidad del médico
            e.id, e.nombre, e.descripcion,

            -- Estado del turno
            est.id, est.nombre, est.descripcion

        FROM turnos t
        LEFT JOIN pacientes p ON t.paciente_id = p.id   -- <--- cambio clave
        JOIN medicos m ON t.medico_id = m.id
        JOIN especialidades e ON m.especialidad_id = e.id
        JOIN estados est ON t.estado_id = est.id
            """

        cursor = self.db.execute(query)
        filas = cursor.fetchall()

        turnos = []
        for f in filas:
            (
                turno_id, fecha,
                pac_id, pac_nom, pac_ape, pac_mail,
                med_id, med_nom, med_ape, med_mail,
                esp_id, esp_nom, esp_desc,
                est_id, est_nom, est_desc
            ) = f

            paciente = None
            if pac_id is not None:
                paciente = Paciente(pac_id, pac_nom, pac_ape, pac_mail)

            especialidad = Especialidad(esp_id, esp_nom, esp_desc)
            medico = Medico(med_id, med_nom, med_ape, med_mail, especialidad)
            estado = Estado(est_id, est_nom, est_desc)

            turno = Turno(turno_id, paciente, medico, estado, fecha)
            turnos.append(turno)

        return turnos
    
    def getById(self, id):
        pass

    def update(self, medico: Medico):
        pass
        

    def deleteById(self, id):
        pass