import { Link } from "react-router-dom";
import { useAuth } from "../../context/AuthContext";

import SecretariaLayout from "./SecretariaLayout";

function SecretariaDashboard() {

  const { usuario } = useAuth();

  return (
    <SecretariaLayout>

      <div className="secretaria-page-title">

        <h1>
          Bienvenida, {usuario?.persona.nombres}
        </h1>

        <p>
          Gestiona la información académica de los
          estudiantes de la institución.
        </p>

      </div>

      <section className="secretaria-card">

        <h2>Gestión de estudiantes</h2>

        <p>
          Registra, consulta y actualiza la información
          de los estudiantes.
        </p>

        <Link
          to="/secretaria/estudiantes"
          className="secretaria-card-link"
        >
          Ir a Gestión de estudiantes
        </Link>

      </section>

    </SecretariaLayout>
  );
}

export default SecretariaDashboard;