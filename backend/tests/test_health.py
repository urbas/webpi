from webpi.app import test_client


def test_healthy():
    healthy = test_client().get("/api/v1/health")
    # NB: Here we explicitly compare against True because we want this to be a boolean.
    # pylint: disable=singleton-comparison
    assert healthy.json["healthy"] == True
