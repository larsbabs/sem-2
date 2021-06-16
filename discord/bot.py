# bot.py
import os
import random
import requests
from discord.ext import commands
#from dotenv import load_dotenv

#load_dotenv()
TOKEN = "ODIzODkzNTQ4MzY1MzgxNzEy.YFncqQ.COyFeSEPKNP7kXR6xBMj5lrbGPY"

bot = commands.Bot(command_prefix='!')

@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'KANKER JODEN',
        'gotem',
        (
            'Deez, deez, deez, deez, deez.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)


#@bot.command(name='?')
async def nine_nine(ctx):

    help_text = """    "embed": {
    "title": "title ~~(did you know you can have markdown here too?)~~",
    "description": "this supports [named links](https://discordapp.com) on top of the previously shown subset of markdown. ```\nyes, even code blocks```",
    "url": "https://discordapp.com",
    "color": 6053045,
    "timestamp": "2021-04-23T14:06:39.796Z",
    "footer": {
      "icon_url": "https://cdn.discordapp.com/embed/avatars/0.png",
      "text": "footer text"
    },
    "thumbnail": {
      "url": "https://cdn.discordapp.com/embed/avatars/0.png"
    },
    "image": {
      "url": "https://cdn.discordapp.com/embed/avatars/0.png"
    },
    "author": {
      "name": "author name",
      "url": "https://discordapp.com",
      "icon_url": "https://cdn.discordapp.com/embed/avatars/0.png"
    },
    "fields": [
      {
        "name": "🤔",
        "value": "some of these properties have certain limits..."
      },
      {
        "name": "😱",
        "value": "try exceeding some of them!"
      },
      {
        "name": "🙄",
        "value": "an informative error should show up, and this view will remain as-is until all issues are fixed"
      },
      {
        "name": "<:thonkang:219069250692841473>",
        "value": "these last two",
        "inline": true
      },
      {
        "name": "<:thonkang:219069250692841473>",
        "value": "are inline fields",
        "inline": true
      }
    ]
  }"""
    await ctx.send(str(help_text))
bot.run(TOKEN)