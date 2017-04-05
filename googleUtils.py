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
