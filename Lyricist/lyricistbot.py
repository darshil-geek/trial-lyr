import discord
import lyricsgenius as genius
import config
import random

api = genius.Genius('aKDMKgolc1ZSD_DDH-QjK2YyRymM1_Jc2jFdAkThZLmCAwg0mMYhfdnsbnOrD_Nu') #add genius bot token
#api = genius.Genius(config.GENIUS_TOKEN)
from dotenv import load_dotenv
load_dotenv()
import os
token = os.environ.get("TOKEN")
from discord.ext import commands
from discord.ext.commands import Bot

#TOKEN = '' #add discord bot token
#TOKEN = config.BOT_TOKEN

client = commands.Bot(command_prefix = '$')
client.remove_command("help")
@client.event
async def on_ready():
  print('Bot is ready!')

@client.command(aliases=['hi','hello','Hello','hey','Hey'])
async def Hi(ctx):
    await ctx.channel.send("Hey,what's up!")

@client.command(aliases=['Info','INFO'])
async def info(ctx):
  embed = discord.Embed(
    title ='BOT INFO',
    description ="I'm Lyricist! I'm your bot. I can search up lyrics, and even give you some pretty basic info on specific songs. \n " +
                "I'm powered by the LyricsGenius API wrapper, which scrapes song data from the Genius website via their web api. Pretty cool huh? \n "+
                "Type $HELP for more instructions! \n",
    colour=discord.Color.random()
)
  await ctx.channel.send(embed=embed)

@client.command()
async def invite(ctx):
    embed = discord.Embed(title="Invite Lyricist Bot to your Discord Server", url="https://discord.com/api/oauth2/authorize?client_id=860175251559022652&permissions=8&scope=bot",
                          description="Use the following link: https://discord.com/api/oauth2/authorize?client_id=860175251559022652&permissions=8&scope=bot", color=discord.Color.random())
    await ctx.send(embed=embed)

#lyrics basic
@client.command()
async def sng(ctx,*arg):
  string=''
  s=''
  string = arg
  for str in string:
    s = s + " "+ str

  s
  lyrics_list=[]
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
            #lyrics_str+=line
            lyrics_list.append(line)
            #await ctx.channel.send("{}".format(line))
      #await ctx.channel.send(lyrics_str) #sending the lyrics in one ugly string

  embed= discord.Embed(
        title = "The lyrics to "+song.title,
        description =  '\n'.join(lyrics_list),
        colour = discord.Colour.random() 
    )
  
  await ctx.channel.send(embed=embed) #ctx.send

#lyrics advanced
@client.command()
async def lyr(ctx, *arg):
  string = ''
  a=''
  s=''
  string = arg
  for str in string:
    if(str == '~'):
      break
    a = a + " " + str

  a
  lyrics_str=''
  lyrics_list=[]
  s_ = string[string.index('~') : len(string)]
  for _s in s_ :
    if(_s == '~'):
      continue
    s = s + " " + _s

  s
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
            #lyrics_str+=line
            lyrics_list.append(line)
            #await ctx.channel.send("{}".format(line))
      #await ctx.channel.send(lyrics_str) #sending the lyrics in one ugly string

  embed= discord.Embed(
        title = 'Embedded lyrics',
        description =  '\n'.join(lyrics_list),
        colour = discord.Colour.random() 
    )
  
  await ctx.channel.send(embed=embed) #ctx.send



#artist quiz
rando = random.randint(0,2)
artist_name=''
@client.command()
async def quiz(ctx):
  embed = discord.Embed(
    title = 'Quiz',
    description = "\n How well do you know your favourite artist? Let's see if you can identify some of their best tracks! \n Enter an artist's name:(ex: $art The Weeknd) \n Identify the song from the lyrics:(ex: $ans Starboy ~ The Weeknd) : \n",
    colour = discord.Colour.random()
  )

  await ctx.channel.send(embed=embed)

