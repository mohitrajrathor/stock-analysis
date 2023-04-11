''' python module to fatch stocks data from web '''
import requests
import pandas as pd
import numpy as np
import datetime
import re


# common funcs. 
def date_parser(date):
    if date is None:
            date = datetime.datetime.now()   # choose today if no date is specified
            d, m, y = [int(i) for i in (date.strftime('%d-%m-%Y')).split('-')]
            return (d, m, y)
        else:
            try:
                d, m, y = [int(i) for i in date.split('-')]
            except:
                if re.match('[0-9]+-[0-9]+-[0-9]+', date):
                    raise BadDateFormat("date is not specified in correct format.")
                else:
                    raise UnknownError('Cannot find out error.')

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
        date : (data-type : str) dd-mm-yyyy format
        return : data-type : pandas Dataframe 
        '''
        d, m, y = date_parser(date)


    def bulk_deals(self, date = None):
        '''
        Fatch bulk deals data
        date : (data-type : str) dd-mm-yyyy format 
        return : pd.DataFrame 
        '''
        d, m, y = date_parser(date)

if __name__ == "__main__":
    pass