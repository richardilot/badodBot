#discord bot to download instagram image/video
#discord package documentation https://discordpy.readthedocs.io/en/latest/
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


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})')

    #bot status or activity, or whatever the fuck you want to call it
    await client.change_presence(
        activity=discord.Game(name='as Offensive Bot'))


@client.event
#message responder function
async def on_message(message):
    if message.author == client.user:
        return

    userMessage = message.content

    #welcome message "hi"
    welcomeMessage = [
        'haha funny poop', 'bing bong', 'stinky poop',
        'bing bong bing bong bing bong', 'nobody fucking cares'
    ]

    if userMessage == 'hi':
        response = random.choice(welcomeMessage)
        await message.channel.send(response)

    #magic word
    magicWords = ['no homo', 'no simp', 'sekadar mengingatkan']

    if userMessage == 'magic word':
        magic = random.choice(magicWords)
        await message.channel.send(magic)

    #LGBTQ is a joke
    whyAreYouGay = ['TRUE', 'FALSE']

    if userMessage == 'am i gay?':
        gay = random.choice(whyAreYouGay)
        await message.channel.send(gay)

        #random quotes to motivates making this piece of shit bot
    motivationalQuotes = [  
      #churchill WWII
      "\"If you're going through hell, keep going.\"\n-Winston Churchill",
      #michael reeves twitch stream
      "\"Advice that I would've wanted, I'd say, to trust my gut more when I was starting out on programming.\"\n-Michael Reeves",
      #elon musk ted-talk
      "\"I do think there’s a good framework for thinking. It is physics. You know, the sort of first principles reasoning. Generally I think there are — what I mean by that is, boil things down to their fundamental truths and reason up from there, as opposed to reasoning by analogy.\"\n-Elon Musk",
      #elon musk AMA reddit
      "\"It is important to view knowledge as sort of semantic tree. Make sure you understand the fundamental principles, ie the trunk and big branches, before you get into the leaves/details or there is nothing for them to hang on to.\"\n-Elon Musk",
      #elon musk the book
      "\"Good ideas are always crazy until they’re not.\"\n-Elon Musk",
      #james may top gear
      "\"Oh cock.\"\n-James May",
      #steve jobs Silicon Valley: a 100 Year Renaissance
      "\"We had nothing to lose, and we had everything to gain. And we figured even if we crash and burn, and lose everything, the experience will have been worth ten time the cost.\"\n-Steve Jobs"
      ]
      
    if userMessage == "motivation":
      quote = random.choice(motivationalQuotes)
      await message.channel.send(quote)

    #Geneva convention, more like geneva suggestion
    frontText, dumbText = userMessage.split('-', 1)

    literalGods = [
        'Gandhi', 'Stalin', 'Hitler', 'Your Mom', 'Frozone', 'Mr. Krab'
    ]
    quotingGandhi = '\"' + dumbText + '\"\n' + '-' + random.choice(literalGods)

    command = 'quote this'
    if command in frontText:
        await message.channel.send(quotingGandhi)


keep_alive()
client.run(TOKEN)
