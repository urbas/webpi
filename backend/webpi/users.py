import base64
import hashlib
import os
from typing import Optional
import yaml
from flask import current_app
from flask_login import UserMixin, login_user


class User(UserMixin):
    def __init__(self, email):
        super(User, self).__init__()
        # pylint: disable=invalid-name
        self.id = email

    @property
    def email(self) -> str:
        # pylint: disable=invalid-name
        return self.id


def user_loader(email: str) -> Optional[User]:
    return User(email) if email in current_app.config["users"] else None  # type: ignore


def auth_user(email: str, password: str) -> Optional[User]:
    users = current_app.config.get("users")
    if users is None:
        return None

    user_record = users.get(email)
    if user_record is None:
        return None

    salt = base64.b64decode(user_record["salt"])
    stored_hashed_password = base64.b64decode(user_record["password"])
    hashed_password = hashlib.scrypt(
        password.encode("utf-8"), salt=salt, n=2 ** 8, r=64, p=1
    )

    if hashed_password != stored_hashed_password:
        return None

    user = User(email)
    login_user(user)
    return user


def serialize_password(password):
    salt = os.urandom(10)
    print(
        yaml.dump(
            {
                "password": base64.b64encode(
                    hashlib.scrypt(
                        password.encode("utf-8"), salt=salt, n=2 ** 8, r=64, p=1
                    )
                ).decode(),
                "salt": base64.b64encode(salt).decode(),
            },
            default_flow_style=False,
        )
    )
