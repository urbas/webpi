import React from "react";
import { shallow } from "enzyme";
import App from "./App";

describe("<App>", function() {
  it("should contain welcome message", () => {
    const wrapper = shallow(<App />);
    expect(
      wrapper.contains(<h1 className="App-title">Welcome to webpi</h1>)
    ).toEqual(true);
  });
});
