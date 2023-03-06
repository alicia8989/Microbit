from microbit import *
import music
contador=0
while True:
    if button_a.get_presses(): 
        display.show(Image.DUCK)
        sleep(400)
    elif button_b.get_presses():
            music.play(music.RINGTONE)
        