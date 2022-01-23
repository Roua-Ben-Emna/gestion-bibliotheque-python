from tkinter import *
import os
import csv
import tkinter.messagebox
root = Tk()  #ouverture de la nouvelle fenêtre contenant le programme
root.title("Hello seeker :)")
root.geometry('1366x768')
fondo = PhotoImage(file= 'ok.png')
background_label = Label(root, image=fondo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def go():
    root.destroy()
    os.startfile('applyjob.py')
B5 = Button(root, text="Brows and Apply for a job offer ",font=30,bd=4,fg="crimson",command =go).place(x=700,y=300,height=35,width=330)
def go2():
    root.destroy()
    os.startfile('update seeker.py')
B5 = Button(root, text="Update job seeker information ",font=30,bd=4,fg="darkred",command =go2).place(x=200,y=300,height=35,width=330)

def RETURN():
    root.destroy()
    os.startfile('project.py')
B5 = Button(root, text="EXIT",bd=5,command=root.destroy ).place(x=900,y=700,height=35,width=90) 

B5 = Button(root, text="RETRUN",bd=5,command=RETURN ).place(x=800,y=700,height=35,width=90)
root.mainloop()