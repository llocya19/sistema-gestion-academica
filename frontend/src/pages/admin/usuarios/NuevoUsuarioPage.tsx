import {
  useEffect,
  useState,
  type FormEvent,
} from "react";
import { Link } from "react-router-dom";

import {
  obtenerRoles,
  crearUsuario,
} from "../../../services/adminService";

import { useAuth } from "../../../context/AuthContext";

import "../AdminLayout.css";
import "./NuevoUsuarioPage.css";

type Rol = {
  id: number;
  nombre: string;
  descripcion: string;
};

function NuevoUsuarioPage() {
  const [roles, setRoles] = useState<Rol[]>([]);
  const [mensaje, setMensaje] = useState("");
  const { usuario, cerrarSesion } = useAuth();

  useEffect(() => {
    async function cargarRoles() {
      const datos = await obtenerRoles();
      setRoles(datos);
    }

    cargarRoles();
  }, []);

  async function manejarSubmit(
    evento: FormEvent<HTMLFormElement>
  ) {
    evento.preventDefault();

    const formulario = evento.currentTarget;
    const datos = new FormData(formulario);

    try {
      const respuesta = await crearUsuario({
        dni: String(datos.get("dni")),
        nombres: String(datos.get("nombres")),
        apellidos: String(datos.get("apellidos")),
        email: String(datos.get("email")),
        password: String(datos.get("password")),
        role_id: Number(datos.get("rol")),
      });

      setMensaje(respuesta.mensaje);
    } catch (error: unknown) {
      const errorApi = error as {
        response?: {
          data?: {
            mensaje?: string;
          };
        };
      };

      setMensaje(
        errorApi.response?.data?.mensaje ??
          "No se pudo crear el usuario"
      );
    }
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
        <div className="nuevo-usuario-header">
          <div className="admin-page-title">
            <h1>Nuevo usuario</h1>
            <p>
              Registra una nueva cuenta de acceso al
              sistema académico.
            </p>
          </div>

          <Link
            to="/admin/usuarios"
            className="nuevo-usuario-volver"
          >
            ← Volver a usuarios
          </Link>
        </div>

        <section className="nuevo-usuario-card">
          <div className="nuevo-usuario-card-header">
            <h2>Información de la cuenta</h2>
            <p>
              Completa los datos personales y de acceso
              del nuevo usuario.
            </p>
          </div>

          <form
            onSubmit={manejarSubmit}
            className="nuevo-usuario-form"
          >
            <div className="nuevo-usuario-grid">
              <div className="form-grupo">
                <label htmlFor="dni">
                  DNI
                </label>

                  <input
                    id="dni"
                    name="dni"
                    type="text"
                    placeholder="Ingrese el DNI"
                    required
                    maxLength={8}
                    inputMode="numeric"
                    pattern="[0-9]{8}"
                    title="El DNI debe contener exactamente 8 dígitos"
                  />
              </div>

              <div className="form-grupo">
                <label htmlFor="rol">
                  Rol
                </label>

                <select
                  id="rol"
                  name="rol"
                  required
                >
                  <option value="">
                    Seleccione un rol
                  </option>

                  {roles.map((rol) => (
                    <option
                      key={rol.id}
                      value={rol.id}
                    >
                      {rol.nombre}
                    </option>
                  ))}
                </select>
              </div>

              <div className="form-grupo">
                <label htmlFor="nombres">
                  Nombres
                </label>

                <input
                  id="nombres"
                  name="nombres"
                  type="text"
                  placeholder="Ingrese los nombres"
                  required
                />
              </div>

              <div className="form-grupo">
                <label htmlFor="apellidos">
                  Apellidos
                </label>

                <input
                  id="apellidos"
                  name="apellidos"
                  type="text"
                  placeholder="Ingrese los apellidos"
                  required
                />
              </div>

              <div className="form-grupo">
                <label htmlFor="email">
                  Correo electrónico
                </label>

                <input
                  id="email"
                  name="email"
                  type="email"
                  placeholder="ejemplo@correo.com"
                  required
                />
              </div>

              <div className="form-grupo">
                <label htmlFor="password">
                  Contraseña
                </label>

                <input
                  id="password"
                  name="password"
                  type="password"
                  placeholder="Ingrese una contraseña"
                  required
                />
              </div>
            </div>

            {mensaje && (
              <div className="form-mensaje">
                {mensaje}
              </div>
            )}

            <div className="nuevo-usuario-acciones">
              <Link
                to="/admin/usuarios"
                className="boton-cancelar"
              >
                Cancelar
              </Link>

              <button
                type="submit"
                className="boton-crear"
              >
                Crear usuario
              </button>
            </div>
          </form>
        </section>
      </main>
    </div>
  );
}

export default NuevoUsuarioPage;