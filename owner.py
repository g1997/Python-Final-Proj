import subprocess
from tkinter import *
import tkinter as tk 
import tkinter.font as tkfont
from tkinter.messagebox import *
import  tkinter.ttk as ttk
import mysql.connector as conn
dbconn=conn.connect(host="localhost",
                    user="root",
                    passwd="",
                    database="hotelmgmtsys"
                    )
def obtain():
    cur=dbconn.cursor()
    sql="select count(fname) from customer_counts"
    cur.execute(sql)
    data=cur.fetchall()
    listbox.insert(END,"No of customers visited: ",data)
    sql3="select count(Emp_ID) from employee"
    cur.execute(sql3)
    data=cur.fetchall()
    listbox.insert(END,"No of Employees: ",data)
    sql4="select avg(salary) from employee"
    cur.execute(sql4)
    data=cur.fetchall()
    listbox.insert(END,"Average salary of employees: ",data)
    sql4="select max(salary) from employee"
    cur.execute(sql4)
    data=cur.fetchall()
    listbox.insert(END,"Highest Salary: ",data)
    sql4="select count(Emp_ID) from employee"
    cur.execute(sql4)
    data=cur.fetchall()
    listbox.insert(END,"Total No of Employees: ",data)
    sql4="select sum(rate) from customer where status='CHECKED-IN'"
    cur.execute(sql4)
    data=cur.fetchall()
    listbox.insert(END,"Total Price : ",data)
    sql4="select count(rate) from customer"
    cur.execute(sql4)
    data=cur.fetchall()
    listbox.insert(END,"Total Price : ",data)
    sql4="select count(fname) from customer where status='BOOKED'"
    cur.execute(sql4)
    data=cur.fetchall()
    listbox.insert(END,"Rooms Booked : ",data)
    sql4="select count(fname) from customer where status='CHECKED-IN'"
    cur.execute(sql4)
    data=cur.fetchall()
    listbox.insert(END,"Rooms Checked-In : ",data)
def cus_data():
    win1=Toplevel(win)
    win1["bg"]="blue"
    win1.geometry("800x300-100+100")
    tree = ttk.Treeview(win1)
    tree.pack(side=TOP)
    scrollbar_horizontal = ttk.Scrollbar(win1, orient='horizontal', command = tree.xview)    
    scrollbar_vertical = ttk.Scrollbar(win1, orient='vertical', command = tree.yview)   
    scrollbar_horizontal.pack(side='bottom', fill=X)    
    scrollbar_vertical.pack(side='right', fill=Y)
    tree.configure(xscrollcommand=scrollbar_horizontal.set, yscrollcommand=scrollbar_vertical.set)
    tree["columns"]=('fname','lname','age','mobile','chk_in_day','month','year','chk_out_day','out_month','out_year','type','chk_in_time','room_no','rate','status')
    tree.column("fname", width=90)
    tree.column("lname", width=90 )
    tree.column("age", width=90 )
    tree.column("mobile", width=90 )
    tree.column("chk_in_day", width=90 )
    tree.column("month", width=90 )
    tree.column("year", width=90 )
    tree.column("chk_out_day", width=90 )
    tree.column("out_month", width=90 )
    tree.column("out_year", width=90 )
    tree.column("type", width=90)
    tree.column("chk_in_time", width=90)
    tree.column("room_no", width=90 )
    tree.column("rate", width=90)
    tree.column("status", width=90)
    tree.heading("fname", text="FIRST NAME")
    tree.heading("lname", text="LAST NAME")
    tree.heading("age", text="AGE" )
    tree.heading("mobile", text="MOBILE_NO" )
    tree.heading("chk_in_day", text="CHECK IN DAY" )
    tree.heading("month", text="CHECK_IN_MONTH" )
    tree.heading("year", text="CHECK_IN_YEAR" )
    tree.heading("chk_out_day", text="CHEK_OUT_DAY" )
    tree.heading("out_month", text="CHECK_OUT_MONTH" )
    tree.heading("out_year", text="CHECK_OUT_YEAR" )
    tree.heading("type", text="type" )
    tree.heading("chk_in_time", text="CHECK_N_TIME")
    tree.heading("room_no", text="Room Number" )
    tree.heading("rate", text="Room Rate" )
    tree.heading("status", text="STATUS" )
    cur=dbconn.cursor()
    sql="Select * from customer"
    cur.execute(sql)
    data=cur.fetchall()
    for i in data:
        tree.insert("", tk.END, values=i)
    win1.mainloop()
def emp_data():
    win1=Toplevel(win)
    win1["bg"]="sky blue"
    win1.geometry("900x400-100+100")
    tree = ttk.Treeview(win1)
    tree.pack(side=TOP)
    scrollbar_horizontal = ttk.Scrollbar(win1, orient='horizontal', command = tree.xview)    
    scrollbar_vertical = ttk.Scrollbar(win1, orient='vertical', command = tree.yview)   
    scrollbar_horizontal.pack(side='bottom', fill=X)    
    scrollbar_vertical.pack(side='right', fill=Y)
    tree.configure(xscrollcommand=scrollbar_horizontal.set, yscrollcommand=scrollbar_vertical.set)
    tree["columns"]=('EID','fname','lname','DOB','Designation','salary')
    tree.column("EID", width=90)
    tree.column("fname", width=90 )
    tree.column("lname", width=90 )
    tree.column("DOB", width=90 )
    tree.column("Designation", width=90 )
    tree.column("salary", width=90 )
    tree.heading("EID", text="EMPLOYEE ID")
    tree.heading("fname", text="FIRST NAME")
    tree.heading("lname", text="LAST NAME" )
    tree.heading("DOB", text="Date Of Birth" )
    tree.heading("Designation", text="Designaton" )
    tree.heading("salary", text="Salary" )
    cur=dbconn.cursor()
    sql="Select * from employee"
    cur.execute(sql)
    data=cur.fetchall()
    for i in data:
        tree.insert("", tk.END, values=i)
    win1.mainloop()

def clear():
    listbox.insert(END," ")
win=Tk()
win["bg"]="sky blue"
win.geometry("900x675-100+100")
frame=Frame(win)
frame.pack(side=TOP)
#frame2=Frame(win)
#frame2.pack(side=BOTTOM)
listbox=Listbox(frame,bd=7,bg="white",fg="black",font=("Cooper Black",12),height=15,width=30)
listbox.pack(side=TOP)
ob_data=Button(frame,text="Get Info",bg="lightcyan2",fg="black",bd=7,command=obtain,font=("Cooper Black",15))
ob_data.pack(side=BOTTOM)
cus_data=Button(frame,text=" Customer Table:",bg="lightcyan2",fg="black",bd=7,command=cus_data,font=("Cooper Black",15))
cus_data.pack(side=BOTTOM)
emp_data=Button(frame,text=" Employee Table:",bg="lightcyan2",fg="black",bd=7,command=emp_data,font=("Cooper Black",15))
emp_data.pack(side=BOTTOM)
clear=Button(frame,text=" Clear:",bg="lightcyan2",fg="black",bd=7,command=clear,font=("Cooper Black",15))
clear.pack(side=BOTTOM)
win.mainloop()
