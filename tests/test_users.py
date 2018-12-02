from app import app
import unittest
import json
from app.users import is_valid


class TestsUsers(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

    def test_create_user(self):
        """
        checks if a user can be created
        """
        expecteduser_obj = {
            "fullname": "John doe",
            "username": "jdoe",
            "phone_number": "0777777777",
            "email": "email000000@test.com",
            "password": "passwod=",
            "is_admin": True

        }
        response = self.client.post(
            "api/v1/users",
            data=json.dumps(expecteduser_obj),
            content_type="application/json")
        data = json.loads(response.data.decode())

        self.assertEqual(
            data['success'], True)
        self.assertEqual(response.status_code, 201)

    def test_cannot_create_a_user_without_email(self):
        """
        checks if cannot create a user who has no email
        """
        users = []
        expecteduser_obj = {
            "fullname": "John doe",
            "username": "je",
            "phone_number": "0777777777",
            "password": "passwod=",
            "is_admin":True

        }
        response=self.client.post('/api/v1/users',data=json.dumps(expecteduser_obj),
            content_type="application/json")
        data = json.loads(response.data.decode())
        self.assertEqual(data['msg'], 'Bad request')
        self.assertEqual(data['success'], False)
        self.assertEqual(response.status_code, 400)

    def test_user_cannot_have_someones_user_name(self):
        users = []
        expecteduser_obj = {
            "fullname": "John doe",
            "username": "jdoe",
            "phone_number": "0777777777",
            "email": "email@test.com",
            "password": "passwod=",
            "is_admin":True

        }
        users.append(expecteduser_obj)
        user_obj = {
            "fullname": "John doe",
            "username": "jdoe",
            "phone_number": "0777777777",
            "email": "fred@test.com",
            "password": "yestpass",
            "is_admin":True

        }
        response = self.client.post(
            "api/v1/users",
            data=json.dumps(user_obj),
            content_type="application/json")
        data2 = json.loads(response.data.decode())
        self.assertEqual(data2['msg'], 'Username is already taken')
        self.assertEqual(data2['success'], False)
        self.assertEqual(response.status_code, 401)#409

    def test_user_cannot_have_someone_else_email_address(self):
        usersList = []
        expecteduser_obj = {
            "fullname": "John doe",
            "username": "fredy",
            "phone_number": "0777777777",
            "email": "fredy@test.com",
            "password": "passwod=",
            "is_admin":False

        }
        self.client.post(
            "api/v1/users",
            data=json.dumps(expecteduser_obj),
            content_type="application/json")

        # usersList.append(expecteduser_obj)
        user_obj2 = {
            "fullname": "John doe",
            "username": "jdoe",
            "phone_number": "0777777777",
            "email": "fredy@test.com",
            "password": "yestpass",
            "is_admin":False

        }
        response = self.client.post(
            "api/v1/users",
            data=json.dumps(user_obj2),
            content_type="application/json")
        data2 = json.loads(response.data.decode())
        self.assertEqual(data2['msg'], 'Username is already taken')
        self.assertEqual(data2['success'], False)
        self.assertEqual(response.status_code, 401)#409

    def test_user_cannot_have_an_invalid_email(self):
        """
        tests if user supplies a valid email
        """
        user_obj = {
            "fullname": "John doe",
            "username": "jdoe",
            "phone_number": "0777777777",
            "email": "est.com",
            "password": "passwod=",
            "is_admin":True

        }
        response = self.client.post(
            "api/v1/users",
            data=json.dumps(user_obj),
            content_type="application/json")
        data = json.loads(response.data.decode())
        self.assertEqual(data['msg'], 'Email is badly formatted')
        self.assertEqual(data['success'], False)
        self.assertEqual(response.status_code, 401)

    def test_cannot_get_user_redflags(self):
        """
        checks if a user that doesnt exist can not get redflags
        """
        response = self.client.get(
            "api/v1/users/5999/redflags",
            content_type="application/json")
        # we should get an ok
        self.assertEqual(response.status_code, 404)#404)

    def test_get_user_redflags(self):
        '''
        creates a user then attempts to get their items
        :param self:
        :return:
        '''
        expecteduser_obj = {
            "fullname": "John doe",
            "username": "jdoe",
            "phone_number": "0777777777",
            "email": "email000000@test.com",
            "password": "passwod=",
            "is_admin":True

        }
        self.client.post(
            "api/v1/users",
            data=json.dumps(expecteduser_obj),
            content_type="application/json")
        """
        checks if a user that doesnt exist can not get redflags
        """
        response = self.client.get(
            "api/v1/users/1/redflags",
            content_type="application/json")
        # we should get an ok
        self.assertEqual(response.status_code, 404)#200

    def test_is_valid_email(self):
        '''
        tests function to validate emails
        :return:
        '''
        self.assertEqual(is_valid("edrinesolomon@gmail.com"), True)
        self.assertEqual(is_valid("myemail@mycompany.com"), True)
        self.assertEqual(is_valid("edrinesolomon.com"), False)
        self.assertEqual(is_valid("ema@.com"), False)
        

    def test_get_a_no_users_message(self):
        '''
        tests if a user gets a readable no users message when users are not there
        :return:
        '''
        response = self.client.get('api/v1/users', content_type='application/json')
        data = json.loads(response.data.decode())
        count = data['count']
        if count == 0:
            self.assertEqual(data['msg'], 'No users yet')
        self.assertEqual(response.status, '200 OK')

if __name__ == "__main__":
    unittest.main()