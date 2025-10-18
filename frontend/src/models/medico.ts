export interface MedicoBase {
    nombre: string 
    apellido: string
    email: string
}
    
export interface Medico extends MedicoBase {
    id: number
}