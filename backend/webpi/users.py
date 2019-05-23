from flask import current_app
from flask_login import UserMixin


def user_loader(email):
    return User(email) if email in current_app.config.users else None


class User(UserMixin):
    def __init__(self, email):
        super(User, self).__init__()
        # pylint: disable=invalid-name
        self.id = email

    @property
    def email(self):
        # pylint: disable=invalid-name
        return self.id
