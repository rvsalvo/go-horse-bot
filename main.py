import discord
import os
import requests
import json
import re

from dotenv import load_dotenv
load_dotenv()

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send("Hello " + message.author.name + "!")
  elif message.content.startswith('$inspireMe'):
    quote = get_quote()
    await message.channel.send(quote)
  else:
    print(message)
    result = re.search("0x([a-fA-F]|[0-9]){40}", message.content)
    if result:
        await message.channel.purge(limit=1)
  

client.run(os.environ['TOKEN'])