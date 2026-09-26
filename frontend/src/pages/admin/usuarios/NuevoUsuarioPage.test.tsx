import { describe, expect, it, vi } from "vitest";
import {
  render,
  screen,
} from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import { MemoryRouter } from "react-router-dom";

import NuevoUsuarioPage from "./NuevoUsuarioPage";
import { AuthProvider } from "../../../context/AuthContext";

import {
  obtenerRoles,
  crearUsuario,
} from "../../../services/adminService";

vi.mock("../../../services/adminService", () => ({
  obtenerRoles: vi.fn(),
  crearUsuario: vi.fn(),
}));

function renderizarPagina() {
  return render(
    <MemoryRouter>
      <AuthProvider>
        <NuevoUsuarioPage />
      </AuthProvider>
    </MemoryRouter>
  );
}



describe("NuevoUsuarioPage - HU02", () => {
  it(
    "muestra el formulario para crear una cuenta de usuario",
    async () => {
      vi.mocked(obtenerRoles).mockResolvedValue([]);

      renderizarPagina();

      expect(
        screen.getByRole("heading", {
          name: /nuevo usuario/i,
        })
      ).toBeInTheDocument();

      expect(
        screen.getByLabelText(/dni/i)
      ).toBeInTheDocument();

      expect(
        screen.getByLabelText(/nombres/i)
      ).toBeInTheDocument();

      expect(
        screen.getByLabelText(/apellidos/i)
      ).toBeInTheDocument();

      expect(
        screen.getByLabelText(/correo electrónico/i)
      ).toBeInTheDocument();

      expect(
        screen.getByLabelText(/^contraseña$/i)
      ).toBeInTheDocument();

      expect(
        screen.getByLabelText(/rol/i)
      ).toBeInTheDocument();

      expect(
        screen.getByRole("button", {
          name: /crear usuario/i,
        })
      ).toBeInTheDocument();

      expect(
        await screen.findByText("Seleccione un rol")
      ).toBeInTheDocument();
    }
  );

  it(
    "carga y muestra los roles disponibles",
    async () => {
      const roles = [
        {
          id: 1,
          nombre: "ADMINISTRADOR",
          descripcion: "Administrador del sistema",
        },
        {
          id: 2,
          nombre: "DIRECTORA",
          descripcion: "Directora",
        },
        {
          id: 3,
          nombre: "SECRETARIA",
          descripcion: "Secretaría",
        },
        {
          id: 4,
          nombre: "DOCENTE",
          descripcion: "Docente",
        },
      ];

      vi.mocked(obtenerRoles).mockResolvedValue(roles);

      renderizarPagina();

      expect(
        await screen.findByRole("option", {
          name: "ADMINISTRADOR",
        })
      ).toBeInTheDocument();

      expect(
        screen.getByRole("option", {
          name: "DIRECTORA",
        })
      ).toBeInTheDocument();

      expect(
        screen.getByRole("option", {
          name: "SECRETARIA",
        })
      ).toBeInTheDocument();

      expect(
        screen.getByRole("option", {
          name: "DOCENTE",
        })
      ).toBeInTheDocument();
    }
  );

  it(
    "envía los datos para crear una cuenta de usuario",
    async () => {
      const user = userEvent.setup();

      vi.mocked(obtenerRoles).mockResolvedValue([
        {
          id: 4,
          nombre: "DOCENTE",
          descripcion: "Docente",
        },
      ]);

      vi.mocked(crearUsuario).mockResolvedValue({
        mensaje: "Usuario creado correctamente",
      });

      renderizarPagina();

      await screen.findByRole("option", {
        name: "DOCENTE",
      });

      await user.type(
        screen.getByLabelText(/dni/i),
        "12345678"
      );

      await user.type(
        screen.getByLabelText(/nombres/i),
        "Pedro"
      );

      await user.type(
        screen.getByLabelText(/apellidos/i),
        "García"
      );

      await user.type(
        screen.getByLabelText(/correo electrónico/i),
        "pedro@test.com"
      );

      await user.type(
        screen.getByLabelText(/^contraseña$/i),
        "123456"
      );

      await user.selectOptions(
        screen.getByLabelText(/rol/i),
        "4"
      );

      await user.click(
        screen.getByRole("button", {
          name: /crear usuario/i,
        })
      );

      expect(crearUsuario).toHaveBeenCalledWith({
        dni: "12345678",
        nombres: "Pedro",
        apellidos: "García",
        email: "pedro@test.com",
        password: "123456",
        role_id: 4,
      });
    }
  );

  it(
    "muestra un mensaje cuando el usuario se crea correctamente",
    async () => {
      const user = userEvent.setup();

      vi.mocked(obtenerRoles).mockResolvedValue([
        {
          id: 4,
          nombre: "DOCENTE",
          descripcion: "Docente",
        },
      ]);

      vi.mocked(crearUsuario).mockResolvedValue({
        mensaje: "Usuario creado correctamente",
      });

      renderizarPagina();

      await screen.findByRole("option", {
        name: "DOCENTE",
      });

      await user.type(
        screen.getByLabelText(/dni/i),
        "11223344"
      );

      await user.type(
        screen.getByLabelText(/nombres/i),
        "Carlos"
      );

      await user.type(
        screen.getByLabelText(/apellidos/i),
        "Prueba"
      );

      await user.type(
        screen.getByLabelText(/correo electrónico/i),
        "carlos@test.com"
      );

      await user.type(
        screen.getByLabelText(/^contraseña$/i),
        "123456"
      );

      await user.selectOptions(
        screen.getByLabelText(/rol/i),
        "4"
      );

      await user.click(
        screen.getByRole("button", {
          name: /crear usuario/i,
        })
      );

      expect(
        await screen.findByText(
          "Usuario creado correctamente"
        )
      ).toBeInTheDocument();
    }
  );

  it(
    "muestra un error cuando el correo ya está registrado",
    async () => {
      const user = userEvent.setup();

      vi.mocked(obtenerRoles).mockResolvedValue([
        {
          id: 4,
          nombre: "DOCENTE",
          descripcion: "Docente",
        },
      ]);

      vi.mocked(crearUsuario).mockRejectedValue({
        response: {
          data: {
            mensaje: "El correo ya está registrado",
          },
        },
      });

      renderizarPagina();

      await screen.findByRole("option", {
        name: "DOCENTE",
      });

      await user.type(
        screen.getByLabelText(/dni/i),
        "99887766"
      );

      await user.type(
        screen.getByLabelText(/nombres/i),
        "Ana"
      );

      await user.type(
        screen.getByLabelText(/apellidos/i),
        "Prueba"
      );

      await user.type(
        screen.getByLabelText(/correo electrónico/i),
        "directora@test.com"
      );

      await user.type(
        screen.getByLabelText(/^contraseña$/i),
        "123456"
      );

      await user.selectOptions(
        screen.getByLabelText(/rol/i),
        "4"
      );

      await user.click(
        screen.getByRole("button", {
          name: /crear usuario/i,
        })
      );

      expect(
        await screen.findByText(
          "El correo ya está registrado"
        )
      ).toBeInTheDocument();
    }
  );

  it(
    "muestra un error cuando el DNI ya está registrado",
    async () => {
      const user = userEvent.setup();

      vi.mocked(obtenerRoles).mockResolvedValue([
        {
          id: 4,
          nombre: "DOCENTE",
          descripcion: "Docente",
        },
      ]);

      vi.mocked(crearUsuario).mockRejectedValue({
        response: {
          data: {
            mensaje: "El DNI ya está registrado",
          },
        },
      });

      renderizarPagina();

      await screen.findByRole("option", {
        name: "DOCENTE",
      });

      await user.type(
        screen.getByLabelText(/dni/i),
        "12345678"
      );

      await user.type(
        screen.getByLabelText(/nombres/i),
        "Pedro"
      );

      await user.type(
        screen.getByLabelText(/apellidos/i),
        "Prueba"
      );

      await user.type(
        screen.getByLabelText(/correo electrónico/i),
        "correo-nuevo@test.com"
      );

      await user.type(
        screen.getByLabelText(/^contraseña$/i),
        "123456"
      );

      await user.selectOptions(
        screen.getByLabelText(/rol/i),
        "4"
      );

      await user.click(
        screen.getByRole("button", {
          name: /crear usuario/i,
        })
      );

      expect(
        await screen.findByText(
          "El DNI ya está registrado"
        )
      ).toBeInTheDocument();
    }
  );

  it(
    "configura los campos obligatorios y valida el formato del DNI",
    async () => {
      vi.mocked(obtenerRoles).mockResolvedValue([]);

      renderizarPagina();

      // Esperamos a que termine la carga asíncrona de roles
      await screen.findByText("Seleccione un rol");

      const dni = screen.getByLabelText(/dni/i);
      const nombres = screen.getByLabelText(/nombres/i);
      const apellidos = screen.getByLabelText(/apellidos/i);
      const email = screen.getByLabelText(/correo electrónico/i);
      const password = screen.getByLabelText(/^contraseña$/i);
      const rol = screen.getByLabelText(/rol/i);

      expect(dni).toBeRequired();
      expect(nombres).toBeRequired();
      expect(apellidos).toBeRequired();
      expect(email).toBeRequired();
      expect(password).toBeRequired();
      expect(rol).toBeRequired();

      expect(dni).toHaveAttribute("maxlength", "8");
      expect(dni).toHaveAttribute("pattern", "[0-9]{8}");
      expect(dni).toHaveAttribute("inputmode", "numeric");
    }
  );
});