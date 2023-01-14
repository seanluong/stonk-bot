import os
import discord
import yfinance as yf

stonk_bot_token = os.environ['STONK_BOT_TOKEN']

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


def parse_message_content(content):
  prefix = "$stonk "
  if not content.startswith(prefix):
    return False, None

  rest = content[len(prefix):].strip()
  if len(rest) == 0:
    return True, None

  return True, rest.split()[0]


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


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if (message.content == "$stonk"):
    await handle_help(message)
    return

  passed, symbol = parse_message_content(message.content)
  print(passed, symbol)
  if not passed:
    return

  if symbol is None:
    await message.reply("No symbol found. For help, try $stonk $help")
    return

  if symbol == "$help":
    await handle_help(message)
  else:
    await handle_stonk(symbol, message)


client.run(stonk_bot_token)
