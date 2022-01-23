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
L1=Label(root, text = 'search for a job offer by\njob offer ID or domain:',font="none 30 italic ",bg='#000044',fg='#ffffff')
L1.place(x=500,y=200,height=95,width=430)
v = StringVar()
E=Entry(root, textvariable=v,font="none 25",width=30)
E.place(x=500,y=295,width=430,height=45)
def ser() :
    choix=E.get()
    with  open('job.csv', 'r') as f:
        reader_f=csv.reader(f)
        h=1
        for line in reader_f:
            for i in line :
                if i==choix :
                    tkinter.messagebox.showinfo("jobs :  ",line)
                    h=0
    if h==1 :
        tkinter.messagebox.showinfo("!!! ","job not found")
        root.destroy()
        os.startfile('seeker.py')                
def RETURN():
    root.destroy()
    os.startfile('project.py')
search = PhotoImage(file= 'ss.png')
B = Button(root,image=search,bd=0,command=ser).place(x=882,y=300,width=40,height=40)
B5 = Button(root, text="RETRUN",font=20,bd=3,command=RETURN ).place(x=650,y=470,width=75)
B5 = Button(root, text="EXIT",font=20,bd=3,command=root.destroy ).place(x=725,y=470)
def go():
    root.destroy()
    os.startfile('seeker2.py')
B5 = Button(root, text="for apply or update a job click here ",font=("Courier",15),bd=3,command= go ,fg='sienna').place(x=800,y=700)
root.mainloop()