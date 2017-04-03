from xlrd import *
from utils import *


class XLRead:

    def __init__(self):
        try:
            self.xlbook = open_workbook(XL_FILE_PATH)
        except Exception as e:
            print("[%s] readUtils got exception while reading file.." % APP_NAME)
            print("[%s] %s" %( APP_NAME, e))

    
