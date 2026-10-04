import {
  describe,
  expect,
  it,
  vi,
  beforeEach
} from "vitest";

import api from "../api/axiosConfig";

import {
  obtenerEstudiantes,
  crearEstudiante
} from "./secretariaService";


vi.mock("../api/axiosConfig", () => ({
  default: {
    get: vi.fn(),
    post: vi.fn(),
  },
}));


describe("secretariaService - HU07", () => {

  beforeEach(() => {
    vi.clearAllMocks();
  });


  it(
    "obtiene los estudiantes desde el backend",
    async () => {

      const estudiantes = [
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
      ];

      vi.mocked(api.get).mockResolvedValue({
        data: {
          estudiantes,
        },
      });

      const resultado =
        await obtenerEstudiantes();

      expect(api.get).toHaveBeenCalledWith(
        "/secretary/students"
      );

      expect(resultado).toEqual(estudiantes);
    }
  );


  it(
    "envia los datos para crear un estudiante",
    async () => {

      const nuevoEstudiante = {
        dni: "12345678",
        nombres: "Lupe",
        apellidos: "Guzman",
        student_code: "EST004",
        telefono: "999999999",
        direccion: "Chincha",
      };

      const respuestaBackend = {
        mensaje:
          "Estudiante creado correctamente",
      };

      vi.mocked(api.post).mockResolvedValue({
        data: respuestaBackend,
      });

      const resultado =
        await crearEstudiante(
          nuevoEstudiante
        );

      expect(api.post).toHaveBeenCalledWith(
        "/secretary/students",
        nuevoEstudiante
      );

      expect(resultado).toEqual(
        respuestaBackend
      );
    }
  );

});