from typing import Optional
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

    if password != user_record.get("password"):
        return None

    user = User(email)
    login_user(user)
    return user
