#feature dev for bacol
import os
import discord
import random
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import webserver
from webserver import keep_alive
from datetime import datetime
import instaloader

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

#bacol feature request image in specific date
#problem 25-06-2020: downloaded file can not be send directly to discord
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    thot, tahun, bulan, tanggal = message.content.split(" ") #split user input
    if message.content == thot + " " + tahun + " " + bulan + " " + tanggal:
      mod=instaloader.Instaloader()

      posts = instaloader.Profile.from_username(mod.context, thot).get_posts()

      SINCE = datetime(int(tahun), int(bulan), int(tanggal)-10)  # further from today, inclusive
      UNTIL = datetime(int(tahun), int(bulan), int(tanggal))  # closer to today, not inclusive

      cunt = 0  # initiate count

      for post in posts:
        postdate = post.date

        if postdate > UNTIL:
            continue
        elif postdate <= SINCE:
            cunt += 1
            if cunt == 2:
                break
            else:
              continue
        else:
            cunt = 0  #set count to 0
            file = discord.File(mod.download_post(post, thot), filename="if she breaths, she's a thot")
            await message.channel.send(file)