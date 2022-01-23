 
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
L1=Label(window, text = 'Delete a job offer ',font="none 25 italic ",bg='#000044',fg='#ffffff')
L1.place(x=500,y=40,height=45,width=450)

nom = Label(window, text = 'code :')
nom.place(x=425, y=200 ,width=75 ,height=30)
zone= Entry(window, width=25 , fg="black")
zone.place(x=500, y=200 , height=30)
def delete(): 
    code=zone.get()
    if code=="":
        tkinter.messagebox.showinfo("Fields error", " Field is empty ", icon="error")
    else :    
        h=0
        with  open('job.csv', 'r') as f:
            reader_f=csv.reader(f)
            for line in reader_f:
                for i in line :
                    if line[0] == code  :
                        h=1
        if h==1 :
            with open("job.csv", 'r') as f:  
                ligne=csv.reader(f)
                with open("joboffer.csv", 'w',newline='') as f1:
                    writr=csv.writer(f1)
                    for i in ligne:
                        if(i[0]!=code):
                            writr.writerow(i)  
            os.remove("job.csv" ) 
            os.rename("joboffer.csv","job.csv") 
            tkinter.messagebox.showinfo("heyy ", "job deleted successfully ", icon="info")   
        else :
            tkinter.messagebox.showinfo("-- ERROR --", "job not found ", icon="warning")
            window.destroy()
            os.startfile('delete job.py')

B = Button(window, text="delete  ",bd=5,command=delete ).place(x=500,y=300,height=35,width=90) 
B5 = Button(window, text="EXIT",bd=5,command=window.destroy ).place(x=500,y=700,height=35,width=90) 
def RETURN():
    window.destroy()
    os.startfile('project.py')
B1= Button(window, text="RETRUN",bd=5,command=RETURN ).place(x=600,y=700,height=35,width=90)
window.mainloop() 