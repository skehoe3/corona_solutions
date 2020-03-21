"""Pymongo database and functions"""

from pymongo import MongoClient, errors

DB_HOST = 'localhost'
CLIENT = MongoClient(DB_HOST, 27017, connect=False)
DB = CLIENT.hack_db
EMPLOYEES = CLIENT.employees
EMPLOYERS = CLIENT.employers

