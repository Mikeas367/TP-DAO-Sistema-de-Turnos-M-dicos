from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 
from routes.medicoRouter import router as medicoRouter
from routes.especialidadRouter import router as especialidadRouter
from routes.turnoRouter import router as turnoRouter
from routes.pacientesRouter import router as pacienteRouter
from routes.reportesRouter import router as reportesRouter
from routes.agendaRouter import router as agendaRouter


app = FastAPI(title="Sistema de Turnos Médicos")

app.include_router(medicoRouter, prefix="/api", tags=["medicos"])
app.include_router(especialidadRouter, prefix="/api")
app.include_router(turnoRouter, prefix="/api")
app.include_router(pacienteRouter, prefix="/api")
app.include_router(reportesRouter, prefix="/api")
app.include_router(agendaRouter, prefix="/api")

origins = [
    "http://localhost:5173",  # URL de tu front-end
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Permitir solo estos orígenes
    allow_credentials=True,
    allow_methods=["*"],         # Permitir GET, POST, PUT, DELETE, OPTIONS...
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "API Sistema de Turnos Médicos funcionando 🚑"}