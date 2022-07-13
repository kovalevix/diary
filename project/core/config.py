from functools import cache

from pydantic import BaseSettings


class DBSettings(BaseSettings):
    username: str
    password: str
    database: str
    host: str
    port: str

    class Config:
        env_prefix = "DB_"
        env_file = ".env"


@cache
def get_db_settings() -> DBSettings:
    return DBSettings()
