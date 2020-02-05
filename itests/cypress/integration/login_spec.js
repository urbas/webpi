describe("Login", () => {
  it("must successfully log in and log out", () => {
    cy.visit("/login");
    cy.get("#isLoggedIn").should(isLoggedInField => {
      expect(isLoggedInField.val()).to.eq('false');
    });
    cy.get("#email").type("foo@bar.com");
    cy.get("#password").type("test1234");
    cy.get("#logInButton").click();
    cy.get("#isLoggedIn").should(isLoggedInField => {
      expect(isLoggedInField.val()).to.eq('true');
    });
    cy.request("api/v1/auth/user").then(response => {
      expect(response.status).to.eq(200);
      expect(response.body).to.have.property("email", "foo@bar.com");
    });
    cy.request("POST", "api/v1/auth/logout");
    cy.request({url: "api/v1/auth/user", failOnStatusCode: false}).then(response => {
      expect(response.status).to.eq(401);
    });
  });
});
