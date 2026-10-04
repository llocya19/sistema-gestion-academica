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
  MemoryRouter
} from "react-router-dom";

import {
  AuthProvider
} from "../../../context/AuthContext";

import EstudiantesPage from "./EstudiantesPage";

import {
  obtenerEstudiantes,
  cambiarEstadoEstudiante
} from "../../../services/secretariaService";


vi.mock(
  "../../../services/secretariaService",
  () => ({
    obtenerEstudiantes: vi.fn(),
    crearEstudiante: vi.fn(),
    cambiarEstadoEstudiante: vi.fn(),
  })
);


const estudiantesPrueba = [
  {
    id: 1,
    codigo: "EST001",
    estado: true,
    persona: {
      dni: "80000001",
      nombres: "Pedro",
      apellidos: "Perez",
    },
  },
  {
    id: 2,
    codigo: "EST002",
    estado: true,
    persona: {
      dni: "80000002",
      nombres: "Lucia",
      apellidos: "Gomez",
    },
  },
  {
    id: 3,
    codigo: "EST003",
    estado: false,
    persona: {
      dni: "80000003",
      nombres: "Jose",
      apellidos: "Lopez",
    },
  },
];


function renderizarPagina() {

  return render(
    <MemoryRouter>
      <AuthProvider>
        <EstudiantesPage />
      </AuthProvider>
    </MemoryRouter>
  );

}


describe("EstudiantesPage - HU07", () => {

  beforeEach(() => {
    vi.clearAllMocks();
  });


  it(
    "carga y muestra los estudiantes registrados",
    async () => {

      vi.mocked(
        obtenerEstudiantes
      ).mockResolvedValue(
        estudiantesPrueba
      );

      renderizarPagina();

      expect(
        await screen.findByText("EST001")
      ).toBeInTheDocument();

      expect(
        screen.getByText("Pedro")
      ).toBeInTheDocument();

      expect(
        screen.getByText("EST002")
      ).toBeInTheDocument();

      expect(
        screen.getByText("Lucia")
      ).toBeInTheDocument();

      expect(
        screen.getByText("EST003")
      ).toBeInTheDocument();

      expect(
        screen.getByText("Jose")
      ).toBeInTheDocument();
    }
  );


  it(
    "filtra estudiantes por codigo",
    async () => {

      const user = userEvent.setup();

      vi.mocked(
        obtenerEstudiantes
      ).mockResolvedValue(
        estudiantesPrueba
      );

      renderizarPagina();

      await screen.findByText("EST001");

      const buscador =
        screen.getByRole("searchbox");

      await user.type(
        buscador,
        "EST002"
      );

      expect(
        screen.getByText("Lucia")
      ).toBeInTheDocument();

      expect(
        screen.queryByText("Pedro")
      ).not.toBeInTheDocument();

      expect(
        screen.queryByText("Jose")
      ).not.toBeInTheDocument();
    }
  );


  it(
    "filtra estudiantes por DNI",
    async () => {

      const user = userEvent.setup();

      vi.mocked(
        obtenerEstudiantes
      ).mockResolvedValue(
        estudiantesPrueba
      );

      renderizarPagina();

      await screen.findByText("EST001");

      await user.type(
        screen.getByRole("searchbox"),
        "80000003"
      );

      expect(
        screen.getByText("Jose")
      ).toBeInTheDocument();

      expect(
        screen.queryByText("Pedro")
      ).not.toBeInTheDocument();
    }
  );


  it(
    "filtra estudiantes por nombre",
    async () => {

      const user = userEvent.setup();

      vi.mocked(
        obtenerEstudiantes
      ).mockResolvedValue(
        estudiantesPrueba
      );

      renderizarPagina();

      await screen.findByText("EST001");

      await user.type(
        screen.getByRole("searchbox"),
        "Pedro Perez"
      );

      expect(
        screen.getByText("EST001")
      ).toBeInTheDocument();

      expect(
        screen.queryByText("EST002")
      ).not.toBeInTheDocument();
    }
  );


  it(
    "muestra un mensaje cuando la busqueda no tiene resultados",
    async () => {

      const user = userEvent.setup();

      vi.mocked(
        obtenerEstudiantes
      ).mockResolvedValue(
        estudiantesPrueba
      );

      renderizarPagina();

      await screen.findByText("EST001");

      await user.type(
        screen.getByRole("searchbox"),
        "NO-EXISTE"
      );

      expect(
        screen.getByText(
          "No se encontraron estudiantes."
        )
      ).toBeInTheDocument();
    }
  );


  it(
    "muestra el estado activo e inactivo de los estudiantes",
    async () => {

      vi.mocked(
        obtenerEstudiantes
      ).mockResolvedValue(
        estudiantesPrueba
      );

      renderizarPagina();

      await screen.findByText("EST001");

      expect(
        screen.getAllByText("Activo")
      ).toHaveLength(2);

      expect(
        screen.getByText("Inactivo")
      ).toBeInTheDocument();
    }
  );

    it(
    "ordena los estudiantes por codigo de menor a mayor",
    async () => {

      const estudiantesDesordenados = [
        estudiantesPrueba[2],
        estudiantesPrueba[0],
        estudiantesPrueba[1],
      ];

      vi.mocked(
        obtenerEstudiantes
      ).mockResolvedValue(
        estudiantesDesordenados
      );

      renderizarPagina();

      await screen.findByText("EST001");

      const codigos =
        screen
          .getAllByText(/EST00[1-3]/)
          .map(
            (elemento) =>
              elemento.textContent
          );

      expect(codigos).toEqual([
        "EST001",
        "EST002",
        "EST003",
      ]);
    }
  );


  it(
    "desactiva un estudiante",
    async () => {

      const user =
        userEvent.setup();

      vi.mocked(
        obtenerEstudiantes
      ).mockResolvedValue(
        estudiantesPrueba
      );

      vi.mocked(
        cambiarEstadoEstudiante
      ).mockResolvedValue({
        mensaje:
          "Estado actualizado correctamente",
      });

      vi.spyOn(
        window,
        "confirm"
      ).mockReturnValue(true);

      renderizarPagina();

      await screen.findByText("EST001");

      const botonesDesactivar =
        screen.getAllByRole(
          "button",
          {
            name: "Desactivar",
          }
        );

      await user.click(
        botonesDesactivar[0]
      );

      await waitFor(() => {

        expect(
          cambiarEstadoEstudiante
        ).toHaveBeenCalledWith(
          1,
          false
        );

      });

      expect(
        screen.getAllByText("Inactivo")
      ).toHaveLength(2);
    }
  );


  it(
    "activa un estudiante inactivo",
    async () => {

      const user =
        userEvent.setup();

      vi.mocked(
        obtenerEstudiantes
      ).mockResolvedValue(
        estudiantesPrueba
      );

      vi.mocked(
        cambiarEstadoEstudiante
      ).mockResolvedValue({
        mensaje:
          "Estado actualizado correctamente",
      });

      vi.spyOn(
        window,
        "confirm"
      ).mockReturnValue(true);

      renderizarPagina();

      await screen.findByText("EST003");

      const botonActivar =
        screen.getByRole(
          "button",
          {
            name: "Activar",
          }
        );

      await user.click(
        botonActivar
      );

      await waitFor(() => {

        expect(
          cambiarEstadoEstudiante
        ).toHaveBeenCalledWith(
          3,
          true
        );

      });

      expect(
        screen.getAllByText("Activo")
      ).toHaveLength(3);
    }
  );

});