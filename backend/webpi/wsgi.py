import os
import yaml
from webpi import app


def create_wsgi_app():
    if "WEBPI_CONFIG" not in os.environ:
        return app.create_app()
    with open(os.environ["WEBPI_CONFIG"]) as config_file:
        return app.create_app(yaml.safe_load(config_file))


APP = create_wsgi_app()
