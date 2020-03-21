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
offers = pd.read_csv("Employee - Form Responses 1.csv", sep=",")
skills = ["Re-Stock shelves", "Lift heavy objects (boxes)", "Deliver goods (i am willing to use my car)", "Work with office programs", "Accounting",  "Look after someone", "Psychological assistance", "Entrance security"]

def get_offers(offer_id=None):
    """
    returns all offers or a specific one

    Args:
        offer_id (str): id of the offer

    Returns:
        requested offers
    """
    
    if offer_id:
        filtered = offers['email']== offer_id
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

#skills = ["Re-Stock shelves", "Lift heavy objects (boxes)", "Deliver goods (i am willing to use my car)", "Work with office programs", "Accounting",  "Look after someone", "Psychological assistance", "Entrance security"]
def build_columns(df, skills):
    """[summary]
    
    Args:
        df ([dataframe]): [dataframe from the employee/employer forms]
        skills ([type]): [list of all possible skills that we could need]
    """

    for i in skills:
        df[i] = np.where(i in df['Please select'], 1, 0)

    return df

def find_matches(employee, employer, employee_id=None, employer_id=None):
    """finds matches for skills needed and skills on offer
    
    Args:
        employee ([dataframe]): [dataframe for the employees who need jobs]
        employer ([dataframe]): [dataframe for the employers who need people]
        employee_id (string): employee_id by which to filter,- optional
        employer_id (string): employer_id by which to filer,- optional
    """

    #you can compare the lists in the skills column, and use that to decide what people match what jobs
    cols_employee = build_columns(employee, skills)
    cols_employer = build_columns(employer, skills)

    


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

