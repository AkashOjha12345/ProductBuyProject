import random
import smtplib
import pymysql
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from tkinter import messagebox
from tkinter import*
from tkinter import font
from tkinter import ttk
from votingsystemdeshboard import*

t=tkinter.Tk()
t.geometry('700x700')
t.config(bg='light blue')

def sendmail():
    from_address = "gringang98@gmail.com"
    to_address = e1.get()

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = 'OTP'
    msg['From'] = from_address
    msg['To'] = to_address

    # Create the message (HTML).
    r=random.randint(100000, 999999)
    html=str(round(r))

    # Record the MIME type - text/html.
    part1 = MIMEText(html, 'html')

    # Attach parts into message container
    msg.attach(part1)

    # Credentials
    username = 'gringang98@gmail.com'  
    password = 'vazjiuqnoctsdywp'

    # Sending the email
    ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo()
    server.starttls()
    server.login(username,password)  
    server.sendmail(from_address, to_address, msg.as_string())  
    server.quit()
    messagebox.showinfo('Hi','mailsend')
    
    db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
    cur=db.cursor()
    em=to_address
    msg=html
    sql="insert into emailotp values('%s','%s')"%(em,msg)
    cur.execute(sql)
    db.commit()
    db.close()
    messagebox.showinfo('hi','otpdone')


def check():
    db=db=pymysql.connect(host='localhost',user='root',password='root',database='votingsystem')
    cur=db.cursor()
    xa=e1.get()
    xb=e2.get()
    sql="select count(*)from emailotp where email='%s'and otp='%s'"%(xa,xb)
    cur.execute(sql)
    data=cur.fetchone()
    if data[0]==0:
        messagebox.showinfo('HI','OTP not Match')
    else:
        messagebox.showinfo('HI','OTP Match')
        showdeshboard()
        db.close()



x=Label(t,text='VOTING SYSTEM LOGIN',font=("Rockwell",30),bg='light blue')
x.place(x=500,y=100)

a=Label(t,text='Email',font=("High Tide",15),bg='light blue')
a.place(x=400,y=250)
e1=Entry(t,width=50)
e1.place(x=500,y=255)


i=Button(t,text='Send OTP',font=("High Tower",10),fg='white',bg='red',command=sendmail)
i.place(x=850,y=250)

b=Label(t,text='OTP',font=("Bakery",15),bg='light blue')
b.place(x=400,y=350)
e2=Entry(t,width=10)
e2.place(x=500,y=350)

j=Button(t,text='Login',font=("High Tower",12),fg='white',bg='red',command=check)
j.place(x=650,y=420)



t.mainloop()