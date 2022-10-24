import typing
from dataclasses import dataclass, field, asdict

from pydantic import PositiveInt


@dataclass(frozen=True, eq=True)
class Address:
    zip_code: PositiveInt = field()
    country: str = field()
    city: str = field()


@dataclass(frozen=True, eq=True)
class UserModel:
    id: int = field(default=None)
    username: str = field(default='username')
    first_name: str = field(default='John')
    last_name: str = field(default='Doe')
    # address: typing.Optional[Address] = field(default_factory={})

    def dump(self):
        return asdict(self)

    @classmethod
    def load(cls, **kwargs):
        return cls(**kwargs)
