import yfinance as yf

def growth_rate(data):
  previouseClose, lastClose = data['Close'][-2], data['Close'][-1]
  return (lastClose - previouseClose) / previouseClose

def close_price(data):
  return data['Close'][-1]

def fetch_stock_price_data(symbol):
  ticker = yf.Ticker(symbol)
  data = ticker.history(period='7d')
  info = ticker.info

  price = close_price(data)
  growth = growth_rate(data)
  name = info.name
  return price, growth, name
