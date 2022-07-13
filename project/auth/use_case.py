from abc import ABC, abstractmethod

from project.auth.models.dto.login import LoginRequest
from project.auth.models.dto.registration import RegistrationRequest, RegistrationResponse
from project.auth.models.entities import CustomUser
from project.auth.repository.user import IUserRepository
from project.auth.services.tokens import ITokenService


class IAuthUseCase(ABC):
    @abstractmethod
    async def registration(self, request: RegistrationRequest) -> RegistrationResponse:
        """
        :param request:
        :return:
        """

    async def login(self, request: LoginRequest):
        """

        :param request:
        :return:
        """


class AuthUseCase(IAuthUseCase):
    def __init__(self, repository: IUserRepository, token: ITokenService):
        self.repository = repository
        self.token = token

    async def registration(self, request: RegistrationRequest) -> RegistrationResponse:
        user = CustomUser(
            name=request.name, password=request.password, email=request.email
        )
        was_created = self.repository.create(user)
        return RegistrationResponse(email=request.email)

    async def login(self, request: LoginRequest):
        pass
