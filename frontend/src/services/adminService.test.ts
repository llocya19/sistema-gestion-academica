import { describe, expect, it, vi } from "vitest";
import api from "../api/axiosConfig";
import {
  obtenerUsuarios,
  crearUsuario,
  obtenerRoles
} from "./adminService";

vi.mock("../api/axiosConfig", () => ({
  default: {
    get: vi.fn(),
    post: vi.fn(),
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


  it("crea una cuenta de usuario desde el backend", async () => {
    const nuevoUsuario = {
      dni: "12345678",
      nombres: "Pedro",
      apellidos: "García",
      email: "pedro@test.com",
      password: "123456",
      role_id: 4,
    };

    const respuestaBackend = {
      mensaje: "Usuario creado correctamente",
    };

    vi.mocked(api.post).mockResolvedValue({
      data: respuestaBackend,
    });

    const resultado = await crearUsuario(nuevoUsuario);

    expect(api.post).toHaveBeenCalledWith(
      "/admin/users",
      nuevoUsuario
    );

    expect(resultado).toEqual(respuestaBackend);
  });

  it("obtiene los roles disponibles desde el backend", async () => {
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
  ];

  vi.mocked(api.get).mockResolvedValue({
    data: {
      roles,
    },
  });

  const resultado = await obtenerRoles();

  expect(api.get).toHaveBeenCalledWith("/admin/roles");
  expect(resultado).toEqual(roles);
});

});