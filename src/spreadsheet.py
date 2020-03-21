"""
Date:	20/03/2020
Author:	Felix Dosch

Interface to read data from Google Spreadsheets
"""
from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

SHEET_CREDENTIALS = {
    'employee':'1QLHP0G7pEutW5QGAH0pcM92gpNRwt1EwBLyvRDcJN_w',
    'employer':'1FFABHCLpotXMV6s2IW4x_5SlMckfuGbNAQFhWw_S4kw'
}


def get_sheet_data(sheetname, datarange='A:M'):
    """
    returns all data from a spreadsheet with given id in selected range

    Args:
        sheet (str): either employee or employer
        datarange (str): the range of the sheet cells to be returned

    Returns:
        requested spreadsheet values
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('config/token.pickle'):
        with open('config/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'config/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('config/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SHEET_CREDENTIALS[sheetname],
                                range=datarange).execute()
    values = result.get('values', [])
    return values


def transform_to_dict_list(inputlist, filterid=None):
    """
    returns a list of dictionaries from given list, filtered by ID

    Args:
        input_list (list(list(str))): list of string lists, where the first list holds the keys for the dictionary to be constructed
        filter (str): ID to be filtered by. If present, list will only contain one dict where ID is given ID

    Returns:
        list of dictionaires containing the data from the list
    """
    outputlist = []
    keys = inputlist[0]
    for x in range(1, len(inputlist)):
        if not filterid:
            outputlist.append(dict(zip(keys, inputlist[x])))
            continue
        if inputlist[x][0] == filterid:
            outputlist.append(dict(zip(keys, inputlist[x])))
            break
    return outputlist