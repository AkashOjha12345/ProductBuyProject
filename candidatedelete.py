import tkinter
import pymysql
from tkinter import messagebox
from tkinter import*
from tkinter import ttk
def showcandidatedelete():
    

    t=tkinter.Tk()
    t.geometry('700x700')
    t.config(bg='olive')
    
    
    lt=[]
    def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
            cur=db.cursor()
            
            sql="select candid from candidate"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()
    
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from candidate where candid='%s'"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','deleted')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        e8.delete(0,100)
    def ct():
        t.destroy()
        
    a=Label(t,text='Candidate ID',font=("Arial",15),bg='light blue')
    a.place(x=50,y=70)
    e1=ttk.Combobox(t)
    filldata()
    e1['values']=lt
    e1.place(x=200,y=70)
    
    i=Button(t,text='Delete',font=("High Tower",15),fg='white',bg='red',command=deletedata)
    i.place(x=200,y=200)
    
    g=Button(t,text='Close',font=("High Tower",15),fg='white',bg='red',command=ct)
    g.place(x=300,y=200)
    
    t.mainloop()