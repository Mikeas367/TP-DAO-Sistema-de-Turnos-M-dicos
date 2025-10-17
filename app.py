from fastapi import FastAPI

from routes.medicoRouter import router as medicoRouter


app = FastAPI(title="Sistema de Turnos Médicos")

app.include_router(medicoRouter, prefix="/api", tags=["medicos"])

@app.get("/")
def root():
    return {"message": "API Sistema de Turnos Médicos funcionando 🚑"}