from tkinter import *
import os
import csv
import tkinter.messagebox
window = Tk()  #ouverture de la nouvelle fenêtre contenant le programme
window.title("Hello seeker :)")
window.geometry('1366x768')
fondo = PhotoImage(file= 'ok.png')
background_label = Label(window, image=fondo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
L1=Label(window, text = 'Brows and Apply for a job offer',font="none 25 italic ",bg='#000044',fg='#ffffff')
L1.place(x=500,y=40,height=45,width=450)
nom = Label(window, text = 'code job :')
nom.place(x=235, y=150,width=150 ,height=30)
zone = Entry(window, width=40 , fg="black")
zone.place(x=375, y=150 , height=30)

nom2 = Label(window, text = 'id card  :')
nom2.place(x=235, y=200,width=150 ,height=30)
zone2 = Entry(window, width=40 , fg="black")
zone2.place(x=375, y=200 , height=30)

nom3= Label(window, text = 'name :')
nom3.place(x=235, y=250,width=150 ,height=30)
zone3 = Entry(window, width=40 , fg="black")
zone3.place(x=375, y=250 , height=30)

nom4 = Label(window, text = 'address :')
nom4.place(x=235, y=300,width=150 ,height=30)
zone4 = Entry(window, width=40 , fg="black")
zone4.place(x=375, y=300 , height=30)

nom5 = Label(window, text = 'phone number :')
nom5.place(x=235, y=350,width=150 ,height=30)
zone5 = Entry(window, width=40 , fg="black")
zone5.place(x=375, y=350 , height=30)

nom6 = Label(window, text = 'university :')
nom6.place(x=235, y=400,width=150 ,height=30)
zone6 = Entry(window, width=40 , fg="black")
zone6.place(x=375, y=400 , height=30)

nom7 = Label(window, text = 'degree  :')
nom7.place(x=235, y=450,width=150 ,height=30)
zone7 = Entry(window, width=40 , fg="black")
zone7.place(x=375, y=450 , height=30)

nom8 = Label(window, text = 'exprience ? :')
nom8.place(x=235, y=500,width=150 ,height=30)
zone8 = Entry(window, width=40 , fg="black")
zone8.place(x=375, y=500 , height=30)

nom9 = Label(window, text = 'skills  :')
nom9.place(x=235, y=550,width=150 ,height=30)
zone9 = Entry(window, width=40 , fg="black")
zone9.place(x=375, y=550 , height=90)

def apply() :
    with open('seekers.csv', 'a',newline='') as f :
        writr=csv.writer(f, delimiter=',')
        codejob=zone.get()
        code=zone2.get()
        with  open('seekers.csv', 'r') as f1:
            read=csv.reader(f1)
            for line in read:
                while line[0]==codejob and line[1]==code:
                    tkinter.messagebox.showinfo("-- ERROR --", "already done ", icon="warning")
                    window.destroy()
                    os.startfile('applyjob.py')               
        name=zone3.get()
        address=zone4.get()
        phone=zone5.get()
        univ=zone6.get()
        degree=zone7.get()
        exprience=zone8.get()
        skills=zone9.get()
        msg=[codejob,code,name ,address,phone,univ,degree, exprience ,skills]    
        writr.writerow(msg)
        tkinter.messagebox.showinfo("success", " well done ", icon="info")

B = Button(window, text="apply ",bd=5,command=apply ).place(x=400,y=650,height=35,width=90) 

B5 = Button(window, text="EXIT",bd=5,command=window.destroy ).place(x=500,y=700,height=35,width=90) 
def RETURN():
    window.destroy()
    os.startfile('project.py')
B1= Button(window, text="RETRUN",bd=5,command=RETURN ).place(x=600,y=700,height=35,width=90)
window.mainloop()     