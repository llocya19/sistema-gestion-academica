type Usuario = {
  id: number;
  email: string;
  estado: boolean;
  rol: string;
  persona: {
    dni: string;
    nombres: string;
    apellidos: string;
  };
};

type UsuariosPageProps = {
  usuarios: Usuario[];
};

function UsuariosPage({ usuarios }: UsuariosPageProps) {
  return (
    <main>
      <h1>Gestión de usuarios</h1>

      <table>
        <thead>
          <tr>
            <th>Usuario</th>
            <th>Correo</th>
            <th>Rol</th>
            <th>Estado</th>
          </tr>
        </thead>

        <tbody>
          {usuarios.map((usuario) => (
            <tr key={usuario.id}>
              <td>
                {usuario.persona.nombres} {usuario.persona.apellidos}
              </td>

              <td>{usuario.email}</td>

              <td>{usuario.rol}</td>

              <td>
                {usuario.estado ? "Activo" : "Inactivo"}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </main>
  );
}

export default UsuariosPage;