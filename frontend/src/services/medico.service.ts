import axios from "axios";
import type { MedicoBase } from "../models";

const API_URL = "http://127.0.0.1:8000/api/medicos";

export const crearMedico = async (medicoData: MedicoBase) => {
  try {
    const response = await axios.post(API_URL, medicoData);
    return response.data;
  } catch (error) {

    throw error;
  }
};

export const listarMedicos = async () => {
  try {
    const response = await axios.get(API_URL)
    return response.data
  } catch (error) {
    throw { mensaje: "Error desconocido" };
  }
}

export const eliminarMedico = async(id: number) => {
  try {
    const response = await axios.delete(API_URL +`/${id}`)
    return response
  } catch (error) {
    throw error;
    
  }
}