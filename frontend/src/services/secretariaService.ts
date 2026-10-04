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

export interface ActualizarEstudiante {
  nombres: string;
  apellidos: string;
  student_code: string;
}

export async function actualizarEstudiante(
  id: number,
  datos: ActualizarEstudiante
) {
  const respuesta = await api.put(
    `/secretary/students/${id}`,
    datos
  );

  return respuesta.data;
}

export async function cambiarEstadoEstudiante(
  id: number,
  estado: boolean
) {
  const respuesta = await api.patch(
    `/secretary/students/${id}/status`,
    {
      status: estado,
    }
  );

  return respuesta.data;
}