from os import *
import datetime
from datetime import date
from datetime import timedelta 
from tkinter.ttk import *
from tkinter import *
import tkinter.font as tkfont
from tkinter.messagebox import *
import mysql.connector as conn
dbconn=conn.connect(host="localhost",
                    user="root",
                    passwd="",
                    database="hotelmgmtsys"
                    )
def login():
    cur=dbconn.cursor()
    sql="select * from admin where id='{}' and pwd='{}'".format(idtxt.get(),pwdtxt.get())
    cur.execute(sql)
    if(cur.fetchall()):
        showinfo(title="Success",message="Record Found")
        win.destroy()
        from subprocess import Popen
        Popen(["python","admin_manage.py"])
    else:
        showerror(title="Failure",message="Record Not Found")
def back():
    win.destroy()
    import hmsproj_main
    hmsproj_main.main()

win=Tk()
win["bg"]="sky blue"
win.geometry("675x400+100+100")
ids=Label(text="Enter admin id:",bg="azure",fg="black",font=("Times New Roman",15))
ids.grid(row="0",column="0")
idtxt=Entry(bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
idtxt.grid(row="0",column="1")
pwd=Label(text="Enter Password:",bg="azure",fg="black",font=("Times New Roman",15))
pwd.grid(row="1",column="0")
pwdtxt=Entry(bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
pwdtxt.grid(row="1",column="1")
login=Button(win,text="Login",bg="lightcyan2",fg="black",bd=7,command=login,font=("Cooper Black",15))
login.grid(row="2",column="1")
back=Button(win,text="Back",bg="lightcyan2",fg="black",bd=7,command=back,font=("Cooper Black",15))
back.grid(row="2",column="2")
win.mainloop()
