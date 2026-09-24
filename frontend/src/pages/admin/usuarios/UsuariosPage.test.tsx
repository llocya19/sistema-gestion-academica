import { describe, expect, it, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import UsuariosPage from "./UsuariosPage";
import { obtenerUsuarios } from "../../../services/adminService";

vi.mock("../../../services/adminService", () => ({
  obtenerUsuarios: vi.fn(),
}));

describe("UsuariosPage - HU02 CA07", () => {
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

    render(<UsuariosPage />);

    await waitFor(() => {
      expect(obtenerUsuarios).toHaveBeenCalledTimes(1);
    });

    expect(screen.getByText("María Directora")).toBeInTheDocument();
    expect(screen.getByText("directora@test.com")).toBeInTheDocument();
    expect(screen.getByText("DIRECTORA")).toBeInTheDocument();
    expect(screen.getByText("Activo")).toBeInTheDocument();

    expect(screen.getByText("Juan Profesor")).toBeInTheDocument();
    expect(screen.getByText("docente@test.com")).toBeInTheDocument();
    expect(screen.getByText("DOCENTE")).toBeInTheDocument();
    expect(screen.getByText("Inactivo")).toBeInTheDocument();
  });
});