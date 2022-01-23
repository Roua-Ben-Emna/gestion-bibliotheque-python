from tkinter import *
import os
root = Tk()  #ouverture de la nouvelle fenêtre contenant le programme
root.title("Hello admin :)")
root.geometry('1366x768')
fondo = PhotoImage(file= 'ok.png')
background_label = Label(root, image=fondo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
def addjob():
    os.startfile('addjob.py')
def browslist():
    os.startfile('brows liste job.py')
def delete():
    os.startfile('delete job.py')
def update():
    os.startfile('update job.py')
B1 = Button(root, text="1. Add new job offer",bd=5,command=addjob,fg="red").place(x=500,y=200,height=35,width=230)  #Insertion des Labels
B2 = Button(root, text="2. Brows and Update a job offer",bd=5,command=update,fg="blue").place(x=500,y=300,height=35,width=230) 
B3 = Button(root, text="3. Delete a job offer",bd=5,command=delete,fg="green").place(x=500,y=400,height=35,width=230) 
B4 = Button(root, text="4. Brows the list of job seekers",bd=5,command=browslist,fg="olive").place(x=500,y=500,height=35,width=230) 
def RETURN():
    root.destroy()
    os.startfile('project.py')
B5 = Button(root, text="RETRUN",bd=5,command=RETURN ).place(x=800,y=700,height=35,width=90) 
B5 = Button(root, text="EXIT",bd=5,command=root.destroy ).place(x=900,y=700,height=35,width=90) 
root.mainloop()
