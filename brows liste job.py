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
L1=Label(window, text = 'Brows the list of job seekers  ',font="none 25 italic ",bg='#000044',fg='#ffffff')
L1.place(x=500,y=40,height=45,width=450)

L1=Label(window, text = '"a --> All the job seekers that applied for job offers \n b --> All the job seekers that applied for the same job offer \n ',font="none 15 italic ",bg='#000044',fg='#ffffff')
L1.place(x=10,y=200,height=75,width=650)
nom = Label(window, text = 'your choice :',fg="darkblue")
nom.place(x=100, y=300 ,width=75 ,height=30)
zone= Entry(window, width=25 , fg="black")
zone.place(x=175, y=300 , height=30)
nom1 = Label(window, text = 'if you choose "b" please input the job offer :',fg="green")
nom1.place(x=100, y=350 ,width=500 ,height=30)
zone1= Entry(window, width=25 , fg="black")
zone1.place(x=100, y=400 , height=30)

def seekers() :
    choix=zone.get()
    if choix=="" or (choix!='a' and choix!='b'):
        tkinter.messagebox.showinfo("Fields error", " Field is empty \n or  invalid choice ", icon="error")
    else :
        h=0
        if choix == 'a' :
            with open('seekers.csv','r') as f :
                reader_f=csv.reader(f)
                for line in reader_f:
                    tkinter.messagebox.showinfo("All the job seekers that applied for job offers",line, icon="info")
        elif choix =='b' :
            with open('seekers.csv','r') as f :
                reader_f=csv.reader(f)
                job=zone1.get()
                if job == "":
                    tkinter.messagebox.showinfo("Fields error", " Field is empty \n please input the job offer ", icon="error")
                    h=1
                else :                    
                    for line in reader_f:
                        if line[0]==job :
                            tkinter.messagebox.showinfo("all the job seekers that applied for the same job offer",line, icon="info")
                            h=1
            if h==0 :
                tkinter.messagebox.showinfo(" !!","seekers not found to this job ", icon="info")

with open('job.csv','r') as f:
    reader_f=csv.reader(f)
    for i in reader_f :
        print(i)
B = Button(window, text="show results ",bd=5,command=seekers ).place(x=500,y=300,height=35,width=90) 
B5 = Button(window, text="EXIT",bd=5,command=window.destroy ).place(x=500,y=700,height=35,width=90) 
def RETURN():
    window.destroy()
    os.startfile('project.py')
B1= Button(window, text="RETRUN",bd=5,command=RETURN ).place(x=600,y=700,height=35,width=90)
window.mainloop() 
 


