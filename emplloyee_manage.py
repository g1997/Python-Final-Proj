import os
import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import tkinter.font as tkfont
from tkinter.messagebox import *
import mysql.connector as conn
dbconn=conn.connect(host="localhost",
                    user="root",
                    passwd="",
                    database="hotelmgmtsys"
                    )
def rete():
    cur=dbconn.cursor()
    sql="select * from employee"
    cur.execute(sql)
    data=cur.fetchall()
    for i in data:
        tree.insert("",tk.END,values=i)
def hide_e():
    frame2.pack_forget()
    frame.pack(side=TOP)


def add_e():
    frame.pack_forget()
    frame2.pack(side=BOTTOM)
    eid=Label(frame2,text="Enter Employee ID:",bg="azure",fg="black",font=("Times New Roman",15))
    eid.pack(side=TOP)
    eidtxt.pack(side=TOP)
    fname=Label(frame2,text="Enter First Name:",bg="azure",fg="black",font=("Times New Roman",15))
    fname.pack(side=TOP)
    fnametxt.pack(side=TOP)
    lname=Label(frame2,text="Enter Last Name:",bg="azure",fg="black",font=("Times New Roman",15))
    lname.pack(side=TOP)
    lnametxt.pack(side=TOP)
    DOB=Label(frame2,text="Enter DOB:",bg="azure",fg="black",font=("Times New Roman",15))
    DOB.pack(side=TOP)
    day.pack(side=TOP)
    month.pack(side=TOP)
    year.pack(side=TOP)
    des=Label(frame2,text="Enter Designation:",bg="azure",fg="black",font=("Times New Roman",15))
    des.pack(side=TOP)
    designation.pack(side=TOP)
    SALARY=Label(frame2,text="Enter Salary:",bg="azure",fg="black",font=("Times New Roman",15))
    SALARY.pack(side=TOP)
    salary.pack(side=TOP)
    add_emp_final.pack(side=TOP)
    hide.pack(side=TOP)
def add_emp_f():
    #print(day.get(),month.get(),year.get())
    cur=dbconn.cursor()
    sql="insert into employee values('{}','{}','{}','{}''/''{}''/''{}','{}',{})".format(eidtxt.get(),fnametxt.get(),lnametxt.get(),int(day.get()),int(month.get()),int(year.get()),designation.get(),salary.get())
    cur.execute(sql)
    dbconn.commit()
    if cur.rowcount>0:
        showinfo(title="Success",message="Record added Successfully")
    else:
        showerror(title="Failure",message="Failed to add Record")
def clear():
    for i in tree.get_children():
        tree.delete(i)
def del_e():
    frame2.pack_forget()
    frame3.pack(side=RIGHT)
    dellbl.pack(side=TOP)
    del_emp.pack(side=TOP)
    del_emp_final.pack(side=TOP)
    hide_del.pack(side=TOP)
def hide_del():
    frame3.pack_forget()
def del_e_final():
    a=askyesno("Conformation","Are you sure yu want to delete the data?")
    if a==True:
        cur=dbconn.cursor()
        sql="delete from employee where Emp_ID='{}'".format(del_emp.get())
        cur.execute(sql)
        dbconn.commit()
        if cur.rowcount>0:
            showinfo("Success","Record Deleted successfully")
        else:
            showerror("Failure","Failed to delete data")
    else:
        return
def update_e():
    frame2.pack_forget()
    frame4.pack(side=LEFT)
    fname.pack(side=TOP)
    lname.pack(side=LEFT)
    desg.pack(side=RIGHT)
    sal.pack(side=RIGHT)
    upd_e.pack(side=BOTTOM)
    hide3.pack(side=BOTTOM)
def update_2():
    frame5.pack(side=RIGHT)
    if(var1.get()==True):
        upd_fname.pack(side=TOP)
        upd_fname_txt.pack(side=TOP)
    if(var2.get()==True):
        upd_lname.pack(side=TOP)
        upd_lname_txt.pack(side=TOP)
    if(var3.get()==True):
        upd_des.pack(side=TOP)
        upd_des_txt.pack(side=TOP)
    if(var4.get()==True):
        upd_sal.pack(side=TOP)
        upd_sal_txt.pack(side=TOP)
    if(var1.get()==False):
        upd_fname.pack_forget()
        upd_fname_txt.pack_forget()
    if(var2.get()==False):
        upd_lname.pack_forget()
        upd_lname_txt.pack_forget()
    if(var3.get()==False):
        upd_des.pack_forget()
        upd_des_txt.pack_forget()
    if(var4.get()==False):
        upd_sal.pack_forget()
        upd_sal_txt.pack_forget()
    eid2.pack(side=TOP)
    eid2_txt.pack(side=TOP)
    updf.pack(side=TOP)
    hide4.pack(side=TOP)
def update_final():
    cur=dbconn.cursor()
    if(upd_fname_txt.get()):
        sql="update employee set E_fname='{}' where Emp_ID='{}'".format(upd_fname_txt.get(),eid2_txt.get())
        cur.execute(sql)
    if(upd_lname_txt.get()):
        sql="update employee set E_lname='{}' where Emp_ID='{}'".format(upd_lname_txt.get(),eid2_txt.get())
        cur.execute(sql)
    if(upd_des_txt.get()):
        sql="update employee set Designation='{}' where Emp_ID='{}'".format(upd_des_txt.get(),eid2_txt.get())
        cur.execute(sql)
    if(upd_sal_txt.get()):
        sql="update employee set Salary={} where Emp_ID='{}'".format(upd_sal_txt.get(),eid2_txt.get())
        cur.execute(sql)
    dbconn.commit()
    if(cur.rowcount>0):
        showinfo(title="Success",message="Record updated Successfully")
    else:
        showerror(title="Failed",message="Failed to update record")
