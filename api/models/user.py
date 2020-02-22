from elasticsearch_dsl import Document, Integer, Text
from argon2 import PasswordHasher


hasher = PasswordHasher()


class User(Document):
    username = Text()
    hashed_password = Text()
    access_level = Integer()

    class Index:
        name = 'users'

    def hash_password(self, password):
        self.hashed_password = hasher.hash(password)

    def verify_password(self, password):
        return hasher.verify(self.hashed_password, password)

    @classmethod
    def find_by_field(cls, field, value):
        s = cls.search()
        s = s.query('match', **{field: value})
        r = s.execute()
        return r

    def save(self, **kwargs):
        r = self.find_by_field('username', self.username)
        if r.hits.total.value > 0 and 'id' not in self.meta:
            raise ValueError('User already exists')

        return super(User, self).save(**kwargs)
