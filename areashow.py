import tkinter
import pymysql
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
def showareashow():
    
    t=tkinter.Tk()
    t.geometry('700x700')
    t.config(bg='olive')
    
   
    def filldata():
        global msg
        msg=" "
        db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
        cur=db.cursor()
        
        sql="select * from area"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            msg=msg+str(res[0])
            msg=msg+"\t"+res[1]
            msg=msg+"\t"+res[2]
            msg=msg+"\t"+res[3]
            msg=msg+"\t"+res[4]
            msg=msg+"\n"
        db.close()
            
            
    
    e1=Text(t,height=100,width=75)
    filldata()
    e1.insert(END,msg)
    e1.place(x=50,y=50)
    
    
    
    
    
    t.mainloop()