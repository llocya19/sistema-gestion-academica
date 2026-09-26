import {useState} from "react";
import {login} from "../../services/authService";

import "./Login.css";

import { useNavigate } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";
import axios from "axios";


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

    if (response.usuario.rol === "ADMINISTRADOR") {
      navigate("/admin");
    } else {
      navigate("/home");
    }

  } catch (error) {

    console.error(error);

    if (
      axios.isAxiosError(error) &&
      error.response?.data?.mensaje === "Usuario desactivado"
    ) {
      setError(
        "Tu cuenta se encuentra desactivada. Contacta con el administrador."
      );
    } else {
      setError(
        "Correo electrónico o contraseña incorrectos."
      );
    }

  } finally {

    setCargando(false);

  }
};



return (
  <div className="login-container">

    <div className="login-wrapper">

      <section className="login-welcome">
        <div className="welcome-content">

          <div className="school-icon">
            🎓
          </div>

          <h1>
            Sistema de Gestión Académica
          </h1>

          <p>
            Una plataforma para organizar y consultar
            la información académica de manera sencilla
            y eficiente.
          </p>

          <div className="school-name">
            I.E.P. George Washington Carver
          </div>

        </div>
      </section>


      <section className="login-form-section">

        <div className="login-card">

          <div className="login-header">
            <span className="login-subtitle">
              Bienvenido
            </span>

            <h2>Iniciar sesión</h2>

            <p>
              Ingresa tus credenciales para acceder
              al sistema.
            </p>
          </div>


          <form onSubmit={handleSubmit}>

            <div className="form-group">

              <label htmlFor="email">
                Correo electrónico
              </label>

              <input
                id="email"
                className="login-input"
                type="email"
                placeholder="ejemplo@correo.com"
                value={email}
                onChange={(e) =>
                  setEmail(e.target.value)
                }
                required
              />

            </div>


            <div className="form-group">

                <label htmlFor="password">
                    Contraseña
                </label>

                <div className="password-container">

                    <input
                    id="password"
                    className="login-input password-input"
                    type={mostrarPassword ? "text" : "password"}
                    placeholder="Ingresa tu contraseña"
                    value={password}
                    onChange={(e) =>
                        setPassword(e.target.value)
                    }
                    required
                    />

                    <button
                    type="button"
                    className="password-toggle"
                    onClick={() =>
                        setMostrarPassword(!mostrarPassword)
                    }
                    aria-label={
                        mostrarPassword
                        ? "Ocultar contraseña"
                        : "Mostrar contraseña"
                    }
                    >
                    {mostrarPassword ? "Ocultar" : "Ver"}
                    </button>

                </div>

            </div>

            {error && (
                <div className="login-error">
                    {error}
                </div>
            )}


            <button
                className="login-button"
                type="submit"
                disabled={cargando}
            >
                {cargando ? "Ingresando..." : "Ingresar"}
            </button>

          </form>


          <p className="login-footer">
            Acceso exclusivo para personal autorizado
          </p>

        </div>

      </section>

    </div>

  </div>
);


}


export default Login;