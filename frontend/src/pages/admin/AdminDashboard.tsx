import { Link } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import "./AdminLayout.css";

function AdminDashboard() {
  const { usuario, cerrarSesion } = useAuth();

  return (
    <div className="admin-layout">
      {/* Menú lateral */}
      <aside className="admin-sidebar">
        <div className="admin-brand">
          <h2>G.W.C.</h2>
          <p>Gestión Académica</p>
        </div>

        <nav className="admin-nav">
          <Link to="/admin">
            Inicio
          </Link>

          <Link to="/admin/usuarios">
            Gestión de usuarios
          </Link>
        </nav>
      </aside>

      {/* Barra superior */}
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

      {/* Contenido principal */}
      <main className="admin-content">
        <div className="admin-page-title">
          <h1>
            Bienvenido, {usuario?.persona.nombres}
          </h1>

          <p>
            Administra las cuentas y accesos de los
            usuarios del sistema académico.
          </p>
        </div>

        <section className="admin-card">
          <h2>Gestión de usuarios</h2>

          <p>
            Consulta, crea y administra las cuentas
            registradas en el sistema.
          </p>

          <Link
            to="/admin/usuarios"
            className="admin-card-link"
          >
            Ir a Gestión de usuarios
          </Link>
        </section>
      </main>
    </div>
  );
}

export default AdminDashboard;