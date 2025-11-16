export interface PacienteBase {
    nombre: string 
    apellido: string
    email: string
    especialidad_id: number
}
    
export interface Paciente extends PacienteBase{
    id: number
    
}