import api from "../api/axiosConfig";

export interface Estudiante {
  id: number;
  codigo: string;
  estado: boolean;

  persona: {
    dni: string;
    nombres: string;
    apellidos: string;
  };
}
export async function obtenerEstudiantes(): Promise<Estudiante[]> {
  const respuesta = await api.get("/secretary/students");

  return respuesta.data.estudiantes;
}

export interface NuevoEstudiante {
  dni: string;
  nombres: string;
  apellidos: string;
  student_code: string;
  telefono?: string;
  direccion?: string;
}

export async function crearEstudiante(
  nuevoEstudiante: NuevoEstudiante
) {
  const respuesta = await api.post(
    "/secretary/students",
    nuevoEstudiante
  );

  return respuesta.data;
}