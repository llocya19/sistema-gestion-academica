import { describe, expect, it } from "vitest";
import { render, screen } from "@testing-library/react";
import AdminDashboard from "./AdminDashboard";

describe("AdminDashboard", () => {
  it("muestra el acceso a la gestión de usuarios", () => {
    render(<AdminDashboard />);

    expect(
      screen.getByText(/gestión de usuarios/i)
    ).toBeInTheDocument();
  });
});