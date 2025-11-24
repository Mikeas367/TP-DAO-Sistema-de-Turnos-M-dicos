from database import Database
from interfaces.interfacePersistencia import IRepository
from models.agenda import Agenda
from models.diaLaboral import DiaLaboral
from models.medico import Medico 

class SqliteAgendaRepository(IRepository):
    def __init__(self, db: Database):
        self.db = db

    def save(self, agenda: Agenda):
        query_agenda = "INSERT INTO agendas_medico (medico_id) VALUES (?)"
        cursor = self.db.execute(query_agenda, (agenda.medico.id,))
        agenda_id = cursor.lastrowid

        for dia in agenda.dias_trabajo:
            query_dia = """
                INSERT INTO agenda_dias_trabajo
                (agenda_id, dia_semana, hora_inicio, hora_fin, duracion_turno_min)
                VALUES (?, ?, ?, ?, ?)
            """
            self.db.execute(query_dia, (
                agenda_id,
                dia.dia_semana,
                dia.hora_inicio.strftime("%H:%M"),
                dia.hora_fin.strftime("%H:%M"),
                dia.duracion_turno_min
            ))
        

    def getAll(self):
        query = """
            SELECT a.id, m.id, m.nombre, m.apellido, m.email
            FROM agendas_medico a
            JOIN medicos m ON a.medico_id = m.id
        """
        cursor = self.db.execute(query)
        filas = cursor.fetchall()

        agendas = []
        from datetime import datetime

        for f in filas:
            agenda_id = f[0]
            medico = Medico(f[1], f[2], f[3], f[4], None)

            # Obtener días de esa agenda
            query_dias = """
                SELECT dia_semana, hora_inicio, hora_fin, duracion_turno_min
                FROM agenda_dias_trabajo
                WHERE agenda_id = ?
            """
            cursor_dias = self.db.execute(query_dias, (agenda_id,))
            dias_filtrados = cursor_dias.fetchall()

            dias = [
                DiaLaboral(
                    dia_semana=d[0],
                    hora_inicio=datetime.strptime(d[1], "%H:%M").time(),
                    hora_fin=datetime.strptime(d[2], "%H:%M").time(),
                    duracion_turno_min=d[3]
                )
                for d in dias_filtrados
            ]

            agendas.append(Agenda(agenda_id, medico, dias))

        return agendas
    

    def getById(self, id):
        # Obtener la agenda
        query_agenda = """
            SELECT a.id, m.id, m.nombre, m.apellido, m.email
            FROM agendas_medico a
            JOIN medicos m ON a.medico_id = m.id
            WHERE a.id = ?
        """
        cursor = self.db.execute(query_agenda, (id,))
        fila = cursor.fetchone()

        if not fila:
            return None

        medico = Medico(fila[1], fila[2], fila[3], fila[4], None)

        # Obtener días laborales
        query_dias = """
            SELECT dia_semana, hora_inicio, hora_fin, duracion_turno_min
            FROM agenda_dias_trabajo
            WHERE agenda_id = ?
        """
        cursor_dias = self.db.execute(query_dias, (id,))
        filas_dias = cursor_dias.fetchall()

        dias = []
        from datetime import datetime
        for d in filas_dias:
            dias.append(
                DiaLaboral(
                    dia_semana=d[0],
                    hora_inicio=datetime.strptime(d[1], "%H:%M").time(),
                    hora_fin=datetime.strptime(d[2], "%H:%M").time(),
                    duracion_turno_min=d[3]
                )
            )

        return Agenda(id=id, medico=medico, dias_trabajo=dias)
    

    def deleteById(self, id):
        return super().deleteById(id)
    

    def update(self, entity):
        return super().update(entity)
    
