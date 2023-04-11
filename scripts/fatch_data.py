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

class UnknownError(Exception):
    """ raised when error is not known. """
    pass

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




# main class section.
class NseIndia:
    """ NseIndia : class to get data from National Stocks Exchange of india. """
    def __init__(self):
        pass

    def get_bhavcopy(self, date = None):
        '''
        Fatch bhavcopy
        parms ->
            date : (data-type : str) dd-mm-yyyy format
        return -> data-type : pandas Dataframe 
        '''
        d, m, y = date_parser(date)
        y = y % 100
        return pd.read_csv(f'https://archives.nseindia.com/archives/sme/bhavcopy/sme{d}{m}{y}.csv') # wrong link


    def bulk_deals(self):
        '''
        Fatch bulk deals data 
        return -> pd.DataFrame 
        '''
        return pd.read_csv('https://archives.nseindia.com/content/equities/bulk.csv')


if __name__ == "__main__":
    pass