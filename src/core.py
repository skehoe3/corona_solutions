"""
Date:	20/03/2020
Author:	Gerrit Lang

Core functionality of this service
"""
import pandas as pd
from geopy import distance
from geopy.geocoders import Nominatim, get_geocoder_for_service
import numpy as np
from src.spreadsheet import get_sheet_data, transform_to_dict_list
from dateutil import parser


# Just for my test
TEST = ["Offer 1", "Offer 2"]

offers = pd.read_csv("employee.csv", sep=",")

SKILLS = ["Re-Stock shelves", "Lift heavy objects (boxes)", "Deliver goods (i am willing to use my car)", "Work with office programs", "Accounting",  "Look after someone", "Psychological assistance", "Entrance security"]

#pandas settings
pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000

def create_offer(offer):
    """
    creates an offer

    Args:
        offer (dict): offer object
    """
    TEST.append(offer)


def get_employees(employee_id=None):
    """
    returns all employees or a specific one

    Args:
        employee_id (str): id of the employee

    Returns:
        requested employees
    """
    result = get_sheet_data(sheetname='employee',datarange='A:N')
    return transform_to_dict_list(result, employee_id)


def get_employers(employer_id=None):
    """
    returns all employers or a specific one

    Args:
        employer_id (str): id of the employer

    Returns:
        requested employers
    """
    result = get_sheet_data(sheetname='employer',datarange='A:N')
    return transform_to_dict_list(result, employer_id)

def compare_lists(a, b):
    """[summary]
    
    Args:
        df ([dataframe]): [dataframe from the employee/employer forms]
        skills ([type]): [list of all possible skills that we could need]
    """

    c = [x for x in a if x in a and x in b]


    return c


def get_matches(employee_id=None):
    """finds matches for skills needed and skills on offer
    
    Args:
        .
    Returns:
        employee_matches: which employers each employee matches with
        employer_matches: which employeees each employer matches with
    """

    #
    employers = get_employers()
    employees = get_employees(employee_id)[0]

    # only employees can list more than one skill, so no need for a second loop
    # for employers
    employees["Skills"] = employees["Skills"].split(', ')
    
    ee_from = parser.parse(employees['From'])
    ee_to = parser.parse(employees['To'])

    employer_matches = []
    for i, employer in enumerate(employers):

        er_from = parser.parse(employer['From'])
        er_to = parser.parse(employer['To'])

        if employer['Skills'] in employees['Skills'] and employer['Zip Code'] == employees['Zip Code'] and er_from >= ee_from and er_to <= ee_to:
                employer_matches.append({'Employer Email': employer.get('Email',''), 'First Name':employer.get('First Name',''), 'Last Name':employer.get('Last Name',''), 'Company':employer.get('Company',''), 'Phone Number':employer.get('Phone number',''), 'Skills':employer.get('Skills',''), 'From': str(er_from), 'To': str(er_to), 'Comments':employer.get('Comments','')})
        
    df = pd.DataFrame(employer_matches)

    return df.to_html()


def find_on_osm(address):
    """
    find coordinates on Open Street Map
    Args:
        address:

    Returns: coordinates

    """
    try:
        geolocator = Nominatim()
        location = geolocator.geocode(address)
        return location.raw
    except AttributeError:
        raise AttributeError("Address not found")


def find_distance(employer, employee):
    """
    Distance between two addresses
    Args:
        employer:
        employee:

    Returns:distance
    """
    try:
        employee_raw = find_on_osm(address=employee)
        employer_raw = find_on_osm(address=employer)
        coordinates = {
            'start': (employee_raw['lat'], employee_raw['lon']),
            'end': (employer_raw['lat'], employer_raw['lon'])
        }
        return distance.distance(coordinates['start'], coordinates['end']).km
    except AttributeError:
        return None

