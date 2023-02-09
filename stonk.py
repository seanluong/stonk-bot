from from_to import from_to
from number_formatter import format_growth_rate, format_price
import poly
import yahoo

HELP_CONTENT = """
  $stonk [SYMBOL]
  
  Examples:
  - $stonk $help: show this help message
  - $stonk AAPL: show the latest stock price of AAPL
"""

def use_polygon(client, symbol):
  try:
    price, growth, name = poly.fetch_stock_price_data(client, symbol)
  except Exception as error:
    print("Failed to fetch data from Polygon {}".format(error))
    return None, False
  return (price, growth, name), True

def use_yahoo(symbol):
  try:
    price, growth, name = yahoo.fetch_stock_price_data(symbol)
  except Exception as error:
    print("Failed to fetch data from Yahoo! Finance {}".format(error))
    return None, False
  return (price, growth, name), True

async def reply(message, results, symbol):
  price, growth, name = results
  await message.reply("{} ({}): {} {}".format(symbol, name, format_price(price), format_growth_rate(growth)))

async def handle_stonk(stockApiClient, symbol, message):
  if symbol is None:
    await message.reply("Ticker symbol cannot be empty")
    return

  results, success = use_polygon(stockApiClient, symbol)
  if success:
    await reply(message, results, symbol)
    return

  results, success = use_yahoo(symbol)
  if success:
    await reply(message, results, symbol)
    return
  
  await message.reply("Cannot get data for {}".format(symbol))


async def handle_help(message):
  await message.reply(HELP_CONTENT)
