import {useForm} from 'react-hook-form'
import { useState } from "react";
import { crearMedico } from '../../services'
import type { MedicoBase } from '../../models';

export const MedicoForm = ()=> {
    
    const {register, handleSubmit, watch, reset} = useForm<MedicoBase>()

    const [mensaje, setMensaje] = useState(""); 
  const [error, setError] = useState("");

    const onSumbit = async (data: MedicoBase)=> {
        try {
            setMensaje("");
            setError("");
            const res = await crearMedico(data);
            setMensaje(res.mensaje); 
            reset(); 
        } catch (err:any) {
            console.log(err.response)
            setError("Error al crear el médico");
        }
    }

    return(
        <>
            <h1> Registro de un nuevo Medico</h1>
            <form onSubmit={handleSubmit(onSumbit)}>
                {/* Nombre */}
                <label htmlFor="nombre">Nombre</label>
                <input type="text" className="form-control"
                    {...register("nombre")}/>

                {/* apellido */}
                <label htmlFor="apellido">Apellido</label>
                <input type="text" className="form-control" 
                    {...register("apellido")}
                />

                {/* email */}
                <label htmlFor="email">Email</label>
                <input type="text" className="form-control"
                    {...register("email")}/>
            
            <button className="btn btn-primary">Crear Medico</button>

            {mensaje && <p style={{ color: "green", marginTop: "10px" }}>{mensaje}</p>}
            {error && <p style={{ color: "red", marginTop: "10px" }}>{error}</p>}

                <pre>
                    {JSON.stringify(watch(), null, 2)}
                </pre>
            </form>


        </>
    )
}