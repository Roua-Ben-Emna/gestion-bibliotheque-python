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
L1=Label(window, text = 'Brows and Update a job offer ',font="none 25 italic ",bg='#000044',fg='#ffffff')
L1.place(x=500,y=40,height=45,width=450)


nom = Label(window, text = 'code :')
nom.place(x=235, y=150,width=150 ,height=30)
zone= Entry(window, width=40, fg="black")
zone.place(x=375, y=150 , height=30)

nom2 = Label(window, text = '  name  :')
nom2.place(x=235, y=200,width=150 ,height=30)
zone2 = Entry(window, width=40 , fg="black")
zone2.place(x=375, y=200 , height=30)

nom3= Label(window, text = 'address :')
nom3.place(x=235, y=250,width=150 ,height=30)
zone3 = Entry(window, width=40 , fg="black")
zone3.place(x=375, y=250 , height=30)

nom4 = Label(window, text = 'phone number :')
nom4.place(x=235, y=300,width=150 ,height=30)
zone4 = Entry(window, width=40 , fg="black")
zone4.place(x=375, y=300 , height=30)

nom5 = Label(window, text = 'email :')
nom5.place(x=235, y=350,width=150 ,height=30)
zone5 = Entry(window, width=40 , fg="black")
zone5.place(x=375, y=350 , height=30)

nom6 = Label(window, text = 'degree:')
nom6.place(x=235, y=400,width=150 ,height=30)
zone6 = Entry(window, width=40 , fg="black")
zone6.place(x=375, y=400 , height=30)

nom7 = Label(window, text = 'exprience  :')
nom7.place(x=235, y=450,width=150 ,height=30)
zone7 = Entry(window, width=40 , fg="black")
zone7.place(x=375, y=450 , height=30)

nom8 = Label(window, text = 'qualification :')
nom8.place(x=235, y=500,width=150 ,height=30)
zone8 = Entry(window, width=40 , fg="black")
zone8.place(x=375, y=500 , height=30)

nom9 = Label(window, text = 'mession description  :')
nom9.place(x=235, y=550,width=150,height=30)
zone9 = Entry(window, width=40 , fg="black")
zone9.place(x=375, y=550 , height=90)

def update():
    code=zone.get()
    name=zone2.get()
    address=zone3.get()
    phone=zone4.get()
    email=zone5.get()
    degree=zone6.get()
    exprience=zone7.get()
    qualification=zone8.get()
    mes_desc=zone9.get()
    if (code=="") or (name=="") or (address=="") or (email=="") or (phone=="") or (degree=="") or (qualification=="") :
        tkinter.messagebox.showinfo("Fields error", " Fields are empty ", icon="error")
    else:
        from tkinter import messagebox
        ch=[code,name ,address,phone,email,degree, exprience ,qualification,mes_desc]
        with open("job.csv", 'r') as f:  
            ligne=csv.reader(f)
            with open("joboffer.csv", 'w',newline='') as f1:
                writr=csv.writer(f1)
                for i in ligne:
                    if(i[0]!=code):
                        writr.writerow(i)
        f=open("joboffer.csv","a",newline='')
        writr=csv.writer(f)
        writr.writerow(ch)
        f.close()     
        os.remove("job.csv" ) 
        os.rename("joboffer.csv","job.csv") 
        messagebox.showinfo("Update", "Job offer updated successfully")

   
B = Button(window, text="update  ",bd=5,command=update ).place(x=400,y=650,height=35,width=90) 

B5 = Button(window, text="EXIT",bd=5,command=window.destroy ).place(x=500,y=700,height=35,width=90) 
def RETURN():
    window.destroy()
    os.startfile('project.py')
B1= Button(window, text="RETRUN",bd=5,command=RETURN ).place(x=600,y=700,height=35,width=90)
window.mainloop() 
