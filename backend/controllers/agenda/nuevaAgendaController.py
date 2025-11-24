from datetime import datetime
from interfaces.interfacePersistencia import IRepository
from models.agenda import Agenda
from models.diaLaboral import DiaLaboral
from schemas.agenda import AgendaCreate


class NuevaAgendaController:
    def __init__(self, agenda_repo: IRepository, medico_repo: IRepository):
        self.agenda_repo = agenda_repo 
        self.medico_repo = medico_repo


    def nuevaAgenda(self, agenda: AgendaCreate):
        medico = self.medico_repo.getById(agenda.medico_id)
        dias_agenda = []
        for dia in agenda.dias_trabajo:
            nuevo_dia = DiaLaboral(dia_semana=dia.dia_semana,
            
            hora_inicio= datetime.strptime(dia.hora_inicio, "%H:%M").time(),
            hora_fin =datetime.strptime(dia.hora_fin, "%H:%M").time(),
            duracion_turno_min= dia.duracion_turno_min)
            
            dias_agenda.append(nuevo_dia)

        nueva_agenda = Agenda(None, medico, dias_agenda)
        self.agenda_repo.save(nueva_agenda)