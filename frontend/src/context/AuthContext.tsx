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
  iniciarSesion: (token: string, usuario: Usuario) => void;
  cerrarSesion: () => void;
}


const AuthContext = createContext<AuthContextType | undefined>(
  undefined
);


export function AuthProvider({ children }: { children: ReactNode }) {

    const [usuario, setUsuario] = useState<Usuario | null>(() => {

        const usuarioGuardado = sessionStorage.getItem("usuario");

        return usuarioGuardado
        ? JSON.parse(usuarioGuardado)
        : null;

    });


    const [token, setToken] = useState<string | null>(() => {

        return sessionStorage.getItem("token");

    });


    const iniciarSesion = (
        nuevoToken: string,
        nuevoUsuario: Usuario
    ) => {

        setToken(nuevoToken);
        setUsuario(nuevoUsuario);

        sessionStorage.setItem(
            "token",
            nuevoToken
        );

        sessionStorage.setItem(
            "usuario",
            JSON.stringify(nuevoUsuario)
        );

    };


    const cerrarSesion = () => {

        setToken(null);
        setUsuario(null);

        sessionStorage.removeItem("token");
        sessionStorage.removeItem("usuario");

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

  const context = useContext(AuthContext);

  if (!context) {
    throw new Error(
      "useAuth debe utilizarse dentro de AuthProvider"
    );
  }

  return context;

}