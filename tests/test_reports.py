from app import app
import unittest
import json
import datetime


class TestsReports(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client(self)
        self.redflag_data = {
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

        self.assertEqual(response.status_code, 400)

    def test_create_redflag(self):
        """
        checks if a redflag can be created
        """
       
        response = self.client.post(
            "api/v1/redflags",
            data=json.dumps(self.redflag_data),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_cannot_create_redflag_that_has_no_owner(self):
        """
        checks if a redflag can not be created without a user
        """
        
        response = self.client.post(
            "api/v1/redflags",
            data=json.dumps(self.redflag_data),
            content_type="application/json")
        # we should get this on successful creation
        self.assertEqual(response.status_code, 201)

    def test_checkcanget_redflags(self):
        '''
        checks
        :return:red flags
        '''
        response = self.client.get("api/v1/redflags")
        # we should get an ok on successful creation
        self.assertEqual(response.status_code, 200)

    def test_can_get_a_redflag(self):
        """
        checks if a single redflag can be returned given its id
        """
        
        self.client.post(
            "api/v1/redflags",
            data=json.dumps(self.redflag_data),
            content_type="application/json")
        response = self.client.get(
            "api/v1/redflags/1",
            data='',
            content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_update_specific_red_flag(self):
        """
        checks if a single redflag can be updated
        """
        
        self.client.post(
            "api/v1/redflags",
            data=json.dumps(self.redflag_data),
            content_type="application/json")
        response = self.client.patch("api/v1/redflags/1",
                                     content_type="application/json",
                                     data=json.dumps({
                                         "id": "1",
                                         "created_on": "22hrs",
                                         "created_by": "1",
                                         "type": "redflag",
                                         "location": "kampala",
                                         "status": "pending",
                                         "image": "image",
                                         "video": "video",
                                         "comment": "invesitgation on going"
                                     }))
        self.assertEqual(response.status_code, 404)

    def test_cant_get_inexistent_redflag(self):
        response = self.client.get(
            "api/v1/redflags/b",
            data='',
            content_type="application/json")
        self.assertEqual(response.status_code, 404)

    def test_delete_red_flags(self):
        
        self.client.post(
            "api/v1/redflags/1",
            data=json.dumps(self.redflag_data),
            content_type="application/json")
        response = self.client.delete("api/v1/redflags/1")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
