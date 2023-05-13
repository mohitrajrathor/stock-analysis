# libraries used
import pandas as pd
import numpy as np

# Indicator programs

# SMA :- Simple Moving Average.
def SMA(col: pd.Series, period: int = 50):
    """
    Calculate SMA using given column
    col : pd.Series
    period : int (default)
    """
    return col.rolling(period).mean().round(2)

# RSI :- Relative Strength Index.
def RSI(change : pd.Series, period: int = 14):
    """
    calculate RSI using price change data.
    change : pd.Sereies
    period : int
    """
    gain = change.where(change > 0, 0)
    loss = change.where(change < 0 , 0)
    loss = loss.abs()
    avgain = gain.rolling(period).mean()
    avloss = loss.rolling(period).mean()
    rs = avgain / avloss
    rsi = 100 - (100 / (1 + rs))
    return rsi.round(2)

# ADX :- Average Directional Index
def ADX(high, low, close, period:int = 14):
    TR = pd.DataFrame({
        'a': high - low,
        'b': abs(high - close.shift()),
        'c': abs(low - close.shift())
    }).max(axis=1)

    # Calculate the Directional Movement (DM)
    DMplus = (high - high.shift()) > (low.shift() - low)
    DMminus = (low.shift() - low) > (high - high.shift())

    # Calculate the True Directional Indicator (+DI) and (-DI)
    TR14 = TR.rolling(window=period).sum()
    DM14plus = DMplus.rolling(window=period).sum()
    DM14minus = DMminus.rolling(window=period).sum()

    DIplus14 = DM14plus / TR14 * 100
    DIminus14 = DM14minus / TR14 * 100

    # Calculate the Directional Movement Index (DMI)
    DX14 = abs(DIplus14 - DIminus14) / (DIplus14 + DIminus14) * 100
    ADX14 = DX14.rolling(window=period).mean()
    return ADX14.round(2)


# calcualte volume weigthed average price.
def VWAP(price: pd.Series, vol:pd.Series, period:int = 14) -> pd.Series:
    num = price * vol
    vmp = num.rolling(period).sum() 
    sv = vol.rolling(period).sum()
    return vmp/sv