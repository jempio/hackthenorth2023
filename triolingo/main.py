from taipy.gui import Gui
from taipy.gui import navigate

from pages.pageOne import pageOne
from pages.pageTwo import pageTwo
from pages.pageThree import pageThree
from reader import readQuote
import bs
import api
import os
import time
from playsound import playsound
import speechToText
import textToSpeech
import script
from script import CNN
import math

my_theme = {
  "palette": {
    "background": {"default": "#F9F5ED"},
    "primary": {"main": "#66283B"}
  }
}

pages = {
     "Home": pageOne,
     "Challenge": pageTwo,
     "Results": pageThree
}

def easy_callback(state):
    quote = api.get_completion("Please generate a unique, original, short, easy English sentence for children to learn.")
    with open('quote.txt', 'w') as f:
        f.write(quote + '\n')
        f.write('Easy')
    refresh()
    navigate(state, to='Challenge')

def medium_callback(state):
    quote = api.get_completion("Please generate a unique, original, short English sentence for intermediate-level students to learn.")
    with open('quote.txt', 'w') as f:
        f.write(quote + '\n')
        f.write('Medium')
    refresh()
    navigate(state, to='Challenge')
    
def hard_callback(state):
    quote = api.get_completion("Please generate a unique, original, short English sentence for advanced-level students to learn.")
    with open('quote.txt', 'w') as f:
        f.write(quote + '\n')
        f.write('Hard')
    refresh()
    navigate(state, to='Challenge')


def refresh():
    with open('bs.py', 'w') as f:
        f.write('import os')
    

def record_callback(state):
  speechToText.recordSpeech()
  with open('score.txt', 'w') as f:
      op = script.inference('audio_file/my_speech.wav')
      input = str(max(10, min(90, math.floor(100 * (op - 5))))) + "%"
      f.write(input)
  refresh()
  navigate(state, to='Results')

def retry_sentence(state):
    refresh()
    navigate(state, to='Challenge')

def get_new_sentence(state):
    refresh()
    navigate(state, to='Home')

def listen_to_ai(state):
    textToSpeech.generateSpeech(readQuote())
    
def listen_to_sentence(state):
    playsound("audio_file/my_speech.wav")


gui_multi_pages = Gui(pages=pages)

if __name__ == '__main__':
    gui_multi_pages.run(port=5004, use_reloader=True, theme=my_theme)
