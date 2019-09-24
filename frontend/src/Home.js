import React, { Component } from "react";

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = { healthy: false };
  }

  async componentDidMount() {
    try {
      const healthResponse = await fetch("/api/v1/health");
      const healthData = await healthResponse.json();
      this.setState({ healthy: healthData.healthy });
    } catch (err) {
      console.log(err);
      this.setState({ healthy: false });
    }
  }

  render() {
    return <div>Health: {this.state.healthy.toString()}</div>;
  }
}

export default Home;
