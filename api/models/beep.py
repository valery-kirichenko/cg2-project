from datetime import datetime

from elasticsearch_dsl import Document, Text, Date


class Beep(Document):
    text = Text()
    date = Date()
    username = Text()

    class Index:
        name = 'beeps'

    @classmethod
    def find_by_field(cls, field, value):
        s = cls.search()
        s = s.query('match', **{field: value})
        r = s.execute()
        return r

    def save(self, **kwargs):
        # a dirty hack to get UTC+0 time from whatever timezone is set on the server
        self.date = datetime.utcfromtimestamp(datetime.now().timestamp())
        return super().save(**kwargs)
