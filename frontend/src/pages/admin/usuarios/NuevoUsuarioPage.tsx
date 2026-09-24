import {
  useEffect,
  useState,
  type FormEvent,
} from "react";

import {
  obtenerRoles,
  crearUsuario,
} from "../../../services/adminService";

type Rol = {
  id: number;
  nombre: string;
  descripcion: string;
};

function NuevoUsuarioPage() {
  const [roles, setRoles] = useState<Rol[]>([]);
  const [mensaje, setMensaje] = useState("");

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

    const respuesta = await crearUsuario({
        dni: String(datos.get("dni")),
        nombres: String(datos.get("nombres")),
        apellidos: String(datos.get("apellidos")),
        email: String(datos.get("email")),
        password: String(datos.get("password")),
        role_id: Number(datos.get("rol")),
    });

    setMensaje(respuesta.mensaje);
  }

  return (
    <main>
      <h1>Nuevo usuario</h1>

      <form onSubmit={manejarSubmit}>
        <div>
          <label htmlFor="dni">DNI</label>
          <input
            id="dni"
            name="dni"
            type="text"
          />
        </div>

        <div>
          <label htmlFor="nombres">Nombres</label>
          <input
            id="nombres"
            name="nombres"
            type="text"
          />
        </div>

        <div>
          <label htmlFor="apellidos">Apellidos</label>
          <input
            id="apellidos"
            name="apellidos"
            type="text"
          />
        </div>

        <div>
          <label htmlFor="email">
            Correo electrónico
          </label>
          <input
            id="email"
            name="email"
            type="email"
          />
        </div>

        <div>
          <label htmlFor="password">
            Contraseña
          </label>
          <input
            id="password"
            name="password"
            type="password"
          />
        </div>

        <div>
          <label htmlFor="rol">Rol</label>

          <select
            id="rol"
            name="rol"
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

        <button type="submit">
          Crear usuario
        </button>
      </form>
      {mensaje && (
        <p>{mensaje}</p>
        )}
    </main>
  );
}

export default NuevoUsuarioPage;