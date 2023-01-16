import os
import discord

from dotenv import load_dotenv
from message_parser import parse_message_content
import stonk

load_dotenv()
stonk_bot_token = os.getenv('STONK_BOT_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


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
    await stonk.handle_stonk(symbol, message)
