"""
Date:	20/03/2020
Author:	Gerrit Lang

Core functionality of this service
"""
import pandas as pd
from geopy import distance
from geopy.geocoders import Nominatim, get_geocoder_for_service
import numpy as np

# Just for my test
TEST = ["Offer 1", "Offer 2"]
offers = pd.read_csv("employee.csv", sep=",")
SKILLS = ["Re-Stock shelves", "Lift heavy objects (boxes)", "Deliver goods (i am willing to use my car)", "Work with office programs", "Accounting",  "Look after someone", "Psychological assistance", "Entrance security"]

#pandas settings
pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000

def get_offers(offer_id=None):
    """
    returns all offers or a specific one

    Args:
        offer_id (str): id of the offer

    Returns:
        requested offers
    """
    
    if offer_id:
        filtered = offers[offers['email']== offer_id]
        html_table = filtered.to_html()
        return html_table
    html_table = offers.to_html()
    return html_table
    

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
    return []


def get_employers(employer_id=None):
    """
    returns all employers or a specific one

    Args:
        employer_id (str): id of the employer

    Returns:
        requested employers
    """
    return []

def compare_lists(a, b):
    """[summary]
    
    Args:
        df ([dataframe]): [dataframe from the employee/employer forms]
        skills ([type]): [list of all possible skills that we could need]
    """

    c = [x for x in a if x in a and x in b]


    return c

def build_columns(employer, employee):
    """[summary]
    
    Args:
        df ([dataframe]): [dataframe from the employee/employer forms]
        skills ([type]): [list of all possible skills that we could need]
    """
    #convert to string
    employer['Please select'] = employer['Please select'].str.replace('"', '')
    employer["fixed_skills"] = employer['Please select'].str.split(', ')

    employee['Please select'] = employee['Please select'].str.replace('"', '')
    employee["fixed_skills"] = employee['Please select'].str.split(', ')

    for i in SKILLS:
        
        employer[i] = np.isin(employer["fixed_skills"], list(i))
        employee[i] = np.isin(employer["fixed_skills"], list(i))

    return employer, employee


def find_matches(employee, employer, employee_id=None, employer_id=None):
    """finds matches for skills needed and skills on offer
    
    Args:
        employee ([dataframe]): [dataframe for the employees who need jobs]
        employer ([dataframe]): [dataframe for the employers who need people]
        employee_id (string): employee_id by which to filter,- optional
        employer_id (string): employer_id by which to filer,- optional
    """
    d = {'test': ['Re-Stock shelves', '2', "3"] }
    # do this for everthing in the incoming arrays
    result = {x: 1 if x in d['test'] else 0 for x in SKILLS }
    
   
    return matches_found


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

