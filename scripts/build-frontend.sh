#!/usr/bin/env bash

set -ex

cd frontend
docker build -t webpi-frontend:latest --build-arg NODE_VERSION=$(<../.nvmrc) .
docker run -i webpi-frontend:latest > webpi-frontend.tar.gz
