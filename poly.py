from from_to import from_to


def growth_rate(data):
  previousClose, lastClose = data[1].close, data[0].close
  return (lastClose - previousClose) / previousClose

def close_price(data):
  return data[0].close

def fetch_stock_price_data(stockApiClient, symbol):
  from_, to = from_to()
  data = stockApiClient.get_aggs(
      ticker=symbol,
      multiplier=1,
      timespan="day",
      from_=from_,
      to=to,
      adjusted=True,
      sort="desc",
      limit=50,
  )
  info = stockApiClient.get_ticker_details(symbol)

  price = close_price(data)
  growth = growth_rate(data)
  name = info.name
  return price, growth, name
