import base64
import yaml
from webpi import users


def test_serialize_password(capsys):
    """check that the salt and password are placed in the dict correctly"""
    users.serialize_password("test1234")
    salted_password = yaml.safe_load(capsys.readouterr().out)
    assert base64.b64decode(salted_password["password"]) == users.hash_password(
        "test1234", base64.b64decode(salted_password["salt"])
    )
