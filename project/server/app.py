from fastapi import FastAPI, Request
from fastapi.responses import Response

from project.auth.delivery.controller import auth
from project.core.database import Base, engine
from project.core.exceptions import ApplicationException


Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.exception_handler(ApplicationException)
def app_exception_handler(request: Request, exc: ApplicationException):
    return Response(
        status_code=exc.code_status,
        content=exc.body
    )


app.include_router(auth)
