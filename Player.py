import os
import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
root.title("Python Music Player")
root.geometry("400x700+290+10")
root.configure(background='#333333')
root.resizable(False, False)
mixer.init()


def AddMusic():
    path = filedialog.askdirectory()
    if path:
       os.chdir(path)
       songs = os.listdir(path)

       for song in songs:
              if song.endswith(".mp3"):
                     Playlist.insert(END, song)


def PlayMusic():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()
    
    

lower_frame = Frame(root , bg = "#FFFFFF", width = 485 , height = 180 )
lower_frame.place ( x = 0 , y = 400)



image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)


frameCnt = 30
frames = [PhotoImage( file='musica.gif',format = 'gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):

    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)
label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)


current_volume = 0.5  

def IncreaseVolume():
    global current_volume
    if current_volume < 1.0:
        current_volume += 0.1 
        mixer.music.set_volume(current_volume)
        UpdateVolumeLabel()

def DecreaseVolume():
    global current_volume
    if current_volume > 0.0:
        current_volume -= 0.1 
        mixer.music.set_volume(current_volume)
        UpdateVolumeLabel()

def UpdateVolumeLabel():
    volume_percentage = int(current_volume * 100)
    volume_label.config(text=f"Volume: {volume_percentage}%")


ButtonPlay = PhotoImage(file="play1.png")
Button( root, image=ButtonPlay, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=PlayMusic).place(x=220, y=487)

ButtonStop = PhotoImage(file="stop1.png")
Button( root, image=ButtonStop, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.stop).place(x=135, y=487)

Buttonvolume = PhotoImage(file="volume.png")
Button(root, image=Buttonvolume, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.unpause).place(x=20, y=487)


ButtonVolumeUp = PhotoImage(file="volume_up.png")
Button(root, image=ButtonVolumeUp, bg="#FFFFFF", bd=0, height=60, width=60,
       command=IncreaseVolume).place(x=70, y=487)

ButtonVolumeDown = PhotoImage(file="volume_down.png")
Button(root, image=ButtonVolumeDown, bg="#FFFFFF", bd=0, height=60, width=60,
       command=DecreaseVolume).place(x=15, y=487)


volume_label = Label(root, text="Volume: 50%", bg="#FFFFFF", font=("calibri", 12, "bold"))
volume_label.place(x=150, y=400)


ButtonPause = PhotoImage(file="pause.png")
Button(root, image=ButtonPause, bg="#FFFFFF", bd=0, height = 60, width =60,
       command=mixer.music.pause).place(x=305, y=487)

      
Menu = PhotoImage(file="menu.png")
Label(root, image=Menu).place(x=0, y=580, width=485, height=120)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=585, width=400, height=100)



Button(root, text="Browse Music", width=59, height=1, font=("calibri",
      12, "bold"), fg="Black", bg="#FFFFFF", command=AddMusic).place(x=-30, y=550)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)



root.mainloop()