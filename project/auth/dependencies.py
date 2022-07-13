from functools import cache

from project.auth.repository.user import UserRepository
from project.auth.services.tokens import TokenService
from project.auth.use_case import AuthUseCase
from project.core.database import session_factory


def get_user_repository() -> UserRepository:
    repository = UserRepository(session_factory)
    return repository


def get_token_service() -> TokenService:
    service = TokenService()
    return service


@cache
def get_auth_depend() -> AuthUseCase:
    user_repo = get_user_repository()
    token_service = get_token_service()
    return AuthUseCase(user_repo, token_service)
