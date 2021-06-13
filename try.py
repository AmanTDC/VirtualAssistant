from tkinter import*
import threading
import keyboard
root = Tk()

def change_back(w,photos):
    i=0
    while True:
        if keyboard.is_pressed('ctrl+shift+alt+k'):
            i+=1
            i%=2
            w.config(image=photos[i])


photo = PhotoImage(file = "play.png")
#photo2=PhotoImage(file="process.png")
photo3 = PhotoImage(file = "stopped.png")
photos=[photo,photo3]
w = Label(root, image=photo)
w.pack()
i=0
'''
if keyboard.press('k'):
    i+=1
    t%=2
    w.config(image=photos[i])
'''       
ent = Entry(root)
ent.pack()
ent.focus_set()
thread=threading.Thread(target=change_back,args=(w,photos,));thread.start()
root.update()
root.mainloop()
