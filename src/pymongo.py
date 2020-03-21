"""Pymongo database and functions"""

from pymongo import MongoClient, errors
from src.spreadsheet import get_sheet_data, transform_to_dict_list

DB_HOST = 'mongodb://localhost'
CLIENT = MongoClient(DB_HOST, 27017, connect=False)
DB = CLIENT['hack_db']
EMPLOYEES = DB['Employees']
EMPLOYERS = DB['Employers']
OFFERS = DB['Offers']

def startup():
    employee = transform_to_dict_list(get_sheet_data(sheetname='employee', datarange='A:M'))
    employer = transform_to_dict_list(get_sheet_data(sheetname='employer', datarange='A:M'))
    EMPLOYEES.insert_many(employee)
    EMPLOYERS.insert_many(employer)

def insert_employee(employee):
    """
    write employee on DB
    Args:
        employee: dict with ID, name, address...

    """
    EMPLOYEES.insert(employee)


def insert_employer(employer):
    """
        write employer on DB
        Args:
            employer: dict with ID, name, address...offer

        """
    EMPLOYEES.insert(employer)


def insert_offer(employer):
    """
        write offer on DB
        Args:
            offer:

        """
    EMPLOYEES.insert(employer)