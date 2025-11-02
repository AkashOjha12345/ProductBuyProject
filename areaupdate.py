import tkinter
import pymysql
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
def showareaupdate():
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='olive')


    
    lt=[]
    def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
            cur=db.cursor()
            
            sql="select areacode from area"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()
            
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
        cur=db.cursor()
        xa=int(e1.get())
        
        sql="select areaname,city,state,country from area where areacode=%d"%(xa)
        cur.execute(sql)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
      
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        db.close()
    
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        sql="Update area set areaname='%s',city='%s',state='%s',country='%s' where areacode=%d"%(xb,xc,xd,xe,xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','Data updated')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        
    def delete():
        t.destroy()
    
    
    a=Label(t,text='Area Code')
    a.place(x=75,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1['values']=lt
    e1.place(x=250,y=100)
    
    g=Button(t,text='Find',font='25',command=finddata,fg='red')
    g.place(x=75,y=150)
    
    b=Label(t,text='Area Name',font=("Arial",15),bg='light blue')
    b.place(x=75,y=200)
    e2=Entry(t,width='25')
    e2.place(x=250,y=200)
    
    c=Label(t,text='City',font=("Arial",15),bg='light blue')
    c.place(x=75,y=250)
    e3=Entry(t,width='25')
    e3.place(x=250,y=250)
    
    
    f=Label(t,text='State',font=("Arial",15),bg='light blue')
    f.place(x=75,y=300)
    e4=Entry(t,width='25')
    e4.place(x=250,y=300)
    
    g=Label(t,text='Country',font=("Arial",15),bg='light blue')
    g.place(x=70,y=350)
    e5=Entry(t,width='25')
    e5.place(x=250,y=350)
    
    
    
    bt=Button(t,text='Close',font=("High Tower",15),fg='white',bg='red',command=delete)
    bt.place(x=300,y=400)
    
    btt=Button(t,text='Update',font=("High Tower",15),fg='white',bg='red',command=updatedata)
    btt.place(x=200,y=400)
    
    
    t.mainloop()
    