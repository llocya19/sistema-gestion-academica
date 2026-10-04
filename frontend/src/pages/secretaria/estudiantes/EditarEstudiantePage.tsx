import {
  useEffect,
  useState,
  type FormEvent
} from "react";

import {
  Link,
  useNavigate,
  useParams
} from "react-router-dom";

import axios from "axios";

import {
  actualizarEstudiante,
  obtenerEstudiantes
} from "../../../services/secretariaService";

import SecretariaLayout from "../SecretariaLayout";

import "./NuevoEstudiantePage.css";


function EditarEstudiantePage() {

  const { id } = useParams();

  const navigate = useNavigate();


  const [dni, setDni] =
    useState("");

  const [studentCode, setStudentCode] =
    useState("");

  const [nombres, setNombres] =
    useState("");

  const [apellidos, setApellidos] =
    useState("");

  const [cargandoDatos, setCargandoDatos] =
    useState(true);

  const [guardando, setGuardando] =
    useState(false);

  const [error, setError] =
    useState("");


  useEffect(() => {

    async function cargarEstudiante() {

      try {

        const estudiantes =
          await obtenerEstudiantes();

        const estudiante =
          estudiantes.find(
            (item) =>
              item.id === Number(id)
          );


        if (!estudiante) {

          setError(
            "No se encontró el estudiante."
          );

          return;
        }


        setDni(
          estudiante.persona.dni
        );

        setStudentCode(
          estudiante.codigo
        );

        setNombres(
          estudiante.persona.nombres
        );

        setApellidos(
          estudiante.persona.apellidos
        );

      } catch (error) {

        console.error(error);

        setError(
          "No se pudieron cargar los datos del estudiante."
        );

      } finally {

        setCargandoDatos(false);

      }

    }


    cargarEstudiante();

  }, [id]);


  async function manejarSubmit(
    event: FormEvent<HTMLFormElement>
  ) {

    event.preventDefault();

    setError("");


    if (!id) {

      setError(
        "No se pudo identificar al estudiante."
      );

      return;
    }


    try {

      setGuardando(true);


      await actualizarEstudiante(
        Number(id),
        {
          nombres: nombres.trim(),
          apellidos: apellidos.trim(),
          student_code:
            studentCode.trim(),
        }
      );


      navigate(
        "/secretaria/estudiantes"
      );

    } catch (error) {

      console.error(error);


      if (axios.isAxiosError(error)) {

        setError(
          error.response?.data?.mensaje ||
          "No se pudo actualizar el estudiante."
        );

      } else {

        setError(
          "No se pudo actualizar el estudiante."
        );

      }

    } finally {

      setGuardando(false);

    }

  }


  return (

    <SecretariaLayout>

      <div className="secretaria-page-title">

        <h1>Editar estudiante</h1>

        <p>
          Actualiza los datos del estudiante
          registrado en el sistema.
        </p>

      </div>


      <section className="nuevo-estudiante-card">

        {cargandoDatos && (

          <p>
            Cargando datos del estudiante...
          </p>

        )}


        {error && (

          <div className="nuevo-estudiante-error">
            {error}
          </div>

        )}


        {!cargandoDatos && dni && (

            <form
                onSubmit={manejarSubmit}
                className="nuevo-estudiante-form"
            >

                <div className="nuevo-estudiante-grid">

                <div className="nuevo-estudiante-campo">

                    <label htmlFor="dni">
                    DNI
                    </label>

                    <input
                    id="dni"
                    type="text"
                    value={dni}
                    disabled
                    />

                    <small className="nuevo-estudiante-ayuda">
                    El DNI no puede modificarse desde esta opción.
                    </small>

                </div>


                <div className="nuevo-estudiante-campo">

                    <label htmlFor="student_code">
                    Código de estudiante
                    </label>

                    <input
                    id="student_code"
                    type="text"
                    value={studentCode}
                    onChange={(event) =>
                        setStudentCode(
                        event.target.value
                        )
                    }
                    required
                    />

                </div>


                <div className="nuevo-estudiante-campo">

                    <label htmlFor="nombres">
                    Nombres
                    </label>

                    <input
                    id="nombres"
                    type="text"
                    value={nombres}
                    onChange={(event) =>
                        setNombres(
                        event.target.value
                        )
                    }
                    required
                    />

                </div>


                <div className="nuevo-estudiante-campo">

                    <label htmlFor="apellidos">
                    Apellidos
                    </label>

                    <input
                    id="apellidos"
                    type="text"
                    value={apellidos}
                    onChange={(event) =>
                        setApellidos(
                        event.target.value
                        )
                    }
                    required
                    />

                </div>

                </div>


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
                    disabled={guardando}
                >
                    {guardando
                    ? "Guardando..."
                    : "Guardar cambios"}
                </button>

                </div>

            </form>

            )}

      </section>

    </SecretariaLayout>

  );

}


export default EditarEstudiantePage;