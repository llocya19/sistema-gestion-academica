
import {
  useEffect,
  useRef,
  useState,
  type ChangeEvent
} from "react";

import { Link } from "react-router-dom";

import {
  obtenerEstudiantes,
  cambiarEstadoEstudiante,
  importarEstudiantesExcel,
  type Estudiante,
  type RespuestaImportacion
} from "../../../services/secretariaService";

import SecretariaLayout from "../SecretariaLayout";
import "./EstudiantesPage.css";

type FiltroEstado = "todos" | "activos" | "inactivos";

function EstudiantesPage() {
  const [estudiantes, setEstudiantes] =
    useState<Estudiante[]>([]);

  const [busqueda, setBusqueda] = useState("");
  const [filtroEstado, setFiltroEstado] =
    useState<FiltroEstado>("todos");

  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState("");

  const [actualizandoId, setActualizandoId] =
    useState<number | null>(null);

  const [importando, setImportando] = useState(false);
  const [errorImportacion, setErrorImportacion] =
    useState("");

  const [resultadoImportacion, setResultadoImportacion] =
    useState<RespuestaImportacion | null>(null);

  const archivoInput = useRef<HTMLInputElement>(null);

  // Cargar estudiantes
  useEffect(() => {
    async function cargarEstudiantes() {
      try {
        const datos = await obtenerEstudiantes();
        setEstudiantes(datos);
      } catch (error) {
        console.error(error);
        setError("No se pudieron cargar los estudiantes.");
      } finally {
        setCargando(false);
      }
    }

    cargarEstudiantes();
  }, []);

  // Activar / desactivar
  async function manejarCambioEstado(estudiante: Estudiante) {
    const nuevoEstado = !estudiante.estado;
    const accion = nuevoEstado ? "activar" : "desactivar";

    const confirmar = window.confirm(
      `¿Deseas ${accion} al estudiante ${estudiante.persona.nombres} ${estudiante.persona.apellidos}?`
    );

    if (!confirmar) return;

    const estadoAnterior = estudiante.estado;

    try {
      setError("");
      setActualizandoId(estudiante.id);

      setEstudiantes((actuales) =>
        actuales.map((item) =>
          item.id === estudiante.id
            ? { ...item, estado: nuevoEstado }
            : item
        )
      );

      await cambiarEstadoEstudiante(
        estudiante.id,
        nuevoEstado
      );
    } catch (error) {
      console.error(error);

      setEstudiantes((actuales) =>
        actuales.map((item) =>
          item.id === estudiante.id
            ? { ...item, estado: estadoAnterior }
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

  // Importar Excel
  async function manejarImportacion(
    event: ChangeEvent<HTMLInputElement>
  ) {
    const archivo = event.target.files?.[0];

    if (!archivo) return;

    setErrorImportacion("");
    setResultadoImportacion(null);

    if (!archivo.name.toLowerCase().endsWith(".xlsx")) {
      setErrorImportacion(
        "Selecciona un archivo Excel con extensión .xlsx."
      );
      event.target.value = "";
      return;
    }

    setImportando(true);

    try {
      const respuesta = await importarEstudiantesExcel(archivo);
      setResultadoImportacion(respuesta);

      // Actualizar el listado después de importar
      try {
        const datosActualizados = await obtenerEstudiantes();
        setEstudiantes(datosActualizados);
        setError("");
      } catch (error) {
        console.error(error);
        setErrorImportacion(
          "La importación se procesó, pero no se pudo actualizar el listado. Recarga la página para consultar los registros."
        );
      }
    } catch (error) {
      console.error(error);
      setErrorImportacion(
        "No se pudo procesar el archivo Excel. Verifica su formato antes de intentarlo nuevamente."
      );
    } finally {
      setImportando(false);
      event.target.value = "";
    }
  }

  // Búsqueda y filtros
  const textoBusqueda = busqueda.toLowerCase().trim();

  const estudiantesFiltrados = estudiantes
    .filter((estudiante) => {
      const nombreCompleto =
        `${estudiante.persona.nombres} ${estudiante.persona.apellidos}`
          .toLowerCase();

      const coincideBusqueda =
        estudiante.codigo.toLowerCase().includes(textoBusqueda) ||
        estudiante.persona.dni.includes(textoBusqueda) ||
        nombreCompleto.includes(textoBusqueda);

      const coincideEstado =
        filtroEstado === "todos" ||
        (filtroEstado === "activos" && estudiante.estado) ||
        (filtroEstado === "inactivos" && !estudiante.estado);

      return coincideBusqueda && coincideEstado;
    })
    .sort((a, b) =>
      a.codigo.localeCompare(b.codigo, undefined, {
        numeric: true,
        sensitivity: "base"
      })
    );

  return (
    <SecretariaLayout>
      {/* Encabezado */}
      <div className="estudiantes-encabezado">
        <div className="secretaria-page-title">
          <h1>Gestión de estudiantes</h1>
          <p>
            {estudiantes.length} estudiantes registrados
            en el sistema
          </p>
        </div>

        <div className="estudiantes-acciones-principales">
          <input
            ref={archivoInput}
            type="file"
            accept=".xlsx"
            aria-label="Seleccionar Excel de estudiantes"
            onChange={manejarImportacion}
            style={{ display: "none" }}
          />

          <button
            type="button"
            className="estudiantes-importar"
            disabled={importando}
            onClick={() => archivoInput.current?.click()}
          >
            {importando
              ? "Importando..."
              : "Importar Excel"}
          </button>

          <Link
            to="/secretaria/estudiantes/nuevo"
            className="estudiantes-nuevo"
          >
            + Nuevo estudiante
          </Link>
        </div>
      </div>

      {/* Resultado de importación */}
      {errorImportacion && (
        <div className="estudiantes-error" role="alert">
          {errorImportacion}
        </div>
      )}

      {resultadoImportacion && (
        <section className="estudiantes-importacion-resultado">
          <h3>Resultado de importación</h3>

          <p>
            Estudiantes creados:{" "}
            <strong>
              {resultadoImportacion.resultado.creados}
            </strong>
          </p>

          <p>
            Filas con errores:{" "}
            <strong>
              {resultadoImportacion.resultado.errores.length}
            </strong>
          </p>

          {resultadoImportacion.resultado.errores.length > 0 && (
            <ul>
              {resultadoImportacion.resultado.errores.map(
                (item, indice) => (
                  <li key={`${item.fila}-${indice}`}>
                    Fila {item.fila}: {item.error}
                  </li>
                )
              )}
            </ul>
          )}
        </section>
      )}

      {/* Filtros */}
      <section className="estudiantes-card estudiantes-filtros">
        <div className="estudiantes-toolbar">
          <input
            type="search"
            className="estudiantes-buscador"
            placeholder="Buscar por código, DNI o nombre..."
            value={busqueda}
            onChange={(event) =>
              setBusqueda(event.target.value)
            }
          />

          <select
            className="estudiantes-select"
            aria-label="Filtrar por estado"
            value={filtroEstado}
            onChange={(event) =>
              setFiltroEstado(
                event.target.value as FiltroEstado
              )
            }
          >
            <option value="todos">Todos los estados</option>
            <option value="activos">Activos</option>
            <option value="inactivos">Inactivos</option>
          </select>
        </div>

        <p className="estudiantes-nota-filtros">
          Los filtros de año, grado y sección se habilitarán
          cuando esté integrada la asociación académica.
        </p>
      </section>

      {/* Listado */}
      <section className="estudiantes-card estudiantes-listado">
        <div className="estudiantes-listado-cabecera">
          <h2>Estudiantes registrados</h2>
          <span>
            {estudiantesFiltrados.length} resultados
          </span>
        </div>

        {cargando && (
          <p>Cargando estudiantes...</p>
        )}

        {error && (
          <div className="estudiantes-error" role="alert">
            {error}
          </div>
        )}

        {!cargando &&
          !error &&
          estudiantesFiltrados.length === 0 && (
            <div className="estudiantes-vacio">
              {busqueda || filtroEstado !== "todos"
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
                    <th>Estudiante</th>
                    <th>Grado</th>
                    <th>Sección</th>
                    <th>Estado</th>
                    <th>Acciones</th>
                  </tr>
                </thead>

                <tbody>
                  {estudiantesFiltrados.map((estudiante) => (
                    <tr key={estudiante.id}>
                      <td>{estudiante.codigo}</td>

                      <td>
                        <div className="estudiantes-identidad">
                          <span className="estudiantes-avatar">
                            {estudiante.persona.nombres
                              .charAt(0)
                              .toUpperCase()}
                          </span>

                          <div>
                            <div className="estudiantes-nombre">
                              <span>{estudiante.persona.nombres}</span>
                              {" "}
                              <span>{estudiante.persona.apellidos}</span>
                            </div>

                            <div className="estudiantes-dni">
                              DNI: {estudiante.persona.dni}
                            </div>
                          </div>
                        </div>
                      </td>

                      <td>
                        <span className="estudiantes-dato-pendiente">
                          —
                        </span>
                      </td>

                      <td>
                        <span className="estudiantes-dato-pendiente">
                          —
                        </span>
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

                      <td>
                        <div className="estudiante-acciones">
                        <Link
                          to={`/secretaria/estudiantes/${estudiante.id}`}
                          className="estudiante-ver-detalle"
                        >
                          Ver detalle
                        </Link>

                          <Link
                            to={`/secretaria/estudiantes/${estudiante.id}/editar`}
                            className="estudiante-editar"
                          >
                            Editar
                          </Link>

                          <button
                            type="button"
                            className={
                              estudiante.estado
                                ? "estudiante-cambiar-estado desactivar"
                                : "estudiante-cambiar-estado activar"
                            }
                            disabled={actualizandoId !== null}
                            onClick={() =>
                              manejarCambioEstado(estudiante)
                            }
                          >
                            {actualizandoId === estudiante.id
                              ? "Actualizando..."
                              : estudiante.estado
                                ? "Desactivar"
                                : "Activar"}
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          )}
      </section>
    </SecretariaLayout>
  );
}

export default EstudiantesPage;
