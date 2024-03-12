import RPi.GPIO as gpio
import time
from pynput.keyboard import Key, Controller

keyboard = Controller()
botaoPin = 26
gpio.setmode(gpio.BCM) 
gpio.setup(botaoPin,gpio.IN, gpio.PUD_UP)
out = False 

def callback(channel): 
    global out
    print("botao pressionado em ", channel)
    keyboard.press('E')
    out = not out 

gpio.add_event_detect(botaoPin,gpio.RISING,callback=callback,bouncetime = 700)

try:
    while True:
        #print("Aguardando evento")
        time.sleep(5)

except keyboardInterrupt:        
    pass
gpio.cleanup()
