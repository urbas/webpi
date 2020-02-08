#!/usr/bin/env bash

set -ex

cd frontend
docker build -t webpi-frontend:latest --file dev.Dockerfile --build-arg NODE_VERSION=$(<../.nvmrc) .
docker run -e CI=true -i webpi-frontend:latest npm test -- --coverage
docker run -i webpi-frontend:latest npm run --silent check-fmt