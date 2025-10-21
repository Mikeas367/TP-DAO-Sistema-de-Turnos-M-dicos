import axios from "axios";
import type { MedicoBase, Medico } from "../models";

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
    throw error;
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

export const obtenerMedicoPorId = async (id: number) => {
  try {
    const response = await axios.get<Medico>(`${API_URL}/${id}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const actualizarMedico = async (id: number, medicoData: Partial<MedicoBase>) => {
  try {
    const response = await axios.put(`${API_URL}/${id}`, medicoData);
    return response.data;
  } catch (error) {
    throw error;
  }
};