import vlc
import os
import time
import cv2 as cv

def exibeIM(path_I):
    cap = cv.imread(path_I)
    cv.namedWindow("OpenCV Window", cv.WINDOW_NORMAL)
    cv.setWindowProperty("OpenCV Window", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)
    cv.imshow("OpenCV Window", cap)

def exibeVI(path_V):
    instance1 = vlc.Instance()
    player = instance1.media_player_new()
    media = instance1.media_new(path_V)
    player.set_media(media)
    player.set_fullscreen(True)
    player.play()
    return player

def exibe(path_I, path_V):
    exibeIM(path_I)

    while True:
        key = cv.waitKey(0) & 0xFF
        key_char = chr(key).lower() if key != -1 else ''  
        if key_char == 'e':
            cv.destroyAllWindows()
            player = exibeVI(path_V)
            while True:
                estado = player.get_state() 
                if estado == vlc.State.Ended:
                    player.stop()
                    player.set_time(0)
                    break
            player.stop()
            exibeIM(path_I)

        if key_char == 'q':
            break


def main():
    video_path = '/home/pinacoteca/Desktop/cod/Pinacoteca-Raspberry/video1.mp4'  
    imagem_path = '/home/pinacoteca/Desktop/cod/Pinacoteca-Raspberry/imagem.jpg'  
    if os.path.exists(imagem_path):
        exibe(imagem_path,  video_path)
    else:
        print("O arquivo de vídeo não foi encontrado.")
            

if __name__ == "__main__":
    main()
