from datetime import datetime

from elasticsearch_dsl import Document, Text, Search, Q, Date


class Beep(Document):
    text = Text()
    date = Date()
    username = Text()

    class Index:
        name = 'beeps'

    def save(self, **kwargs):
        # a dirty hack to get UTC+0 time from whatever timezone is set on the server
        self.date = datetime.utcfromtimestamp(datetime.now().timestamp())
        return super().save(**kwargs)
