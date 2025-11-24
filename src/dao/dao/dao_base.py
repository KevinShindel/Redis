from abc import ABC

from src.dao.model.model import UserModel


class UserDaoBase(ABC):

    def create(self, user: UserModel, *args, **kwargs):
        raise NotImplementedError

    def delete(self, user_id: int, *args, **kwargs):
        raise NotImplementedError

    def get(self, user_id: int, *args, **kwargs):
        raise NotImplementedError
