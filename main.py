#discord bot to download instagram image/video
#discord package documentation https://discordpy.readthedocs.io/en/latest/
#instaloader package documentation https://instaloader.github.io/cli-options.html
#author: https://github.com/pounder8686 & https://github.com/richardilot

import os
import random
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import webserver
from webserver import keep_alive
import time

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

#message responder function
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    welcomeMessage = ['haha funny poop',
                      'bing bong',
                      (
                          'bing bong bing bong bing bong'
                         ),
                     ]

    if message.content == 'hi':
        response = random.choice(welcomeMessage)
        await message.channel.send(response)

keep_alive()
client.run(TOKEN)