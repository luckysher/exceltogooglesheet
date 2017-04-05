import unittest
from utils import spreadsheetId, getLogger
from readUtils import *
from googleUtils import GoogleUtils

logger = getLogger()

class TestGoogleSpreadsheet(unittest.TestCase):

    def setUp(self):
        logger.debug("Setting up test for google sheets")
        self.readUtil = XLRead()

    # test case for reading data from xl file
    def testReadDataFromXlFile(self):
        self.readUtil.readData(0)

    # test case for reading data from the google sheet
    def testGoogleSheetRead(self):
        logger.debug("Getting Data from google sheet..")
        googleUtils = GoogleUtils()
        rangeName = 'demosheet!A2:E'
        # get spread sheets from google
        gSpreadsheet = googleUtils.getSpreadsheets()
        # get rows for spreadsheetId and sheet name
        rows = googleUtils.getRowsFromSpreadsheets(gSpreadsheet, spreadsheetId, rangeName)
        if not rows:
            logger.debug('No data found for range: %s' % rangeName)
        else:
            logger.debug("Got %d rows google sheet for range: %s" % (rows.__len__(), rangeName))
            logger.debug("  Sr.No.     Name       Age       Marks")
            logger.debug("------------------------------------------")
            for row in rows:
                logger.debug('  %d     %s       %d         %d' % (int(row[0]), row[1], int(row[2]), int(row[3])))

    # write data to google sheet at given range
    def testGoogleSheetWrite(self):
        values = [
            ['21', 'Kaliver', '24', '500']
        ]
        googleUtils = GoogleUtils()
        googleUtils.writeDataToGoogleSheet(spreadsheetId, values, valueInputOption=valueInputOption)

    # write data to second google sheet at given range
    def testGoogleSheetWriteSecondSheet(self):
        values = [
            ['2', 'Jam', '24', '5000']
        ]
        googleUtils = GoogleUtils()
        googleUtils.writeDataToGoogleSecondSheet(spreadsheetId, values, valueInputOption=valueInputOption)

    # write data to google sheet at a given Column
    def testGoogleSheetWriteColumn(self):
        values = [
            ['110']
        ]
        googleUtils = GoogleUtils()
        googleUtils.writeDataToGoogleSheet(spreadsheetId, values, valueInputOption=valueInputOption, rangeName='demosheet!A2:A2')

    def tearDown(self):
        logger.debug("Tearing down test for google sheets")

if __name__ == "__main__":
    unittest.main()