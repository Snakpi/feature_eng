api_key = 'et2e34iAR7xpJj9TtAaH'
import pandas as pd
import pandas_datareader.data as web
def get_symbols(symbols, source, start=None, end=None): 
    out = pd.DataFrame()
    for sym in symbols:
        df = web.DataReader(sym, source, start, end, access_key=api_key)[['AdjOpen', 'AdjHigh','AdjLow', 'AdjClose', 'AdjVolume']].reset_index()
        df.columns = ['date', 'open', 'high', 'low', 'close', 'volume']
        df['symbol'] = sym
        df = df.set_index(['date', 'symbol'])
        out = pd.concat([out, df], axis=0) ### for stacking on top of previous data 
    return out
