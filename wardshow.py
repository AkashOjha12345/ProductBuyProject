import tkinter
import pymysql
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
def showwardshow():
        
    t=tkinter.Tk()
    t.geometry('700x700')
    t.config(bg='olive')
    
    
    def filldata():
        global msg
        msg=""
        db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
        cur=db.cursor()
        sql="select * from wards"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            msg=msg+"\t"+(res[0])
            msg=msg+"\t"+(res[1])
            msg=msg+"\t"+(res[2])
            msg=msg+"\t"+(res[3])
            msg=msg+"\n"
        db.close()
            
    e1=Text(t,height=40,width=70)
    e1.place(x=50,y=50)
    filldata()
    e1.insert(END,msg)
    t.mainloop()