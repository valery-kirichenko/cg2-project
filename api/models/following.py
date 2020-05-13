from elasticsearch_dsl import Document, Text, Q
from .user import User


class Following(Document):
    user_from = Text()
    user_to = Text()

    class Index:
        name = 'followings'

    @classmethod
    def is_following(cls, user_from, user_to):
        s = cls.search()
        s = s.query(Q('bool', must=[Q('match', user_to=user_to), Q('match', user_from=user_from)]))
        r = s.execute()
        return r.hits.total.value > 0

    @classmethod
    def get_followings(cls, username):
        s = cls.search().query('match', user_from=username)
        return [hit.user_to for hit in s.scan()]

    @classmethod
    def find(cls, user_from, user_to):
        s = cls.search()
        s = s.query(Q('bool', must=[Q('match', user_to=user_to), Q('match', user_from=user_from)]))
        r = s.execute()
        return r

    def save(self, **kwargs):
        r1 = User.find_by_field('username', self.user_to)
        r2 = User.find_by_field('username', self.user_from)
        if r1.hits.total.value == 0 or r2.hits.total.value == 0:
            raise ValueError('User does not exist')
        if self.user_from == self.user_to:
            raise ValueError('User cannot follow himself')
        if self.is_following(self.user_from, self.user_to):
            raise ValueError('Already following')

        return super(Following, self).save(**kwargs)
