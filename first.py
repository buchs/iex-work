#!/usr/bin/env python3.5

from iexfinance import Stock
from iexfinance import get_available_symbols as gas

# Documentation on iexfinance: https://addisonlynch.github.io/iexfinance/stable/ref.html

# load all symbols - list 
symbols = gas()

# look at Tesla
tsla = Stock('TSLA')
opn = tsla.get_open()
pri = tsla.get_price()
print('Tesla: open price %f, current price %f' % (opn, pri))

# look at AA (Alcoa?)
aa = Stock('AA')
eps = aa.get_latest_eps()
pri = aa.get_price()
print('AA: latest EPS %f, current price %f' % (eps, pri))

# show symbols and company name for each
# for s in symbols:
#   if s['isEnabled'] == True: print(s['symbol'] + ', ' + s['name'])

# Apple
apple = Stock('AAPL')
apple.get_key_stats()
apple.get_volume()
apple.get_earnings()
apple.get_quote()
apple.get_quote()['peRatio']
apple.get_quote()['close']


def pStock(symbol):
  priceCriteria = 5.00
  data = Stock(symbol)
  quote = data.get_quote()
  pe = quote['peRatio']
  close = quote['close']
  sts = data.get_key_stats() 
  cName = sts['companyName']

  # apply criteria
  if close > priceCriteria:
    return

  # print the results for what is left
  print('%s,%s,%s,%s' % (symbol,cName,close,pe))

# test
# pStock('AAPL')

# Now run against all symbols
for s in symbols:
    pStock(s['symbol'])
