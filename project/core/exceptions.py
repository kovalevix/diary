from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel


@dataclass
class ApplicationException(Exception):
    body: BaseModel | Any
    code_status: int
