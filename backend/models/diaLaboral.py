from datetime import time

class DiaLaboral:
    def __init__(self, dia_semana: int, hora_inicio: time, hora_fin: time, duracion_turno_min: int = 30):
        self.dia_semana = dia_semana        # 0 = lunes ... 6 = domingo
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.duracion_turno_min = duracion_turno_min