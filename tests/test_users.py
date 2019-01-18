from app import app
import unittest
import json
from app.views.users import is_valid


class TestsUsers(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)
        self.create_user = {
            "firstname": "solo ed",
            "lastname": "ed",
            "othernames": "",
            "username": "soloo",
            "phone_number": "0781433304",
            "email": "email000000@test.com",
            "is_admin": True

        }

    def test_create_user(self):

        # checks if a user can be created

        
        response = self.client.post(
            "api/v1/users",
            data=json.dumps(self.create_user),
            content_type="application/json")
        results = json.loads(response.data.decode())

        self.assertEqual(
            results['success'], True)
        self.assertEqual(response.status_code, 201)

    def test_cannot_create_a_user_without_email(self):
        """
        checks if cannot create a user who has no email
        """
        expecteduser_obj = {
            "firstname": "solo ed",
            "lastname": "ed",
            "othernames": "",
            "username": "soloo",
            "phone_number": "0781433304",
            "is_admin": True

        }
        response = self.client.post(
            '/api/v1/users',
            data=json.dumps(expecteduser_obj),
            content_type="application/json")
        data = json.loads(response.data.decode())
        self.assertEqual(data['msg'], 'Email is missing')
        self.assertEqual(data['success'], False)
        self.assertEqual(response.status_code, 400)

    def test_cannot_create_a_user_without_firstname(self):
        """
        checks if cannot create a user who has no firstname
        """
        expecteduser_obj = {
            
            "lastname": "ed",
            "othernames": "",
            "username": "soloo",
            "email": "edrine@g.co",
            "phone_number": "0781433304",
            "is_admin": True

        }
        response = self.client.post(
            '/api/v1/users',
            data=json.dumps(expecteduser_obj),
            content_type="application/json")
        data = json.loads(response.data.decode())
        self.assertEqual(data['msg'], 'firstname must be provided')
        self.assertEqual(response.status_code, 400)

    def test_cannot_create_a_user_without_lastname(self):
        """
        checks if cannot create a user who has no lastname
        """
        expecteduser_obj = {
            
            "firstname": "solo",
            "othernames": "",
            "username": "soloo",
            "email": "edrine@g.co",
            "phone_number": "0781433304",
            "is_admin": True

        }
        response = self.client.post(
            '/api/v1/users',
            data=json.dumps(expecteduser_obj),
            content_type="application/json")
        data = json.loads(response.data.decode())
        self.assertEqual(data['msg'], 'lastname must be provided')
        self.assertEqual(response.status_code, 400)

    def test_cannot_create_a_user_without_username(self):
        """
        checks if cannot create a user who has no usertname
        """
        expecteduser_obj = {
            
            "firstname": "solo",
            "lastname": "solo ed",
            "othernames": "",
            "email": "edrine@g.co",
            "phone_number": "0781433304",
            "is_admin": True

        }
        response = self.client.post(
            '/api/v1/users',
            data=json.dumps(expecteduser_obj),
            content_type="application/json")
        data = json.loads(response.data.decode())
        self.assertEqual(data['msg'], 'User must have a username')
        self.assertEqual(response.status_code, 400)

    def test_user_cannot_have_someones_user_name(self):
        """
        checks if cannot create a user with the same username
        """
        users = []
        
        users.append(self.create_user)
        user_obj = {
            "firstname": "solo ed",
            "lastname": "ed",
            "othernames": "",
            "username": "soloo",
            "phone_number": "0781433304",
            "email": "edrine@gmail.com",
            "is_admin": True

        }
        response = self.client.post(
            "api/v1/users",
            data=json.dumps(user_obj),
            content_type="application/json")
        data2 = json.loads(response.data.decode())
        self.assertEqual(data2['success'], False)
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_have_someone_else_email_address(self):
        """
        checks if cannot create a user with the same email adress
        """
        # usersList = []
        
        self.client.post(
            "api/v1/users",
            data=json.dumps(self.create_user),
            content_type="application/json")

        user_obj2 = {
            "firstname": "solo ed",
            "lastname": "ed",
            "username": "soloo",
            "phone_number": "0781433304",
            "email": "email@test.com",
            "is_admin": True,
            "othernames": "my other"

        }
        response = self.client.post(
            "api/v1/users",
            data=json.dumps(user_obj2),
            content_type="application/json")
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], False)
        self.assertEqual(response.status_code, 409)

    def test_user_cannot_have_an_invalid_email(self):
        """
        tests if user supplies a valid email
        """
        user_obj = {
            "firstname": "solo ed",
            "lastname": "ed",
            "username": "soloo",
            "phone_number": "0781433304",
            "email": "solo123",
            "othernames": "my other",
            "is_admin": True

        }
        response = self.client.post(
            "api/v1/users",
            data=json.dumps(user_obj),
            content_type="application/json")
        data = json.loads(response.data.decode())
        self.assertEqual(data['success'], False)
        self.assertEqual(response.status_code, 401)

    def test_get_a_no_users_message(self):
        '''
        tests if a user gets a readable no users message when users are not there
        :return:
        '''
        response = self.client.get(
            'api/v1/users', content_type='application/json')
        data = json.loads(response.data.decode())
        count = data['count']
        if count == 0:
            self.assertEqual(data['msg'], 'No users yet')
        self.assertEqual(response.status, '200 OK')


if __name__ == "__main__":
    unittest.main()
