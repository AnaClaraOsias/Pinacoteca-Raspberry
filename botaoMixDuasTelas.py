import vlc
import os
import time
import cv2 as cv



def exibe(path_I, path_V):
    cap = cv.imread(path_I)
    cv.namedWindow("OpenCV Window", cv.WINDOW_NORMAL)
    cv.moveWindow("OpenCV Window", 0, 0)

    cv.setWindowProperty("OpenCV Window", cv.WND_PROP_FULLSCREEN, cv.WINDOW_FULLSCREEN)


    instance1 = vlc.Instance("--no-xlib ")
    player = instance1.media_player_new()
    media = instance1.media_new(path_V)
    player.set_media(media)
    player.set_fullscreen(True)

    cv.imshow("OpenCV Window", cap)
    while True:
        key = cv.waitKey(0) & 0xFF
        key_char = chr(key).lower() if key != -1 else ''  
        if key_char == 'e':
            player.play() 
            while True:
                estado = player.get_state() 
                if estado == vlc.State.Ended:
                    player.stop()
                    player.set_time(0)
                    break
            player.stop()

        if key_char == 'q':
            break

cv.destroyAllWindows()


def main():
    video_path = '/home/pinacoteca/Desktop/video1.mp4'
    imagem_path = './imagem.jpg'
    if os.path.exists(imagem_path):
        exibe(imagem_path,  video_path)
    else:
        print("O arquivo de vídeo não foi encontrado.")
            

if __name__ == "__main__":
    main()
