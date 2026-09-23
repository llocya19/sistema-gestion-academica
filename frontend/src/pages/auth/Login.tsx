import { useState } from "react";
import { useNavigate } from "react-router-dom";

import { login } from "../../services/authService";
import { useAuth } from "../../context/AuthContext";
import logoGwc from "../../assets/logo-gwc.png";

import "./Login.css";


function Login(){

const { iniciarSesion } = useAuth();
const navigate = useNavigate();

const [email,setEmail]=useState("");
const [password,setPassword]=useState("");

const [mostrarPassword, setMostrarPassword] = useState(false);
const [error, setError] = useState("");
const [cargando, setCargando] = useState(false);




const handleSubmit = async (e: React.FormEvent) => {
  e.preventDefault();

  setError("");
  setCargando(true);

  try {

    const response = await login({
      email,
      password
    });

    iniciarSesion(
      response.access_token,
      response.usuario
    );

    navigate("/home");

  } catch (error) {

    console.error(error);

    setError(
      "Correo electrónico o contraseña incorrectos."
    );

  } finally {

    setCargando(false);

  }
};



return (
  <main className="login-page">

    <div className="login-layout">

      {/* PANEL IZQUIERDO */}
      <section className="login-brand-panel">

        <div className="brand-content">

          <div className="brand-logo-container">
            <img
              src={logoGwc}
              alt="Logo de la I.E.P. George Washington Carver"
              className="brand-logo"
            />
          </div>

          <div className="brand-school">
            <span>I.E.P.</span>
            <strong>George Washington Carver</strong>
            <small>Chincha</small>
          </div>

          <div className="brand-title">
            <h1>
              Sistema de
              <span> Gestión Académica</span>
            </h1>

            <p>
              Información académica organizada,
              accesible y eficiente.
            </p>
          </div>

          <div className="brand-divider"></div>

          <div className="brand-features">

            <div className="brand-feature">
              <div className="feature-icon">✓</div>

              <div>
                <strong>Procesos organizados</strong>
                <p>
                  Información académica centralizada
                  en un solo lugar.
                </p>
              </div>
            </div>

            <div className="brand-feature">
              <div className="feature-icon">✓</div>

              <div>
                <strong>Acceso rápido</strong>
                <p>
                  Consulta la información necesaria
                  de manera sencilla.
                </p>
              </div>
            </div>

            <div className="brand-feature">
              <div className="feature-icon">✓</div>

              <div>
                <strong>Gestión académica</strong>
                <p>
                  Herramientas para apoyar las
                  actividades del personal educativo.
                </p>
              </div>
            </div>

          </div>

        </div>

        <div className="brand-decoration decoration-one"></div>
        <div className="brand-decoration decoration-two"></div>

      </section>


      {/* PANEL DERECHO */}
      <section className="login-form-section">

        <div className="login-card">

          <header className="login-header">

            <span className="login-subtitle">
              SISTEMA ACADÉMICO
            </span>

            <h2>¡Bienvenido!</h2>

            <p>
              Ingresa tus credenciales para acceder
              al sistema.
            </p>

          </header>


          <form onSubmit={handleSubmit}>

            {/* CORREO */}
            <div className="form-group">

              <label htmlFor="email">
                Correo electrónico
              </label>

              <div className="input-container">

                <span className="input-icon">
                  ✉
                </span>

                <input
                  id="email"
                  className="login-input"
                  type="email"
                  placeholder="Ingresa tu correo electrónico"
                  value={email}
                  onChange={(e) =>
                    setEmail(e.target.value)
                  }
                  autoComplete="email"
                  required
                />

              </div>

            </div>


            {/* CONTRASEÑA */}
            <div className="form-group">

              <label htmlFor="password">
                Contraseña
              </label>

              <div className="input-container password-container">

                <span className="input-icon">
                  🔒
                </span>

                <input
                  id="password"
                  className="login-input password-input"
                  type={
                    mostrarPassword
                      ? "text"
                      : "password"
                  }
                  placeholder="Ingresa tu contraseña"
                  value={password}
                  onChange={(e) =>
                    setPassword(e.target.value)
                  }
                  autoComplete="current-password"
                  required
                />

                <button
                  type="button"
                  className="password-toggle"
                  onClick={() =>
                    setMostrarPassword(
                      !mostrarPassword
                    )
                  }
                  aria-label={
                    mostrarPassword
                      ? "Ocultar contraseña"
                      : "Mostrar contraseña"
                  }
                >
                  {mostrarPassword
                    ? "Ocultar"
                    : "Ver"}
                </button>

              </div>

            </div>


            {/* MENSAJE DE ERROR */}
            {error && (
              <div
                className="login-error"
                role="alert"
              >
                {error}
              </div>
            )}


            {/* BOTÓN */}
            <button
              className="login-button"
              type="submit"
              disabled={cargando}
            >
              {cargando
                ? "Ingresando..."
                : "Iniciar sesión"}
            </button>

          </form>


          <div className="login-help">
            <span>¿Necesitas ayuda?</span>
            <p>
              Comunícate con el administrador
              del sistema.
            </p>
          </div>

        </div>


        <footer className="page-footer">
          <strong>
            I.E.P. George Washington Carver
          </strong>

          <span>
            Sistema de Gestión Académica
          </span>
        </footer>

      </section>

    </div>

  </main>
);


}


export default Login;