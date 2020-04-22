import unittest

from elasticsearch_dsl import Index

from app import app
from api.models.user import User


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        s = User.search()
        s.query('match', username='unittest1').delete()
        s.query('match', username='unittest2').delete()
        s.query('match', username='unittest3').delete()
        s.query('match', username='unittest4').delete()
        Index('users').flush()

    def test_register(self):
        response = self.app.post('/api/auth/register', json={'username': 'unittest1', 'password': '123456'})
        print(response.json)
        self.assertEqual(200, response.status_code)

    def test_repeated_register(self):
        self.app.post('/api/auth/register', json={'username': 'unittest2', 'password': '123456'})
        response = self.app.post('/api/auth/register', json={'username': 'unittest2', 'password': '123456'})
        self.assertEqual(422, response.status_code)

    def test_login(self):
        self.app.post('/api/auth/register', json={'username': 'unittest3', 'password': '123456'})
        response = self.app.post('/api/auth/login', json={'username': 'unittest3', 'password': '123456'})
        self.assertEqual(200, response.status_code)

    def test_retrieve(self):
        response = self.app.get('/api/beep/qXjUonEBD4ucMZjUMi1j')
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
