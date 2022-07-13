from abc import ABC, abstractmethod

import sqlalchemy.exc
from sqlalchemy.orm import sessionmaker

from project.auth.models.entities import CustomUser
from project.auth.models.dto.registration import RegistrationResponse
from project.auth.exceptions import UserAlreadyExistException


class IUserRepository(ABC):
    @abstractmethod
    def create(self, user: CustomUser) -> RegistrationResponse:
        """

        :param user:
        :return:
        """


class UserRepository(IUserRepository):
    def __init__(self, db: sessionmaker):
        self.db: sessionmaker = db

    def create(self, user: CustomUser) -> bool:
        was_created = True
        with self.db() as session:
            session.add(user)
            try:
                session.commit()
            except sqlalchemy.exc.IntegrityError:
                was_created = False
                raise UserAlreadyExistException(body=None)
        return was_created
