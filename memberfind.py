import tkinter
import pymysql
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
def showmemberfind():
        
    t=tkinter.Tk()
    t.geometry('800x700')
    t.config(bg='olive')
    
    lt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
        cur=db.cursor()
        
        sql="select memid from members"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
        cur=db.cursor()
        xa=int(e1.get())
        
        sql="select memname,memaddress,memphoneno from members where memid=%d"%(xa)
        cur.execute(sql)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
      
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
       
        db.close()
    def delete():
        t.destroy()
    
    a=Label(t,text='Member ID',font=("Arial",15),bg='light blue')
    a.place(x=75,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1['values']=lt
    e1.place(x=250,y=100)
    
    g=Button(t,text='Find',font=("High Tower",15),fg='white',bg='red',command=finddata)
    g.place(x=75,y=150)
    
    b=Label(t,text='Member Name',font=("Arial",15),bg='light blue')
    b.place(x=75,y=200)
    e2=Entry(t,width='25')
    e2.place(x=250,y=200)
    
    c=Label(t,text='Member Address',font=("Arial",15),bg='light blue')
    c.place(x=75,y=250)
    e3=Entry(t,width='25')
    e3.place(x=250,y=250)
    
    
    f=Label(t,text='Member Phoneno',font=("Arial",15),bg='light blue')
    f.place(x=75,y=300)
    e4=Entry(t,width='25')
    e4.place(x=250,y=300)
    
    btt=Button(t,text='Close',font=("High Tower",15),fg='white',bg='red',command=delete)
    btt.place(x=300,y=350)
    
    
    
    t.mainloop()