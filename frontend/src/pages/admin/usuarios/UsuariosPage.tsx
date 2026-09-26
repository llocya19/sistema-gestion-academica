import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import {
  obtenerUsuarios,
  cambiarEstadoUsuario,
} from "../../../services/adminService";

type Usuario = {
  id: number;
  email: string;
  estado: boolean;
  rol: string;
  persona: {
    dni: string;
    nombres: string;
    apellidos: string;
  };
};

function UsuariosPage() {
  const [usuarios, setUsuarios] = useState<Usuario[]>([]);

  useEffect(() => {
    async function cargarUsuarios() {
      const datos = await obtenerUsuarios();
      setUsuarios(datos);
    }

    cargarUsuarios();
  }, []);

  async function manejarCambioEstado(
    usuarioId: number,
    estadoActual: boolean
  ) {
    await cambiarEstadoUsuario(
      usuarioId,
      !estadoActual
    );

    setUsuarios((usuariosActuales) =>
      usuariosActuales.map((usuario) =>
        usuario.id === usuarioId
          ? {
              ...usuario,
              estado: !estadoActual,
            }
          : usuario
      )
    );
  }

  return (
    <main>
      <h1>Gestión de usuarios</h1>
      
      <Link to="/admin/usuarios/nuevo">
        Nuevo usuario
      </Link>

      <table>
        <thead>
          <tr>
            <th>Usuario</th>
            <th>Correo</th>
            <th>Rol</th>
            <th>Estado</th>
            <th>Acciones</th>
          </tr>
        </thead>

        <tbody>
          {usuarios.map((usuario) => (
            <tr key={usuario.id}>
              <td>
                {usuario.persona.nombres} {usuario.persona.apellidos}
              </td>

              <td>{usuario.email}</td>

              <td>{usuario.rol}</td>

              <td>
                {usuario.estado ? "Activo" : "Inactivo"}
              </td>

              <td>
                <button
                  type="button"
                  onClick={() =>
                    manejarCambioEstado(
                      usuario.id,
                      usuario.estado
                    )
                  }
                >
                  {usuario.estado ? "Desactivar" : "Activar"}
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </main>
  );
}

export default UsuariosPage;