import React, { Component } from "react";

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = { email: "", password: "" };

    this.onEmailChanged = this.onEmailChanged.bind(this);
    this.onPasswordChanged = this.onPasswordChanged.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  onEmailChanged(event) {
    this.setState({ email: event.target.value });
  }

  onPasswordChanged(event) {
    this.setState({ password: event.target.value });
  }

  async onSubmit(event) {
    try {
      const login_response = await fetch("/api/v1/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(this.state)
      });
      const login_data = await login_response.json();
      console.log(login_data);
    } catch (err) {
      console.log(err);
    }
  }

  render() {
    return (
      <div>
        <form
          className="pure-form pure-form-stacked"
          onSubmit={event => {
            this.onSubmit(event);
            event.preventDefault();
          }}
        >
          <fieldset>
            <input
              id="email"
              type="text"
              placeholder="Email"
              value={this.state.email}
              onChange={this.onEmailChanged}
            />
            <input
              id="password"
              type="password"
              placeholder="Password"
              value={this.state.password}
              onChange={this.onPasswordChanged}
            />
            <button
              id="log-in-button"
              type="submit"
              className="pure-button pure-button-primary"
            >
              Log in
            </button>
          </fieldset>
        </form>
      </div>
    );
  }
}

export default Login;
