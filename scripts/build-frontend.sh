#!/usr/bin/env bash

set -ex

cd frontend
sudo docker build -t webpi-frontend:latest --build-arg NODE_VERSION=$(<../.nvmrc) .
sudo docker run -i webpi-frontend:latest > webpi-frontend.tar.gz
