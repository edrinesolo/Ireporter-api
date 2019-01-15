[![Build Status](https://travis-ci.org/edrinesolo/Ireporter-api.svg?branch=develop)](https://travis-ci.org/edrinesolo/Ireporter-api)
[![Coverage Status](https://coveralls.io/repos/github/edrinesolo/Ireporter-api/badge.svg?branch=develop)](https://coveralls.io/github/edrinesolo/Ireporter-api?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/a99a88d28ad37a79dbf6/maintainability)](https://codeclimate.com/github/codeclimate/codeclimate/maintainability)

# Ireporter-api
REST api for the ireporter project

## Installation

Create a virtual environment for the project.

```
virtualenv "name of the virtual environment"
```
Then Activate the venv using:
```
source "name of the virtual environment/bin/activate
```

* Navigate to the application directory:

```
cd Ireporter-api
```

* Create a virtual environment to install the
application in. You could install virtualenv and virtualenvwrapper.
Within your virtual environment, install the application package dependencies with:

```
pip install -r requirements.txt
```

* Run the application with:

```
python run.py
```
* for tests run in terminal using:

```
py.test
```

#### URL endpoints

| URL Endpoint | HTTP Methods | Summary |
| -------- | ------------- | --------- |
| `api/v1/redflags` | `POST`  | Creates a new Redflag|
| `api/v1/redflags/<int:id>` | `GET` | Retrieves a specific redflag given its identifier|
| `api/v1/users` | `GET` | Retrieve all users |
| `api/v1/users` | `POST` |  Creates a new User |
| 

