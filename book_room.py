from os import system
import tkinter as tk
import datetime
from datetime import date
from datetime import timedelta 
from tkinter.ttk import *
from tkinter import *
import tkinter.font as tkfont
from tkinter.messagebox import *
#import book_customer as bk
import random
import mysql.connector as conn
AC=list()
NON_AC=list()
Ac_rate=5000
Non_ac_rate=2500
result=list()
res=list()
dbconn=conn.connect(host="localhost",
                    user="root",
                    passwd="",
                    database="hotelmgmtsys"
                    )
def allot_ac():# to allot ac room to customer
    cur=dbconn.cursor()
    cur2=dbconn.cursor()
    sql="select * from ac_room"
    cur.execute(sql)
    result=cur.fetchall()
    for i in result:
        res.append(list(i))
    for i in res:
        for j in i:
            if int(allottxt.get())==j:
                    cur=dbconn.cursor()
                    date1=date(int(year.get()),int(month.get()),int(day.get()))
                    date2=date(int(year2.get()),int(month2.get()),int(day2.get()))
                    days1=(date2-date1)
                    days1=days1//timedelta(days=1)
                    rate_ac=days1*Ac_rate
                    print(fnametxt.get(),lnametxt.get(),agetxt.get(),mobiletxt.get(),int(day.get()),int(month.get()),int(year.get()),int(day2.get()),int(month2.get()),int(year2.get()),int(allottxt.get()),rate_ac)
                    sql="insert into  customer values('{}','{}',{},{},{},{},{},{},{},{},'AC','NA',{},{},'BOOKED')".format(fnametxt.get(),lnametxt.get(),agetxt.get(),mobiletxt.get(),int(day.get()),int(month.get()),int(year.get()),int(day2.get()),int(month2.get()),int(year2.get()),int(allottxt.get()),rate_ac)
                    cur.execute(sql)
                    if cur.rowcount>0 and cur2.rowcount>0:
                        showinfo(title="Success",message="Record Added")
                        win1.destroy()
                        win.destroy()
                        from subprocess import Popen
                        Popen(["python","book_room.py"])
                    else:
                        showinfo(title="Failure",message="Failed to Add record")
            else:
                showinfo(title="Failure",message="Failed to Add record")
def allot_nonac(): # to allot non_ac room to customer
    cur=dbconn.cursor()
    cur2=dbconn.cursor()
    sql="select * from non_ac_room"
    cur.execute(sql)
    result=cur.fetchall()
    for i in result:
        res.append(list(i))
    for i in res:
        for j in i:
            if int(allottxt.get())==j:
                cur=dbconn.cursor()
                date1=date(int(year.get()),int(month.get()),int(day.get()))
                date2=date(int(year2.get()),int(month2.get()),int(day2.get()))
                days1=(date2-date1)
                days1=days1//timedelta(days=1)
                rate_ac=days1*Non_ac_rate
                sql="insert into  customer values('{}','{}',{},'{}',{},{},{},{},{},{},'NON-AC','NA',{},{},'BOOKED')".format(fnametxt.get(),lnametxt.get(),agetxt.get(),mobiletxt.get(),int(day.get()),int(month.get()),int(year.get()),int(day2.get()),int(month2.get()),int(year2.get()),int(allottxt.get()),rate_ac)
                cur.execute(sql)
                sql2="delete from non_ac_room where non_ac={}".format(allottxt.get())
                cur.execute(sql2)
                dbconn.commit()
                if cur.rowcount>0:
                        showinfo(title="Success",message="Record Added")
                        win1.destroy()
                        win.destroy()
                        from subprocess import Popen
                        Popen(["python","book_room.py"])
                    
                else:
                    showerror(title="Failure",message="Failed to Add record")
            else:
                showerror(title="Failure",message="Room Not Available")

