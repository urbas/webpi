from json import dumps

from webpi.app import test_client

TEST_USERS = {"foo@bar.com": {"password": "mystery"}}


def test_login_logout():
    with test_client(users=TEST_USERS) as client:
        login_response = client.post(
            "/api/v1/auth/login",
            data=dumps({"email": "foo@bar.com", "password": "mystery"}),
            content_type="application/json",
        )
        assert login_response.status_code == 200

        user_response = client.get("/api/v1/auth/user")
        assert user_response.status_code == 200
        assert user_response.json == {"email": "foo@bar.com"}

        logout_response = client.post("/api/v1/auth/logout")
        assert logout_response.status_code == 200

        user_response = client.get("/api/v1/auth/user")
        assert user_response.status_code == 401


def test_login_invalid():
    assert test_client().post("/api/v1/auth/login").status_code == 400


def test_wrong_password():
    with test_client(users=TEST_USERS) as client:
        login_response = client.post(
            "/api/v1/auth/login",
            data=dumps({"email": "foo@bar.com", "password": "wrong"}),
            content_type="application/json",
        )
        assert login_response.status_code == 400

        user_response = client.get("/api/v1/auth/user")
        assert user_response.status_code == 401


def test_wrong_user():
    with test_client(users=TEST_USERS) as client:
        login_response = client.post(
            "/api/v1/auth/login",
            data=dumps({"email": "wrong@email.com", "password": "mystery"}),
            content_type="application/json",
        )
        assert login_response.status_code == 400

        user_response = client.get("/api/v1/auth/user")
        assert user_response.status_code == 401


def test_missing_password():
    with test_client(users=TEST_USERS) as client:
        login_response = client.post(
            "/api/v1/auth/login",
            data=dumps({"email": "foo@bar.com"}),
            content_type="application/json",
        )
        assert login_response.status_code == 400

        user_response = client.get("/api/v1/auth/user")
        assert user_response.status_code == 401


def test_missing_email():
    with test_client(users=TEST_USERS) as client:
        login_response = client.post(
            "/api/v1/auth/login",
            data=dumps({"password": "mystery"}),
            content_type="application/json",
        )
        assert login_response.status_code == 400

        user_response = client.get("/api/v1/auth/user")
        assert user_response.status_code == 401
