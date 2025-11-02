import tkinter
import pymysql
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
def showvotingdataupdate():
        
    t=tkinter.Tk()
    t.geometry('700x700')
    t.config(bg='olive')
    
    
    lt=[]
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
        cur=db.cursor()
        
        sql="select areacode from votingdata"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
        cur=db.cursor()
        xa=int(e1.get())
        
        sql="select areaname,wardno,wardname,candid,candname from votingdata where areacode=%d"%(xa)
        cur.execute(sql)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
      
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        db.close()
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
        cur=db.cursor()
        xa=e1.get()
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        xf=e6.get()
        sql="update votingdata set areaname='%s',wardno='%s',wardname='%s',candid='%s',candname='%s' where wardno=%s"%(xb,xc,xd,xe,xf,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Updated')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
     
    def ct():
        t.destroy()
            
    a=Label(t,text='Cand ID',font=("Arial",15),bg='light blue')
    a.place(x=75,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1['values']=lt
    e1.place(x=200,y=100)
    
    
    b=Label(t,text='Area Name',font=("Arial",15),bg='light blue')
    b.place(x=70,y=150)
    e2=Entry(t,width='25')
    e2.place(x=200,y=150)
    
    
    c=Label(t,text='Ward No',font=("Arial",15),bg='light blue')
    c.place(x=70,y=200)
    e3=Entry(t,width='25')
    e3.place(x=200,y=200)
    
    d=Label(t,text='Ward Name',font=("Arial",15),bg='light blue')
    d.place(x=70,y=250)
    e4=Entry(t,width='25')
    e4.place(x=200,y=250)
    
    e=Label(t,text='Cand ID',font=("Arial",15),bg='light blue')
    e.place(x=70,y=300)
    e5=Entry(t,width='25')
    e5.place(x=200,y=300)
    
    f=Label(t,text='Cand Name',font=("Arial",15),bg='light blue')
    f.place(x=70,y=350)
    e6=Entry(t,width='25')
    e6.place(x=200,y=350)
    
    x=Button(t,text='Find',font=("High Tower",15),fg='white',bg='red',command=finddata)
    x.place(x=100,y=390)
    
    y=Button(t,text='Update',font=("High Tower",15),fg='white',bg='red',command=updatedata)
    y.place(x=190,y=390)
    
    g=Button(t,text='Close',font=("High Tower",15),fg='white',bg='red',command=ct)
    g.place(x=300,y=390)
    
    t.mainloop()