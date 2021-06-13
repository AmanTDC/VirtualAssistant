from tkinter import*
import threading
import keyboard
import time
root = Tk()

def change_back(w,photos):
    while True:
        if keyboard.is_pressed('f9+f8'):
            i=0
            w.config(image=photos[0])
            time.sleep(0.1)

        if keyboard.is_pressed('f8+f7'):
            i=1
            w.config(image=photos[1])
            time.sleep(0.1)


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
