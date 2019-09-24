import React, { Component } from "react";

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = { email: "", password: "", loggedIn: false };
    this.onEmailChanged = this.onEmailChanged.bind(this);
    this.onPasswordChanged = this.onPasswordChanged.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  async componentDidMount() {
    try {
      const userResponse = await fetch("/api/v1/auth/user");
      this.setState({ loggedIn: userResponse.ok });
    } catch (err) {
      this.setState({ loggedIn: false });
    }
  }

  onEmailChanged(event) {
    this.setState({ email: event.target.value });
  }

  onPasswordChanged(event) {
    this.setState({ password: event.target.value });
  }

  async onSubmit(event) {
    try {
      const loginResponse = await fetch("/api/v1/auth/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          email: this.state.email,
          password: this.state.password
        })
      });
      this.setState({ loggedIn: loginResponse.ok });
    } catch (err) {
      this.setState({ loggedIn: false });
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
            <input id="isLoggedIn" type="hidden" value={this.state.loggedIn} />
            <button
              id="logInButton"
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
