import vlc
import os
import time
import cv2 as cv
import RPi.GPIO as gpio
from pynput.keyboard import Key, Controller

##ALTERE AQUI O CAMINHO PARA O VIDEO E IMAGEM DESEJADOS
video_path = '/home/pinacoteca/Desktop/cod/Pinacoteca-Raspberry/video.mp4'   
imagem_path = '/home/pinacoteca/Desktop/cod/Pinacoteca-Raspberry/imagem.jpg'

#Instancias para o controle do botao
keyboard = Controller()
botaoPin = 26               	            #Esse pino é considerando a numeração BCM da gpio (imagem na internet) equivale ao segundo pino mais proximo as entradas USB na fileira interna da placa
gpio.setmode(gpio.BCM)      	            #Escolhe o modo BCM
gpio.setup(botaoPin,gpio.IN, gpio.PUD_UP)   #Coloca o pino alto 
out = False 

#define o evento quando o botao é pressionado. Esse evento ocorre em paralelo com o restante do programa
def callback(channel): 
    global out
    #print("botao pressionado em ", channel)
    keyboard.press('E')
    out = not out 
gpio.add_event_detect(botaoPin,gpio.RISING,callback=callback,bouncetime = 700)


def exibe(path_I, path_V):
#Instancia e configuracao da janela de imagem
	cap = cv.imread(path_I)
	cv.namedWindow("OpenCV Window", cv.WINDOW_NORMAL)
	#cv.moveWindow("OpenCV Window", 0, 0)   configura em qual tela sera exibido caso haja mais de uma 
	cv.setWindowProperty("OpenCV Window", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)

#Instancia e configuracao da janela de video
	player = vlc.MediaPlayer()
	player.toggle_fullscreen()
	media=vlc.Media(path_V)
	player.set_media(media)


	cv.imshow("OpenCV Window", cap)        #Exibe imagem
	
#Lê o teclado, se o botao for pressionado (equivalente a apertar 'e' no teclado) o video é exibido, se a letra 'q' for apertada o programa encerra
	while True:
		key = cv.waitKey(0) & 0xFF
		key_char = chr(key).lower() if key != -1 else ''  
		
		if key_char == 'e' :
			FIM = vlc.State.Ended
			player.play() 
			time.sleep(2)
			
			while True:
				estado = player.get_state() 
				if estado == FIM:
					player.stop()
				#	player.set_time(0)
					break
		
		if key_char == 'q':
			break

cv.destroyAllWindows()

def main():

	if os.path.exists(imagem_path):
		exibe(imagem_path,  video_path)
	else:
		print("O arquivo de imagem não foi encontrado.")
            
if __name__ == "__main__":
    main()
