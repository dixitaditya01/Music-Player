#Project 2 - Music Player

#importing libraries 
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog

#creating the root window 
root=Tk()
root.title('Python Music Player')
#initialize mixer 
mixer.init()

#add many songs to the playlist of python mp3 player
def addsongs():
    #to open a file  
    temp_song=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),("band Files","*.band")))
    ##loop through every item in the list to insert in the listbox
    for s in temp_song:
        s=s.replace("/Users/adityadixit/Desktop/Coding/Code Clause/Music_player","")
    songs_list.insert(END,s)
     
#to delete the song
def deletesong():
    curr_song=songs_list.curselection()
    songs_list.delete(curr_song[0])

#to play the song
def Play():
    song=songs_list.get(ACTIVE)
    song=f'/Users/adityadixit/Desktop/Coding/Code Clause/Music_player/{song}'
    mixer.music.load(song)
    mixer.music.play()

#to pause the song 
def Pause():
    mixer.music.pause()

#to stop the  song 
def Stop():
    mixer.music.stop()
    songs_list.selection_clear(ACTIVE)

#to resume the song
def Resume():
    mixer.music.unpause()

#create the listbox to contain songs
songs_list=Listbox(root,selectmode=SINGLE,bg="black",fg="white",font=('arial',15),height=12,width=47,selectbackground="gray",selectforeground="black")
songs_list.grid(columnspan=9)

#font is defined which is to be used for the button font 
defined_font = font.Font(family='Helvetica')

#play button
play_button=Button(root,text="Play",width =7,command=Play)
play_button['font']=defined_font
play_button.grid(row=1,column=0)

#pause button 
pause_button=Button(root,text="Pause",width =7,command=Pause)
pause_button['font']=defined_font
pause_button.grid(row=1,column=1)

#stop button
stop_button=Button(root,text="Stop",width =7,command=Stop)
stop_button['font']=defined_font
stop_button.grid(row=1,column=2)

#resume button
Resume_button=Button(root,text="Resume",width =7,command=Resume)
Resume_button['font']=defined_font
Resume_button.grid(row=1,column=3)

#menu 
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)

mainloop()