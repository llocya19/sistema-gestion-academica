import { describe, expect, it, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import UsuariosPage from "./UsuariosPage";
import {
  obtenerUsuarios,
  cambiarEstadoUsuario,
} from "../../../services/adminService";
import userEvent from "@testing-library/user-event";

vi.mock("../../../services/adminService", () => ({
  obtenerUsuarios: vi.fn(),
  cambiarEstadoUsuario: vi.fn(),
}));

describe("UsuariosPage - HU02", () => {

  it("carga y muestra el estado actual de las cuentas", async () => {
    const usuarios = [
      {
        id: 1,
        email: "directora@test.com",
        estado: true,
        rol: "DIRECTORA",
        persona: {
          dni: "12345678",
          nombres: "María",
          apellidos: "Directora",
        },
      },
      {
        id: 2,
        email: "docente@test.com",
        estado: false,
        rol: "DOCENTE",
        persona: {
          dni: "87654321",
          nombres: "Juan",
          apellidos: "Profesor",
        },
      },
    ];

    vi.mocked(obtenerUsuarios).mockResolvedValue(usuarios);

    render(
      <MemoryRouter>
        <UsuariosPage />
      </MemoryRouter>
    );

    await waitFor(() => {
      expect(obtenerUsuarios).toHaveBeenCalledTimes(1);
    });

    expect(
      screen.getByText("María Directora")
    ).toBeInTheDocument();

    expect(
      screen.getByText("directora@test.com")
    ).toBeInTheDocument();

    expect(
      screen.getByText("DIRECTORA")
    ).toBeInTheDocument();

    expect(
      screen.getByText("Activo")
    ).toBeInTheDocument();

    expect(
      screen.getByText("Juan Profesor")
    ).toBeInTheDocument();

    expect(
      screen.getByText("docente@test.com")
    ).toBeInTheDocument();

    expect(
      screen.getByText("DOCENTE")
    ).toBeInTheDocument();

    expect(
      screen.getByText("Inactivo")
    ).toBeInTheDocument();
  });


  it("muestra un acceso para crear un nuevo usuario", async () => {
    vi.mocked(obtenerUsuarios).mockResolvedValue([]);

    render(
      <MemoryRouter>
        <UsuariosPage />
      </MemoryRouter>
    );

    expect(
      await screen.findByRole("link", {
        name: /nuevo usuario/i,
      })
    ).toHaveAttribute(
      "href",
      "/admin/usuarios/nuevo"
    );
  });

  it("muestra la acción correspondiente según el estado de la cuenta", async () => {
    vi.mocked(obtenerUsuarios).mockResolvedValue([
      {
        id: 1,
        email: "directora@test.com",
        estado: true,
        rol: "DIRECTORA",
        persona: {
          dni: "12345678",
          nombres: "María",
          apellidos: "Directora",
        },
      },
      {
        id: 2,
        email: "docente@test.com",
        estado: false,
        rol: "DOCENTE",
        persona: {
          dni: "87654321",
          nombres: "Juan",
          apellidos: "Profesor",
        },
      },
    ]);

    render(
      <MemoryRouter>
        <UsuariosPage />
      </MemoryRouter>
    );

    expect(
      await screen.findByRole("button", {
        name: /^desactivar$/i,
      })
    ).toBeInTheDocument();

    expect(
      screen.getByRole("button", {
        name: /^activar$/i,
      })
    ).toBeInTheDocument();
  });

  it("desactiva una cuenta activa al presionar Desactivar", async () => {
    const user = userEvent.setup();

    vi.mocked(obtenerUsuarios).mockResolvedValue([
      {
        id: 5,
        email: "docente@test.com",
        estado: true,
        rol: "DOCENTE",
        persona: {
          dni: "12345678",
          nombres: "Juan",
          apellidos: "Profesor",
        },
      },
    ]);

    vi.mocked(cambiarEstadoUsuario).mockResolvedValue({
      mensaje: "Estado actualizado correctamente",
    });

    render(
      <MemoryRouter>
        <UsuariosPage />
      </MemoryRouter>
    );

    const botonDesactivar = await screen.findByRole(
      "button",
      {
        name: /^desactivar$/i,
      }
    );

    await user.click(botonDesactivar);

    expect(cambiarEstadoUsuario).toHaveBeenCalledWith(
      5,
      false
    );
  });

  it("activa una cuenta inactiva al presionar Activar", async () => {
    const user = userEvent.setup();

    vi.mocked(obtenerUsuarios).mockResolvedValue([
      {
        id: 6,
        email: "secretaria@test.com",
        estado: false,
        rol: "SECRETARIA",
        persona: {
          dni: "87654321",
          nombres: "Ana",
          apellidos: "Secretaria",
        },
      },
    ]);

    vi.mocked(cambiarEstadoUsuario).mockResolvedValue({
      mensaje: "Estado actualizado correctamente",
    });

    render(
      <MemoryRouter>
        <UsuariosPage />
      </MemoryRouter>
    );

    const botonActivar = await screen.findByRole(
      "button",
      {
        name: /^activar$/i,
      }
    );

    await user.click(botonActivar);

    expect(cambiarEstadoUsuario).toHaveBeenCalledWith(
      6,
      true
    );
  });

});