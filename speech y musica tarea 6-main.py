# Imports go at the top
from microbit import *
import music
import speech

speech.say("Mototruco")
lstNotas= ['a:3', 'a', 'g', 'f', 'g:4']

music.play(lstNotas)