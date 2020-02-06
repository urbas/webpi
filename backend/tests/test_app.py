from webpi import app

TEST_CONFIG = {
    "secret_key": "foo bar",
    "users": {
        "foo@bar.com": {
            "password": "MaIWphuXxWHfTHSk0Bsk7Y/5If7V+ZzgDNZiKek4eKS3ucKn+GZwX0ZMxtYHCRC2"
            "tMiqQyGHFnL9JNQfiaEdIw==",
            "salt": "RRcyQZF51iM=",
        }
    },
}


def test_secret_key():  # pylint: disable=invalid-name
    """check that the secret key of the app is read from the configuration"""
    assert app.create_app(TEST_CONFIG).secret_key == TEST_CONFIG["secret_key"]
