describe("Health", () => {
  it("frontend should be able to query the backend", () => {
    cy.visit("/");
    cy.contains("Health: true");
  });
});
