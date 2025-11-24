from interfaces.interfacePersistencia import IRepository
from fastapi import HTTPException, status
from models.turno import Turno
from schemas.turnoSchema import TurnoCreate
from datetime import datetime, timedelta



class RegistrarNuevoTurnoController:
    def __init__(self, turno_repo: IRepository, estado_repo: IRepository, medico_repo: IRepository):
        self.turno_repo = turno_repo
        self.estado_repo = estado_repo
        self.medico_repo = medico_repo
        self.fecha_hora_actual = None

    
    def registrar_nuevo_turno(self, turno: TurnoCreate):
        fecha_turno_str = turno.fecha
        fecha_turno_a_validar = datetime.strptime(fecha_turno_str, "%Y-%m-%dT%H:%M")

        turnos = self.buscarTurnos()
        self.obtener_fecha_hora_actual()
        self.validar_fecha(fecha_turno_a_validar)
        self.validar_superposicion(turnos, fecha_turno_a_validar)
        
        estado_libre = self.buscar_estado_libre()
        medico = self.buscarMedico(turno.medico_id)
        
        nuevo_turno = Turno(None, None, medico, estado_libre, fecha_turno_a_validar)
        self.turno_repo.save(nuevo_turno)


    def obtener_fecha_hora_actual(self):
        fechaHoraActual = datetime.now()
        self.fecha_hora_actual = fechaHoraActual

    def validar_fecha(self, fecha_turno_a_validar: str):
        if fecha_turno_a_validar < self.fecha_hora_actual:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No se crear un turno para una fecha pasada"
            )
    
    def validar_superposicion(self, turnos, fecha_turno_a_validar: str):
        margen = timedelta(minutes=5)
        for turno in turnos:
            fecha_turno_existente = datetime.strptime(turno.fecha, "%Y-%m-%d %H:%M")
            if abs(fecha_turno_existente - fecha_turno_a_validar) < margen:
                raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Existe una superpocicion con otro turno"
                )
        

    def buscarMedico(self, medico_id: int):
        medico = self.medico_repo.getById(medico_id)
        return medico

    def buscarTurnos(self):
        # deveria ir una clausula try para evitar errores
        turnos = self.turno_repo.getAll()
        return turnos
    
    
            
        

    def buscar_estado_libre(self):
        estados = self.estado_repo.getAll()
        for e in estados:
            if e.es_libre():
                return e
    