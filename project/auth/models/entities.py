from uuid import uuid4

from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from project.core.database import Base


class CustomUser(Base):
    __tablename__: str = "CustomUser"

    id: Column = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name: Column = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
