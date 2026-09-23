import {
  createContext,
  useContext,
  useState,
  type ReactNode
} from "react";


interface Usuario {

  id: number;

  email: string;

  persona: {

    nombres: string;

    apellidos: string;

  };

  rol: string;

}


interface AuthContextType {

  usuario: Usuario | null;

  token: string | null;

  iniciarSesion: (
    token: string,
    usuario: Usuario
  ) => void;

  cerrarSesion: () => void;

}


const AuthContext = createContext<
  AuthContextType | undefined
>(undefined);



export function AuthProvider({
  children
}: {
  children: ReactNode
}) {


  // Recuperar usuario guardado
  const [usuario, setUsuario] = useState<Usuario | null>(() => {


    const usuarioGuardado =
      localStorage.getItem("usuario");


    return usuarioGuardado
      ? JSON.parse(usuarioGuardado)
      : null;


  });



  // Recuperar token guardado
  const [token, setToken] = useState<string | null>(() => {


    return localStorage.getItem("token");


  });



  // Guardar sesión
  const iniciarSesion = (

    nuevoToken: string,

    nuevoUsuario: Usuario

  ) => {


    setToken(nuevoToken);

    setUsuario(nuevoUsuario);



    localStorage.setItem(

      "token",

      nuevoToken

    );



    localStorage.setItem(

      "usuario",

      JSON.stringify(nuevoUsuario)

    );


  };




  // Cerrar sesión
  const cerrarSesion = () => {


    setToken(null);

    setUsuario(null);



    localStorage.removeItem(

      "token"

    );



    localStorage.removeItem(

      "usuario"

    );


  };




  return (

    <AuthContext.Provider

      value={{

        usuario,

        token,

        iniciarSesion,

        cerrarSesion

      }}

    >

      {children}


    </AuthContext.Provider>

  );


}




export function useAuth() {


  const context =
    useContext(AuthContext);



  if (!context) {


    throw new Error(

      "useAuth debe utilizarse dentro de AuthProvider"

    );


  }


  return context;


}