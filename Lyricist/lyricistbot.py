import discord
from discord import activity
import lyricsgenius as genius
from discord import Spotify
import config
import random
from dotenv import load_dotenv
load_dotenv()
import os
from discord.ext import commands
from discord import Color
from discord.ext.commands import Bot, bot
import praw
intents = discord.Intents.all()

token = os.environ.get("TOKEN")                       #add Discord Bot token
api = genius.Genius('aKDMKgolc1ZSD_DDH-QjK2YyRymM1_Jc2jFdAkThZLmCAwg0mMYhfdnsbnOrD_Nu')   #add genius token

client = commands.Bot(command_prefix = '.',intents=intents)  #assigning command prefix
client.remove_command("help")


@client.event
async def on_ready():
  print('Bot is ready!')



@client.command(aliases=['hi','hello','Hello','hey','Hey'])
async def Hi(ctx):
    await ctx.channel.send("Hey, what's up!")



#pinging the bot event
'''@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send(f"no pinging bot {message.author.mention} <:kekw:862204617159868437>")
'''

#Spotify lyrics
from discord import Spotify
@client.command()
async def spt(ctx, user: discord.Member = None):
  try:   
    user = user or ctx.author
    for activity in user.activities:
        if isinstance(activity,discord.Spotify):
            spotify_result = activity
        else:
            await ctx.channel.send(f'{user.name} is not playing any songs on Spotify or the discord status has been set invisible.')
      
    if spotify_result!= None:
      
      lyrics_list=[]      #list to store lyrics of the song
      await ctx.channel.send("Searching for lyrics to {}...".format(spotify_result.title))
      song = api.search_song(spotify_result.title,spotify_result.artist)
      if song:
        url = song.url
        await ctx.channel.send("Here's a link to the annotated lyrics: \n{}".format(url))
        lyrics = song.lyrics.split("\n")
        for line in lyrics:
            if line == '':
              lyrics.remove(line)
            else:
              lyrics_list.append(line)
            

      embed= discord.Embed(
        title = "The lyrics to "+song.title,
        description =  '\n'.join(lyrics_list),
        colour = discord.Colour.from_rgb(57,255,20) 
    )
  
      await ctx.channel.send(embed=embed)
  except UnboundLocalError as e:
    await ctx.channel.send("The user is either offline or Spotify is playing ads at the moment. Please try sometime later. ")
    

#invite BOT
@client.command()
async def invite(ctx):
    embed = discord.Embed(title="Invite Lyricist Bot to your Discord Server", url="https://discord.com/api/oauth2/authorize?client_id=860175251559022652&permissions=8&scope=bot",
                          description="Use the following link: https://bit.ly/3dS30LJ", color=discord.Color.from_rgb(57,255,20))
    await ctx.send(embed=embed)



#Finding lyrics using Song name
@client.command()
async def sng(ctx,*arg):
  strng=''       #empty string to store input from user(arg)
  s=''            #empty string to store song name
  strng = arg
  for str in strng:
    s = s + " "+ str

  s
  lyrics_list=[]  #list to store lyrics of the song
  
  if len(arg) == 0:  #if no input from the user
    embed= discord.Embed(
        title = "Error",
        description ="Please enter the song name in the following format: .sng Shape of you",
        colour = discord.Colour.from_rgb(255,7,58) 
    )
    await ctx.channel.send(embed=embed)
  
  if len(arg) !=0:
    await ctx.channel.send("Searching for lyrics to {}...".format(s))
    song = api.search_song(s)
    if song:
        url = song.url
        await ctx.channel.send("Here's a link to the annotated lyrics: \n{}".format(url))
        lyrics = song.lyrics.split("\n")
        for line in lyrics:
          if line == '':
            lyrics.remove(line)
          else:
            lyrics_list.append(line)

        embed= discord.Embed(
        title = "The lyrics to "+song.title,
        description =  '\n'.join(lyrics_list),
        colour = discord.Colour.from_rgb(57,255,20) 
    )               
  
        await ctx.channel.send(embed=embed) 



