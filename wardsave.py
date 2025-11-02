import tkinter
import pymysql
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
def showwardsave():
        
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
            sql="insert into wards values('%s','%s','%s','%s')"%(xa,xb,xc,xd)
            cur.execute(sql)
            db.commit()
            db.close()
            messagebox.showinfo('Hi','Saved')
            e1.delete(0,100)
            e2.delete(0,100)
            e3.delete(0,100)
            e4.delete(0,100)
            
    
    def ct():
        t.destroy()
        
    a=Label(t,text='Ward No',font=("Arial",15),bg='light blue')
    a.place(x=50,y=70)
    e1=Entry(t,width=30)
    e1.place(x=200,y=70)
    
    b=Label(t,text='Area Code',font=("Arial",15),bg='light blue') 
    b.place(x=50,y=100)
    e2=Entry(t,width=30)
    e2.place(x=200,y=100)
    
    c=Label(t,text='Area Name',font=("Arial",15),bg='light blue')
    c.place(x=50,y=130)
    e3=Entry(t,width=30)
    e3.place(x=200,y=130)
    
    d=Label(t,text='Ward Name',font=("Arial",15),bg='light blue')
    d.place(x=50,y=160)
    e4=Entry(t,width=30)
    e4.place(x=200,y=160)
    
    i=Button(t,text='Save',font=("High Tower",15),fg='white',bg='red',command=savedata)
    i.place(x=200,y=350)
    
    g=Button(t,text='Close',font=("High Tower",15),fg='white',bg='red',command=ct)
    g.place(x=300,y=350)
    
    t.mainloop()