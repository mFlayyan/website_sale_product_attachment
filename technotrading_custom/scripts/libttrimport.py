""" 

2011, stefan@therp.nl

This file provides backend functions for importing the VWN dBase III files,
based on http://packages.python.org/dbf/

"""

import sys

try:
    import params
except ImportError, err:
    print """ 
Could not find params.py. It is not included in the repository,
protecting sensitive data from ending up there.

Please create it with the following contents:

import openerplib
def get_connection():
   return openerplib.get_connection(
           hostname="localhost",
           database="crmwebdev61",
           login="admin",
           password="xxx",
           port=9272,
           )

def get_base_path():
    return "/srv/data/dbf/"

"""
    sys.exit(1)

def get_connection():
    return params.get_connection()

def test_connection(connection):
    # performs a test, printing the user's name
    user_model = connection.get_model("res.users")
    ids = user_model.search([("login", "=", "admin")])
    user_info = user_model.read(ids[0], ["name"])
    print user_info["name"] + ' is connected'
