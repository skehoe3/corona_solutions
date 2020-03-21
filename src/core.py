"""
Date:	20/03/2020
Author:	Gerrit Lang

Core functionality of this service
"""
from geopy import distance
from geopy.geocoders import Nominatim
from src.spreadsheet import get_sheet_data, transform_to_dict_list


# Just for my test
TEST = ["Offer 1", "Offer 2"]


def get_offers(offer_id=None):
    """
    returns all offers or a specific one

    Args:
        offer_id (str): id of the offer

    Returns:
        requested offers
    """
    return TEST


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
    #
    result = get_sheet_data(sheetname='employee',datarange='A:M')
    employee = transform_to_dict_list(result, employee_id)
    # insert_employee(employee_id)
    print(employee)
    return employee



def get_employers(employer_id=None):
    """
    returns all employers or a specific one

    Args:
        employer_id (str): id of the employer

    Returns:
        requested employers
    """
    result = get_sheet_data(sheetname='employer',datarange='A:M')
    return transform_to_dict_list(result, employer_id)


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

