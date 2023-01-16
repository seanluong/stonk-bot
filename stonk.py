import yfinance as yf

from number_formatter import format_growth_rate, format_price


def growth_rate(data):
  previouseClose, lastClose = data['Close'][-2], data['Close'][-1]
  return (lastClose - previouseClose) / previouseClose

def close_price(data):
  return data['Close'][-1]

def fetch_price_data(symbol):
  ticker = yf.Ticker(symbol)
  data = ticker.history(period='7d')
  info = ticker.info
  return data, info

async def handle_stonk(symbol, message):
  if symbol is None:
    await message.reply("Ticker symbol cannot be empty")
    return

  try:
    data, info = fetch_price_data(symbol)
    price = close_price(data)
    growth = growth_rate(data)
    name = info["shortName"]
    await message.reply("{} ({}): {} {}".format(symbol, name, format_price(price), format_growth_rate(growth)))
  except Exception as error:
    print(error)
    await message.reply("Cannot get data for {}".format(symbol))
    return


async def handle_help(message):
  content = """
  $stonk [SYMBOL]
  
  Examples:
  - $stonk $help: show this help message
  - $stonk AAPL: show the latest stock price of AAPL
"""
  await message.reply(content)
