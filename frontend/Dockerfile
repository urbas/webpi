ARG NODE_VERSION
ARG NPM_INSTALL_EXTRA_ARGS=""
FROM node:${NODE_VERSION}-slim

ADD *.json /
RUN npm ci --no-save --only=production && npm cache clean --force

ENV NODE_PATH=/node_modules
ENV PATH=/node_modules/.bin:$PATH
WORKDIR /sources
ADD . /sources
RUN npm run build

CMD tar -C build -c .