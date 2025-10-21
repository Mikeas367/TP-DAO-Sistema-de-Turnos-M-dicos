export interface MedicoBase {
    nombre: string 
    apellido: string
    email: string
    especialidad_id: number
}
    
export interface Medico extends MedicoBase {
    id: number
}