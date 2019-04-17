ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}-slim

ENV SRC_DIR=/sources
WORKDIR ${SRC_DIR}
ADD requirements_deployment.txt setup.py ${SRC_DIR}/
RUN pip install --no-cache-dir -e .
RUN pip install --no-cache-dir -r requirements_deployment.txt

ADD . ${SRC_DIR}

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "python", "-c", "import requests; r = requests.get(\"http://localhost:5000/api/v1/health\"); r.raise_for_status()" ]

CMD gunicorn -b 0.0.0.0:5000 -w 4 webpi.app:APP