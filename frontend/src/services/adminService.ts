import api from "../api/axiosConfig";

export async function obtenerUsuarios() {
  const respuesta = await api.get("/admin/users");

  return respuesta.data.usuarios;
}