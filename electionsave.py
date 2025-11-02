import tkinter 
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
def showelectionschedulesave():
        
    t=tkinter.Tk()
    t.geometry('600x600')
    
    
    
    t.config(bg='olive')
    
    def savedata():
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0 or len(e5.get())==0 :
            messagebox.showinfo('Warning','Please Fill the data')
        else:
            db=pymysql.connect(host='Localhost',user='root',password='root',database='votingsystem')
            cur=db.cursor()
            xa=(e1.get())
            xb=(e2.get())
            xc=(e3.get())
            xd=(e4.get())
            xe=(e5.get())
    
            sql="insert into electionschedule values('%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe)
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Done','Saved')
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
         
    
    def delete():
        t.destroy()
    
       
    a=Label(t,text='ELECTIONSCHEDULE',font='55',fg='white',bg='black')
    a.place(x=180,y=50)
    
    b=Label(t,text='Ward NO',font=("Arial",15),bg='light blue')
    b.place(x=70,y=125)
    e1=Entry(t,width='25')
    e1.place(x=400,y=125)
    
    d=Label(t,text='Ward Name',font=("Arial",15),bg='light blue')
    d.place(x=70,y=200)
    e2=Entry(t,width='25')
    e2.place(x=400,y=200)
    
    
    e=Label(t,text='Area No',font=("Arial",15),bg='light blue')
    e.place(x=70,y=275)
    e3=Entry(t,width='25')
    e3.place(x=400,y=275)
    
    
    f=Label(t,text='Area Name',font=("Arial",15),bg='light blue')
    f.place(x=70,y=350)
    e4=Entry(t,width='25')
    e4.place(x=400,y=350)
    
    g=Label(t,text='Date of election',font=("Arial",15),bg='light blue')
    g.place(x=70,y=425)
    e5=Entry(t,width='25')
    e5.place(x=400,y=425)
    
    
    bt=Button(t,text='Insert',font=("High Tower",15),fg='white',bg='red',command=savedata)
    bt.place(x=200,y=525)
    
    btt=Button(t,text='Close',font=("High Tower",15),fg='white',bg='red',command=delete)
    btt.place(x=380,y=525)
    
    
    
    t.mainloop()