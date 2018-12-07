import datetime
import re




class User:
    """
   user data structure
    """
    
    


    def __init__(self):
        self.users = []
      
    def is_user_exist(self, id):
        """check if parcel not exist in the parcel list """
        for user in self.users:
            if user['user_id'] == id:
                return True

    def create_new_user(self, request_data):
        self.newuser = {
            "user_id": len(users) + 1,
            "firstname":request_data['firstname'],
            "lastname":request_data['lastname'],
            "othernames":request_data['othernames'],
            "email":request_data['email'],
            "phone_number":request_data['phone_number'],
            "username":request_data['username'],
            "joined": datetime.datetime.now(),
            "is_admin":request_data['is_admin']

        }
        self.users.append(self.newuser)
        return {"msg": "user created", "user": self.newuser.get('user_id')}

   

    def is_valid_user_request(self, newuser):
        """
        helper to check required fields
        """

        if "username" in newuser and "fullname" in newuser and "phone_number" in newuser and \
                "email" in newuser and "password" in newuser:
            return True
        else:
            return False

    def is_valid(self, email):
        """helper for chcking valid emails"""

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False
        return True

    def user_exists(self, id):
        '''
        helper to check user exists
        '''

        for user in self.users:
            if user['user_id'] == id:
                return True
        return False

    def is_email_taken(self, email):
        for user in self.users:
            if user['email'] == email:
                return False
        return True

    def is_username_taken(self, username):
        for user in self.users:
            if user['username'] == username:
                return False
        return True