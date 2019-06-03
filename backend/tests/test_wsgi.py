from flask import Flask
from webpi.wsgi import APP


def test_wsgi_app():
    print("hello")
    assert isinstance(APP, Flask)
