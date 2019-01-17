[![Build Status](https://travis-ci.org/edrinesolo/Ireporter-api.svg?branch=develop)](https://travis-ci.org/edrinesolo/Ireporter-api)
[![Coverage Status](https://coveralls.io/repos/github/edrinesolo/Ireporter-api/badge.svg?branch=develop)](https://coveralls.io/github/edrinesolo/Ireporter-api?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/f4ebb30e428384336ca5/maintainability)](https://codeclimate.com/github/edrinesolo/Ireporter-api/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/0917007869d84b40a20a38a7afecdf63)](https://www.codacy.com/app/edrinesolo/Ireporter-api?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=edrinesolo/Ireporter-api&amp;utm_campaign=Badge_Grade)

# Ireporter-api
REST api for the ireporter project

# Installation

Create a virtual environment for the project.

```
virtualenv "name of the virtual environment"
```
Then Activate the venv using:
```
source "name of the virtual environment / bin / activate
```

* Navigate to the application directory:

```
cd Ireporter - api
```

* Create a virtual environment to install the
application in. You could install virtualenv and virtualenvwrapper.
Within your virtual environment, install the application package dependencies with:

```
pip install - r requirements.txt
```

* Run the application with:

```
python run.py
```
* for tests run in terminal using:

```
py.test
```

# URL endpoints

| URL Endpoint | HTTP Methods | Summary |
| -------- | ------------- | --------- |
| `api/v1/redflags` | `POST` | Creates a new Redflag|
| `api/v1/redflags / <int: id >` | `GET` | Retrieves a specific redflag given its identifier|
| `api/v1/users` | `GET` | Retrieve all users |
| `api/v1/users` | `POST` | Creates a new User |
| `api/v1/redflags/<int:id>` | `PUT` | Update a specific redflag |
| `api/v1/redflags/<int:id>` | `PATCH` | Update a comment record in a red flag |
| `api/v1/redflags/<int:id>` | `DELETE` | Delete a Redflags |

# Example New User body
```
Example body
{
    "firstname": "sabaalo",
    "lastname": "solomon",
    "othernames": "edrine",
    "email": "edrinesolomon@gmail.com",
    "phone_number": "0781433304",
    "username": "edrinesolo",
    "registered": "09/02/2019",
    "is_admin": "true"

}
```
# Example New RedFlag Body
```
{
    "comment": "invesitgation on going",
    "created_by": 1,
    "created_on": "Thu, 17 Jan 2019 10:13:51 GMT",
    "id": 3,
    "image": "image",
    "location": "makindye",
    "status": "rejected",
    "type": "redflag",
    "video": "image"
}
```
# Deployement
[Heroku Deployement](https://ireporter---v1.herokuapp.com)

# Author
[Edrine Solomon](https://github.com/edrinesolo)
