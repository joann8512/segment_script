import vlc
import time
from time import sleep
import keyboard

def write_file(name, t):
    file = open("{}.txt".format(name), "a")
    file.write(str(t)+'\n')
    file.close()

def main():
    path = 'C:/Users/joann/Downloads/A_lovely_night.mp4'
    name = path.split('/')[-1].split('.')[0]
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(path)
    player.set_media(Media)
    # making keyboard input enable
    player.video_set_key_input(True)
    print("3")
    sleep(1) # Or however long you expect it to take to open vlc
    print("2")
    sleep(1)
    print("1")
    sleep(1)
    player.play()
    sleep(0.5) # Or however long you expect it to take to open vlc
    begin = time.time()
    while player.is_playing():
        get_key = True
        while get_key:
            if keyboard.is_pressed('a'):  # if key 'q' is pressed
                #print('You Pressed A Key!')
                c = time.time() - begin
                print("Cut for start at {}".format(c))
                sleep(0.5)
                write_file(name, c)
                get_key = False
            elif keyboard.is_pressed('d'):
                p = time.time() - begin
                print("Cut for end at {}".format(p))
                sleep(0.5)
                write_file(name, p)
                get_key = False
    print("End of Song!")

if __name__ == "__main__":
    main()
