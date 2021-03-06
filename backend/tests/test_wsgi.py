import yaml
from flask import Flask
from webpi import wsgi
from tests import test_app


def test_wsgi_app():
    assert isinstance(wsgi.APP, Flask)


def test_conf_file(fs, monkeypatch):
    fs.create_file(
        "/etc/webpi/config.yaml", contents=yaml.dump(test_app.TEST_CONFIG),
    )
    monkeypatch.setenv("WEBPI_CONFIG", "/etc/webpi/config.yaml")
    app = wsgi.create_wsgi_app()
    assert test_app.TEST_CONFIG["users"] == app.config["users"]
