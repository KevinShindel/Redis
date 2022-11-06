from config.common import DEFAULT_DAO_KEY_PREFIX


def prefixed_key(f):
    def prefixed_method(self, *args, **kwargs):
        key = f(self, *args, **kwargs)
        return '%s:%s' % (self.prefix, key)

    return prefixed_method


class KeySchema:

    def __init__(self, prefix: str = DEFAULT_DAO_KEY_PREFIX):
        self.prefix = prefix


class UserKeySchema(KeySchema):

    @prefixed_key
    def user_hash_key(self, user_id):
        return 'users:info:%s' % user_id

    @prefixed_key
    def user_ids_key(self):
        return 'users:ids'
