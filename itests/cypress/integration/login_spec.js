describe("Login", () => {
  it("must successfully log in", () => {
    cy.visit("/login");
    cy.get("#email").type("foo@bar.com");
    cy.get("#password").type("test1234");
    cy.get("#log-in-button").click();
    cy.request("api/v1/auth/user").then(response => {
      expect(response.status).to.eq(200);
      expect(response.body).to.have.property("email", "foo@bar.com");
    });
  });
});
