import api from "../api/axiosConfig";

export async function obtenerUsuarios() {
  const respuesta = await api.get("/admin/users");

  return respuesta.data.usuarios;
}

export async function crearUsuario(nuevoUsuario: {
  dni: string;
  nombres: string;
  apellidos: string;
  email: string;
  password: string;
  role_id: number;
}) {
  const respuesta = await api.post(
    "/admin/users",
    nuevoUsuario
  );

  
  return respuesta.data;
}

export async function obtenerRoles() {
  const respuesta = await api.get("/admin/roles");
  return respuesta.data.roles;
}