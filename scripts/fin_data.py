''' python module to fatch stocks data from web '''

# libraries.
import requests                # making web requests
import pandas as pd            # dealing with csv files
import numpy as np             # deal with large arrays
import zipfile, os, re, datetime


# constants.
headers = {
    'user-agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36'
}    # used to indicate that a webbrowser is requesting a web page.


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
            date : (data-type : str) ddmmmyyyy format e.g. for 17-APR-2023 it is 17APR2023
        return -> data-type : pandas Dataframe 
        link : 
            https://archives.nseindia.com/content/historical/EQUITIES/2023/APR/cm17APR2023bhav.csv.zip
        '''
        if date is None:
            date = datetime.datetime.now().strftime('%d%b%Y')

        try :
            res = requests.get(f'https://archives.nseindia.com/content/historical/EQUITIES/2023/APR/cm{date.lower()}bhav.csv.zip', headers= headers)
            print(res.status_code)
            bhav = res.content
            with open('I:\\Programming\\WorkShop\\stock-analysis\\data\\bhav.zip', 'wb') as z:
                z.write(bhav)
            with open('I:\\Programming\\WorkShop\\stock-analysis\\data\\bhav.csv', 'r') as bhav:
                with zipfile.ZipFile('I:\\Programming\\WorkShop\\stock-analysis\\data\\bhav.csv') as z:
                    with z.open(f'cm{date}bhav.csv', 'rb') as c:
                        bhav.write(c.read())

            os.remove('I:\\Programming\\WorkShop\\stock-analysis\\data\\bhav.zip')
            flag = False

        except Exception as e:
            print(e)
            flag = True

        finally:
            if flag:
                print('Fatching bhavcopy failed. :(')
            else:
                print('Successfully Fatched bhavcopy.')


    def bulk_deals(self):
        '''
        Fatch bulk deals data 
        return -> pd.DataFrame 
        '''
        return pd.read_csv('https://archives.nseindia.com/content/equities/bulk.csv')


class yahoo:
    def __init__(self) -> None:
        pass

    def historical_data(self, symbol: str, _from:str, to = datetime.datetime.now().strftime('%d-%m-%Y') ):
        '''
        Fatch historical data:
        params:
            symbol : stocks or etf symbol
            _from  : starting date from (dd-mm-yyyy)
            to     : end date (dd-mm-yyyy)

        link : 
            https://query1.finance.yahoo.com/v7/finance/download/SBIN.NS?period1=1673827200&period2=1681603200&interval=1d&events=history&includeAdjustedClose=true
        '''
        start_date = int(datetime.datetime(*(list(reversed([int(i) for i in _from.split('-')]))), 5, 30, 0).timestamp())
        end_date = int(datetime.datetime(*(list(reversed([int(i) for i in to.split('-')]))), 17, 30, 0).timestamp())

        res = requests.get(f'https://query1.finance.yahoo.com/v7/finance/download/{symbol}.NS?period1={start_date}&period2={end_date}&interval=1d&events=history&includeAdjustedClose=true', headers = headers)

        with open(f'.\\data\\{symbol}.csv', 'wb') as fh:
            fh.write(res.content)

        return f'data\\{symbol}.csv'  # return the name or locaion of the file so that we can
                                      #  easily find out the location of the csv file.

    




if __name__ == "__main__":
    ticker = yahoo()
    print(ticker.historical_data('SBIN', '01-04-2023'))