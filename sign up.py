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
texte=Label(window, text="To get started please sign up.",bd=0, font="courriel 30 italic ",bg="#000000",fg="#ffffff")
texte.pack()
frame.pack(side=LEFT)


nom1 = Label(window, text = 'admin name :')
nom1.place(x=700, y=350,width=75 ,height=20)
zone1 = Entry(window, width=25 , fg="black")
zone1.place(x=775, y=350 , height=20)

m1= Label(window, text = 'email:')
m1.place(x=300, y=390, width=75, height=20)
var_texte = StringVar()   #importation de la zone de saisie StringVar
ligne_texte = Entry(window, textvariable=var_texte, width=25, fg="black",show='*')
ligne_texte.place(x=375, y=390 , height=20)    #insertion de la zone de saisie

m = Label(window, text = 'password :')
m.place(x=700, y=450,width=75 ,height=20)
zone= Entry(window, width=25 , fg="black",show='*')
zone.place(x=775, y=450 , height=20)

m1= Label(window, text = 'Verification code (administrator):')
m1.place(x=200, y=490, width=200, height=20)
var_texte = StringVar()   #importation de la zone de saisie StringVar
zone2= Entry(window, textvariable=var_texte, width=25, fg="black")
zone2.place(x=390, y=490 , height=20)    #insertion de la zone de saisie

def verif():
    import csv
    c=zone2.get()
    if c=="admin2020" :
        with open('inscri1.csv','r') as f :
            a=zone1.get()
            b=zone.get()
            reader_f=csv.reader(f)
            for line in reader_f:
                if line[0] ==a  :
                    tkinter.messagebox.showinfo("!!! ","Already \n have \nan account")
                    window.destroy()
                    os.startfile('out.py')
            with open('inscri1.csv','a',newline='') as f :
                writer = csv.writer(f)
                writer.writerow([a,b])
                tkinter.messagebox.showinfo(" ","welcome your account is created as an administrator",icon="info")
    elif c=="" :
        with open('inscri.csv','r') as f :
            a=zone1.get()
            b=zone.get()
            reader_f=csv.reader(f)
            for line in reader_f:
                if line[0] ==a  :
                    tkinter.messagebox.showinfo("!!! ","Already \n have \nan account")
                    window.destroy()
                    os.startfile('out.py')
            with open('inscri.csv','a',newline='') as f :
                writer = csv.writer(f)
                writer.writerow([a,b])
                tkinter.messagebox.showinfo("!!! ","welcome your account is created as a seeker",icon="info")
    else :
        tkinter.messagebox.showinfo("!!! "," invalid code \n try again ",icon="error")


Button(window, text="create my account",width=5, command = verif ).place(x=525, y=600 ,height=40,width=200)

def RETURN():
    window.destroy()
    os.startfile('project.py')
B5 = Button(window, text="EXIT",bd=5,command=window.destroy ).place(x=900,y=700,height=35,width=90) 

B5 = Button(window, text="RETRUN",bd=5,command=RETURN ).place(x=800,y=700,height=35,width=90)
window.mainloop()