import axios from "axios";
import type { Medico } from "../components/models";

const API_URL = "http://127.0.0.1:8000/api/medicos";

export const crearMedico = async (medicoData: Medico) => {
  try {
    const response = await axios.post(API_URL, medicoData);
    return response.data;
  } catch (error) {
    // Puedes manejar errores de forma más detallada si quieres
    throw { mensaje: "Error desconocido" };
  }
};