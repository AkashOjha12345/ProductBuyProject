import tkinter
import pymysql
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
def showvotingdatafind():
        
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
    
    def delete():
        t.destroy()
    
    a=Label(t,text='Area code',font=("Arial",15),bg='light blue')
    a.place(x=75,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1['values']=lt
    e1.place(x=250,y=100)
    
    g=Button(t,text='Find',font=("High Tower",15),fg='white',bg='red',command=finddata)
    g.place(x=75,y=150)
    
    
    b=Label(t,text='Area Name',font=("Arial",15),bg='light blue')
    b.place(x=70,y=200)
    e2=Entry(t,width='25')
    e2.place(x=400,y=200)
    
    
    c=Label(t,text='Ward No',font=("Arial",15),bg='light blue')
    c.place(x=70,y=275)
    e3=Entry(t,width='25')
    e3.place(x=400,y=275)
    
    d=Label(t,text='Ward Name',font=("Arial",15),bg='light blue')
    d.place(x=70,y=350)
    e4=Entry(t,width='25')
    e4.place(x=400,y=350)
    
    e=Label(t,text='Cand ID',font=("Arial",15),bg='light blue')
    e.place(x=70,y=425)
    e5=Entry(t,width='25')
    e5.place(x=400,y=425)
    
    f=Label(t,text='Cand Name',font=("Arial",15),bg='light blue')
    f.place(x=70,y=500)
    e6=Entry(t,width='25')
    e6.place(x=400,y=500)
    
    g=Button(t,text='Find',font=("High Tower",15),fg='white',bg='red',command=finddata)
    g.place(x=75,y=150)
    
    btt=Button(t,text='Close',font=("High Tower",15),fg='white',bg='red',command=delete)
    btt.place(x=450,y=550)
    
    t.mainloop()