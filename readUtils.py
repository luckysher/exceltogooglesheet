# XLRead class for reading data from the excel file

from xlrd import *
from utils import *


class XLRead:

    def __init__(self):
        try:
            self.xlbook = open_workbook(XL_FILE_PATH)
        except Exception as e:
            print("[%s] readUtils got exception while reading file.." % APP_NAME)
            print("[%s] %s" %( APP_NAME, e))

    def readData(self, startRow, endRow=None):
        cursheet = self.xlbook.sheet_by_index(0)
        endRow = cursheet.nrows
        print("Sr:   Name     Age   Marks")
        for row in range(startRow, endRow):
            # get data in the current row
            rowDataList = cursheet.row(row)

            # check for empty row
            if rowDataList[0].value == '' and rowDataList[1].value == '' and rowDataList[2].value == '' and rowDataList[3].value == '':
                continue    # no need to process the row further
            try:
                id = int(rowDataList[0].value)
                name = str(rowDataList[1].value)
                age = int(rowDataList[2].value)
                marks = int(rowDataList[3].value)

                print("%d   %s     %d   %d" % (id, name, age, marks))
            except Exception as e:
                pass
