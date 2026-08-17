from pydantic import PositiveInt
from redis_om import EmbeddedJsonModel, Field, JsonModel


class Address(EmbeddedJsonModel):
    country: str = Field(index=False)
    city: str = Field(index=False)
    zip_code: PositiveInt | None = Field(index=False)


class User(JsonModel):

    username: str = Field(default="user", index=True)
    first_name: str = Field(default="John", index=True)
    last_name: str = Field(default="Doe", index=True)
    address: Address
    skills: list[str] | None = Field(index=False)
    age: PositiveInt = Field(index=False)
