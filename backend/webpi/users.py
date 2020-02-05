from typing import Optional
from flask import current_app
from flask_login import UserMixin


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
    return User(email) if email in current_app.config.users else None  # type: ignore
