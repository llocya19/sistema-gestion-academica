import {
  useEffect,
  useState
} from "react";

import { Link } from "react-router-dom";

import {
  obtenerEstudiantes,
  cambiarEstadoEstudiante,
  type Estudiante
} from "../../../services/secretariaService";

import SecretariaLayout from "../SecretariaLayout";

import "./EstudiantesPage.css";


function EstudiantesPage() {

  const [estudiantes, setEstudiantes] =
    useState<Estudiante[]>([]);

  const [busqueda, setBusqueda] =
    useState("");

  const [cargando, setCargando] =
    useState(true);

  const [error, setError] =
    useState("");

  const [actualizandoId, setActualizandoId] =
    useState<number | null>(null);


  // ==========================================
  // CARGAR ESTUDIANTES
  // ==========================================

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


  // ==========================================
  // ACTIVAR / DESACTIVAR ESTUDIANTE
  // ==========================================

  async function manejarCambioEstado(
  estudiante: Estudiante
) {

  const nuevoEstado =
    !estudiante.estado;

  const accion =
    nuevoEstado
      ? "activar"
      : "desactivar";


  const confirmar =
    window.confirm(
      `¿Deseas ${accion} al estudiante ${estudiante.persona.nombres} ${estudiante.persona.apellidos}?`
    );


  if (!confirmar) {
    return;
  }


  // Guardamos el estado anterior por si ocurre un error
  const estadoAnterior =
    estudiante.estado;


  try {

    setError("");

    setActualizandoId(
      estudiante.id
    );


    // Actualización inmediata en pantalla
    setEstudiantes(
      (estudiantesActuales) =>
        estudiantesActuales.map(
          (item) =>
            item.id === estudiante.id
              ? {
                  ...item,
                  estado: nuevoEstado
                }
              : item
        )
    );


    // Guardamos el cambio en el backend
    await cambiarEstadoEstudiante(
      estudiante.id,
      nuevoEstado
    );


  } catch (error) {

    console.error(error);


    // Si el backend falla,
    // regresamos al estado anterior
    setEstudiantes(
      (estudiantesActuales) =>
        estudiantesActuales.map(
          (item) =>
            item.id === estudiante.id
              ? {
                  ...item,
                  estado: estadoAnterior
                }
              : item
        )
    );


    setError(
      "No se pudo actualizar el estado del estudiante."
    );


  } finally {

    setActualizandoId(null);

  }

}


  // ==========================================
  // BUSCADOR
  // ==========================================

  const textoBusqueda =
    busqueda
      .toLowerCase()
      .trim();


  const estudiantesFiltrados =
  estudiantes
    .filter(
      (estudiante) => {

        const nombreCompleto =
          `${estudiante.persona.nombres} ${estudiante.persona.apellidos}`
            .toLowerCase();

        return (
          estudiante.codigo
            .toLowerCase()
            .includes(textoBusqueda)
          ||
          estudiante.persona.dni
            .includes(textoBusqueda)
          ||
          nombreCompleto
            .includes(textoBusqueda)
        );

      }
    )
    .sort(
      (a, b) =>
        a.codigo.localeCompare(
          b.codigo,
          undefined,
          {
            numeric: true,
            sensitivity: "base"
          }
        )
    );


  // ==========================================
  // INTERFAZ
  // ==========================================

  return (

    <SecretariaLayout>

      <div className="secretaria-page-title">

        <h1>
          Gestión de estudiantes
        </h1>

        <p>
          Consulta y administra los estudiantes
          registrados en el sistema.
        </p>

      </div>


      <section className="estudiantes-card">

        {/* ============================= */}
        {/* BUSCADOR Y NUEVO ESTUDIANTE */}
        {/* ============================= */}

        <div className="estudiantes-toolbar">

          <input
            type="search"
            className="estudiantes-buscador"
            placeholder="Buscar por código, DNI o nombre..."
            value={busqueda}
            onChange={(event) =>
              setBusqueda(
                event.target.value
              )
            }
          />


          <Link
            to="/secretaria/estudiantes/nuevo"
            className="estudiantes-nuevo"
          >
            + Nuevo estudiante
          </Link>

        </div>


        <h2>
          Estudiantes registrados
        </h2>


        {/* ============================= */}
        {/* CARGANDO */}
        {/* ============================= */}

        {cargando && (

          <p>
            Cargando estudiantes...
          </p>

        )}


        {/* ============================= */}
        {/* ERROR */}
        {/* ============================= */}

        {error && (

          <div className="estudiantes-error">

            {error}

          </div>

        )}


        {/* ============================= */}
        {/* SIN RESULTADOS */}
        {/* ============================= */}

        {!cargando &&
          !error &&
          estudiantesFiltrados.length === 0 && (

            <div className="estudiantes-vacio">

              {busqueda
                ? "No se encontraron estudiantes."
                : "No hay estudiantes registrados."}

            </div>

          )}


        {/* ============================= */}
        {/* TABLA DE ESTUDIANTES */}
        {/* ============================= */}

        {!cargando &&
          !error &&
          estudiantesFiltrados.length > 0 && (

            <div className="estudiantes-tabla-contenedor">

              <table className="estudiantes-tabla">

                <thead>

                  <tr>

                    <th>
                      Código
                    </th>

                    <th>
                      DNI
                    </th>

                    <th>
                      Nombres
                    </th>

                    <th>
                      Apellidos
                    </th>

                    <th>
                      Estado
                    </th>

                    <th>
                      Acciones
                    </th>

                  </tr>

                </thead>


                <tbody>

                  {estudiantesFiltrados.map(
                    (estudiante) => (

                      <tr key={estudiante.id}>

                        {/* CÓDIGO */}

                        <td>
                          {estudiante.codigo}
                        </td>


                        {/* DNI */}

                        <td>
                          {estudiante.persona.dni}
                        </td>


                        {/* NOMBRES */}

                        <td>
                          {estudiante.persona.nombres}
                        </td>


                        {/* APELLIDOS */}

                        <td>
                          {estudiante.persona.apellidos}
                        </td>


                        {/* ESTADO */}

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


                        {/* ACCIONES */}

                        <td>

                          <div className="estudiante-acciones">

                            {/* EDITAR */}

                            <Link
                              to={
                                `/secretaria/estudiantes/${estudiante.id}/editar`
                              }
                              className="estudiante-editar"
                            >
                              Editar
                            </Link>


                            {/* ACTIVAR / DESACTIVAR */}

                            <button
                              type="button"
                              className={
                                estudiante.estado
                                  ? "estudiante-cambiar-estado desactivar"
                                  : "estudiante-cambiar-estado activar"
                              }
                              disabled={
                                actualizandoId !== null
                              }
                              onClick={() =>
                                manejarCambioEstado(
                                  estudiante
                                )
                              }
                            >

                              {actualizandoId ===
                              estudiante.id

                                ? "Actualizando..."

                                : estudiante.estado

                                  ? "Desactivar"

                                  : "Activar"
                              }

                            </button>

                          </div>

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