@client.command()
async def art(ctx,*arg):
    artist_name=''                #empty string to store artist name
    string = arg
    for str in string:
        artist_name = artist_name + str
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
        colour = discord.Colour.random() 
    )

    await ctx.channel.send(embed=embed)

    await ctx.channel.send('Guess the song using $adns [song name] ~ [artist_name]')

@client.command()
async def ans(ctx,*arg):      # $name Viva La Vida ~ Coldplay
    await ctx.channel.send('Please wait for the result....')
    artist_name=''
    songname=''                    #empty string to store song name
    string = arg
    for str in string:
        if str == '~':
            break
        songname = songname + str + " "
    a=string[string.index('~') : len(string)]
    for str in a:
        if str == '~':
            continue
        artist_name = artist_name+" "+ str  #string stored artist name
               
    artist = api.search_artist(artist_name,max_songs=3)
    song = artist.songs.pop(rando)
    name = song.title
    name = ''.join(name)
    songname = songname[:-1]
    #songname=songname.lower
    #name=name.lower
    #print(type(name))
    if songname == name:
        await ctx.channel.send("Correct. Well done!")
    else:
        await ctx.channel.send("Incorrect. The right answer is "+ name)   


#quotes

from quotes import song_lyrics_quotes
@client.command()
async def quotes(ctx):
  x=random.randint(0,41)
  lyricsquotes = song_lyrics_quotes.copy()
  discordquote = lyricsquotes.pop(x)
  embed= discord.Embed(
        title = "Music Quote",
        description =  discordquote,
        colour = discord.Colour.random() 
    )
  await ctx.channel.send(embed=embed)



@client.command()
async def ping(ctx):
    embed = discord.Embed(
        color=discord.Color.blue(),
        title="Lyricist Bot - Ping Test",
        description=f"Pong! {round(client.latency * 1000, 2)} ms"
    )
    await ctx.send(embed=embed)
#emote = 'https://cdn.discordapp.com/emojis/792797495431528519.png?v=1'
@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.channel.send(f"no pinging bot {message.author.mention} <:kekw:862204617159868437>")

#help
@client.command(aliases=['Help'])
async def help(ctx):
    embed= discord.Embed(
        title = 'Lyricist command list',
        description = 'Here you can find a list of commands you can use.',
        colour = discord.Colour.random() 
    )
    embed.add_field(name='1',value='`$help`: Use this command to get help about how to use the bot.',inline = False)
    embed.add_field(name='2',value='`$info`: Use this command to get basic info of the bot.',inline = False)
    embed.add_field(name='3',value='`$lyr`: Use this command to get lyrics of songs.(used as `$lyr` artist_name ~ song_name[ex: `$lyr` Coldplay ~ Viva la Vida])',inline = False)
    embed.add_field(name='4',value="`$sng`: Use this command to get lyrics of songs.(used as `$sng` song_name[ex: $sng Demons]) .Use `$lyr` if the specified song can't be found])",inline = False)
    embed.add_field(name='5',value="`$quiz`: Use this command for a quiz. Follow the commands given religiously",inline = False)
    embed.add_field(name='6',value="`$art`: Use this command to start the quiz.(used as `$art` artist_name[ex: `$art` Imagine Dragons])", inline = False)
    embed.add_field(name='7',value="`$ans`: Use this command to give input for the asnwer of the quiz.(used as `$ans` song_name ~ artist_name[ex: `$ans` Believer ~ Imagine Dragons])", inline = False)
    embed.add_field(name='8',value="`$quotes`: Use this command to generate a lyrical quote.(used as `$quote`)", inline= False)
    embed.add_field(name='9',value="`$invite`: Use this command to get the link to invite this bot to your server.(used as `$invite`)", inline= False)
    embed.add_field(name='10',value="`$ping`: Use this command to check the host server's latency.(used as `$ping`)", inline= False)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/858669942160883724/862036601411862538/iu.png')

    await ctx.channel.send(embed=embed)

client.run(token)
