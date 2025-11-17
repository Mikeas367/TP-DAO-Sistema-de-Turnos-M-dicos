import os
from interfaces.interfacePersistencia import IRepository
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

class ReporteAsistencia:
    def __init__(self, turno_repo: IRepository):
        self.turno_repo = turno_repo
    
    def buscar_turnos(self):
        turnos = self.turno_repo.getAll()

        turnosAsistidos = []
        turnosNoAsistidos = []

        for turno in turnos:
            if turno.es_asistido():
                turnosAsistidos.append(turno)
            elif turno.es_no_asistido():
                turnosNoAsistidos.append(turno)

        return turnosAsistidos, turnosNoAsistidos


    def generarReporteAsistencia(self, ruta_pdf="Reports/reporte_asistencias.pdf"):
        turnosAsistidos, turnosNoAsistidos = self.buscar_turnos()


        labels = ["Asistencias", "Inasistencias"]
        sizes = [len(turnosAsistidos), len(turnosNoAsistidos)]

        plt.figure(figsize=(4, 4))
        plt.pie(
            sizes,
            labels=labels,
            autopct='%1.1f%%',
            startangle=90
        )
        plt.title("Asistencias vs Inasistencias")

        # Guardar gráfico temporalmente
        grafico_path = "grafico_torta.png"
        plt.savefig(grafico_path, dpi=120, bbox_inches="tight")
        plt.close()


        doc = SimpleDocTemplate(ruta_pdf, pagesize=A4)
        styles = getSampleStyleSheet()
        story = []

        # Título
        story.append(Paragraph("Reporte de Asistencias", styles["Title"]))
        story.append(Spacer(1, 20))

        # Tabla resumen
        data_resumen = [
            ["Tipo", "Cantidad"],
            ["Asistencias", len(turnosAsistidos)],
            ["Inasistencias", len(turnosNoAsistidos)],
        ]

        tabla_resumen = Table(data_resumen)
        tabla_resumen.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.grey),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("GRID", (0,0), (-1,-1), 1, colors.black),
        ]))

        story.append(tabla_resumen)
        story.append(Spacer(1, 20))

        # Insertar gráfico
        story.append(Paragraph("Gráfico de Asistencias:", styles["Heading2"]))
        story.append(Spacer(1, 10))

        story.append(Image(grafico_path, width=300, height=300))
        story.append(Spacer(1, 30))

        # Finalizar PDF
        doc.build(story)

        # Borrar imagen temporal
        if os.path.exists(grafico_path):
            os.remove(grafico_path)

        return ruta_pdf
