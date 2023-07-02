import os
#from tvDatafeed import TvDatafeed, Interval
import json
import pprint
import financeData
import pandas as pd
from indicator import *
import numpy as np


# Intraday stocks selection Stretegy:
# 1. High Demand(liquidity)
# 2. High price fluctuations
# 3. Market Trends
# 4. Sector Trends
# 5. Momentum Stocks
# 6. Technical analysis



# making symbol list
bhav = pd.read_csv(
    "I:\\Programming\\WorkShop\\stock-analysis\\data\\bhav21APR2023.csv")
bhav = bhav[
    (bhav["SERIES"] == "EQ") & (bhav["TOTTRDQTY"] > 50000) & (
        bhav["LAST"] < 1000) & (bhav["TOTALTRADES"] > 20000)
]

# fatching data with tvdatafeed.
with open("I:\\Programming\\WorkShop\\Conf-Data\\password.json", 'r') as fh:
    pswd = fh.read()
    pD = json.loads(pswd)

user = pD["TradingView"]["user"]
pwd = pD["TradingView"]["password"]
print(user, pwd)

#tv = TvDatafeed(user, pwd)

stocks = []

# method apply on data will be putted there.

# data = tv.get_hist(symbol='BANKBARODA', exchange='NSE',
#                        interval=Interval.in_5_minute, n_bars=1000)
# print(list(data.iloc[-1]))

# for sym in bhav["SYMBOL"]:
#     try:
#         data = tv.get_hist(symbol = sym, exchange='NSE',
#                         interval=Interval.in_5_minute, n_bars=1000)
#         data['SMA20'] = SMA(data['close'], period = 20)
#         data['RSI14'] = RSI(data['close']-data['open'], 14)
#         data["ADX14"] = ADX(data['high'], data['low'], data['close'])
#         lstrow = list(data.iloc[-1])
#         if lstrow[-1] >= 25 and lstrow[-2] <= 30:
#             stocks.append(lstrow[0])
#             if lstrow[-3] < lstrow[-5]:
#                 print("Bullish", end=" ")
#             print(lstrow)
#     except Exception as e:
#         print(sym)

ma = []
volume = []

yahoo = financeData.yahoo()

for tic in bhav['SYMBOL']:
    path = yahoo.historical_data(tic, '01-01-2023')
    data = pd.read_csv(path)
    data['SMA5'] = SMA(data['Close'],period=5)
    data['SMA25'] = SMA(data['Close'],period=25)
    data['RSI14'] = RSI(data['Close'] - data['Open'], 14)
    data['ADX'] = ADX(data['High'], data['Low'], data['Close'])
    lr = data.iloc[-1]
    if lr[-1]>25 and abs(lr[-4]-lr[-3])/lr[-3]*100 < 1:
        ma.append(tic)
    if lr[-5] > 10*data['Volume'].iloc[-21:-1].mean():
        volume.append(tic)

    os.remove(path)
    # print(data.iloc[-1])
    
    
print('Moving Average Stocks:')
manpy = np.array(ma)
print(manpy)
np.save('moving_avg_stocks', manpy)

print('Volume gainer Stocks:')
volnpy = np.array(volume)
print(volnpy)
np.save('volume_gainer',volnpy)