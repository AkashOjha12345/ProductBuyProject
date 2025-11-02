import tkinter
import pymysql
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
def showelectionscheduledelete():
        
    t=tkinter.Tk()
    t.geometry('500x500')
    t.config(bg='olive')
        
    
    lt=[]
    def filldata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
            cur=db.cursor()
            
            sql="select wardno from electionschedule"
            cur.execute(sql)
            data=cur.fetchall()
            for res in data:
                lt.append(res[0])
            db.close()
     
    def deletedata():
         db=pymysql.connect(host='Localhost',user='root',password='root',database='votingsystem')
         cur=db.cursor()
         xa=int(e1.get())
         sql="delete from electionschedule where wardno=%d"%(xa)
         cur.execute(sql)
         db.commit()
         db.close()
         messagebox.showinfo('Hi','deleted')
         e1.delete(0,100)
    def delete():
        t.destroy()
     
    a=Label(t,text='Ward No',font=("Arial",15),bg='light blue')
    a.place(x=75,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1['values']=lt
    e1.place(x=180,y=100)
     
    bt=Button(t,text='Delete',font=("High Tower",15),fg='white',bg='red',command=deletedata)
    bt.place(x=100,y=200)
    btt=Button(t,text='Close',font=("High Tower",15),fg='white',bg='red',command=delete)
    btt.place(x=200,y=200)
    
     
    t.mainloop()
     