def viewtable_ac():
    win1=Toplevel(win)
    win1["bg"]="sky blue"
    win1.geometry("800x300-100+100")
    tree = ttk.Treeview(win1)
    tree.pack(side=TOP)
    scrollbar_horizontal = ttk.Scrollbar(win1, orient='horizontal', command = tree.xview)    
    scrollbar_vertical = ttk.Scrollbar(win1, orient='vertical', command = tree.yview)   
    scrollbar_horizontal.pack(side='bottom', fill=X)    
    scrollbar_vertical.pack(side='right', fill=Y)
    tree.configure(xscrollcommand=scrollbar_horizontal.set, yscrollcommand=scrollbar_vertical.set)
    tree["columns"]=('fname','lname','chk_in_day','month','year','chk_out_day','out_month','out_year','chk_in_time','room_no','status')
    tree.column("fname", width=90)
    tree.column("lname", width=90 )
    tree.column("chk_in_day", width=90 )
    tree.column("month", width=90 )
    tree.column("year", width=90 )
    tree.column("chk_out_day", width=90 )
    tree.column("out_month", width=90 )
    tree.column("out_year", width=90 )
    tree.column("chk_in_time", width=90)
    tree.column("room_no", width=90 )
    tree.column("status", width=90)
    tree.heading("fname", text="FIRST NAME")
    tree.heading("lname", text="LAST NAME")
    tree.heading("chk_in_day", text="CHECK IN DAY" )
    tree.heading("month", text="CHECK_IN_MONTH" )
    tree.heading("year", text="CHECK_IN_YEAR" )
    tree.heading("chk_out_day", text="CHEK_OUT_DAY" )
    tree.heading("out_month", text="CHECK_OUT_MONTH" )
    tree.heading("out_year", text="CHECK_OUT_YEAR" )
    tree.heading("chk_in_time", text="CHECK_N_TIME")
    tree.heading("room_no", text="Room Number" )
    tree.heading("status", text="STATUS" )
    cur=dbconn.cursor()
    sql=" select fname,lname,chk_in_day,chk_in_month,chk_in_year,chk_out_day,chk_out_month,chk_out_year,check_in_time,room_no,status from customer where type='AC'"
    cur.execute(sql)
    data=cur.fetchall()
    for i in data:
        tree.insert("", tk.END, values=i)
    win1.mainloop()
def viewtable_nonac():
    win1=Toplevel(win)
    win1["bg"]="sky blue"
    win1.geometry("800x300-100+100")
    tree = ttk.Treeview(win1)
    tree.pack(side=TOP)
    scrollbar_horizontal = ttk.Scrollbar(win1, orient='horizontal', command = tree.xview)    
    scrollbar_vertical = ttk.Scrollbar(win1, orient='vertical', command = tree.yview)   
    scrollbar_horizontal.pack(side='bottom', fill=X)    
    scrollbar_vertical.pack(side='right', fill=Y)
    tree.configure(xscrollcommand=scrollbar_horizontal.set, yscrollcommand=scrollbar_vertical.set)
    tree["columns"]=('fname','lname','chk_in_day','month','year','chk_out_day','out_month','out_year','chk_in_time','room_no','status')
    tree.column("fname", width=90)
    tree.column("lname", width=90 )
    tree.column("chk_in_day", width=90 )
    tree.column("month", width=90 )
    tree.column("year", width=90 )
    tree.column("chk_out_day", width=90 )
    tree.column("out_month", width=90 )
    tree.column("out_year", width=90 )
    tree.column("chk_in_time", width=90)
    tree.column("room_no", width=90 )
    tree.column("status", width=90)
    tree.heading("fname", text="FIRST NAME")
    tree.heading("lname", text="LAST NAME")
    tree.heading("chk_in_day", text="CHECK IN DAY" )
    tree.heading("month", text="CHECK_IN_MONTH" )
    tree.heading("year", text="CHECK_IN_YEAR" )
    tree.heading("chk_out_day", text="CHEK_OUT_DAY" )
    tree.heading("out_month", text="CHECK_OUT_MONTH" )
    tree.heading("out_year", text="CHECK_OUT_YEAR" )
    tree.heading("chk_in_time", text="CHECK_N_TIME")
    tree.heading("room_no", text="Room Number" )
    tree.heading("status", text="STATUS" )
    cur=dbconn.cursor()
    sql=" select fname,lname,chk_in_day,chk_in_month,chk_in_year,chk_out_day,chk_out_month,chk_out_year,check_in_time,room_no,status from customer where type='NON-AC'"
    cur.execute(sql)
    data=cur.fetchall()
    for i in data:
        tree.insert("", tk.END, values=i)
    
