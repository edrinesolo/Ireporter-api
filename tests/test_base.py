from app import app
import unittest
import json


class TestsStart(unittest.TestCase):

    def setUp(self):
         self.app = app.test_client()
        
       
    
    def test_if_can_get_users(self):

        response = self.app.get('api/v1/users')
        self.assertEqual(response.status_code, 200)


    def test_if_can_get_redflags(self):
        response = self.app.get('api/v1/redflags')
        self.assertEqual(response.status_code, 200)

    def test_redflag_not_json(self):
        """ Test redflag content to be posted not in json format """
        expectedreq = {
            'incident_type': 'redflag/whistle blowing',
            'comment_description': 'office taking a bribe',
            'status': 'under invesitagation',
            'current_location': 'kamwokya,bukoto street',
            'created': "Sat, 10 Nov 2018 13:46:41 GMT"
        }
        result = self.app.post(
            '/api/v1/redflags',
            content_type = 'text/html',
            data=json.dumps(expectedreq)
        )
        self.assertEqual(result.status_code,401)
        self.assertIn('Content-type must be application/json',str(result.data))
    def test_create_user_request_not_json(self):
        """ Test redflag content to be posted not in json format """
        expectedreq = {
             'incident_type': 'redflag/whistle blowing',
            'comment_description': 'office taking a bribe',
            'status': 'under invesitagation',
            'current_location': 'kamwokya,bukoto street',
            'created': "Sat, 10 Nov 2018 13:46:41 GMT"
        }
        result = self.app.post(
            '/api/v1/users',
            content_type = 'text/html',
            data=json.dumps(expectedreq)
        )
        self.assertEqual(result.status_code,401)
        self.assertIn('Content-type must be application/json',str(result.data))

if __name__ == "__main__":
    unittest.main()
