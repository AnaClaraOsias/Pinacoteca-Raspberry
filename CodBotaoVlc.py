import vlc
import os
import time
import cv2 as cv


# Função para abrir o player de vídeo VLC
def abrir_player_de_video(video_path):  
    instance = vlc.Instance("--no-xlib")
    player = instance.media_player_new()
    media = instance.media_new(video_path)
    player.set_media(media)

    
    while True:
      tecla = input("Digite 'E' para dar play e 'Q' para terminar: ")
      if tecla == 'E':
        player.play()
      else:
        break
      while True:
        estado = player.get_state() 
        if estado == vlc.State.Ended:
          player.stop()
          player.set_time(0)
          break
        time.sleep(1)


def main():
    video_path = '/home/pinacoteca/Desktop/cod/Pinacoteca-Raspberry/video.mp4'  
    if os.path.exists(video_path):
      abrir_player_de_video(video_path)
    else:
      print("O arquivo de vídeo não foi encontrado.")

   
if __name__ == "__main__":
    main()