#Finding lyrics using Artist name and song name
@client.command()
async def lyr(ctx, *arg):
  string = ''     #empty string to store user input(arg)
  a=''            #empty string to store artist name
  s=''            #empty string to store song name
  string = arg

  if len(arg) == 0:  #if no input from the user
    embed= discord.Embed(
        title = "Error",
        description ="Please enter in the following format to search for lyrics: .lyr Coldplay ~ Viva La Vida ",
        colour = discord.Colour.from_rgb(255,7,58) 
    )
    await ctx.channel.send(embed=embed)
  
  
  for str in string:
    if(str == '~'):
      break
    a = a + " " + str

  a

  lyrics_list=[]                               #list to store lyrics of the song
  s_ = string[string.index('~') : len(string)] #Slicing method 
  for _s in s_ :
    if(_s == '~'):
      continue
    s = s + " " + _s

  s
  
  
  if len(arg) !=0:
    await ctx.channel.send("Searching for the lyrics to {} by {} ...".format(s, a))
    song = api.search_song(s, a)
    if song:
      url = song.url
      await ctx.channel.send("Here's a link to the annotated lyrics: \n{}".format(url))
      lyrics = song.lyrics.split("\n")
      for line in lyrics:
          if line == '':
            lyrics.remove(line)
          else:
            lyrics_list.append(line)

      embed= discord.Embed(
        title = 'Embedded lyrics',
        description =  '\n'.join(lyrics_list),
        colour = discord.Colour.from_rgb(57,255,20)
    )
  
      await ctx.channel.send(embed=embed) 



#artist quiz
rando = random.randint(0,2)      #To generate random number
artist_name=''                   #empty string to store artist name
@client.command()
async def art(ctx,*arg):
    artist_name=''                #empty string to store artist name
    string = arg                  #string to store input from user(arg)

    for str in string:
        artist_name = artist_name + str
    if len(arg) == 0:  #if no input from the user
      embed= discord.Embed(
        title = "Error",
        description ="Please enter the artist name in the following format to begin the quiz: .art Coldplay",
        colour = discord.Colour.from_rgb(255,7,58) 
      )
      await ctx.channel.send(embed=embed)
    
    if len(arg) !=0:
      await ctx.channel.send("Please wait for the lyrics....\n")
    
      artist = api.search_artist(artist_name, max_songs=3) 
      song = artist.songs.pop(rando)
      lyrics_list = []
      if song:
          url = song.url
          lyrics = song.lyrics.split("\n")
          for line in lyrics:
            if line == '':
                lyrics.remove(line)
            else:
                lyrics_list.append(line)
    
          embed= discord.Embed(
            title = 'Here are the lyrics',
            description =  '\n'.join(lyrics_list),
            colour = discord.Colour.from_rgb(57,255,20) 
          )

          await ctx.channel.send(embed=embed)

          await ctx.channel.send('Guess the song using .ans [song name] ~ [artist_name] (ex: .ans Viva La Vida ~ Coldplay) ')

@client.command()
async def ans(ctx,*arg):  # .ans Viva La Vida ~ Coldplay
    if len(arg) == 0:
      embed= discord.Embed(
        title = "Error",
        description ="Please enter answer in the following format: .ans Viva La Vida ~ Coldplay ",
        colour = discord.Colour.from_rgb(255,7,58) 
      )
      await ctx.channel.send(embed=embed)
    
    if len(arg) != 0:
      await ctx.channel.send('Please wait for the result....')
      artist_name=''        #empty string to store artist name
      songname=''           #empty string to store song name
      string = arg
      for str in string:
        if str == '~':
            break
        songname = songname + str + " "
    
      a=string[string.index('~') : len(string)]    #Slicing method to get artist name
      for str in a:
        if str == '~':
            continue
        artist_name = artist_name+" "+ str  

      artist = api.search_artist(artist_name,max_songs=3)
      song = artist.songs.pop(rando)
      name = song.title        #assigning title of song to a string
      name = ''.join(name)
      songname = songname[:-1]
      songname = songname.lower()
      name = name.lower()
      if songname == name:
        embed= discord.Embed(
        title = "Correct",
        description ="Well done. The song is indeed "+ name + " by" + artist_name,
        colour = discord.Colour.from_rgb(57,255,20) 
        )
        await ctx.channel.send(embed=embed)
        
      else:
        embed= discord.Embed(
        title = "Incorrect",
        description ="Hard luck. The right answer is "+ name,
        colour = discord.Colour.from_rgb(255,7,58) 
        )
        await ctx.channel.send(embed=embed)
           



#Music quotes
from quotes import song_lyrics_quotes     #importing from quotes.py
@client.command(aliases=['Quotes','QUOTES'])
async def quotes(ctx):
  x=random.randint(0,41)                  #To generate random number
  lyricsquotes = song_lyrics_quotes.copy()
  discordquote = lyricsquotes.pop(x)      #Returning a quote from discord.py
  embed= discord.Embed(
        title = "Quotes from famous artists",
        description =  discordquote,
        colour = discord.Colour.from_rgb(57,255,20) 
    )
  await ctx.channel.send(embed=embed)



