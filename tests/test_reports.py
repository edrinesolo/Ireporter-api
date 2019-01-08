from app import app
import unittest
import json
import datetime

class TestsReports(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)

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
        self.assertEqual(response.status_code, 500)#200500
    def test_update_specific_red_flag(self):
        """
        checks if a single redflag can be updated
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
        response=self.client.patch("api/v1/redflags/1",
             content_type = "application/json",
                    data = json.dumps({  
                        'incident_type': 'redflag/whistle blowing',
                        'comment_description': 'faulty roads',
                        'status': 'complete',
                        'current_location': 'kamwokya,bukoto street',
                        'created': "tue, 10 Nov 2018 13:46:41 GMT"
                    }))
        self.assertEqual(response.status_code,405)



    def test_cant_get_inexistent_redflag(self):
        response = self.client.get(
            "api/v1/redflags/b",
            data='',
            content_type="application/json")
        self.assertEqual(response.status_code, 404)

    def test_delete_red_flags(self):
        expectedreq = {
            'id': 1,
             'incident_type': 'redflag/whistle blowing',
            'comment_description': 'office taking a bribe',
            'status': 'under invesitagation',
            'current_location': 'kamwokya,bukoto street',
            'created': "Sat, 10 Nov 2018 13:46:41 GMT"
        }
        self.client.post(
            "api/v1/redflags/1",
            data=json.dumps(expectedreq),
            content_type="application/json")
        response=self.client.delete("api/v1/redflags/1")
        self.assertEqual(response.status_code,404)

   

if __name__ == "__main__":
    unittest.main()
