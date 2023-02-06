# Imports go at the top
from microbit import *
i= 0
lista_amigos = ["Lucas", "María", "Esteban","Abulai", "Nico", "Eva", "Julia", "Pepe"]

while True:
      if button_a.was_pressed():
          i= i - 1
          sleep (500)
      elif button_b.was_pressed():
          i= i + 1
          sleep (500)
      else:
          display.show(i)
          sleep (500)
          display.show (lista_amigos[i])
          sleep (500)