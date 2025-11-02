import tkinter
import pymysql
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
def showmemberdelete():
        
    t=tkinter.Tk()
    t.geometry('700x700')
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
     
    def deletedata():
         db=pymysql.connect(host='Localhost',user='root',password='root',database='votingsystem')
         cur=db.cursor()
         xa=int(e1.get())
         
         sql="delete from members where memid=%d"%(xa)
         cur.execute(sql)
         db.commit()
         db.close()
         messagebox.showinfo('Hi','deleted')
         e1.delete(0,100)
    def delete():
         t.destroy()
        
    a=Label(t,text='Member Id',font=("Arial",15),bg='light blue')
    a.place(x=75,y=100)
    e1=ttk.Combobox(t)
    filldata()
    e1['values']=lt
    e1.place(x=180,y=100)
     
    bt=Button(t,text='Delete',font=("High Tower",15),fg='white',bg='red',command=deletedata)
    bt.place(x=150,y=200)
    
    btt=Button(t,text='Close',font=("High Tower",15),fg='white',bg='red',command=delete)
    btt.place(x=250,y=200)
    t.mainloop()
     