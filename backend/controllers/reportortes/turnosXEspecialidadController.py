import os
from interfaces.interfacePersistencia import IRepository
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker


class ReporteTurnosXEspecialidad:
    def __init__(self, turno_repo: IRepository, especialidad_repo: IRepository):
        self.turno_repo = turno_repo
        self.especialidad_repo = especialidad_repo

    def conteo_por_especialidades(self, especialidades, turnos):
        contador = {}
        for esp in especialidades:
            contador[esp.nombre] = 0
        
        for turno in turnos:
            esp_nombre =  turno.medico.especialidad.nombre 
            contador[esp_nombre] += 1 

        return contador



    def generarReporte(self):
        especialidades = self.especialidad_repo.getAll()
        turnos = self.turno_repo.getAll()
        contador = self.conteo_por_especialidades(especialidades, turnos)
        self.generar_grafico_barras(contador)

    
    def generar_grafico_barras(self, data_conteo: dict, filename: str = "Reports/reporte_turnos_especialidad.pdf"):
        
        if not data_conteo:
            print("No hay datos para generar el gráfico.")
            return

        # 1. Preparar los datos
        especialidades = list(data_conteo.keys()) 
        cantidades = list(data_conteo.values()) 

        # 2. Crear la figura y los ejes
        fig, ax = plt.subplots(figsize=(10, 6))

        # 3. Generar el gráfico de barras
        bars = ax.bar(especialidades, cantidades, color='#4CAF50')

        # 4. Personalizar el gráfico
        ax.set_xlabel('Especialidad', fontsize=12)
        ax.set_ylabel('Número de Turnos', fontsize=12)
        ax.set_title('Conteo de Turnos por Especialidad', fontsize=16, fontweight='bold')
        
        
        ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
        
    
        ax.set_ylim(bottom=0)
        
        plt.xticks(rotation=45, ha='right')
        
        
        for bar in bars:
            yval = bar.get_height()
            
            ax.text(bar.get_x() + bar.get_width()/2, yval + 0.1, int(yval), ha='center', va='bottom', fontsize=10)

        plt.tight_layout() 
        
        # 5. Guardar el gráfico como PDF
        plt.savefig(filename, bbox_inches='tight')
        plt.close(fig) 
        print(f"El gráfico se ha guardado exitosamente como '{filename}'")