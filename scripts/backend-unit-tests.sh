#!/usr/bin/env bash

set -ex

cd backend
docker build -t webpi-backend:latest --file dev.Dockerfile --build-arg PYTHON_VERSION=$(<../.python-version) .
docker run -i webpi-backend:latest black --check webpi tests
docker run -i webpi-backend:latest flake8 webpi tests
docker run -i webpi-backend:latest mypy webpi tests
docker run -i webpi-backend:latest pytest
