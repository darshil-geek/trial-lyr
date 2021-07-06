import discord
import lyricsgenius as genius
import config
import random
api = genius.Genius('aKDMKgolc1ZSD_DDH-QjK2YyRymM1_Jc2jFdAkThZLmCAwg0mMYhfdnsbnOrD_Nu') #add genius bot token


from dotenv import load_dotenv
load_dotenv()
import os
token = os.environ.get("TOKEN")
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix = '$')
client.remove_command("help")
@client.event
async def on_ready():
  print('Bot is ready!')



@client.command(aliases=['hi','hello','Hello'])
async def Hi(ctx):
    await ctx.channel.send("What's up!")



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
        title = s,
        description =  '\n'.join(lyrics_list),
        colour = discord.Colour.random() 
    )
  
  await ctx.channel.send(embed=embed) #ctx.send

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


song_lyrics_quotes = [
    "You’ve got enemies? Good, that means you actually stood up for something. – Eminem",

    "You gotta be able to smile through the bullshit. – Tupac",

    "I can see your sad even when you smile even when you laugh I can see if in your eyes deep inside you wanna cry. – Eminem",

    "And I’m thankful for everyday that I’m givin’Both the easy and hard ones I’m livin",

    "It isn’t where I am, It’s only where I’ll go from here",

    'Times Are Hard for Dreamers. - Amelie',

    'Don’t hold me back ’cause today all my dreams will come true! ,Good Morning Baltimore- Hairspray',

    'Emancipate yourselves from mental slavery.None but ourselves can free our minds. ― Bob Marley',


    "Don't criticize what you can't understand. ― Bob Dylan",

    'funny how a beautiful song could tell such a sad story, ― Sarah Dessen, Lock and Key',

    'The story of life is quicker than the wink of an eye, the story of love is hello and goodbye...until we meet again ― Jimi Hendrix',

    "you're an expert at sorry and keeping the lines blurry ― Taylor Swift",


    'Would you destroy Something perfect in order to make it beautiful?― Gerard Way',

    "Get up, stand up, Stand up for your rights. Get up, stand up, Don't give up the fight. ― Bob Marley, Bob Marley - Legend",

    'We all shine on...like the moon and the stars and the sun...we all shine on...come on and on and on...― john lennon',

    "Close your eyes and I'll kiss you, Tomorrow I'll miss you.― Paul McCartney",

    "When pain brings you down, don't be silly, don't close your eyes and cry, you just might be in the best position to see the sun shine. ― Alanis Morissette",


    'Excuse me while I kiss the sky. ― Jimi Hendrix',


    'You have every right to a beautiful life. ― Selena Gomez',


    "You don't know you're beautiful. ― One Direction",

    'Work it, make it, do it, makes us: harder, better, faster, stronger – Daft Punk Harder, Better, Faster',

    'Sing with me, sing for the year, sing for the laughter and sing it for the tear. – Aerosmith “Dream On',

    'Would you destroy Something perfect in order to make it beautiful? ― Gerard Way',

    'I think there is a song out there to describe just about any situation. ― Criss Jami, Killosophy',

    'When pain brings you down, don’t be silly, don’t close your eyes and cry, you just might be in the best position to see the sun shine. ― Alanis Morissette',

    'Love me or hate me, i swear it won’t make or break me. ― Lil Wayne',

    'It’s my life and it’s now or never! Cause I ain’t gonna live forever, I just want live while I’m alive. It’s my life! – Bon Jovi “It’s My Life',

    'Get up, stand up, Stand up for your rights. Get up, stand up, Don’t give up the fight. ― Bob Marley, Bob Marley – Legend',

    'And if at first your don’t succeed, then dust yourself off and try again! – Aaliyah Try Again',

    'Don’t criticize what you can’t understand. ― Bob Dylan',

    'I won’t be afraid just as long as you stand, stand by me. – Ben E. King Stand By Me',

    'I’m a survivor, I’m not gonna give up, I’m not gonna, stop I’m gonna work harder. – Destiny’s Child “Survivor',

    'The story of life is quicker than the wink of an eye, the story of love is hello and goodbye…until we meet again ― Jimi Hendrix',

    'You’re an expert at sorry and keeping the lines blurry. ― Taylor Swift',

    'I will survive! Oh as long as I know how to love I know I will stay alive! – Gloria Gaynor I Will Survive',

    'We are the world, we are the children, we are the ones who make a brighter day, so let’s start giving. – United Support of Artists for Africa We Are The World',

    'Every little thing is gonna be alright! – Bob Marley',

    'Don’t give up. You’ve got a reason to live. Can’t forget you only get what you give. – New Radicals “You Get What You Give',

    'You may say I’m a dreamer, but I’m not the only one. – John Lennon, Imagine',

    'You only get one shot, do not miss your chance to blow. This opportunity comes once in a lifetime – Eminem Lose Yourself',

    'I’d rather laugh with the sinners than cry with the saints, the sinners are much more fun. ― Billy Joel',

    'Don’t stop, never give up. Hold your head high and reach the top. Let the world see what you have got. Bring it all back to you. – S Club 7 ,Bring it all back'
]

lyrics_quotes=song_lyrics_quotes.copy()




@client.command()
async def quotes(ctx):
    x=random.randint(1,30)
    quote=song_lyrics_quotes.pop(x)
    embed= discord.Embed(
        title = "Music Quote",
        description =  quote,
        colour = discord.Colour.random() 
    )
    await ctx.channel.send(embed=embed)

#quiz
@client.command()
async def quiz(ctx,*arg):
  #string = ''
  artist_name=''
  string= arg
  for i in string:
    artist_name = artist_name + " " + i
  artist_details=api.search_artist(artist_name, max_songs=3)
  x=random.randint(0,2)
  song = artist_details.songs.pop(x)
  embed= discord.Embed(
    title = 'Welcome to the Quiz !',
    description=artist_details.songs.artist,
    #description=song,
    colour = discord.Colour.random() 
  )
  await ctx.channel.send(embed=embed)


#for help
@client.command()
async def help(ctx):
    embed= discord.Embed(
        title = 'Lyricist command list',
        description = 'Here you can find a list of commands you can use.',
        colour = discord.Colour.random() 
    )
    embed.add_field(name='$help',value='Use this command to get help about how to use the bot.',inline = True)
    embed.add_field(name='$sng',value='Use this command to get lyrics of songs.(used as $sng song_name)',inline = True)
    embed.add_field(name='$lyr',value='This command is to be used if you do not get the desired lyrics using the $sng command.(used as $lyr artist_name ~ song_name)',inline = True)

    
    embed.set_thumbnail(url='https://picsum.photos/200/300')

    await ctx.channel.send(embed=embed)

client.run(token)
