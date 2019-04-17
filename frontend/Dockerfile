ARG NODE_VERSION
FROM node:${NODE_VERSION}-slim

ADD *.json /
RUN npm install --no-save && npm cache clean --force

ENV NODE_PATH=/node_modules
ENV PATH=/node_modules/.bin:$PATH
WORKDIR /sources
ADD . /sources

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "node", "-e", "http = require(\"http\"); r = http.get(\"http://localhost:3000/\", (res) => { if (res.statusCode != 200) {throw \"Frontend not healthy.\"}})" ]

ENV BACKEND_HOST=backend

CMD BACKEND_URL=http://${BACKEND_HOST}:5000 npm start