import yfinance as yf


def fetch_price_data(symbol):
  ticker = yf.Ticker(symbol)
  today = ticker.history(period='1d')
  close_price = today['Close'].get(0)
  return close_price


async def handle_stonk(symbol, message):
  price = fetch_price_data(symbol)
  if symbol is None or price is None:
    await message.reply("No data found for {}".format(symbol))
    return

  await message.reply("{}: ${:,.5f}".format(symbol, price))


async def handle_help(message):
  content = """
  $stonk [SYMBOL]
  
  Examples:
  - $stonk $help: show this help message
  - $stonk AAPL: show the latest stock price of AAPL
"""
  await message.reply(content)
