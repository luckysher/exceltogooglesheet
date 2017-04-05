#######################################################
##             EXCEL TO GOOGLE SHEET                 ##
#######################################################

About Project:
--------------
 The 'EXCEL TO GOOGLE SHEET' is python application that for writing the excel sheets data to the google spread sheets.
 This application uses the 'Google spread sheet API', python 'xlrd' package for reading the data from the simple excel
 files and write/read data from/to google sheets.

Setting up project requirements:
 -------------------------------
 $ pip install -r requirements.txt

How to get the client ID, secrets
 ------------------------------
 Go to link:
 - https://console.developers.google.com/flows/enableapi?apiid=sheets.googleapis.com
 - login to using gmail credentials

 then
 - Click Continue, then Go to credentials.
 - On the Add credentials to your project page, click the Cancel button.
 - At the top of the page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button.
 - Select the Credentials tab, click the Create credentials button and select OAuth client ID.
 - Select the application type Other, enter the name "Google Sheets API Quickstart", and click the Create button.
 - Click OK to dismiss the resulting dialog.
 - Click the file_download (Download JSON) button to the right of the client ID.
 - Move this file to your working directory and rename it client_secret.json.


Runing test cases:
 ------------------
 # todo