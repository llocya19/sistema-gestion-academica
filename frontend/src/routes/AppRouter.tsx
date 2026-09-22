import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import Login from "../pages/auth/Login";
import Home from "../pages/home/Home";
import { AuthProvider } from "../context/AuthContext";


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
            element={<Home />}
          />

        

        </Routes>

      </AuthProvider>

    </BrowserRouter>

  );

}


export default AppRouter;