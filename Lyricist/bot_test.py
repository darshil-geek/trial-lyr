import discord
import lyricsgenius as genius
import config

api = genius.Genius('')
api = genius.Genius(config.GENIUS_TOKEN)

from discord.ext import commands
from discord.ext.commands import Bot
import random

TOKEN = ''
TOKEN = config.BOT_TOKEN

client = commands.Bot(command_prefix = '-')
quiz = False
@client.event
async def on_ready():
  print('Bot is ready!')

@client.event
async def on_message(message):
  if message.content.upper() == ('HI'):
    await client.send_message(message.channel, "What's up!")
  
  if message.content.upper() == '-HOW ARE YOU?':
    await client.send_message(message.channel, "I'm doing well(planning on taking over the world), but I would be better if you ask me to search up lyrics :). How about you?")

  if message.content.upper() == '-I AM FINE' or message.content.upper() == "I'M FINE" or message.content.upper()== "I AM GOOD" or message.content.upper()== "I'M GOOD":
    await client.send_message(message.channel, "Brilliant")

  if message.content.upper() == '-WHAT ARE YOU?' or message.content.upper() == '-WHAT DO YOU DO?' or message.content.upper()=='-WHO ARE YOU?':
    await client.send_message(message.channel, "I'm Lyricist! I'm your bot. I can search up lyrics, and even give you some pretty basic info on specific songs.")
    await client.send_message(message.channel, "I'm powered by the LyricsGenius API wrapper, which scrapes song data from the Genius website via their web api. Pretty cool huh?")
    await client.send_message(message.channel, "Type -HELP for more instructions!")

  if message.content.upper() == "-HELP":
    await client.send_message(message.channel, "Here are some useful kewords: \n '-lyr' [artist] - [song] *I'll recite the lyrics, If.. If I can find the song*")
    await client.send_message(message.channel, "'-alb' [artist] - [song] *I'll tell you the album it's featured on, If.. If I can find the song*")
    await client.send_message(message.channel, "'-rel' [artist] - [song] *I'll tell you when the song was released, If.. If I can find the song*")
    await client.send_message(message.channel, "I'm not the smartest bot, so any typos or errors might screw up my search. I'm no Alexa but I'm still cool :D !")

  if message.content.upper().startswith('-LYR'):
    userID = message.author.id
    if message.content.find("-") == -1:
      await client.send_message(message.channel, "Sorry <@%s>, the song search must follow the [artist] - [song] structure. Type *-help* for more details. " % (userID))
    else: 
      args = message.content.lower().replace("-lyr", "").split("-")
      a = args[0]
      s = args[1]
      await client.send_message(message.channel, "Searching for the lyrics to  *{}*  by  *{}* ...".format(s, a))
      song = api.search_song(s, a)
      if song:
        url = song.url
        lyrics = song.lyrics.split("\n")
        for line in lyrics:
          if line == '':
            lyrics.remove(line)
          else:
            await client.send_message(message.channel, "*{}*".format(line))
        await client.send_message(message.channel, "here's a link to the annotated lyrics: \n{}".format(url))
      else:
        await client.send_message(message.channel, "I was unable to find the queried song. My apologies :(  " +
        "Check for typos and try again.")

  if message.content.upper().startswith('-ALB'):
    userID = message.author.id
    if message.content.find("-") == -1:
      await client.send_message(message.channel, "Sorry <@%s>, the song search must follow the [artist] - [song] structure. Type *-help* for more details. " % (userID))
    else: 
      args = message.content.lower().replace('!alb', "").split('-')
      a = args[0]
      s = args[1]
      await client.send_message(message.channel, "Finding the album for  *{}*  by  *{}* ...".format(s, a))
      song = api.search_song(s, a)
      if song:
        if song.album:
          album = song.album
          album_url = song.album_url
          await client.send_message(message.channel, "*{}*  is featured on the album  *{}*  by  *{}*".format(s, album, a))
          await client.send_message(message.channel, "Here's a link to the album on Genius: \n{}".format(album_url))
        else: 
          await client.send_message(message.channel, "I found the song... but is it a single? Because I couldn't find any album associated to it")
      else:
        await client.send_message(message.channel, "I was unable to find the queried song. My apologies :( " +
        "Check for typos and try again.")

  if message.content.upper().startswith('-REL'):
    userID = message.author.id
    if message.content.find("-") == -1:
      await client.send_message(message.channel, "Sorry <@%s>, the song search must follow the [artist] - [song] structure. Type *-help* for more details. " % (userID))
    else: 
      args = message.content.lower().replace('!rel', "").split('-')
      a = args[0]
      s = args[1]
      await client.send_message(message.channel, "Finding the release date for the track  *{}*  by  *{}* ...".format(s, a))
      song = api.search_song(s, a)
      if song:
        if song.year:
          release_date = song.year
          await client.send_message(message.channel, "Release date for  *{}*  by  *{}* :  *{}*".format(s, a, release_date))
        else:
          await client.send_message(message.channel, "I found the song... but I can't seem to determine the release date. I'm sorry, blame Genius xD")
      else:
        await client.send_message(message.channel, "I was unable to find the queried song. My apologies :( " +
        "Check for typos and try again.")
client.run(TOKEN)