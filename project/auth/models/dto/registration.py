from pydantic import BaseModel


class RegistrationRequest(BaseModel):
    name: str
    email: str
    password: str


class RegistrationResponse(BaseModel):
    email: str
