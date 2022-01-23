from tkinter import *
import os
import tkinter.messagebox

window= Tk()
window.title("hire now")
window.geometry('1366x768')
window.minsize(450, 360)
fondo = PhotoImage(file= 'ok2.png')
background_label = Label(window, image=fondo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

frame=Frame(window,bg='black')
texte=Label(window, text="welcome to our\n Recruitment Company",bd=0, font="courriel 30 italic ",bg="#000000",fg="#ffffff")
texte.pack()
frame.pack(side=LEFT)


nom = Label(window, text = 'user name :')
nom.place(x=300, y=350,width=75 ,height=20)
zone = Entry(window, width=25 , fg="black")
zone.place(x=375, y=350 , height=20)

nom1 = Label(window, text = 'admin name :')
nom1.place(x=700, y=350,width=75 ,height=20)
zone1 = Entry(window, width=25 , fg="black")
zone1.place(x=775, y=350 , height=20)

m1= Label(window, text = 'password:')
m1.place(x=300, y=375, width=75, height=20)

var_texte = StringVar()   #importation de la zone de saisie StringVar
ligne_texte = Entry(window, textvariable=var_texte, width=25, fg="black",show='*')

ligne_texte.place(x=375, y=375 , height=20)    #insertion de la zone de saisie

m= Label(window, text = 'password : ')
m.place(x=700, y=375, width=75, height=20)
var_texte1 = StringVar()
ligne_texte1 = Entry(window, textvariable=var_texte1, width=25, fg="black",show='*')
ligne_texte1.place(x=775, y=375 , height=20)



Button(window, text="Exit",width=5, command = window.destroy).place(x=800, y=450 ,height=40,width=75)


def verification1():
    import csv
    with  open('inscri1.csv', 'r') as f:
        a=zone1.get()
        b=ligne_texte1.get()
        reader_f=csv.reader(f)
        h=0
        for line in reader_f:
            if line[0]==a and line[1]==b:
                h=1
    if h==0 :
        tkinter.messagebox.showinfo("-- ERROR --", "Incorrect password!\n              OR\nIncorrect username", icon="warning")
    else :
        window.destroy()
        os.startfile('admin.py')
   
      
Button(window, text="LOGIN",width=5, command = verification1 ).place(x=725, y=450 ,height=40,width=75)#Bouton qui verifie que le mot de passe est bon

seeker=Label(window, text='Job seeker :',font="courriel 20 underline italic ")
seeker.place(x=300,y=310,height=35)

admin=Label(window, text='Adminstrator :',font="courriel 20 underline italic ")
admin.place(x=700,y=310,height=35)

Button(window, text="Exit",width=5, command = window.destroy).place(x=400, y=450 ,height=40,width=75)


def verification():
    import csv
    with  open('inscri.csv', 'r') as f:
        a=zone.get()
        b=ligne_texte.get()
        reader_f=csv.reader(f)
        h=0
        for line in reader_f:
            if line[0]==a and line[1]==b:
                h=1
    if h==0 :
        tkinter.messagebox.showinfo("-- ERROR --", "Incorrect password!\n              OR\nIncorrect username", icon="warning")
    else :
        window.destroy()
        os.startfile('seeker.py')

Button(window, text="LOGIN",width=5, command = verification ).place(x=325, y=450 ,height=40,width=75)#Bouton qui verifie que le mot de passe est bon
def out():
    window.destroy()
    os.startfile('sign up.py')
Button(window, text="sign up",width=5, command = out ).place(x=600, y=720 ,height=40,width=75)#boutton sign out









window.mainloop()
