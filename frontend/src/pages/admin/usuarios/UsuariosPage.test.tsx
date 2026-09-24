import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import UsuariosPage from "./UsuariosPage";

describe("UsuariosPage - HU02 CA07", () => {
  it("muestra el estado actual de las cuentas", () => {
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

    render(<UsuariosPage usuarios={usuarios} />);

    expect(screen.getByText("María Directora")).toBeInTheDocument();
    expect(screen.getByText("directora@test.com")).toBeInTheDocument();
    expect(screen.getByText("Activo")).toBeInTheDocument();

    expect(screen.getByText("Juan Profesor")).toBeInTheDocument();
    expect(screen.getByText("docente@test.com")).toBeInTheDocument();
    expect(screen.getByText("Inactivo")).toBeInTheDocument();
  });
});