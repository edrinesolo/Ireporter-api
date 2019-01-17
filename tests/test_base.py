from app import app
import unittest
import json
import datetime


class TestsStart(unittest.TestCase):

    def setUp(self):

        self.app = app.test_client()

    def test_if_can_get_users(self):
        response = self.app.get('/api/v1/users')
        self.assertEqual(response.status_code, 200)

    def test_if_can_get_welcome(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_if_can_get_redflags(self):
        response = self.app.get('/api/v1/redflags')
        self.assertEqual(response.status_code, 200)

    def test_redflag_not_json(self):
        """ Test redflag content to be posted not in json format """
        expectedreq = {
            "id": "1",
            "created_on": "22hrs",
            "created_by": "1",
            "type": "intervene",
            "location": "kampala",
            "status": "pending",
            "image": "image",
            "video": "video",
            "comment": "invesitgation on going"
        }
        result = self.app.post(
            '/api/v1/redflags',
            content_type='text/html',
            data=json.dumps(expectedreq)
        )
        data = json.loads(result.data.decode())
        self.assertEqual(result.status_code, 401)
        self.assertEqual(
            data['failed'],
            'content-type must be application/json')

    def test_create_user_request_not_json(self):
        """ Test redflag content to be posted not in json format """
        expectedreq = {

            "user_id": "1",
            "firstname": "sabaalo",
            "lastname": "solomon",
            "othernames": "edrine",
            "email": "edrinesolomon@gmail",
            "phone_number": "0781433304",
            "username": "edrinesolo",
            "registered": "09/02/2019",
            "is_admin": "true"

        }
        result = self.app.post(
            '/api/v1/users',
            content_type='text/html',
            data=json.dumps(expectedreq)
        )
        data = json.loads(result.data.decode())
        self.assertEqual(result.status_code, 401)
        self.assertEqual(
            data['failed'],
            'content-type must be application/json')

    def test_if_user_cant_delete_innexistent_flag(self):
        res = self.app.delete('/api/v1/redflags/1')
        data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['msg'], 'item not found')

    def test_if_user_cant_view_an_innexistent_flag(self):
        res = self.app.delete('/api/v1/redflags/1')
        data = json.loads(res.data.decode())
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['msg'], 'item not found')


if __name__ == "__main__":
    unittest.main()
