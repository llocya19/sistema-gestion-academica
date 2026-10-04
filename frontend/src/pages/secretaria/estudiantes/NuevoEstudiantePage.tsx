import {
  useState,
  type FormEvent
} from "react";

import {
  Link,
  useNavigate
} from "react-router-dom";

import axios from "axios";

import {
  crearEstudiante
} from "../../../services/secretariaService";

import SecretariaLayout from "../SecretariaLayout";

import "./NuevoEstudiantePage.css";


function NuevoEstudiantePage() {

  const navigate = useNavigate();

  const [error, setError] =
    useState("");

  const [cargando, setCargando] =
    useState(false);


  const handleSubmit = async (
    e: FormEvent<HTMLFormElement>
  ) => {

    e.preventDefault();

    setError("");
    setCargando(true);

    const datos =
      new FormData(e.currentTarget);

    try {

      await crearEstudiante({

        dni: String(
          datos.get("dni")
        ).trim(),

        nombres: String(
          datos.get("nombres")
        ).trim(),

        apellidos: String(
          datos.get("apellidos")
        ).trim(),

        student_code: String(
          datos.get("student_code")
        ).trim(),

        telefono: String(
          datos.get("telefono")
        ).trim(),

        direccion: String(
          datos.get("direccion")
        ).trim()

      });

      navigate(
        "/secretaria/estudiantes"
      );

    } catch (error) {

      console.error(error);

      if (axios.isAxiosError(error)) {

        setError(
          error.response?.data?.mensaje ||
          "No se pudo registrar el estudiante."
        );

      } else {

        setError(
          "No se pudo registrar el estudiante."
        );

      }

    } finally {

      setCargando(false);

    }

  };


  return (

    <SecretariaLayout>

      <div className="secretaria-page-title">

        <h1>Registrar estudiante</h1>

        <p>
          Ingresa los datos del nuevo estudiante.
        </p>

      </div>


      <section className="nuevo-estudiante-card">

        <form onSubmit={handleSubmit}>

          <div className="nuevo-estudiante-grid">

            <div className="nuevo-estudiante-campo">

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
                onInput={(e) => {
                  e.currentTarget.value =
                    e.currentTarget.value.replace(
                      /\D/g,
                      ""
                    );
                }}
              />

            </div>


            <div className="nuevo-estudiante-campo">

              <label htmlFor="student_code">
                Código de estudiante
              </label>

              <input
                id="student_code"
                name="student_code"
                type="text"
                placeholder="Ej. EST004"
                required
              />

            </div>


            <div className="nuevo-estudiante-campo">

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


            <div className="nuevo-estudiante-campo">

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


            <div className="nuevo-estudiante-campo">

              <label htmlFor="telefono">
                Teléfono
              </label>

              <input
                id="telefono"
                name="telefono"
                type="tel"
                placeholder="Opcional"
              />

            </div>


            <div className="nuevo-estudiante-campo">

              <label htmlFor="direccion">
                Dirección
              </label>

              <input
                id="direccion"
                name="direccion"
                type="text"
                placeholder="Opcional"
              />

            </div>

          </div>


          {error && (

            <div className="nuevo-estudiante-error">
              {error}
            </div>

          )}


          <div className="nuevo-estudiante-acciones">

            <Link
              to="/secretaria/estudiantes"
              className="nuevo-estudiante-cancelar"
            >
              Cancelar
            </Link>

            <button
              type="submit"
              className="nuevo-estudiante-guardar"
              disabled={cargando}
            >
              {cargando
                ? "Registrando..."
                : "Registrar estudiante"}
            </button>

          </div>

        </form>

      </section>

    </SecretariaLayout>

  );
}


export default NuevoEstudiantePage;