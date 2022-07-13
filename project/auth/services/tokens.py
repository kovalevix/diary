from abc import ABC, abstractmethod


class ITokenService(ABC):
    @abstractmethod
    def verify(self):
        """

        :return:
        """


class TokenService(ITokenService):
    def verify(self):
        pass
