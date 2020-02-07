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
        self.id = email

    @property
    def email(self) -> str:
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
    if hash_password(password, salt) != base64.b64decode(user_record["password"]):
        return None

    user = User(email)
    login_user(user)
    return user


def hash_password(password: str, salt: bytes) -> bytes:
    return hashlib.scrypt(password.encode("utf-8"), salt=salt, n=2 ** 8, r=64, p=1)


def serialize_password(password: str) -> None:
    """
    prints the salted-hashed password as YAML so you can paste it directly into your configuration
    """
    salt = os.urandom(10)
    print(
        yaml.dump(
            {
                "password": base64.b64encode(hash_password(password, salt)).decode(),
                "salt": base64.b64encode(salt).decode(),
            },
            default_flow_style=False,
        )
    )
