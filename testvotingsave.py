import tkinter 
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def showvotingsaves():
    
       
    t=tkinter.Tk()
    t.geometry('600x600')
    
    
    
    t.config(bg='olive')
   
    
    def savedata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            xd=e4.get()
            xe=e5.get()
            xf=e6.get()
            sql="insert into votingdata values('%s','%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf)
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi','Saved')
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
         
    
    def delete():
        t.destroy()
    
       
    a=Label(t,text='VOTING DATA',font=("Arial",15),fg='white',bg='black')
    a.place(x=250,y=50)
    
    b=Label(t,text='Area code',font=("Arial",15),bg='light blue')
    b.place(x=70,y=125)
    e1=Entry(t,width='25')
    e1.place(x=400,y=125) 
    
    c=Label(t,text='Area Name',font=("Arial",15),bg='light blue')
    c.place(x=70,y=200)
    e2=Entry(t,width='25')
    e2.place(x=400,y=200)
    
    
    d=Label(t,text='Ward No',font=("Arial",15),bg='light blue')
    d.place(x=70,y=275)
    e3=Entry(t,width='25')
    e3.place(x=400,y=275)
    
    e=Label(t,text='Ward Name',font=("Arial",15),bg='light blue')
    e.place(x=70,y=350)
    e4=Entry(t,width='25')
    e4.place(x=400,y=350)
    
    f=Label(t,text='Cand ID',font=("Arial",15),bg='light blue')
    f.place(x=70,y=425)
    e5=Entry(t,width='25')
    e5.place(x=400,y=425)
    
    g=Label(t,text='Cand Name',font=("Arial",15),bg='light blue')
    g.place(x=70,y=500)
    e6=Entry(t,width='25')
    e6.place(x=400,y=500)
    
    
    
    
    bt=Button(t,text='Insert',font=("High Tower",15),fg='white',bg='red',command=savedata)
    bt.place(x=200,y=540)
    
    btt=Button(t,text='Close',font=("High Tower",15),fg='white',bg='red',command=delete)
    btt.place(x=380,y=540)
    
    
    t.mainloop()