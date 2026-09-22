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

  const [usuario, setUsuario] = useState<Usuario | null>(null);
  const [token, setToken] = useState<string | null>(null);


  const iniciarSesion = (
    nuevoToken: string,
    nuevoUsuario: Usuario
  ) => {

    setToken(nuevoToken);
    setUsuario(nuevoUsuario);

  };


  const cerrarSesion = () => {

    setToken(null);
    setUsuario(null);

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