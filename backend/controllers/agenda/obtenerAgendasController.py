from interfaces.interfacePersistencia import IRepository


class ObtenerAgendaController:
    def __init__(self, agenda_repo: IRepository):
        self.agenda_repo = agenda_repo

    
    def obtener_agendas(self):
        return self.agenda_repo.getAll()
    
    def obtener_agenda_por_id(self, id: int):
        return self.agenda_repo.getById(id)