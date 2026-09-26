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



        </Routes>

      </AuthProvider>

    </BrowserRouter>

  );

}


export default AppRouter;