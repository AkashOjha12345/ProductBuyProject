import tkinter
import pymysql
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
def showwardupdate():
    t=tkinter.Tk()
    t.geometry('700x700')
    t.config(bg='olive')
        
    
    lt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
        cur=db.cursor()
        
        sql="select wardno from wards"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
        cur=db.cursor()
        xa=e1.get()
        sql="select wardno,areacode,areaname,wardname from wards where wardno='%s'"%(xa)
        cur.execute(sql)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        data=cur.fetchone()
        e2.insert(0,data[1])
        e3.insert(0,data[2])
        e4.insert(0,data[3])
        db.close()
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
        cur=db.cursor()
        xa=e1.get()
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        sql="update wards set areacode='%s',areaname='%s',wardname='%s' where wardno=%s"%(xb,xc,xd,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Updated')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
     
    def ct():
        t.destroy()
            
    a=Label(t,text='Ward No',font=("Arial",15),bg='light blue')
    a.place(x=50,y=70)
    e1=ttk.Combobox(t)
    filldata()
    e1['values']=lt
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
    
    x=Button(t,text='Find',font=("High Tower",15),fg='white',bg='red',command=finddata)
    x.place(x=100,y=350)
    
    y=Button(t,text='Update',font=("High Tower",15),fg='white',bg='red',command=updatedata)
    y.place(x=190,y=350)
    
    g=Button(t,text='Close',font=("High Tower",15),fg='white',bg='red',command=ct)
    g.place(x=300,y=350)
    
    t.mainloop()