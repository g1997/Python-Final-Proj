import os
import random
import random
import tkinter as tk
from tkinter import *
from datetime import * 
import tkinter.ttk as ttk
import tkinter.font as tkfont
from tkinter.messagebox import *
import mysql.connector as conn
import datetime
data=list()
data1=list()
fetch_data=list()
fetch_data2=list()
dbconn=conn.connect(host="localhost",
                    user="root",
                    passwd="",
                    database="hotelmgmtsys"
                    )
cur=dbconn.cursor()
def rets(): # to get data of all customers  
    cur=dbconn.cursor()
    sql="Select * from customer"
    cur.execute(sql)
    data=cur.fetchall()
    for i in data:
        tree.insert("", tk.END, values=i)
        
def clear():#to clear the table
    text.delete('1.0', END)
def search():# to search a customer 
     frame3.pack(side=RIGHT)
     searchlbl.grid(row="2",column="0")
     searchtxt.grid(row="2",column="1")
     search2.grid(row="3",column="0")
     hide.grid(row="3",column="1")
def search2s():# subset of search function
    cur=dbconn.cursor()
    sql="select * from customer where fname='{}'".format(searchtxt.get())
    cur.execute(sql)
    fetch_data=list(cur.fetchall())
    if(fetch_data):
        for i in fetch_data:
            tree.insert("", tk.END, values=i)
    else:
        showerror(title="Failure",message="Record not found")
def clears():
    for i in tree.get_children():
            tree.delete(i)
def close_field():
    frame3.pack_forget()
def close_field2():
    frame4.pack_forget()
#def close_field():
#     frame3.pack_forget()
#     frame3.unpack()
def chkin_cus():
    for i in tree.get_children():
            tree.delete(i)
    frame4.pack(side=RIGHT)
    cur=dbconn.cursor()
    sql="select * from customer where status='BOOKED'".format(searchtxt.get())
    cur.execute(sql)
    fetch_data=list(cur.fetchall())
    if(fetch_data):
        for i in fetch_data:
            tree.insert("", tk.END, values=i)
    c_chkin.grid(row="0",column="0")
    cus_chk_in.grid(row="0",column="1")
    chkin_mob_lbl.grid(row="2",column="0")
    chkin_mob.grid(row="2",column="1")
    chkin.grid(row="3",column="0")
    hide2.grid(row="3",column="1")
    
def del_final():# change customer status from BOOKED TO CHECKED-IN 
    cur=dbconn.cursor()
    now = datetime.datetime.now()
    print(now.strftime("%H:%M:%S"),cus_chk_in.get())
    '''
    sql="update customer set status='CHECKED-IN',check_in_time='{}' where fname='{}' and mob_no={}".format(now.strftime("%H:%M:%S"),cus_chk_in.get(),chkin_mob.get())
    cur.execute(sql)
    sql2="insert into customer_counts values('{}')".format(cus_chk_in.get())
    cur.execute(sql2)
    '''
    rate="select rate,type from customer where fname='{}' and mob_no={}".format(cus_chk_in.get(),chkin_mob.get())
    cur.execute(rate)
    rate=cur.fetchall()
    types=str(rate[0][1])
    rates=str(rate[0][0])
    if(types=='AC' and rates=='0'):
        sql3="update customer set rate=5000,status='CHECKED-IN' where fname='{}' and mob_no='{}'".format(cus_chk_in.get(),chkin_mob.get())
        cur.execute(sql3)
    elif(types=='NON_AC' and rates=='0'):
        sql3="update customer set rate=2500,status='CHECKED-IN' where fname='{}' and mob_no='{}'".format(cus_chk_in.get(),chkin_mob.get())
        cur.execute(sql3)
    try:
        dbconn.commit()
        showinfo('Success','Record Updated Successfully')
    except Exception as e:
        print(e)
def emp_data():# to open emplloyee manage program
    win.destroy()
    from subprocess import Popen
    Popen(["python", "emplloyee_manage.py"])

def book_room():#open book_room program
    win.destroy()
    from subprocess import Popen
    Popen(["python", "book_room.py"])

def order_cus():
    frame5.pack(side=RIGHT)
    orderlbl.grid(row='0',column='0')
    order_fname.grid(row='0',column='1')
    order_roomno_lbl.grid(row='1',column='0')
    order_roomno.grid(row='1',column='1')
    order_order_lbl.grid(row='2',column='0')
    order_order.grid(row='2',column='1')
    order_quantity_lbl.grid(row='3',column='0')
    order_quantity.grid(row='3',column='1')
    order_price_lbl.grid(row='4',column='0')
    order_price.grid(row='4',column='1')
    order_chkin.grid(row='5',column='0')
    order_hide.grid(row='5',column='1')
    cur=dbconn.cursor()
    sql="select * from customer where status='CHECKED-IN'"
    cur.execute(sql)
    fetch_data=cur.fetchall()
    if(fetch_data):
        for i in fetch_data:
            tree.insert("", tk.END, values=i)

