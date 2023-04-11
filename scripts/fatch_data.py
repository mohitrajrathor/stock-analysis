''' python module to fatch stocks data from web '''
import requests
import pandas as pd
import numpy as np
import datetime
import re


# exceptions class.
class BadDateFormat(Exception):
    """ raised if date is not specified in correct or instructed format. """
    pass

class UnKnownErrors(Exception):
    """ raised when error is not known. """
    pass



# main class section.
class NseIndia:
    """ NseIndia : class to get data from National Stocks Exchange of india. """
    def __init__(self):
        pass

    def get_bhavcopy(self, date = None):
        '''
        Fatch bhavcopy
        date : (data-type : str) dd-mm-yyyy formate
        return : (data-type : pandas Dataframe) 
        '''
        if date is None:
            date = datetime.datetime.now()   # choose today if no date is specified
        else:
            try:
                d, m, y = [int(i) for i in date.split('-')]
            except:
                if re.match('[0-9]+-[0-9]+-[0-9]+', date):
                    raise BadDateFormat("date is not specified in correct format.")
                else:
                    raise UnknownError('Cannot find out error.')