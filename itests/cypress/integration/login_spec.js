describe("Login", () => {
  it("login screen should contain username and password fields", () => {
    cy.visit("/login");
    cy.get("#username")
      .type("foo@bar.com")
      .should("have.value", "foo@bar.com");
    cy.get("#password")
      .type("test1234")
      .should("have.value", "test1234");
    cy.get("#log-in-button").click();
  });
});