def order_final(): # add order in order_customer table 
    cur=dbconn.cursor()
    sql="select * from customer where fname='{}' and room_no={}".format(order_fname.get(),order_roomno.get())
    print(order_fname.get(),order_roomno.get())
    cur.execute(sql)
    if(cur.fetchone()):
        sql2="insert into customer_order values('{}',{},'{}',{},{})".format(order_fname.get(),order_roomno.get(),order_order.get(),order_quantity.get(),order_price.get())
        cur.execute(sql2)
        dbconn.commit()
        if(cur.rowcount>0):
          showinfo('Success','Record Updated Successfully')
        else:
            showerror('Error','Failed to Update Record')
    else:
        showerror('Error','Customer Not Found')
    pass
def order_hide():# to hide order frame
    for i in tree.get_children():
            tree.delete(i)
    frame5.pack_forget()

def order_view(): # too view orders made by customers
    win1=Toplevel(win)
    win1["bg"]="sky blue"
    win.geometry("1000x875-100+20")
    frame=Frame(win1)
    frame.pack(side=TOP)
    tree=ttk.Treeview(frame)
    tree.pack(side=TOP)
    scrollbar_horizontal = ttk.Scrollbar(frame, orient='horizontal', command = tree.xview)    
    scrollbar_vertical = ttk.Scrollbar(frame, orient='vertical', command = tree.yview)   
    scrollbar_horizontal.pack(side='bottom', fill=X)    
    scrollbar_vertical.pack(side='right', fill=Y)
    tree.configure(xscrollcommand=scrollbar_horizontal.set, yscrollcommand=scrollbar_vertical.set)
    tree["columns"]=('fname','room_no','orders','quantity','price')
    tree.column("fname", width=90)
    tree.column("room_no", width=90 )
    tree.column("orders", width=90 )
    tree.column("quantity", width=90 )
    tree.column("price", width=90 )
    tree.heading("fname", text="FIRST NAME")
    tree.heading("room_no", text="ROOM NO")
    tree.heading("orders", text="ORDERS" )
    tree.heading("quantity", text="QUANTITY" )
    tree.heading("price", text="PRICE" )
    cur=dbconn.cursor()
    sql="Select * from customer_order"
    cur.execute(sql)
    data=cur.fetchall()
    for i in data:
        tree.insert("", tk.END, values=i)
    pass
def checkout(): #to checkout customer
    now=datetime.datetime.now()
    print(int(now.strftime('%d')),now.strftime('%m'),now.strftime('%Y'))
    sql="select * from customer where status='CHECKED-IN' and(chk_out_day={} and chk_out_month={} and chk_out_year={})".format(int(now.strftime('%d')),int(now.strftime('%m')),int(now.strftime('%Y')))
    cur.execute(sql)
    data=cur.fetchall()
    print(data)
    for i in data:
        tree.insert("", tk.END, values=i)
    pass
def bills():# to generate bills
    frame6.pack(side=RIGHT)
    data2=list()
    bill_fname_lbl.grid(row='0',column='0')
    bill_fname.grid(row='0',column='1')
    bill_room_lbl.grid(row='1',column='0')
    bill_room.grid(row='1',column='1')
    bill_room_btn.grid(row='2',column='0')
    bill_room_hide.grid(row='2',column='1')
    
