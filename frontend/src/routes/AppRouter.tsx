import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import Login from "../pages/auth/Login";
import Home from "../pages/home/Home";
import ProtectedRoute from "./ProtectedRoute";
import { AuthProvider } from "../context/AuthContext";
import AdminDashboard from "../pages/admin/AdminDashboard";
import UsuariosPage from "../pages/admin/usuarios/UsuariosPage";
import NuevoUsuarioPage from "../pages/admin/usuarios/NuevoUsuarioPage";
import SecretariaDashboard from "../pages/secretaria/SecretariaDashboard";
import EstudiantesPage from "../pages/secretaria/estudiantes/EstudiantesPage";
import NuevoEstudiantePage from "../pages/secretaria/estudiantes/NuevoEstudiantePage";
import EditarEstudiantePage from "../pages/secretaria/estudiantes/EditarEstudiantePage";
import DetalleEstudiantePage from "../pages/secretaria/estudiantes/DetalleEstudiantePage";


function AppRouter() {

  return (

    <BrowserRouter>

      <AuthProvider>

        <Routes>

          <Route
            path="/"
            element={<Login />}
          />

          <Route
            path="/home"
            element={
            <ProtectedRoute>
                <Home />
            </ProtectedRoute>
            }
          />

          <Route
            path="/admin"
            element={
              <ProtectedRoute>
                <AdminDashboard />
              </ProtectedRoute>
            }
          />

          <Route
            path="/admin/usuarios"
            element={
              <ProtectedRoute>
                <UsuariosPage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/admin/usuarios/nuevo"
            element={
              <ProtectedRoute>
                <NuevoUsuarioPage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/secretaria"
            element={
              <ProtectedRoute>
                <SecretariaDashboard />
              </ProtectedRoute>
            }
          />

          <Route
            path="/secretaria/estudiantes"
            element={
              <ProtectedRoute>
                <EstudiantesPage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/secretaria/estudiantes/nuevo"
            element={
              <ProtectedRoute>
                <NuevoEstudiantePage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/secretaria/estudiantes/:id/editar"
            element={
              <ProtectedRoute>
                <EditarEstudiantePage />
              </ProtectedRoute>
            }
          />

          <Route
            path="/secretaria/estudiantes/:id"
            element={
              <ProtectedRoute>
                <DetalleEstudiantePage />
              </ProtectedRoute>
            }
          />


        </Routes>

      </AuthProvider>

    </BrowserRouter>

  );

}


export default AppRouter;