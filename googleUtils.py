###############################################
# Google utils file for headling google funs #
# like getting credentials, spread sheets    #
###############################################

from __future__ import print_function

from oauth2client.file import Storage
from oauth2client import client
from apiclient import discovery
from oauth2client import tools
import httplib2
import os
from utils import *
import sys
sys.argv = sys.argv[:1]

logger = getLogger()


try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None


class GoogleUtils:
    """
    Class for handling google spread sheet functionalities
    like: get client credentials, discovery service etc..
    """

    # get the credentials for handling google sheet data
    def getCredentials(self, credFilePath):
        """
        :param credFilePath: Path to the client credentials file
        :return: credentials
        """
        credentials = None
        store = Storage(credFilePath)


        logger.debug("Getting client credentials...")
        # check if file exist having credentials
        if os.path.exists(credFilePath):
            credentials = store.get()

        # check if the given credentials are valid
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APP_NAME
            if flags:
                credentials = tools.run_flow(flow, store, flags)
            else:
                credentials = tools.run_flow(flow, store)

        return credentials

    # get discovery service for getting the google sheet
    def getDiscoveryService(self, credFilePath):
        """
        :param credFilePath: Path to the client credentials file
        :return: spread sheet discovery service object
        """

        discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?version=v4')
        # get client credendials
        credentials = self.getCredentials(credFilePath)
        http = credentials.authorize(httplib2.Http())
        # get discovery service
        service = discovery.build('sheets', 'v4', http=http, discoveryServiceUrl=discoveryUrl)

        return service
    # get the spead sheets object
    def getSpreadsheets(self):
        """
        :return: google spread sheets object
        """
        service = self.getDiscoveryService(CREDENTIALS_FILE)
        spreadSheets = service.spreadsheets()

        return spreadSheets

    def getRowsFromSpreadsheets(self, gSpreadsheets, spreadsheetId, rangeName):
        """
        :param gSpreadsheet: Google spread sheet object
        :param rangeName: Sheetname and range to read
        :return: row list
        """
        data = gSpreadsheets.values().get(spreadsheetId=spreadsheetId, range=rangeName).execute()
        rows = data.get('values', [])

        return rows

    # function for writing data to the given sheet
    def writeDataToGoogleSheet(self, spreadSheetId, values, valueInputOption, rangeName=None):
        logger.debug("Writing Data to google sheet..")

        body = {
            'values': values
        }

        # get spread sheets from google
        gSpreadsheet = self.getSpreadsheets()
        gSpreadsheet.values().update(spreadsheetId=spreadsheetId, range=rangeName, valueInputOption=valueInputOption, body=body).execute()


    # function for writing data to the second sheet
    def writeDataToGoogleSecondSheet(self, spreadSheetId, values, valueInputOption, rangeName=None):
        logger.debug("Writing Data to google sheet..")

        body = {
            'values': values
        }

        # get spread sheets from google
        gSpreadsheet = self.getSpreadsheets()
        gSpreadsheet.values().update(spreadsheetId=spreadsheetId, range=rangeName, valueInputOption=valueInputOption,
                                 body=body).execute()