def bill_gen_final():# generate final bill in txt format
    data2=list()
    data3=list()
    data4=list()
    price_list=list()
    f=open("C:\\Users\\Ganesh B Kamath\\Desktop\\{}_{}.txt".format(bill_fname.get(),bill_room.get()),'w+')
    fname="select fname from customer where fname='{}' and room_no={}".format(bill_fname.get(),bill_room.get())
    cur.execute(fname)
    fname=cur.fetchall()
    fname=str(fname[0][0])
    lname="select lname from customer where fname='{}' and room_no={}".format(bill_fname.get(),bill_room.get())
    cur.execute(lname)
    lname=cur.fetchall()
    lname=str(lname[0][0])
    room_no="select lname from customer where fname='{}' and room_no={}".format(bill_fname.get(),bill_room.get())
    cur.execute(room_no)
    room_no=cur.fetchall()
    room_no=str(room_no[0][0])
    order="select orders from customer_order where fname='{}' and room_no={}".format(bill_fname.get(),bill_room.get())
    cur.execute(order)
    orders=cur.fetchall()
    orders=list(orders)
    quantity="select quantity from customer_order where fname='{}' and room_no={}".format(bill_fname.get(),bill_room.get())  
    cur.execute(quantity)
    quantities=cur.fetchall()
    quantities=list(quantities)
    price="select price from customer_order where fname='{}' and room_no={}".format(bill_fname.get(),bill_room.get())
    cur.execute(price)
    prices=cur.fetchall()
    prices=list(prices)
    price_sum="select sum(price) from customer_order where fname='{}' and room_no={}".format(bill_fname.get(),bill_room.get())
    cur.execute(price_sum)
    price_sums=list(cur.fetchall())
    for i in price_sums:
        price_list.append(list(i))
    total_price=str(price_list[0][0])
    total_price=float(total_price)
    rate="select rate from customer where fname='{}' and room_no={}".format(bill_fname.get(),bill_room.get())
    cur.execute(rate)
    rates=cur.fetchall()
    rates=str(rates[0][0])
    rates=float(rates)
    final_bill=(rates+total_price)*1.8
    for i in orders:
        data2.append(list(i))
    for i in quantities:
        data3.append(list(i))
    for i in prices:
        data4.append(list(i))
    n=len(data2)
    f.write("Customer Name:{} {}".format(fname,lname))
    f.write("\n\n")
    f.write("orders\t\tquantity\t\t\tprice\n")
    for i in range(n):
        f.write(str(data2[i][0]))
        f.write("|");
        f.write("\t\t\t");
        f.write(str(data3[i][0]))
        f.write("|");
        f.write("\t\t\t")
        f.write(str(data4[i][0]))
        f.write("\n")
    f.write("\t\t\t\t\t\tTotal={}".format(total_price))
    f.write("\n\n\n")
    f.write("Room Rate={}\n".format(rates))
    f.write("Tax=18%\n")
    f.write("\n\nGrand_total={}\n".format(final_bill))
    showinfo('Success','Bill Generated')
    f.close()
    pass
def bill_gen_hide():
    frame6.pack_forget()

