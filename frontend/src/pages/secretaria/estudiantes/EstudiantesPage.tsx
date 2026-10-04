import {
  useEffect,
  useState
} from "react";

import {
  obtenerEstudiantes,
  type Estudiante
} from "../../../services/secretariaService";

import SecretariaLayout from "../SecretariaLayout";

import "./EstudiantesPage.css";
import { Link } from "react-router-dom";


function EstudiantesPage() {

  const [estudiantes, setEstudiantes] =
    useState<Estudiante[]>([]);

  const [busqueda, setBusqueda] =
    useState("");

  const [cargando, setCargando] =
    useState(true);

  const [error, setError] =
    useState("");


  useEffect(() => {

    async function cargarEstudiantes() {

      try {

        const datos =
          await obtenerEstudiantes();

        setEstudiantes(datos);

      } catch (error) {

        console.error(error);

        setError(
          "No se pudieron cargar los estudiantes."
        );

      } finally {

        setCargando(false);

      }

    }

    cargarEstudiantes();

  }, []);


  const textoBusqueda =
    busqueda.toLowerCase().trim();


  const estudiantesFiltrados =
    estudiantes.filter((estudiante) => {

      const nombreCompleto =
        `${estudiante.persona.nombres} ${estudiante.persona.apellidos}`
          .toLowerCase();

      return (
        estudiante.codigo
          .toLowerCase()
          .includes(textoBusqueda) ||

        estudiante.persona.dni
          .includes(textoBusqueda) ||

        nombreCompleto
          .includes(textoBusqueda)
      );

    });


  return (

    <SecretariaLayout>

      <div className="secretaria-page-title">

        <h1>Gestión de estudiantes</h1>

        <p>
          Consulta y administra los estudiantes
          registrados en el sistema.
        </p>

      </div>


      <section className="estudiantes-card">

        <div className="estudiantes-toolbar">

          <input
            type="search"
            className="estudiantes-buscador"
            placeholder="Buscar por código, DNI o nombre..."
            value={busqueda}
            onChange={(e) =>
              setBusqueda(e.target.value)
            }
          />

          <Link
            to="/secretaria/estudiantes/nuevo"
            className="estudiantes-nuevo"
          >
            + Nuevo estudiante
          </Link>

          


        </div>


        <h2>Estudiantes registrados</h2>


        {cargando && (
          <p>Cargando estudiantes...</p>
        )}


        {error && (
          <div className="estudiantes-error">
            {error}
          </div>
        )}


        {!cargando &&
          !error &&
          estudiantesFiltrados.length === 0 && (

            <div className="estudiantes-vacio">

              {busqueda
                ? "No se encontraron estudiantes."
                : "No hay estudiantes registrados."}

            </div>

          )}


        {!cargando &&
          !error &&
          estudiantesFiltrados.length > 0 && (

            <div className="estudiantes-tabla-contenedor">

              <table className="estudiantes-tabla">

                <thead>

                  <tr>
                    <th>Código</th>
                    <th>DNI</th>
                    <th>Nombres</th>
                    <th>Apellidos</th>
                    <th>Estado</th>
                  </tr>

                </thead>

                <tbody>

                  {estudiantesFiltrados.map(
                    (estudiante) => (

                      <tr key={estudiante.id}>

                        <td>
                          {estudiante.codigo}
                        </td>

                        <td>
                          {estudiante.persona.dni}
                        </td>

                        <td>
                          {estudiante.persona.nombres}
                        </td>

                        <td>
                          {estudiante.persona.apellidos}
                        </td>

                        <td>

                          <span
                            className={
                              estudiante.estado
                                ? "estudiante-estado activo"
                                : "estudiante-estado inactivo"
                            }
                          >
                            {estudiante.estado
                              ? "Activo"
                              : "Inactivo"}
                          </span>

                        </td>

                      </tr>

                    )
                  )}

                </tbody>

              </table>

            </div>

          )}

      </section>

    </SecretariaLayout>

  );
}


export default EstudiantesPage;