ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}-slim

ENV SRC_DIR=/sources
WORKDIR ${SRC_DIR}
ADD requirements_dev.txt setup.py ${SRC_DIR}/
RUN pip install --no-cache-dir -e .
RUN pip install --no-cache-dir -r requirements_dev.txt

ADD . ${SRC_DIR}

CMD FLASK_ENV=development FLASK_APP=webpi/app.py flask run --host=0.0.0.0