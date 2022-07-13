from dataclasses import dataclass

from project.core.exceptions import ApplicationException


@dataclass
class UserAlreadyExistException(ApplicationException):
    code_status: int = 409
