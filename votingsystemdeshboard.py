import tkinter
import pymysql
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from areasave import*
from areafind import*
from areadelete import*
from areaupdate import*
from areashow import*
from candidatesave import*
from candidatefind import*
from candidatedelete import*
from candidateupdate import*
from candidateshow import*
from wardsave import*
from wardfind import*
from warddelete import*
from wardupdate import*
from wardshow import*
from electionsave import*
from electionfind import*
from electiondelete import*
from electionupdate import*
from electionshow import*
from membersave import*
from memberfind import*
from memberdelete import*
from memberupdate import*
from membershow import*
from testvotingsave import*
from votingdatafind import*
from votingdatadelete import*
from votingdataupdate import*
from votingdatashow import*
from resultsave import*
from resultfind import*
from resultdelete import*
from resultupdate import*
from resultshow import*

def showdeshboard():
    

    t=tkinter.Tk()
    t.geometry('1000x1000')
    t.config(bg='light blue')
    
    s=Label(t,text='VOTING SYSTEM APPLICATION',font=("Georgia",20),fg='olive',bg='light blue')
    s.place(x=400,y=30)
    
    a=Label(t,text='AREA :-',font=("High Tower",20),fg='black',bg='light blue')
    a.place(x=60,y=100)
    
    
    b1=Button(t,text='SAVE',font=("High Tower",15),fg='white',bg='red',command=showareasavedata)
    b1.place(x=80,y=150)
    
    b2=Button(t,text='FIND',font=("High Tower",15),fg='white',bg='red',command=showareafind)
    b2.place(x=180,y=150)
    
    
    b3=Button(t,text='DELETE',font=("High Tower",15),fg='white',bg='red',command=showareadelete)
    b3.place(x=260,y=150)
    
    b4=Button(t,text='UPDATE',font=("High Tower",15),fg='white',bg='red',command=showareaupdate)
    b4.place(x=370,y=150)
    
    b5=Button(t,text='SHOW',font=("High Tower",15),fg='white',bg='red',command=showareashow)
    b5.place(x=480,y=150)
    
    b=Label(t,text='CANDIDATE :-',font=("High Tower",20),fg='black',bg='light blue')
    b.place(x=60,y=200)
    
    
    b6=Button(t,text='SAVE',font=("High Tower",15),fg='white',bg='red',command=showcandidatesave)
    b6.place(x=80,y=250)
    
    b7=Button(t,text='FIND',font=("High Tower",15),fg='white',bg='red',command=showcandidatefind)
    b7.place(x=180,y=250)
    
    
    b8=Button(t,text='DELETE',font=("High Tower",15),fg='white',bg='red',command=showcandidatedelete)
    b8.place(x=260,y=250)
    
    b9=Button(t,text='UPDATE',font=("High Tower",15),fg='white',bg='red',command=showcandidateupdate)
    b9.place(x=370,y=250)
    
    b10=Button(t,text='SHOW',font=("High Tower",15),fg='white',bg='red',command=showcandidateshow)
    b10.place(x=480,y=250)
    
    C=Label(t,text='WARD :-',font=("High Tower",20),fg='black',bg='light blue')
    C.place(x=60,y=300)
    
    
    b11=Button(t,text='SAVE',font=("High Tower",15),fg='white',bg='red',command=showwardsave)
    b11.place(x=80,y=350)
    
    b12=Button(t,text='FIND',font=("High Tower",15),fg='white',bg='red',command=showwardfind)
    b12.place(x=180,y=350)
    
    
    b13=Button(t,text='DELETE',font=("High Tower",15),fg='white',bg='red',command=showwarddelete)
    b13.place(x=260,y=350)
    
    b14=Button(t,text='UPDATE',font=("High Tower",15),fg='white',bg='red',command=showwardupdate)
    b14.place(x=370,y=350)
    
    b15=Button(t,text='SHOW',font=("High Tower",15),fg='white',bg='red',command=showwardshow)
    b15.place(x=480,y=350)
    
    d=Label(t,text='ELECTION SCHEDULE :-',font=("High Tower",20),fg='black',bg='light blue')
    d.place(x=60,y=400)
    
    
    b11=Button(t,text='SAVE',font=("High Tower",15),fg='white',bg='red',command=showelectionschedulesave)
    b11.place(x=80,y=450)
    
    b12=Button(t,text='FIND',font=("High Tower",15),fg='white',bg='red',command=showelectionschedulefind)
    b12.place(x=180,y=450)
    
    
    b13=Button(t,text='DELETE',font=("High Tower",15),fg='white',bg='red',command=showelectionscheduledelete)
    b13.place(x=260,y=450)
    
    b14=Button(t,text='UPDATE',font=("High Tower",15),fg='white',bg='red',command=showelectionscheduleupdate)
    b14.place(x=370,y=450)
    
    b15=Button(t,text='SHOW',font=("High Tower",15),fg='white',bg='red',command=showelectionscheduleshow)
    b15.place(x=480,y=450)
    
    
    e=Label(t,text='MEMBER :-',font=("High Tower",20),fg='black',bg='light blue')
    e.place(x=60,y=500)
    
    
    b16=Button(t,text='SAVE',font=("High Tower",15),fg='white',bg='red',command=showmembersave)
    b16.place(x=80,y=550)
    
    b17=Button(t,text='FIND',font=("High Tower",15),fg='white',bg='red',command=showmemberfind)
    b17.place(x=180,y=550)
    
    
    b18=Button(t,text='DELETE',font=("High Tower",15),fg='white',bg='red',command=showmemberdelete)
    b18.place(x=260,y=550)
    
    b19=Button(t,text='UPDATE',font=("High Tower",15),fg='white',bg='red',command=showmemberupdate)
    b19.place(x=370,y=550)
    
    b20=Button(t,text='SHOW',font=("High Tower",15),fg='white',bg='red',command=showmembershow)
    b20.place(x=480,y=550)
    
    f=Label(t,text='VOTINGDATA :-',font=("High Tower",20),fg='black',bg='light blue')
    f.place(x=60,y=600)
    
    
    b21=Button(t,text='SAVE',font=("High Tower",15),fg='white',bg='red',command=showvotingsaves)
    b21.place(x=80,y=650)
    
    b22=Button(t,text='FIND',font=("High Tower",15),fg='white',bg='red',command=showvotingdatafind)
    b22.place(x=180,y=650)
    
    
    b23=Button(t,text='DELETE',font=("High Tower",15),fg='white',bg='red',command=showvotingdatadelete)
    b23.place(x=260,y=650)
    
    b24=Button(t,text='UPDATE',font=("High Tower",15),fg='white',bg='red',command=showvotingdataupdate)
    b24.place(x=370,y=650)
    
    
    b25=Button(t,text='SHOW',font=("High Tower",15),fg='white',bg='red',command=showvotingdatashow)
    b25.place(x=480,y=650)
    
    g=Label(t,text='RESULTDATA :-',font=("High Tower",20),fg='black',bg='light blue')
    g.place(x=60,y=700)
    
    b26=Button(t,text='SAVE',font=("High Tower",15),fg='white',bg='red',command=showresultdatasave)
    b26.place(x=80,y=750)
    
    b27=Button(t,text='FIND',font=("High Tower",15),fg='white',bg='red',command=showresultfind)
    b27.place(x=180,y=750)
    
    
    b28=Button(t,text='DELETE',font=("High Tower",15),fg='white',bg='red',command=showresultdelete)
    b28.place(x=260,y=750)
    
    b29=Button(t,text='UPDATE',font=("High Tower",15),fg='white',bg='red',command=showresultupdate)
    b29.place(x=370,y=750)
    
    b30=Button(t,text='SHOW',font=("High Tower",15),fg='white',bg='red',command=showresultshow)
    b30.place(x=480,y=750)
    
    
    
    
    
    
    t.mainloop()