def validate(val): #to check available ac and non-ac rooms 
    if(val==1):
        win1.title("Allot Rooms")
        win1.geometry("600x300+700+300")
        win1["bg"]="sky blue"
        cur=dbconn.cursor()
        sql="select * from ac_room"
        cur.execute(sql)
        result=list(cur.fetchall())
        sql2="select room_no from customer where type='AC' and status='CHECKED-IN'"
        cur.execute(sql2)
        result2=list(cur.fetchall())
        res=Label(win1,bg="lawn green",text="Avalable AC Rooms:  ",font=("arial black",15))
        resultLabel = Label(win1,bg="lawn green",text =result,font=("arial black",15))
        res.grid(row="1",column="0")
        resultLabel.grid(row="1",column="1")
        res2=Label(win1,bg="red2",text="Checked-In Rooms:  ",font=("arial black",15))
        resultLabel2= Label(win1,bg="red2",text =result2,font=("arial black",15))
        res2.grid(row="2",column="0")
        resultLabel2.grid(row="2",column="1")
        allot=Label(win1,text="Select Room to Allot",bg="azure",fg="black",font=("Times New Roman",15))
        allot.grid(row="3",column="0")
        allottxt.grid(row="3",column="1")
        alt=Button(win1,text="Allot Room",bg="lightcyan2",fg="black",bd=7,command=allot_ac,font=("Cooper Black",15))
        alt.grid(row="4",column="0")
        view_table=Button(win1,text="View Ac table",bg="lightcyan2",fg="black",bd=7,command=viewtable_ac,font=("Cooper Black",15))
        view_table.grid(row="4",column="1")
        win.mainloop()
    elif(val==2):
        win1.title("Allot Rooms")
        win1.geometry("600x300+700+300")
        win1["bg"]="sky blue"
        cur=dbconn.cursor()
        sql="select * from non_ac_room"
        cur.execute(sql)
        result=list(cur.fetchall())
        sql2="select room_no from customer where type='NON-AC' and status='CHECKED-IN'"
        cur.execute(sql2)
        result2=list(cur.fetchall())
        res=Label(win1,bg="lawn Green",text="Avalable NON-AC Rooms:  ",font=("arial black",15))
        resultLabel = Label(win1,bg="lawn green",text=result,font=("arial black",15))
        res.grid(row="1",column="0")
        resultLabel.grid(row="1",column="1")
        res2=Label(win1,bg="red2",text="Checked-In Rooms:  ",font=("arial black",15))
        resultLabel2 = Label(win1,bg="red2",text=result2,font=("arial black",15))
        res2.grid(row="2",column="0")
        resultLabel2.grid(row="2",column="1")
        allot=Label(win1,text="Select Room to Allot",bg="azure",fg="black",font=("Times New Roman",15))
        allot.grid(row="3",column="0")
        allottxt.grid(row="3",column="1")
        alt_nac=Button(win1,text="Allot Room",bg="lightcyan2",fg="black",bd=7,command=allot_nonac,font=("Cooper Black",15))
        alt_nac.grid(row="4",column="0")
        view_table=Button(win1,text="View Non-Ac table",bg="lightcyan2",fg="black",bd=7,command=viewtable_nonac,font=("Cooper Black",15))
        view_table.grid(row="4",column="1")
        win1.mainloop()
        win.mainloop()
