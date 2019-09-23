import React, { Component } from "react";

class Login extends Component {
  render() {
    return (
      <div>
        <form className="pure-form pure-form-stacked">
            <fieldset>
                <input id="username" type="text" placeholder="Username"/>
                <input id="password" type="password" placeholder="Password"/>
                <button id="log-in-button" type="submit" className="pure-button pure-button-primary">Log in</button>
            </fieldset>
        </form>
      </div>
    );
  }
}

export default Login;
