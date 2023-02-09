import os
import discord
from polygon import RESTClient
from dotenv import load_dotenv
from message_parser import parse_message_content
import stonk

load_dotenv()

# initialize Discord API client
stonk_bot_token = os.getenv('STONK_BOT_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# initialize Polygon API client
polygon_api_key = os.getenv('POLYGON_API_KEY')
polygonClient = RESTClient(api_key=polygon_api_key)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if (message.content == "$stonk"):
    await stonk.handle_help(message)
    return

  passed, symbol = parse_message_content(message.content)
  if not passed:
    return

  if symbol is None:
    await message.reply("No symbol found. For help, try $stonk $help")
    return

  if symbol == "$help":
    await stonk.handle_help(message)
  else:
    await stonk.handle_stonk(polygonClient, symbol, message)