def book(): # to book room
    try:
        if(int(agetxt.get())<18):
            showerror(title="Failure",message="Must be greater than 18 to book")
            return
        if(fnametxt.get()=="" or lnametxt.get()==""):
            showerror(title="Failure",message="Name field cannot be left blank")
            return
        elif(agetxt.get()==""):
            showerror(title="Failure",message="Age field cannot be left blank")
            return
        elif(mobiletxt.get()==""):
            showerror(title="Failure",message="Mobile field cannot be left blank")
            return
        elif(len(str(mobiletxt.get()))<10):
            showerror(title="Failure",message="Mobile number too small")
            return
        elif(len(str(mobiletxt.get()))>10):
            showerror(title="Failure",message="Mobile number too large")
            return
        date1=date(int(year.get()),int(month.get()),int(day.get()))
        date2=date(int(year2.get()),int(month2.get()),int(day2.get()))
        if(date1<date.today()):
            showerror(title="Error",message="Please select a valid check-in date!!!")
            return
        if(date2<date.today()):
            showerror(title="Error",message="Please select a valid check-out date!!!")
            return
        if(sel.get()==1):
            validate(sel.get())
        elif(sel.get()==2):
            validate(sel.get())
    except Exception as e:
        print(e)
def back():
    win.destroy()
    import admin_manage
    

win=Tk()
win1=Toplevel(win)
win["bg"]="sky blue"
win.geometry("675x400+100+100")
fname=Label(text="Enter first name",bg="azure",fg="black",font=("Times New Roman",15))
fname.grid(row="0",column="0")
fnametxt=Entry(win,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
fnametxt.grid(row="0",column="1")
lname=Label(text="Enter Last name",bg="azure",fg="black",font=("Times New Roman",15))
lname.grid(row="0",column="2")
lnametxt=Entry(win,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
lnametxt.grid(row="0",column="3")
age=Label(text="Age",bg="azure",fg="black",font=("Times New Roman",15))
age.grid(row="1",column="0")
agetxt=Entry(win,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
agetxt.grid(row="1",column="1")
mobileno=Label(text="Enter Mobile No:",bg="azure",fg="black",font=("Times New Roman",15))
mobileno.grid(row="2",column="0")
mobiletxt=Entry(win,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
mobiletxt.grid(row="2",column="1")
check_in=Label(text="Check In:",bg="azure",fg="black",font=("Times New Roman",15))
check_in.grid(row="3",column="0")
day=Spinbox(win,bg="snow2",bd=5, from_=1, to=31, width=10,font=15)
day.grid(row="3",column="1")
month=Spinbox(win,bg="snow2",bd=5, from_=1, to=12, width=10,font=15)
month.grid(row="3",column="2")
year=Spinbox(win,bg="snow2",bd=5, from_=2005, to=2050, width=10,font=15)
year.grid(row="3",column="3")
check_out=Label(text="Check Out:",bg="azure",fg="black",font=("Times New Roman",15))
check_out.grid(row="4",column="0")
day2=Spinbox(win,bg="snow2",bd=5, from_=1, to=31, width=10,font=15)
day2.grid(row="4",column="1")
v=str()
month2=Spinbox(win,bg="snow2",bd=5, from_=1, to=12, width=10,font=15)
month2.grid(row="4",column="2")
year2=Spinbox(win,bg="snow2",bd=5, from_=2005, to=2050, width=10,font=15)
year2.grid(row="4",column="3")
sel=IntVar()
rad1 = Radiobutton(win,text='AC', value=1,bg="snow2",font=15,variable=sel)
rad2 = Radiobutton(win,text='Non-AC', value=2,bg="snow2",font=15,variable=sel)
rad1.grid(row="5",column="0")
rad2.grid(row="5",column="1")
win1=Toplevel(win)
book=Button(win,text="Book",bg="lightcyan2",fg="black",bd=7,command=book,font=("Cooper Black",15))
book.grid(row="8",column="0")
back=Button(win,text="Back",bg="lightcyan2",fg="black",bd=7,command=back,font=("Cooper Black",15))
back.grid(row="8",column="1")
allottxt=Entry(win1,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
win.mainloop()

