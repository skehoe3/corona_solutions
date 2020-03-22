"""Pymongo database and functions"""

import sched, time
from pymongo import MongoClient, errors
from src.spreadsheet import get_sheet_data, transform_to_dict_list

DB_HOST = 'mongodb://localhost'
CLIENT = MongoClient(DB_HOST, 27017, connect=False)
DB = CLIENT['hack_db']
EMPLOYEES = DB['Employees']
EMPLOYERS = DB['Employers']
OFFERS = DB['Offers']

def startup():
    """read the current sheets and write them in clear DB"""
    update_employees()
    update_employers()


def update_employees():
    """
    update DB with the spreadsheet
    """
    EMPLOYEES.drop()
    employee = transform_to_dict_list(get_sheet_data(sheetname='employee', datarange='A:M'))
    EMPLOYEES.insert_many(employee)


def update_employers():
    """
    update DB with the spreadsheet

    """
    EMPLOYERS.drop()
    employer = transform_to_dict_list(get_sheet_data(sheetname='employer', datarange='A:M'))
    EMPLOYERS.insert_many(employer)


def get_employees(employee_id=None):
    """
    All current employees of specific one
    Args:
        employee_id: if given, only this one
    Returns: list(dict), employees
    """
    if employee_id:
        return EMPLOYEES.find_one({"ID": employee_id})
    return EMPLOYEES.find()


def get_employeer(employer_id=None):
    """
        All current employers of specific one
        Args:
            employer_id: if given, only this one
        Returns: list(dict), employers
        """
    if employer_id:
        return EMPLOYERS.find_one({"ID": employer_id})
    return EMPLOYERS.find()


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

# s = sched.scheduler(time.time, time.sleep)
# def do_update(sc):
#     startup()
#     # do your stuff
#     s.enter(120, 1, do_update, (sc,))
#
# s.enter(10, 1, do_update, (s,))
# s.run()