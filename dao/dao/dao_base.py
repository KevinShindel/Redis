from abc import ABC

from redis_dao.model.model import UserModel


class UserDaoBase(ABC):

    def create(self, user: UserModel, *args, **kwargs):
        raise NotImplemented

    def delete(self, user_id: int, *args, **kwargs):
        raise NotImplemented

    def get(self,  user_id: int, *args, **kwargs):
        raise NotImplemented

