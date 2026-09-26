import { render, screen, fireEvent, waitFor } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";
import { describe, it, expect, vi } from "vitest";

import Login from "./Login";
import * as authService from "../../services/authService";
import { AxiosError } from "axios";


vi.mock("../../services/authService");

vi.mock("../../context/AuthContext", () => ({
  useAuth: () => ({
    iniciarSesion: vi.fn(),
  }),
}));


describe("Login", () => {

  it("muestra un mensaje específico cuando el usuario está desactivado", async () => {

    const axiosError = new AxiosError(
    "Request failed with status code 403",
    "ERR_BAD_REQUEST",
    undefined,
    undefined,
    {
        data: {
        mensaje: "Usuario desactivado",
        },
        status: 403,
        statusText: "Forbidden",
        headers: {},
        config: {} as any,
    }
    );

    vi.mocked(authService.login).mockRejectedValue(axiosError);

    render(
      <MemoryRouter>
        <Login />
      </MemoryRouter>
    );

    fireEvent.change(
      screen.getByLabelText("Correo electrónico"),
      {
        target: {
          value: "docente@prueba.com",
        },
      }
    );

    fireEvent.change(
      screen.getByLabelText("Contraseña"),
      {
        target: {
          value: "123456",
        },
      }
    );

    fireEvent.click(
      screen.getByRole("button", {
        name: "Ingresar",
      })
    );

    await waitFor(() => {
      expect(
        screen.getByText(
          "Tu cuenta se encuentra desactivada. Contacta con el administrador."
        )
      ).toBeInTheDocument();
    });

  });

  it("muestra un mensaje de error cuando las credenciales son incorrectas", async () => {

    const axiosError = new AxiosError(
        "Request failed with status code 403",
        "ERR_BAD_REQUEST",
        undefined,
        undefined,
        {
        data: {
            mensaje: "Contraseña incorrecta",
        },
        status: 403,
        statusText: "Forbidden",
        headers: {},
        config: {} as any,
        }
    );

    vi.mocked(authService.login).mockRejectedValue(axiosError);

    render(
        <MemoryRouter>
        <Login />
        </MemoryRouter>
    );

    fireEvent.change(
        screen.getByLabelText("Correo electrónico"),
        {
        target: {
            value: "docente@prueba.com",
        },
        }
    );

    fireEvent.change(
        screen.getByLabelText("Contraseña"),
        {
        target: {
            value: "incorrecta",
        },
        }
    );

    fireEvent.click(
        screen.getByRole("button", {
        name: "Ingresar",
        })
    );

    await waitFor(() => {
        expect(
        screen.getByText(
            "Correo electrónico o contraseña incorrectos."
        )
        ).toBeInTheDocument();
    });

    });

});