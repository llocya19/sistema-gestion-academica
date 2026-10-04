import type { ReactNode } from "react";
import { Link } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

import "./SecretariaLayout.css";

interface SecretariaLayoutProps {
  children: ReactNode;
}

function SecretariaLayout({
  children
}: SecretariaLayoutProps) {

  const { usuario, cerrarSesion } = useAuth();

  return (
    <div className="secretaria-layout">

      <aside className="secretaria-sidebar">

        <div className="secretaria-brand">
          <h2>G.W.C.</h2>
          <p>Gestión Académica</p>
        </div>

        <nav className="secretaria-nav">

          <Link to="/secretaria">
            Inicio
          </Link>

          <Link to="/secretaria/estudiantes">
            Gestión de estudiantes
          </Link>

        </nav>

      </aside>


      <header className="secretaria-header">

        <div>
          <strong>Panel de Secretaría</strong>
        </div>

        <div className="secretaria-header-user">

          <div className="secretaria-user-info">

            <span className="secretaria-user-name">
              {usuario?.persona.nombres}{" "}
              {usuario?.persona.apellidos}
            </span>

            <span className="secretaria-user-role">
              Secretaría
            </span>

          </div>

          <button
            type="button"
            className="secretaria-logout"
            onClick={cerrarSesion}
          >
            Cerrar sesión
          </button>

        </div>

      </header>


      <main className="secretaria-content">
        {children}
      </main>

    </div>
  );
}

export default SecretariaLayout;