win=Tk()
win["bg"]="sky blue"
win.geometry("1100x675-100+20")
frame=Frame(win)
frame.pack(side=TOP)
tree=ttk.Treeview(frame)
tree.pack(side=TOP)
scrollbar_horizontal = ttk.Scrollbar(frame, orient='horizontal', command = tree.xview)    
scrollbar_vertical = ttk.Scrollbar(frame, orient='vertical', command = tree.yview)   
scrollbar_horizontal.pack(side='bottom', fill=X)    
scrollbar_vertical.pack(side='right', fill=Y)
tree.configure(xscrollcommand=scrollbar_horizontal.set, yscrollcommand=scrollbar_vertical.set)
tree["columns"]=('fname','lname','age','mobile','chk_in_day','month','year','chk_out_day','out_month','out_year','type','chk_in_time','room_no','rate','status')
tree.column("fname", width=90)
tree.column("lname", width=90)
tree.column("age", width=90 )
tree.column("mobile", width=90 )
tree.column("chk_in_day", width=90 )
tree.column("month", width=90 )
tree.column("year", width=90 )
tree.column("chk_out_day", width=90 )
tree.column("out_month", width=90 )
tree.column("out_year", width=90 )
tree.column("type", width=90 )
tree.column("chk_in_time", width=90 )
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
tree.heading("chk_in_time", text="CHECK_IN_TIME" )
tree.heading("room_no", text="Room Number" )
tree.heading("rate", text="Room Rate" )
tree.heading("status", text="Status" )
#t1=Entry(frame)
#t1.pack(side=TOP)
frame2=Frame(win,bd=5)
frame2.pack(side=BOTTOM)
frame3=Frame(win,bd=5)
frame3.pack(side=RIGHT)
frame4=Frame(win,bd=5)
frame4.pack(side=RIGHT)
frame5=Frame(win,bd=5)
frame5.pack(side=LEFT)
frame6=Frame(win,bd=5)
frame6.pack(side=RIGHT)
#frame 2 components
retrive=Button(frame2,text="All Data",bg="azure",fg="black",bd=7,command=rets,font=("Cooper Black",15))
retrive.grid(row="0",column="0")
retrive2=Button(frame2,text="Clear Data",bg="azure",fg="black",command=clear,bd=7,font=("Cooper Black",15))
retrive2.grid(row="0",column="1")
book_room=Button(frame2,text="Book Room",bg="azure",fg="black",bd=7,command=book_room,font=("Cooper Black",15))
book_room.grid(row="0",column="6")
search=Button(frame2,text="Search Customer:",bg="azure",fg="black",bd=7,command=search,font=("Cooper Black",15))
search.grid(row="0",column="1")
emp=Button(frame2,text="Employee Data",bg="azure",fg="black",bd=7,command=emp_data,font=("Cooper Black",15))
emp.grid(row="0",column="5")
clear=Button(frame2,text="Clear",bg="azure",fg="black",bd=7,command=clears,font=("Cooper Black",15))
clear.grid(row="0",column="2")
chkin_customer=Button(frame2,text="Check-In",bg="azure",fg="black",bd=7,command=chkin_cus,font=("Cooper Black",15))
chkin_customer.grid(row="0",column="3")
customer_order=Button(frame2,text="Order",bg="azure",fg="black",bd=7,command=order_cus,font=("Cooper Black",15))
customer_order.grid(row="0",column="4")
ord_view=Button(frame2,text="View Orders",bg="azure",fg="black",bd=7,command=order_view,font=("Cooper Black",15))
ord_view.grid(row="1",column="0")
check_out=Button(frame2,text="Check_out",bg="azure",fg="black",bd=7,command=checkout,font=("Cooper Black",15))
check_out.grid(row="1",column="1")
bill=Button(frame2,text="Bill",bg="azure",fg="black",bd=7,command=bills,font=("Cooper Black",15))
bill.grid(row="1",column="2")
#frame 3 cmmponents
searchtxt=Entry(frame3,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
searchlbl=Label(frame3,bg="azure",text ="Enter Customer name:",font=("arial black",15))
search2=Button(frame3,text="Search.....",bg="azure",fg="black",bd=7,command=search2s,font=("Cooper Black",15))
#close=Button(frame2,text="Close Below tabs",bg="azure",fg="black",bd=7,command=close_field,font=("Cooper Black",15))
hide=Button(frame3,text="Hide",bg="azure",fg="black",bd=7,command=close_field,font=("Cooper Black",15))
# frame 4 cmmponents
deltxt=Entry(frame4,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
cus_chk_in=Entry(frame4,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
c_chkin=Label(frame4,bg="azure",text ="Enter Customer name:",font=("arial black",15))
chkin_mob=Entry(frame4,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
chkin_mob_lbl=Label(frame4,bg="azure",text ="Enter Customer mobile:",font=("arial black",15))
dellbl=Label(frame4,bg="azure",text ="Enter Customer name:",font=("arial black",15))
delph=Label(frame4,bg="azure",text ="Enter Customer Phone Number:",font=("arial black",15))
delphtxt=Entry(frame4,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
chkin=Button(frame4,text="Check-Ins",bg="azure",fg="black",bd=7,command=del_final,font=("Cooper Black",15))
hide2=Button(frame4,text="Hide",bg="azure",fg="black",bd=7,command=close_field2,font=("Cooper Black",15))
# frame 5 cmmponents
order_fname=Entry(frame5,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
orderlbl=Label(frame5,bg="azure",text ="Enter Customer name:",font=("arial black",15))
order_roomno=Entry(frame5,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
order_roomno_lbl=Label(frame5,bg="azure",text ="Enter Customer Room No:",font=("arial black",15))
order_order=Entry(frame5,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
order_order_lbl=Label(frame5,bg="azure",text ="Enter order:",font=("arial black",15))
order_quantity=Spinbox(frame5,bg="snow2",bd=5, from_=1, to=20, width=10,font=10)
order_quantity_lbl=Label(frame5,bg="azure",text ="Enter Quantity:",font=("arial black",15))
order_price=Entry(frame5,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
order_price_lbl=Label(frame5,bg="azure",text ="Enter price:",font=("arial black",15))
order_chkin=Button(frame5,text="Order",bg="azure",fg="black",bd=7,command=order_final,font=("Cooper Black",15))
order_hide=Button(frame5,text="Hide",bg="azure",fg="black",bd=7,command=order_hide,font=("Cooper Black",15))
# frame 6 cmmponents
bill_fname_lbl=Label(frame6,bg="azure",text ="Enter Customer Name:",font=("arial black",15))
bill_fname=Entry(frame6,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
bill_room_lbl=Label(frame6,bg="azure",text ="Enter Customer Room_No:",font=("arial black",15))
bill_room=Entry(frame6,bg="snow2",fg="black",font=("Times New Roman",15),bd=5)
bill_room_btn=Button(frame6,text="Generate",bg="azure",fg="black",bd=7,command=bill_gen_final,font=("Cooper Black",15))
bill_room_hide=Button(frame6,text="Hide",bg="azure",fg="black",bd=7,command=bill_gen_hide,font=("Cooper Black",15))
#close.grid(row="0",column="3")
win.mainloop()
