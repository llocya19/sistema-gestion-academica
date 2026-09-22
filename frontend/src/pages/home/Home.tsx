import { useAuth } from "../../context/AuthContext";


function Home() {

  const { usuario, cerrarSesion } = useAuth();


  return (

    <div>

      <h1>
        Bienvenido, {usuario?.persona.nombres}
      </h1>

      <p>
        Correo: {usuario?.email}
      </p>

      <p>
        Rol: {usuario?.rol}
      </p>

      <button onClick={cerrarSesion}>
        Cerrar sesión
      </button>

    </div>

  );

}


export default Home;