import React, { Component } from "react";
import { BrowserRouter as Router, Route } from "react-router-dom";
import "purecss/build/pure.css";
import "./App.css";
import Home from "./Home.js"
import Login from "./Login.js"

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Route exact path="/" component={Home} />
          <Route path="/login" component={Login} />
        </div>
      </Router>
    );
  }
}

export default App;
