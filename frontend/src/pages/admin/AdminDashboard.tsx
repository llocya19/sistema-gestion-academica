import { Link } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

function AdminDashboard() {
  const { usuario, cerrarSesion } = useAuth();

  return (
    <div>
      <header>
        <h1>Panel de administración</h1>

        <div>
          <span>
            {usuario?.persona.nombres} {usuario?.persona.apellidos}
          </span>

          <button type="button" onClick={cerrarSesion}>
            Cerrar sesión
          </button>
        </div>
      </header>

      <aside>
        <h2>G.W.C.</h2>

        <nav>
          <Link to="/admin">Inicio</Link>

          <Link to="/admin/usuarios">
            Gestión de usuarios
          </Link>
        </nav>
      </aside>

      <main>
        <h2>
          Bienvenido, {usuario?.persona.nombres}
        </h2>

        <p>
          Administra las cuentas y accesos de los usuarios
          del sistema.
        </p>

        <section>
          <h2>Gestión de usuarios</h2>

          <p>
            Consulta y administra las cuentas registradas
            en el sistema.
          </p>

          <Link to="/admin/usuarios">
            Ir a Gestión de usuarios
          </Link>
        </section>
      </main>
    </div>
  );
}

export default AdminDashboard;