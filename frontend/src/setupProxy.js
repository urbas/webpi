const proxy = require("http-proxy-middleware");

const backend_url = process.env.BACKEND_URL || "http://localhost:5000/";

module.exports = function(app) {
  app.use(proxy("/api", { target: backend_url }));
};
