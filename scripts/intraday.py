from tvDatafeed import TvDatafeed, Interval
import json
import pprint
import fin_data
import pandas as pd


# Intraday stocks selection Stretegy:
# 1. High Demand(liquidity)
# 2. High price fluctuations
# 3. Market Trends
# 4. Sector Trends
# 5. Momentum Stocks
# 6. Technical analysis

# indicators funcs.
def MA(data: pd.DataFrame, period: int, name=None):
    data[f"MA{period}"] = data['Close'].rolling(period).mean()
    return data[f"MA{period}"]


def RSI(data: pd.DataFrame, period: int, name=None):
    data['RSI'] = None


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

tv = TvDatafeed(user, pwd)

stocks = []

# method apply on data will be putted there.
for sym in bhav["SYMBOL"]:
    data = tv.get_hist(symbol=sym, exchange='NSE',
                       interval=Interval.in_5_minute, n_bars=1000)
