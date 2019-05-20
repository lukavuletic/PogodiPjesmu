import pygame as pg
import random
import glob, os

print('Press mouse key if the played song is correct')
print('Press keyboard key if the played song isn\'t correct')

song_list = []
os.chdir("songs")
for file in glob.glob("*.mp3"):
    song_list.append(file)

song_list_size = len(song_list)

#select a random song from song_list
selected_song = '{}'.format(song_list[int(random.random() * song_list_size)])

shown_song = '{}'.format(song_list[int(random.random() * song_list_size)])

def open_window():
  (width, height) = (480, 250)
  background_colour = (105,105,105)

  #display the window
  screen = pg.display.set_mode((width, height))
  screen.fill(background_colour)
  pg.display.flip()

  #set the window's title
  pg.display.set_caption('Alarm')

  #show the name of the song
  pg.font.init()
  my_font = pg.font.SysFont('asdfasdfasdfas', 30)
  
  text_surface = my_font.render('{}'.format(shown_song[:-4]), False, (255, 255, 255))
  screen.blit(text_surface,(27,80))

  #keep the window open
  
  pg.display.update()
  play_music(selected_song)
  pg.quit()

def play_music(selected_song, volume=0.8):
    score = 0
    window_running = True
    #set pygame's mixer
    freq = 44100
    bitsize = -16
    channels = 2
    buffer = 2048
    pg.mixer.init(freq, bitsize, channels, buffer)    
    pg.mixer.music.set_volume(volume)

    clock = pg.time.Clock()

    #check whether file is correct
    try:
        pg.mixer.music.load(selected_song)
        print('Song {} loaded!'.format(selected_song))
    except pg.error:
        print('Song {} not found! ({})'.format(selected_song, pg.get_error()))
        return

    #play the song
    pg.mixer.music.play()
    while pg.mixer.music.get_busy() and window_running:
         clock.tick(5)
         for event in pg.event.get():
          if event.type == pg.QUIT:
            window_running = False
            break
          #if the song is wrong press down
          elif event.type == pg.KEYDOWN:
            if shown_song != selected_song:
              print('You guessed that the song isn\'t correct')
              pg.time.wait(3000)
              window_running = False
              break
            else:
              print('You lost')
              pg.time.wait(3000)
              window_running = False
              break
          #if correct, press up
          elif event.type == pg.MOUSEBUTTONDOWN:
            if shown_song == selected_song:
              print('You guessed that the song is correct')
              pg.time.wait(3000)
              window_running = False
              break
            else:
              print('You lost')
              pg.time.wait(3000)
              window_running = False
              break

open_window()