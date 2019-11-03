#HOTEL MANAGEMENT SYSTEM USING PYTHON TKINTER DBMS
import subprocess
from tkinter import *
import tkinter.font as tkfont
from tkinter.messagebox import *
#from tkinter.ttk import *
import mysql.connector as conn

def admin():
    try:
        win.destroy()
        from subprocess import Popen
        Popen(["python", "admin_login.py"])
    except Exception as e:
        print(e)
def owner():
    try:
        win.destroy()
        from subprocess import Popen
        Popen(["python", "owner_login.py"])
    except Exception as e:
        print(e)
def main():
    try:
        win.geometry("400x300")
        #win["bg"]="blue"
        #admin=Button(win,text="Admin login",bg="lightcyan2",fg="snow2",bd=7,command=admin,font=("Cooper Black",15))
        admin_login.grid(row="0",column="0")
        #book=Button(win,text="Book Room",bg="lightcyan2",fg="snow2",bd=7,command=book,font=("Cooper Black",15))
        owner_login.grid(row="0",column="3")
        win.mainloop()
    except Exception as e:
        print(e)
try:
    win=Tk()
    win["bg"]="sky blue"
    admin_login=Button(win,text="Admin login",bg="lightcyan2",fg="black",bd=7,command=admin,font=("Cooper Black",15))
    owner_login=Button(win,text="Owner Login",bg="lightcyan2",fg="black",bd=7,command=owner,font=("Cooper Black",15))
    #search=Button(win,text="Search Customer",bg="lightcyan2",fg="snow2",bd=7,command=book,font=("Cooper Black",15))
    main()
    admin()
    owner()
except Exception as e:
    print(e)
