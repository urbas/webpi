#!/usr/bin/env bash

set -ex

NODE_VERSION=$(<.nvmrc) PYTHON_VERSION=$(<.python-version) docker-compose build --parallel
NODE_VERSION=$(<.nvmrc) PYTHON_VERSION=$(<.python-version) docker-compose run itests npm run itests