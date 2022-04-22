import discord
import os
import requests
import json
import re

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

help_command = commands.DefaultHelpCommand(
    no_category = 'Commands'
)

client = commands.Bot(command_prefix="$", description="Hey there, I'm the GoHorse bot!", help_command=help_command)

## client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.command()
async def hello(ctx):
  await ctx.send("Hello " + ctx.author.name + "!")

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  await client.change_presence(activity=discord.Game('GoHorse'))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$inspireme') or message.content.startswith('$inspireMe'):
    quote = get_quote()
    await message.channel.send(quote)
  else:
    print(message)
    result = re.search("0x([a-fA-F]|[0-9]){40}", message.content)
    if result:
        await message.channel.purge(limit=1)
    await client.process_commands(message)

client.run(os.environ['TOKEN'])