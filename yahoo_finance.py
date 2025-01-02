import yfinance as yf

msft = yf.Ticker('MSFT')

#print(msft.info)

hist = msft.history(period='1y')
#print(hist)

#metadata
#print(msft.history_metadata)

#print(msft.actions)

#print(msft.dividends)

#print(msft.splits)

#print(msft.capital_gains)

print(msft.get_shares_full(start='2022-11-11', end=None))