import { describe, expect, it, vi } from "vitest";
import api from "../api/axiosConfig";
import { obtenerUsuarios } from "./adminService";

vi.mock("../api/axiosConfig", () => ({
  default: {
    get: vi.fn(),
  },
}));

describe("adminService - HU02", () => {
  it("obtiene las cuentas de usuario desde el backend", async () => {
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
    ];

    vi.mocked(api.get).mockResolvedValue({
      data: {
        usuarios,
      },
    });

    const resultado = await obtenerUsuarios();

    expect(api.get).toHaveBeenCalledWith("/admin/users");
    expect(resultado).toEqual(usuarios);
  });
});