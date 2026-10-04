import {
  beforeEach,
  describe,
  expect,
  it,
  vi
} from "vitest";

import {
  render,
  screen,
  waitFor
} from "@testing-library/react";

import userEvent from "@testing-library/user-event";

import {
  MemoryRouter,
  Route,
  Routes
} from "react-router-dom";

import {
  AuthProvider
} from "../../../context/AuthContext";

import EditarEstudiantePage
  from "./EditarEstudiantePage";

import {
  actualizarEstudiante,
  obtenerEstudiantes
} from "../../../services/secretariaService";


vi.mock(
  "../../../services/secretariaService",
  () => ({
    obtenerEstudiantes: vi.fn(),
    actualizarEstudiante: vi.fn(),
  })
);


const estudiantePrueba = {
  id: 1,
  codigo: "EST001",
  estado: true,
  persona: {
    dni: "80000001",
    nombres: "Pedro",
    apellidos: "Perez",
  },
};


function renderizarPagina() {

  return render(

    <MemoryRouter
      initialEntries={[
        "/secretaria/estudiantes/1/editar"
      ]}
    >

      <AuthProvider>

        <Routes>

          <Route
            path="/secretaria/estudiantes/:id/editar"
            element={
              <EditarEstudiantePage />
            }
          />

          <Route
            path="/secretaria/estudiantes"
            element={
              <div>
                Lista de estudiantes
              </div>
            }
          />

        </Routes>

      </AuthProvider>

    </MemoryRouter>

  );

}


describe(
  "EditarEstudiantePage - HU07",
  () => {

    beforeEach(() => {

      vi.clearAllMocks();

      vi.mocked(
        obtenerEstudiantes
      ).mockResolvedValue([
        estudiantePrueba
      ]);

    });


    it(
      "carga los datos actuales del estudiante",
      async () => {

        renderizarPagina();

        expect(
          await screen.findByDisplayValue(
            "EST001"
          )
        ).toBeInTheDocument();

        expect(
          screen.getByDisplayValue(
            "Pedro"
          )
        ).toBeInTheDocument();

        expect(
          screen.getByDisplayValue(
            "Perez"
          )
        ).toBeInTheDocument();

        expect(
          screen.getByDisplayValue(
            "80000001"
          )
        ).toBeInTheDocument();
      }
    );


    it(
      "mantiene el DNI deshabilitado durante la edicion",
      async () => {

        renderizarPagina();

        const dni =
          await screen.findByDisplayValue(
            "80000001"
          );

        expect(
          dni
        ).toBeDisabled();
      }
    );


    it(
      "envia los datos modificados del estudiante",
      async () => {

        const user =
          userEvent.setup();

        vi.mocked(
          actualizarEstudiante
        ).mockResolvedValue({
          mensaje:
            "Estudiante actualizado correctamente",
        });

        renderizarPagina();

        const nombres =
          await screen.findByDisplayValue(
            "Pedro"
          );

        await user.clear(
          nombres
        );

        await user.type(
          nombres,
          "Pedro Luis"
        );


        const botonGuardar =
          screen.getByRole(
            "button",
            {
              name:
                "Guardar cambios",
            }
          );

        await user.click(
          botonGuardar
        );


        await waitFor(() => {

          expect(
            actualizarEstudiante
          ).toHaveBeenCalledWith(
            1,
            {
              nombres:
                "Pedro Luis",
              apellidos:
                "Perez",
              student_code:
                "EST001",
            }
          );

        });

      }
    );


    it(
      "muestra el error cuando el codigo del estudiante ya existe",
      async () => {

        const user =
          userEvent.setup();

        vi.mocked(
          actualizarEstudiante
        ).mockRejectedValue({
          isAxiosError: true,
          response: {
            data: {
              mensaje:
                "El código del estudiante ya existe",
            },
          },
        });

        renderizarPagina();

        const codigo =
          await screen.findByDisplayValue(
            "EST001"
          );

        await user.clear(
          codigo
        );

        await user.type(
          codigo,
          "EST002"
        );

        await user.click(
          screen.getByRole(
            "button",
            {
              name:
                "Guardar cambios",
            }
          )
        );


        expect(
          await screen.findByText(
            "El código del estudiante ya existe"
          )
        ).toBeInTheDocument();

      }
    );

  }
);