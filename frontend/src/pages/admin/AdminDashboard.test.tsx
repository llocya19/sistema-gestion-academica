import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import { MemoryRouter } from "react-router-dom";

import AdminDashboard from "./AdminDashboard";
import { AuthProvider } from "../../context/AuthContext";

describe("AdminDashboard", () => {
  it("muestra el acceso a la gestión de usuarios", () => {
    render(
      <MemoryRouter>
        <AuthProvider>
          <AdminDashboard />
        </AuthProvider>
      </MemoryRouter>
    );

    expect(
    screen.getByRole("link", {
        name: /^gestión de usuarios$/i,
    })
    ).toBeInTheDocument();
  });
});