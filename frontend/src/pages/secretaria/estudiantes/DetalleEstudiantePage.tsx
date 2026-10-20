
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

import SecretariaLayout from "../SecretariaLayout";

import {
  obtenerEstudiantes,
  type Estudiante
} from "../../../services/secretariaService";

import "./DetalleEstudiantePage.css";

function DetalleEstudiantePage() {
  const { id } = useParams<{ id: string }>();

  const [estudiante, setEstudiante] =
    useState<Estudiante | null>(null);

  const [cargando, setCargando] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let activo = true;

    async function cargarDetalle() {
      const estudianteId = Number(id);

      if (!Number.isInteger(estudianteId) || estudianteId <= 0) {
        setError("El identificador del estudiante no es válido.");
        setCargando(false);
        return;
      }

      try {
        const estudiantes = await obtenerEstudiantes();

        if (!activo) return;

        const encontrado = estudiantes.find(
          (item) => item.id === estudianteId
        );

        if (!encontrado) {
          setError("No se encontró al estudiante solicitado.");
        } else {
          setEstudiante(encontrado);
        }
      } catch (error) {
        console.error(error);

        if (activo) {
          setError(
            "No se pudo consultar la información del estudiante."
          );
        }
      } finally {
        if (activo) {
          setCargando(false);
        }
      }
    }

    cargarDetalle();

    return () => {
      activo = false;
    };
  }, [id]);

  const nombreCompleto = estudiante
    ? `${estudiante.persona.nombres} ${estudiante.persona.apellidos}`
    : "";

  return (
    <SecretariaLayout>
      <div className="detalle-estudiante-pagina">
        <nav
          className="detalle-estudiante-ruta"
          aria-label="Ruta de navegación"
        >
          <Link to="/secretaria/estudiantes">
            ← Estudiantes
          </Link>

          <span>/</span>

          <span>
            {estudiante ? nombreCompleto : "Detalle"}
          </span>
        </nav>

        {cargando && (
          <div className="detalle-estudiante-mensaje">
            Cargando información del estudiante...
          </div>
        )}

        {!cargando && error && (
          <div
            className="detalle-estudiante-error"
            role="alert"
          >
            {error}
          </div>
        )}

        {!cargando && estudiante && (
          <>
            {/* TARJETA PRINCIPAL */}
            <section className="detalle-estudiante-card">
              <div className="detalle-estudiante-perfil">
                <div className="detalle-estudiante-avatar">
                  {estudiante.persona.nombres
                    .charAt(0)
                    .toUpperCase()}
                </div>

                <div className="detalle-estudiante-identidad">
                  <h1>{nombreCompleto}</h1>

                  <div className="detalle-estudiante-resumen">
                    <span>
                      Cód. <strong>{estudiante.codigo}</strong>
                    </span>

                    <span className="detalle-separador">·</span>

                    <span>
                      DNI:{" "}
                      <strong>{estudiante.persona.dni}</strong>
                    </span>
                  </div>
                </div>

                <div className="detalle-estudiante-perfil-acciones">
                  <span
                    className={
                      estudiante.estado
                        ? "detalle-estudiante-estado activo"
                        : "detalle-estudiante-estado inactivo"
                    }
                  >
                    {estudiante.estado ? "Activo" : "Inactivo"}
                  </span>

                  <Link
                    to={`/secretaria/estudiantes/${estudiante.id}/editar`}
                    className="detalle-estudiante-editar"
                  >
                    Editar
                  </Link>
                </div>
              </div>

              <div className="detalle-estudiante-datos">
                <div>
                  <span className="detalle-etiqueta">
                    Nombres
                  </span>
                  <strong>
                    {estudiante.persona.nombres}
                  </strong>
                </div>

                <div>
                  <span className="detalle-etiqueta">
                    Apellidos
                  </span>
                  <strong>
                    {estudiante.persona.apellidos}
                  </strong>
                </div>

                <div>
                  <span className="detalle-etiqueta">
                    Teléfono
                  </span>
                  <strong>
                    {estudiante.persona.telefono?.trim() ||
                      "No disponible"}
                  </strong>
                </div>

                <div>
                  <span className="detalle-etiqueta">
                    Dirección
                  </span>
                  <strong>
                    {estudiante.persona.direccion?.trim() ||
                      "No disponible"}
                  </strong>
                </div>
              </div>
            </section>

            {/* APODERADO */}
            <section className="detalle-estudiante-card">
              <h2 className="detalle-seccion-titulo">
                Datos del apoderado
              </h2>

              <p className="detalle-estudiante-aviso">
                Esta información todavía no está disponible
                en el servicio actual de estudiantes.
              </p>
            </section>

            {/* INFORMACIÓN ACADÉMICA */}
            <section className="detalle-estudiante-card detalle-academica">
              <div className="detalle-estudiante-tabs">
                <span
                  className="detalle-tab activo"
                  aria-current="page"
                >
                  Información académica
                </span>

                <button type="button" disabled>
                  Calificaciones
                </button>

                <button type="button" disabled>
                  Asistencia
                </button>

                <button type="button" disabled>
                  Historial
                </button>

                <button type="button" disabled>
                  Observaciones
                </button>
              </div>

              <div className="detalle-estudiante-contenido">
                <h3>Datos académicos</h3>

                <div className="detalle-estudiante-datos-academicos">
                  <div>
                    <span>Año académico</span>
                    <strong>Pendiente de integración</strong>
                  </div>

                  <div>
                    <span>Grado actual</span>
                    <strong>Pendiente de integración</strong>
                  </div>

                  <div>
                    <span>Sección</span>
                    <strong>Pendiente de integración</strong>
                  </div>
                </div>

                <p className="detalle-estudiante-aviso">
                  Los datos de grado y sección se mostrarán
                  cuando esté integrada la asociación académica.
                  Las demás pestañas se desarrollarán en las
                  historias de consulta y gestión académica.
                </p>
              </div>
            </section>
          </>
        )}
      </div>
    </SecretariaLayout>
  );
}

export default DetalleEstudiantePage;