#Bot Ping Test
@client.command(aliases=['Ping','PING'])
async def ping(ctx):
    embed = discord.Embed(
        color=discord.Color.from_rgb(57,255,20),
        title="Lyricist Bot - Ping Test",
        description=f"Pong! {round(client.latency * 1000, 2)} ms"
    )
    await ctx.send(embed=embed)

   

#help
@client.command(aliases=['Help','HELP'])
async def help(ctx):
    embed= discord.Embed(
        title = 'Lyricist command list',
        description = 'Here you can find a list of commands you can use.\n',
        colour = discord.Colour.from_rgb(57,255,20) 
    )
    embed.add_field(name='1',value='`.help`: Use this command to get help about how to use the bot.\n',inline = False)
    embed.add_field(name='2',value="`.sng`: Use this command to get lyrics of songs (used as `.sng` song_name [ex: .sng Demons] ). Use `.lyr` if the specified song can't be found])\n",inline = False)
    embed.add_field(name='3',value='`.spt` : Use this command to get the lyrics of the song playing on your spotify\n', inline = False)
    embed.add_field(name='4',value='`.lyr`: Use this command to get lyrics of songs (used as `.lyr` artist_name ~ song_name [ex: `.lyr` Coldplay ~ Viva la Vida])\n',inline = False)    
    embed.add_field(name='5',value="`.art`: Use this command to guess the song of the artist/band mentioned after this command (used as `.art` artist_name [ex: `.art` Imagine Dragons])\n", inline = False)
    embed.add_field(name='6',value="`.quotes`: Use this command to generate a lyrical quote (used as `.quote`)\n", inline= False)
    embed.add_field(name='7',value="`.invite`: Use this command to get the link to invite this bot to your server (used as `.invite`)\n", inline= False)
    embed.add_field(name='8',value="`.ping`: Use this command to check the host server's latency (used as `.ping`)\n", inline= False)
    embed.add_field(name ='9',value="`.imemes` : Use this command to get desimemes.)\n",inline = False)
    embed.add_field(name='10',value="`.progmemes` : Use this command to get memes related to programming.\n", inline= False)
    embed.add_field(name='11',value="`.upmusic` : Use this command to get the latest trends going on in the music industry.\n", inline= False)
    await ctx.channel.send(embed=embed)

#memes
reddit=praw.Reddit(client_id='66q44f4e7k-W9g',
                    client_secret='78Xzv77rYyxq2Nd4vGXhbZ2JCtmQBg',
                    user_agent="trial"
)

@client.command()
async def imemes(ctx):
    meme_choices=["IndianDankMemes","dankinindia","IndianMeyMeys"]
    x=random.choice(meme_choices)
    subreddit= reddit.subreddit(x)
    top=subreddit.hot(limit=50)
    all_subs=[]

    for submission in top:
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    
    embed = discord.Embed(title=name, url=random_sub.url,
                           color=discord.Color.random(),
                           )
    embed.set_image(url=random_sub.url)
    await ctx.send(embed=embed)


@client.command()
async def progmemes(ctx):
    meme_choices=["ProgrammerHumor","programmingmemes"]
    x=random.choice(meme_choices)
    subreddit= reddit.subreddit(x)
    top=subreddit.hot(limit=50)
    all_subs=[]

    for submission in top:
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    
    embed = discord.Embed(title=name, url=random_sub.url,
                           color=discord.Color.random(),
                           )
    embed.set_image(url=random_sub.url)
    await ctx.send(embed=embed)

@client.command()
async def bnews(ctx):
    meme_choices=["Entrepreneur", "startups"]
    x=random.choice(meme_choices)
    subreddit= reddit.subreddit(x)
    top=subreddit.hot(limit=50)
    all_subs=[]

    for submission in top:
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    
    embed = discord.Embed(title=name, url=random_sub.url,
                           color=discord.Color.random(),
                           )
    #embed.set_image(url=random_sub.url)
    await ctx.send(embed=embed)

@client.command()
async def upmusic(ctx):
    meme_choices=["Music","jazznoir"]
    x=random.choice(meme_choices)
    subreddit= reddit.subreddit(x)
    top=subreddit.hot(limit=50)
    all_subs=[]

    for submission in top:
        all_subs.append(submission)
    random_sub=random.choice(all_subs)
    name=random_sub.title
    
    embed = discord.Embed(title=name, url=random_sub.url,
                           color=discord.Color.random(),
                           )
   
    await ctx.send(embed=embed)

client.run(token)
