from interfaces.interfacePersistencia import IRepository 

class TurnoMedicoController:
    def __init__(self, repo_medico: IRepository, repoturnos: IRepository):
        self.repo_medico = repo_medico
        self.repo_turnos = repoturnos
    
    def buscar_turnos_medico(self, medico_id: int):
        turnos = self.repo_turnos.getAll()
        turnos_medico = []
        for t in turnos:
            if t.sos_de_medico(medico_id) and t.esta_ocupado():
                #print(t)
                turnos_medico.append(t)

        for t in turnos_medico:
            print(t)
        return turnos_medico


        


        