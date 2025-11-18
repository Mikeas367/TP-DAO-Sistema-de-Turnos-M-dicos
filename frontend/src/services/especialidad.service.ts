import axios from "axios";
import type { Especialidad, EspecialidadBase } from "../models/especialidad";
const API_URL = "http://127.0.0.1:8000/api/especialidad";


export const listarEspecialidad = async () => {
  try {
    const response = await axios.get(API_URL)
    return response.data
  } catch (error) {
    throw error;
  }
}

export const crearEspecialidad = async (data: EspecialidadBase) => {
  try {
    const response = await axios.post(API_URL, data);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const eliminarEspecialidad = async (id: number) => {
  try {
    const response = await axios.delete(`${API_URL}/${id}`);
    return response;
  } catch (error) {
    throw error;
  }
};

export const obtenerEspecialidadPorId = async (id: number) => {
  try {
    const response = await axios.get<Especialidad>(`${API_URL}/${id}`);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const actualizarEspecialidad = async (id: number, data: Partial<EspecialidadBase>) => {
  try {
    const response = await axios.put(`${API_URL}/${id}`, data);
    return response.data;
  } catch (error) {
    throw error;
  }
};