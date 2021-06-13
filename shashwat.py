#import statements
from tkinter import *
import tkinter.messagebox
import tkinter.font
from PIL import ImageTk,Image
import os
import time
path_play=os.path.normpath("play.png")
path_proc=os.path.normpath("process.png")
path_stop=os.path.normpath("stopped.png")
#os.startfile(path)
app=Tk()
app.title('Welcom')
play_img =Image.open(path_play)
proc_img =Image.open(path_proc)
stop_img =Image.open(path_stop)
background_image1=ImageTk.PhotoImage(play_img)
background_image2=ImageTk.PhotoImage(proc_img)
background_image3=ImageTk.PhotoImage(stop_img)

background_label = Label(app, image=background_image1)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
Images=[background_image1,background_image2,background_image3]
i=0
while True:
    background_label.image=Images[2]
    time.sleep(3)
    i+=1
    i%=3


'''

background_image=window.PhotoImage('test.png')
background_label = window.Label(parent, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
'''
