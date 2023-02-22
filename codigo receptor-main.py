from microbit import *
#importamos radio
import radio

radio.on()
radio.config(channel=43)

#Siempre en ejecución 
while True:
    message = radio.receive()
    sleep (20)
    if message is not None:
        display.scroll(str(message))
