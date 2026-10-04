import {
  beforeEach,
  describe,
  expect,
  it,
  vi
} from "vitest";

import {
  render,
  screen
} from "@testing-library/react";

import userEvent from "@testing-library/user-event";

import {
  MemoryRouter
} from "react-router-dom";

import axios from "axios";

import {
  AuthProvider
} from "../../../context/AuthContext";

import NuevoEstudiantePage
  from "./NuevoEstudiantePage";

import {
  crearEstudiante
} from "../../../services/secretariaService";


vi.mock(
  "../../../services/secretariaService",
  () => ({
    obtenerEstudiantes: vi.fn(),
    crearEstudiante: vi.fn(),
  })
);


vi.mock("axios", () => ({
  default: {
    isAxiosError: vi.fn(),
  },
}));


function renderizarPagina() {

  return render(
    <MemoryRouter>
      <AuthProvider>
        <NuevoEstudiantePage />
      </AuthProvider>
    </MemoryRouter>
  );

}


async function completarFormulario() {

  const user = userEvent.setup();

  await user.type(
    screen.getByLabelText(/dni/i),
    "12345678"
  );

  await user.type(
    screen.getByLabelText(
      /código de estudiante/i
    ),
    "EST004"
  );

  await user.type(
    screen.getByLabelText(/nombres/i),
    "Lupe"
  );

  await user.type(
    screen.getByLabelText(/apellidos/i),
    "Guzman"
  );

  return user;

}


describe(
  "NuevoEstudiantePage - HU07",
  () => {

    beforeEach(() => {

      vi.clearAllMocks();

      vi.mocked(
        axios.isAxiosError
      ).mockReturnValue(true);

    });


    it(
      "muestra el formulario para registrar un estudiante",
      () => {

        renderizarPagina();

        expect(
          screen.getByRole("heading", {
            name: /registrar estudiante/i,
          })
        ).toBeInTheDocument();

        expect(
          screen.getByLabelText(/dni/i)
        ).toBeInTheDocument();

        expect(
          screen.getByLabelText(
            /código de estudiante/i
          )
        ).toBeInTheDocument();

        expect(
          screen.getByLabelText(/nombres/i)
        ).toBeInTheDocument();

        expect(
          screen.getByLabelText(/apellidos/i)
        ).toBeInTheDocument();

        expect(
          screen.getByLabelText(/teléfono/i)
        ).toBeInTheDocument();

        expect(
          screen.getByLabelText(/dirección/i)
        ).toBeInTheDocument();
      }
    );


    it(
      "envia los datos para registrar un estudiante",
      async () => {

        vi.mocked(
          crearEstudiante
        ).mockResolvedValue({
          mensaje:
            "Estudiante creado correctamente",
        });

        renderizarPagina();

        const user =
          await completarFormulario();

        await user.click(
          screen.getByRole("button", {
            name: /registrar estudiante/i,
          })
        );

        expect(
          crearEstudiante
        ).toHaveBeenCalledWith({
          dni: "12345678",
          nombres: "Lupe",
          apellidos: "Guzman",
          student_code: "EST004",
          telefono: "",
          direccion: "",
        });
      }
    );


    it(
      "muestra un error cuando el DNI ya esta registrado",
      async () => {

        vi.mocked(
          crearEstudiante
        ).mockRejectedValue({
          response: {
            data: {
              mensaje:
                "El DNI ya está registrado",
            },
          },
        });

        renderizarPagina();

        const user =
          await completarFormulario();

        await user.click(
          screen.getByRole("button", {
            name: /registrar estudiante/i,
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
      "muestra un error cuando el codigo del estudiante ya existe",
      async () => {

        vi.mocked(
          crearEstudiante
        ).mockRejectedValue({
          response: {
            data: {
              mensaje:
                "El código del estudiante ya existe",
            },
          },
        });

        renderizarPagina();

        const user =
          await completarFormulario();

        await user.click(
          screen.getByRole("button", {
            name: /registrar estudiante/i,
          })
        );

        expect(
          await screen.findByText(
            "El código del estudiante ya existe"
          )
        ).toBeInTheDocument();
      }
    );


    it(
      "configura los campos obligatorios y valida el DNI",
      () => {

        renderizarPagina();

        const dni =
          screen.getByLabelText(/dni/i);

        const codigo =
          screen.getByLabelText(
            /código de estudiante/i
          );

        const nombres =
          screen.getByLabelText(/nombres/i);

        const apellidos =
          screen.getByLabelText(/apellidos/i);

        const telefono =
          screen.getByLabelText(/teléfono/i);

        const direccion =
          screen.getByLabelText(/dirección/i);

        expect(dni).toBeRequired();
        expect(codigo).toBeRequired();
        expect(nombres).toBeRequired();
        expect(apellidos).toBeRequired();

        expect(telefono).not.toBeRequired();
        expect(direccion).not.toBeRequired();

        expect(dni).toHaveAttribute(
          "maxlength",
          "8"
        );

        expect(dni).toHaveAttribute(
          "pattern",
          "[0-9]{8}"
        );

        expect(dni).toHaveAttribute(
          "inputmode",
          "numeric"
        );
      }
    );

  }
);