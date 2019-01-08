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
        expectedreq ={
	
        "comment":"corrupt officer",
        "type":"Red_flag",
        "location":"kamwokya",
        "status":"investigation",
        "image":"",
        "video":""

        }
        result = self.app.post(
            '/api/v1/redflags',
            content_type = 'text/html',
            data=json.dumps(expectedreq)
        )
        data=json.loads(result.data.decode())
        self.assertEqual(result.status_code,401)
        self.assertEqual(data['failed'],'content-type must be application/json')

    def test_create_user_request_not_json(self):
        """ Test redflag content to be posted not in json format """
        expectedreq = {
             'incident_type': 'government intervention',
            'comment_description': 'broken bridge at river nile',
            'status': 'bidding',
            'current_location': 'jinja',
            'created': 'dec 29 2018 : 01:04AM'
        }
        result = self.app.post(
            '/api/v1/users',
            content_type = 'text/html',
            data=json.dumps(expectedreq)
        )
        data=json.loads(result.data.decode())
        self.assertEqual(result.status_code,401)
        self.assertEqual(data['failed'],'content-type must be application/json')
       

    def test_if_user_cant_delete_innexistent_flag(self):
        res=self.app.delete('/api/v1/redflags/1')
        data=json.loads(res.data.decode())
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['msg'],'item not found')
    def test_if_user_cant_view_an_innexistent_flag(self):
        res=self.app.delete('/api/v1/redflags/1')
        data=json.loads(res.data.decode())
        self.assertEqual(res.status_code,404)
        self.assertEqual(data['msg'],'item not found')

# 

def create_Redflag(self):
        self.new_report = Report(
            id=1,
            incident_type='red flag',
            comment_description='officer taking a bribe',
            status='under invesitagation',
            current_location= 'kamwokya,bukoto street',
            created=datetime.datetime.now(),
            user_id=1
           
        )

    def test_welcome(self):
        '''
        checks if the app is up and running
        '''
        response = self.client.get(
            "api/v1/redflags",
            content_type="application/json")
        # we should get this on successful creation
        self.assertEqual(response.status_code, 200)

    def test_create_redflag_with_no_data(self):
        """
        checks if a redflags cant be created without any data
        """
        expectedreq = {

        }
        response = self.client.post(
            "api/v1/redflags",
            data=json.dumps(expectedreq),
            content_type="application/json")
        # we should get this on successful creation
        self.assertEqual(response.status_code, 401)

    def test_create_redflag(self):
        """
        checks if a redflag can be created
        """
        expectedreq = {
            'incident_type': 'redflag/whistle blowing',
            'comment_description': 'office taking a bribe',
            'status': 'under invesitagation',
            'current_location': 'kamwokya,bukoto street',
            'created': "Sat, 10 Nov 2018 13:46:41 GMT"
        }
        response = self.client.post(
            "api/v1/redflags",
            data=json.dumps(expectedreq),
            content_type="application/json")
        self.assertEqual(response.status_code, 401)

    def test_cannot_create_redflag_that_has_no_owner(self):
        """
        checks if a redflag can not be created without a user
        """
        expectedreq = {
            'incident_type': 'redflag/whistle blowing',
            'comment_description': 'office taking a bribe',
            'status': 'under invesitagation',
            'current_location': 'kamwokya,bukoto street',
            'created': "Sat, 10 Nov 2018 13:46:41 GMT"
        }
        response = self.client.post(
            "api/v1/redflags",
            data=json.dumps(expectedreq),
            content_type="application/json")
        # we should get this on successful creation
        self.assertEqual(response.status_code, 401)

    def test_checkcanget_redflags(self):
        '''
        checks
        :return:
        '''
        response = self.client.get("api/v1/redflags")
        # we should get an ok on successful creation
        self.assertEqual(response.status_code, 200)

    def test_can_get_a_redflag(self):
        """
        checks if a single redflag can be returned given its id
        """
        expectedreq = {
            'id': 1,
             'incident_type': 'redflag/whistle blowing',
            'comment_description': 'office taking a bribe',
            'status': 'under invesitagation',
            'current_location': 'kamwokya,bukoto street',
            'created': "Sat, 10 Nov 2018 13:46:41 GMT"
        }
        self.client.post(
            "api/v1/redflags",
            data=json.dumps(expectedreq),
            content_type="application/json")
        response = self.client.get(
            "api/v1/redflags/1",
            data='',
            content_type="application/json")
        self.assertEqual(response.status_code, 405)#200500

    def test_cant_get_inexistent_redflag(self):
        response = self.client.get(
            "api/v1/redflags/b",
            data='',
            content_type="application/json")
        self.assertEqual(response.status_code, 404)


    

if __name__ == "__main__":
    unittest.main()
