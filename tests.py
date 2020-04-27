import unittest

from elasticsearch_dsl import Index

from app import app
from api.models.user import User


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    @classmethod
    def tearDownClass(cls):
        s = User.search()
        resp = s.query('match', username='unittest1').delete()
        print(resp)
        s.query('match', username='unittest2').delete()
        s.query('match', username='unittest3').delete()

    def test_register(self):
        response = self.app.post('/api/auth/register', json={'username': 'unittest1', 'password': '123456'})
        Index('users').flush()
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

    def test_login_wrong_password(self):
        self.app.post('/api/auth/register', json={'username': 'unittest4', 'password': '123456'})
        response = self.app.post('/api/auth/login', json={'username': 'unittest4', 'password': '1234567'})
        self.assertEqual(401, response.status_code)

    def test_login_nonexistent_user(self):
        response = self.app.post('/api/auth/login', json={'username': 'unittest5', 'password': '123456'})
        self.assertEqual(401, response.status_code)

    def test_beep(self):
        self.app.post('/api/auth/register', json={'username': 'unittest6', 'password': '123456'})
        login_response = self.app.post('/api/auth/login', json={'username': 'unittest6', 'password': '123456'})
        beep_response = self.app.post('/api/beep', json={'text': 'Test beep'},
                                      headers={'Authorization': f'Bearer {login_response.json["token"]}'})
        self.assertEqual(200, beep_response.status_code)
        return beep_response

    def test_nonexistent_beep(self):
        response = self.app.get('/api/beep/nonexistentid')
        self.assertEqual(404, response.status_code)

    def test_retrieve(self):
        beep_response = self.test_beep()
        response = self.app.get(f'/api/beep/{beep_response.json["beep_id"]}')
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
