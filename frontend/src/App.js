import React, { Component } from "react";
import logo from "./logo.svg";
import "./App.css";
import axios from "axios";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = { healthy: "" };
  }

  async componentDidMount() {
    try {
      const health_response = await axios.get("/api/v1/health");
      this.setState({ healthy: health_response.data.healthy });
    } catch (err) {
      console.log(err);
      this.setState({ healthy: false });
    }
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to webpi</h1>
        </header>
        <div>Health: {this.state.healthy.toString()}</div>
      </div>
    );
  }
}

export default App;
