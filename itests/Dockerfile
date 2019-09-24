FROM cypress/browsers:chrome69

ADD *.json /
RUN npm ci --no-save && npm cache clean --force

ENV NODE_PATH=/node_modules
ENV PATH=/node_modules/.bin:$PATH
WORKDIR /sources
ADD . /sources

CMD npm run itests