import tkinter
import pymysql
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
def showcandidatesave():
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
            xh=e8.get()
            sql="insert into candidate values('%s','%s','%s','%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf,xg,xh)
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
            e8.delete(0,100)
    
    def ct():
        t.destroy()
        
    a=Label(t,text='Cand ID',font=("Arial",15),bg='light blue')
    a.place(x=50,y=70)
    e1=Entry(t,width=30)
    e1.place(x=200,y=70)
    
    b=Label(t,text='Cand Name',font=("Arial",15),bg='light blue') 
    b.place(x=50,y=100)
    e2=Entry(t,width=30)
    e2.place(x=200,y=100)
    
    c=Label(t,text='Address',font=("Arial",15),bg='light blue')
    c.place(x=50,y=130)
    e3=Entry(t,width=30)
    e3.place(x=200,y=130)
    
    d=Label(t,text='Email',font=("Arial",15),bg='light blue')
    d.place(x=50,y=160)
    e4=Entry(t,width=30)
    e4.place(x=200,y=160)
    
    e=Label(t,text='Phone NO',font=("Arial",15),bg='light blue')
    e.place(x=50,y=190)
    e5=Entry(t,width=30)
    e5.place(x=200,y=190)
    
    f=Label(t,text='Age',font=("Arial",15),bg='light blue')
    f.place(x=50,y=220)
    e6=Entry(t,width=30)
    e6.place(x=200,y=220)
    
    g=Label(t,text='Word NO',font=("Arial",15),bg='light blue')
    g.place(x=50,y=250)
    e7=Entry(t,width=30)
    e7.place(x=200,y=250)
    
    h=Label(t,text='Status',font=("Arial",15),bg='light blue')
    h.place(x=50,y=280)
    e8=Entry(t,width=30)
    e8.place(x=200,y=280)
    
    i=Button(t,text='Save',font=("High Tower",15),fg='white',bg='red',command=savedata)
    i.place(x=200,y=350)
    
    g=Button(t,text='Close',font=("High Tower",15),fg='white',bg='red',command=ct)
    g.place(x=300,y=350)
    
    t.mainloop()