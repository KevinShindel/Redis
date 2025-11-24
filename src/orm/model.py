from typing import Optional, List

from pydantic import PositiveInt
from redis_om import JsonModel, EmbeddedJsonModel, Field


class Address(EmbeddedJsonModel):
    country: str = Field(index=False)
    city: str = Field(index=False)
    zip_code: Optional[PositiveInt] = Field(index=False)


class User(JsonModel):

    username: str = Field(default='user', index=True)
    first_name: str = Field(default='John', index=True)
    last_name: str = Field(default='Doe', index=True)
    address: Address
    skills: Optional[List[str]] = Field(index=False)
    age: PositiveInt = Field(index=False)
