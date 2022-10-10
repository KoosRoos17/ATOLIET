import discord
import os

from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
  
  print('System Online')
  
Token = os.environ['TOKEN']

client.run(Token)
