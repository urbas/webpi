import React, { Component } from "react";

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = { healthy: false };
  }

  async componentDidMount() {
    try {
      const health_response = await fetch("/api/v1/health");
      const health_data = await health_response.json();
      this.setState({ healthy: health_data.healthy });
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
