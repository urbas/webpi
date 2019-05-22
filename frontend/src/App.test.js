import React from "react";
import { shallow } from "enzyme";
import App from "./App";

describe("<App>", function() {
  it("should contain welcome message", () => {
    const wrapper = shallow(<App />);
    expect(
      wrapper.contains(<h1 className="App-title">webpi</h1>)
    ).toEqual(true);
  });

  it("should contain the health message", () => {
    const wrapper = shallow(<App />);
    expect(
      wrapper.contains(<div>Health: false</div>)
    ).toEqual(true);
  });
});