def hide_frame4():
     frame4.pack_forget()
def hide_frame5():
    frame5.pack_forget()
def back():
    win.destroy()
    import admin_manage
win=Tk()
win["bg"]="sky blue"
win.geometry("900x610+100-120")
frame=Frame(win)
frame.pack(side=TOP)
frame2=Frame(win,bg="lemon chiffon")
frame2.pack(side=BOTTOM)
frame3=Frame(win)
frame3.pack(side=RIGHT)
frame4=Frame(win)
frame4.pack(side=LEFT)
frame5=Frame(win)
frame5.pack(side=RIGHT)
tree=ttk.Treeview(frame)
tree.pack(side=TOP)
win_scrollbar_horizontal = ttk.Scrollbar(frame2, orient='horizontal', command = tree.xview)    
win_scrollbar_vertical = ttk.Scrollbar(frame2, orient='vertical', command = tree.yview)   
win_scrollbar_horizontal.pack(side='bottom', fill=X)    
win_scrollbar_vertical.pack(side='right', fill=Y)
tree.configure(xscrollcommand=win_scrollbar_horizontal.set, yscrollcommand=win_scrollbar_vertical.set)
scrollbar_horizontal = ttk.Scrollbar(frame, orient='horizontal', command = tree.xview)    
scrollbar_vertical = ttk.Scrollbar(frame, orient='vertical', command = tree.yview)   
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
retrive=Button(frame,text="Retrive Data",bg="lightcyan2",fg="black",bd=7,command=rete,font=("Cooper Black",15))
retrive.pack(side=LEFT)
add_emp=Button(frame,text="Add Employee",bg="lightcyan2",fg="black",bd=7,command=add_e,font=("Cooper Black",15))
add_emp.pack(side=RIGHT)
eidtxt=Entry(frame2,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
fnametxt=Entry(frame2,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
lnametxt=Entry(frame2,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
day=Spinbox(frame2,bg="snow2",bd=5, from_=1, to=31, width=10,font=15)
month=Spinbox(frame2,bg="snow2",bd=5, from_=1, to=12, width=10,font=15)
year=Spinbox(frame2,bg="snow2",bd=5, from_=1900, to=2030, width=10,font=15)
designation=Entry(frame2,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
salary=Entry(frame2,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
#eid=Label(text="Enter Employee ID:",bg="azure",fg="black",font=("Times New Roman",15))
add_emp_final=Button(frame2,text="Add",bg="lightcyan2",fg="black",bd=7,command=add_emp_f,font=("Cooper Black",15))
hide=Button(frame2,text="Hide",bg="lightcyan2",fg="black",bd=7,command=hide_e,font=("Cooper Black",15))
clear=Button(frame,text="Clear",bg="lightcyan2",fg="black",bd=7,command=clear,font=("Cooper Black",15))
clear.pack(side=LEFT)
delete=Button(frame,text="Delete Employee",bg="lightcyan2",fg="black",bd=7,command=del_e,font=("Cooper Black",15))
delete.pack(side=RIGHT)
update=Button(frame,text="Update Employee",bg="lightcyan2",fg="black",bd=7,command=update_e,font=("Cooper Black",15))
update.pack(side=LEFT)
back=Button(frame,text="Back",bg="lightcyan2",fg="black",command=back,bd=7,font=("Cooper Black",15))
back.pack(side=RIGHT)
del_emp=Entry(frame3,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
del_emp_final=Button(frame3,text="Delete",bg="lightcyan2",fg="black",bd=7,command=del_e_final,font=("Cooper Black",15))
dellbl=Label(frame3,bg="azure",text ="Enter Employee ID:",font=("arial black",15))
hide_del=Button(frame3,text="Hide",bg="lightcyan2",fg="black",bd=7,command=hide_del,font=("Cooper Black",15))
var1=IntVar()
fname=Checkbutton(frame4,text="First name",variable=var1)
var2=IntVar()
lname=Checkbutton(frame4,text="Last name",variable=var2)
var3=IntVar()
desg=Checkbutton(frame4,text="Designation",variable=var3)
var4=IntVar()
sal=Checkbutton(frame4,text="Salary",variable=var4)
upd_e=Button(frame4,text="Update",bg="lightcyan2",fg="black",bd=7,command=update_2,font=("Cooper Black",15))
upd_fname=Label(frame5,bg="azure",text ="Enter new First name:",font=("arial black",15))
upd_fname_txt=Entry(frame5,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
upd_lname=Label(frame5,bg="azure",text ="Enter new Last name:",font=("arial black",15))
upd_lname_txt=Entry(frame5,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
upd_des=Label(frame5,bg="azure",text ="Enter new Designation:",font=("arial black",15))
upd_des_txt=Entry(frame5,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
upd_sal=Label(frame5,bg="azure",text ="Enter new Salary:",font=("arial black",15))
upd_sal_txt=Entry(frame5,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
eid2=Label(frame5,bg="azure",text ="Enter Employee ID:",font=("arial black",15))
eid2_txt=Entry(frame5,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
updf=Button(frame5,text="Update",bg="lightcyan2",fg="black",bd=7,command=update_final,font=("Cooper Black",15))
hide3=Button(frame4,text="Hide",bg="lightcyan2",fg="black",bd=7,command=hide_frame4,font=("Cooper Black",15))
hide4=Button(frame5,text="Hide",bg="lightcyan2",fg="black",bd=7,command=hide_frame5,font=("Cooper Black",15))
win.mainloop()
