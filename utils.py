import logging

APP_NAME = 'EXCEL TO GOOGLE SHEET'

CLIENT_SECRET_FILE = 'client_secret.json'

# google sheet Id from which to read
spreadsheetId = 'mygooglespreadsheetid'

# credentials file name
CREDENTIALS_FILE = 'credential.json'

# data sample file path
XL_FILE_PATH = '/path/to/data/Samples/data.xlsx'

# set settings for the logger and return logger
def getLogger():
    logging.basicConfig(format='[%(name)s][%(levelname)s] %(message)s', level=logging.DEBUG)
    logger = logging.getLogger(APP_NAME)
    return logger

