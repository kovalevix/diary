from fastapi import APIRouter, Depends

from project.auth.dependencies import get_auth_depend
from project.auth.models.dto.login import LoginRequest
from project.auth.models.dto.registration import RegistrationRequest
from project.auth.use_case import IAuthUseCase

auth = APIRouter()


@auth.post("/registration")
async def registration(request: RegistrationRequest, use_case: IAuthUseCase = Depends(get_auth_depend)):
    return await use_case.registration(request)


@auth.post("/login")
async def login(request: LoginRequest, use_case: IAuthUseCase = Depends(get_auth_depend)):
    return await use_case.login(request)
