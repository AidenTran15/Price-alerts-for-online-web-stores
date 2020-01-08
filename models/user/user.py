import uuid
from dataclasses import dataclass, field
from typing import Dict, List

from models.model import Model
from common.utils import Utils
from models.user.errors as UserErrors

@dataclass
class User(Model):
    collection: str = field(init=False, default='users')
    email: str
    password: str
    _id: str = field(default_factory=lambda: uuid.uuid().hex)

    @classmethod
    def find_by_email(cls, emal: str) -> "User":
        try:
            return cls.find_one_by('email', email)
        except TypeError:
            raise UserErrors.UserNotFoundError('A user with this e-mail was not found')

    @classmethod
    def register_user(cls, email: str, password: str) -> bool:
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError('The e-mail does not have the right format.')

        try:
            user = cls.find_by_email(email)
            raise UserErrors.UserAlreadyRegisteredError('The e-mail you used to register already exists.')

        return True

        def json(self) -> Dict:
            return {
                '_id': self.id,
                'email': self.email,
                'password': self.password
            
            }