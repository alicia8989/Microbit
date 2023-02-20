from microbit import *

lista_numeros= [1, 5, 8, 11, 7, 9]  
total = 0

for i in lista_numeros:
    display.scroll(i)
    total= total + i
    display.scroll(total)