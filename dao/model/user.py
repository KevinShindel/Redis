from redis_dao.core.dao_redis import RedisDaoBase
from redis_dao.dao.dao_base import UserDaoBase
from redis_dao.model.model import UserModel


class UserDaoRedis(UserDaoBase, RedisDaoBase):

    def create(self, user: UserModel, *args, **kwargs):
        hash_key = self.key_schema.user_hash_key(user_id=user.id)
        client = kwargs.get('pipeline', self.redis)
        client.hset(name=hash_key, mapping=user.dump())
        # client.hset(name=hash_key, mapping=FlatSiteSchema().dump(user))
        user_ids_key = self.key_schema.user_ids_key()
        return bool(client.sadd(user_ids_key, user.id))

    def delete(self, user_id: int, *args, **kwargs):
        hash_key = self.key_schema.user_hash_key(user_id=user_id)
        client = kwargs.get('pipeline', self.redis)
        client.hdel(name=hash_key)
        user_ids_key = self.key_schema.user_ids_key()
        return bool(client.srem(user_ids_key, user_id))

    def get(self,  user_id: int, *args, **kwargs):
        hash_key = self.key_schema.user_hash_key(user_id=user_id)
        client = kwargs.get('pipeline', self.redis)
        instance = client.hgetall(name=hash_key)
        return UserModel.load(**instance)
