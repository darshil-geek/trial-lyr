import lyricsgenius as genius
import config
api = genius.Genius(config.GENIUS_TOKEN)

#The following is a scratch file for the genius bot

def get_lyrics():
  """This function allows the user to search for specific song lyrics by inputing the artist and song name"""
  a = input('Enter an artist`s name: (ex: Coldplay)')
  a
  s = input('Enter a song by this artist: (Viva La Vida)')
  s

  lyrics = api.search_song(s, a).lyrics
  print(lyrics)

def artist_quiz():
  """This function asks a trivia question (concerning lyrics) for the user's favorite artist"""
  print('How well do you know your favorite artist`s music??! Let`s see if you can identify some of their best tracks!')
  a = input('Enter an artist`s name: (ex: Kendrick Lamar) ')
  artist = api.search_artist(a, max_songs=3)
  song = artist.songs.pop()
  print('Here come the lyrics...')
  print(song.lyrics)
  answer = input('Name this song: ')
  if answer == song.title:
    print('Correct!')
  else:
    print('Sorry, the correct answer is  {}'.format(song.title))

if __name__ == '__main__':
  #get_lyrics()
  artist_quiz()
