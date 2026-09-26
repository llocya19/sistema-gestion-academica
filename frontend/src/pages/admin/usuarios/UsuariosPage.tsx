import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import {
  obtenerUsuarios,
  cambiarEstadoUsuario,
} from "../../../services/adminService";
import { useAuth } from "../../../context/AuthContext";
import "../AdminLayout.css";
import "./UsuariosPage.css";

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
  const { usuario, cerrarSesion } = useAuth();

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
      usuariosActuales.map((usuarioActual) =>
        usuarioActual.id === usuarioId
          ? {
              ...usuarioActual,
              estado: !estadoActual,
            }
          : usuarioActual
      )
    );
  }

  return (
    <div className="admin-layout">
      <aside className="admin-sidebar">
        <div className="admin-brand">
          <h2>G.W.C.</h2>
          <p>Gestión Académica</p>
        </div>

        <nav className="admin-nav">
          <Link to="/admin">
            Inicio
          </Link>

          <Link
            to="/admin/usuarios"
            className="admin-nav-active"
          >
            Gestión de usuarios
          </Link>
        </nav>
      </aside>

      <header className="admin-header">
        <div>
          <strong>Panel de Administración</strong>
        </div>

        <div className="admin-header-user">
          <div className="admin-user-info">
            <span className="admin-user-name">
              {usuario?.persona.nombres}{" "}
              {usuario?.persona.apellidos}
            </span>

            <span className="admin-user-role">
              Administrador
            </span>
          </div>

          <button
            type="button"
            className="admin-logout"
            onClick={cerrarSesion}
          >
            Cerrar sesión
          </button>
        </div>
      </header>

      <main className="admin-content">
        <div className="usuarios-header">
          <div className="admin-page-title">
            <h1>Gestión de usuarios</h1>
            <p>
              Administra las cuentas y accesos de los
              usuarios del sistema.
            </p>
          </div>

          <Link
            to="/admin/usuarios/nuevo"
            className="usuarios-nuevo"
          >
            + Nuevo usuario
          </Link>
        </div>

        <section className="usuarios-card">
          <div className="usuarios-card-header">
            <div>
              <h2>Cuentas de usuario</h2>
              <p>
                Usuarios registrados en el sistema académico.
              </p>
            </div>
          </div>

          <div className="usuarios-tabla-contenedor">
            <table className="usuarios-tabla">
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
                {usuarios.map((usuarioCuenta) => (
                  <tr key={usuarioCuenta.id}>
                    <td>
                      <div className="usuario-datos">
                        <div className="usuario-avatar">
                          {usuarioCuenta.persona.nombres
                            .charAt(0)
                            .toUpperCase()}
                        </div>

                        <div>
                          <strong>
                            {usuarioCuenta.persona.nombres}{" "}
                            {usuarioCuenta.persona.apellidos}
                          </strong>

                          <span>
                            DNI: {usuarioCuenta.persona.dni}
                          </span>
                        </div>
                      </div>
                    </td>

                    <td>{usuarioCuenta.email}</td>

                    <td>
                      <span className="usuario-rol">
                        {usuarioCuenta.rol}
                      </span>
                    </td>

                    <td>
                      <span
                        className={
                          usuarioCuenta.estado
                            ? "estado estado-activo"
                            : "estado estado-inactivo"
                        }
                      >
                        <span className="estado-punto" />
                        {usuarioCuenta.estado
                          ? "Activo"
                          : "Inactivo"}
                      </span>
                    </td>

                    <td>
                      <button
                        type="button"
                        className={
                          usuarioCuenta.estado
                            ? "usuario-accion usuario-desactivar"
                            : "usuario-accion usuario-activar"
                        }
                        onClick={() =>
                          manejarCambioEstado(
                            usuarioCuenta.id,
                            usuarioCuenta.estado
                          )
                        }
                      >
                        {usuarioCuenta.estado
                          ? "Desactivar"
                          : "Activar"}
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      </main>
    </div>
  );
}

export default UsuariosPage;