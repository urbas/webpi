#!/usr/bin/env bash

set -e

test -n "$TWINE_PASSWORD" || (echo "TWINE_PASSWORD env var needed" && exit 1)

SRC_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." >/dev/null 2>&1 && pwd )"

LATEST_RELEASE_TAG=$(git describe --tags '--match=v*' --abbrev=0)

cd $SRC_DIR/backend

docker build -t webpi-backend:latest --build-arg PYTHON_VERSION=$(cat ../.python-version) .
docker run --env=WEBPI_VERSION=${LATEST_RELEASE_TAG#v} webpi-backend:latest bash -c "pip install --user --upgrade setuptools wheel twine && python setup.py sdist bdist_wheel && python -m twine upload --non-interactive -u __token__ -p $TWINE_PASSWORD --skip-existing $* dist/*"