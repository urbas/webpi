import React from "react";
import { shallow } from "enzyme";
import Home from "./Home";

describe("<Home>", function() {
  it("should contain the health message", () => {
    expect(shallow(<Home />).contains("Health: ")).toEqual(true);
  });
});
