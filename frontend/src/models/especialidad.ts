export interface EspecialidadBase {
    nombre: string 
    descripcion: string
}
    
export interface Especialidad extends EspecialidadBase {
    id: number
}