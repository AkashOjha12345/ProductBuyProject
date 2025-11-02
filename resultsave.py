import tkinter
import pymysql
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
def showresultdatasave():
        
    t=tkinter.Tk()
    t.geometry('700x700')
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
            xg=e7.get()
            sql="insert into resultdata values('%s','%s','%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf,xg)
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi','Saved')
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            e5.delete(0,100)
            e5.delete(0,100)
            e6.delete(0,100)
            e7.delete(0,100)
            
    
    def ct():
        t.destroy()
        
    a=Label(t,text='Area Code',font=("Arial",15),bg='light blue')
    a.place(x=50,y=70)
    e1=Entry(t,width=30)
    e1.place(x=200,y=70)
    
    b=Label(t,text='Area Name',font=("Arial",15),bg='light blue') 
    b.place(x=50,y=110)
    e2=Entry(t,width=30)
    e2.place(x=200,y=110)
    
    c=Label(t,text='Ward no',font=("Arial",15),bg='light blue')
    c.place(x=50,y=140)
    e3=Entry(t,width=30)
    e3.place(x=200,y=140)
    
    d=Label(t,text='Ward Name',font=("Arial",15),bg='light blue')
    d.place(x=50,y=170)
    e4=Entry(t,width=30)
    e4.place(x=200,y=170)
    
    e=Label(t,text='Cand ID',font=("Arial",15),bg='light blue')
    e.place(x=50,y=200)
    e5=Entry(t,width=30)
    e5.place(x=200,y=200)
    
    f=Label(t,text='Cand Name',font=("Arial",15),bg='light blue')
    f.place(x=50,y=230)
    e6=Entry(t,width=30)
    e6.place(x=200,y=230)
    
    g=Label(t,text='No of votes',font=("Arial",15),bg='light blue')
    g.place(x=50,y=260)
    e7=Entry(t,width=30)
    e7.place(x=200,y=260)
    
    
    i=Button(t,text='Save',font=("High Tower",15),fg='white',bg='red',command=savedata)
    i.place(x=200,y=360)
    
    g=Button(t,text='Close',font=("High Tower",15),fg='white',bg='red',command=ct)
    g.place(x=300,y=360)
    
    t.mainloop()