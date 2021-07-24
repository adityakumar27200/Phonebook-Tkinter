from Tkinter import *
from tkMessageBox import *
from string import split
import sqlite3
con=sqlite3.Connection('hrdb')
cur=con.cursor()

cur.execute('create table if not exists contactid_1(Cid INTEGER primary key AUTOINCREMENT ,Fname varchar(20) default "NULL",Mname varchar(20) default "NULL",Lname varchar(20) default "NULL",Company varchar(20) default "NULL",Address varchar(20) default "NULL",City varchar(20) default "NULL",Pincode varchar(20) default "NULL",Website varchar(20) default "NULL",Bdate varchar(15))')
cur.execute('create table if not exists phone_1(Cid integer,Ctype varchar(15),Pno varchar(15),primary key(Cid,Pno),constraint fk_1 foreign key (Cid) references contactid_1(Cid))') 
cur.execute('create table if not exists Email_1(Cid integer,Emailtype varchar(15),Emailid varchar(20),primary key(Cid,Emailid),constraint fk_1 foreign key (Cid) references contactid_1(Cid))')
con.commit()


#INTRODUCTION WINDOW

root1=Tk()
def destroy(self):
    root1.destroy()
root1.title("PHONEBOOK")
root1.geometry('800x500')
root1.configure(bg='salmon')
Label(root1,text='JAYPEE UNIVERSITY OF ENGINEERING AND TECHNOLOGY',font='times 20 bold',fg='blue',bg='salmon').pack()
Label(root1,text='PHONEBOOK PROJECT',font='times 20 bold',fg='blue',bg='salmon').pack()
Label(root1,text='DEVELOPED BY',font='times 20 bold',fg='blue',bg='salmon').pack()
Label(root1,text='ADITYA KUMAR',font='times 20 bold',fg='blue',bg='salmon').pack()
Label(root1,text='181B015',font='times 20 bold',fg='blue',bg='salmon').pack()

root1.bind('<Motion>',destroy)
root1.mainloop()

#SAVE

def save():
    if v1.get()==1:
        e12="office"
    elif v1.get()==2:
        e12="Home"
    else :
        e12="Mobile"
    if v2.get()==1:
        e13="Office"
    else :
        e13="Personal"

    try:
        v3=int(e10.get())
    except:
        Label(root,text='*required in number*',font='Arial 8',fg='red',bg='salmon').grid(row=12,column=2)
        return


    contactid=(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get(),e9.get())
    
    phone=(e12,e10.get())
    email=(e13,e11.get())
    print (contactid,phone,email)
    cur.execute("select MAX(Cid) from contactid_1")
    X=cur.fetchall()[0][0]+1
    cur.execute("insert into contactid_1(Fname,Mname,Lname,Company ,Address,City,Pincode,Website ,Bdate) values(?,?,?,?,?,?,?,?,?)",contactid)
    cur.execute("insert into phone_1 values(?,?,?)",(X,e12,e10.get()))
    cur.execute("insert into email_1 values(?,?,?)",(X,e13,e11.get()))
    con.commit()
    showinfo('info','contact successfully saved')
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e5.delete(0,END)
    e6.delete(0,END)
    e7.delete(0,END)
    e8.delete(0,END)
    e9.delete(0,END)
    e10.delete(0,END)
    e11.delete(0,END)

#SEARCH

def search():
    
    def showdetail(name):
        root3=Tk()
        root3.geometry('400x500')
        root3.configure(bg='salmon')

        def delete():
            cur.execute('delete from contactid_1 where Cid=?',(x[0][0],))
            con.commit()
            cur.execute('delete from phone_1 where Cid=?',(x[0][0],))
            con.commit()
            cur.execute('delete from Email_1 where Cid=?',(x[0][0],))
            con.commit()
            showinfo('delete','contact delete successfully')
            root3.destroy()
            
        def close():
            E=askokcancel('Alert','press ok for exit')
            if E==True:
                root3.destroy()

        y=['','','']
        x=split(name)
        print (name)
        for i in range(len(x)):
            y[i]=x[i]
        print (tuple(y))
        
        cur.execute('select * from contactid_1 where Fname=? or Mname=? or Lname=?',tuple(y))
        x=cur.fetchall()
        cur.execute('select * from phone_1 where Cid=?',(x[0][0],))
        y=cur.fetchall()
        cur.execute('select * from Email_1 where Cid=?',(x[0][0],))
        z=cur.fetchall()
        print (y)
        print (z)
        Label(root3,text='First Name: ',font='times 10 bold',bg='salmon').grid(row=2,column=0)
        Label(root3,text='Middle Name: ',font='times 10 bold',bg='salmon').grid(row=3,column=0)
        Label(root3,text='Last Name: ',font='times 10 bold',bg='salmon').grid(row=4,column=0)
        Label(root3,text='Company Name: ',font='times 10 bold',bg='salmon').grid(row=5,column=0)
        Label(root3,text='Address: ',font='times 10 bold',bg='salmon').grid(row=6,column=0)
        Label(root3,text='City: ',font='times 10 bold',bg='salmon').grid(row=7,column=0)
        Label(root3,text='Pin Code: ',font='times 10 bold',bg='salmon').grid(row=8,column=0)
        Label(root3,text='Website URL: ',font='times 10 bold',bg='salmon').grid(row=9,column=0)
        Label(root3,text='Date of Birth: ',font='times 10 bold',bg='salmon').grid(row=10,column=0)
        Label(root3,text='Select Phone Type ',font='times 10 bold',bg='salmon').grid(row=11,column=0)
        Label(root3,text='Phone Number: ',font='times 10 bold',bg='salmon').grid(row=12,column=0)
        Label(root3,text='Select Email Type ',font='times 10 bold',bg='salmon').grid(row=13,column=0)
        Label(root3,text='Emailid: ',font='times 10 bold',bg='salmon').grid(row=14,column=0)

        Label(root3,text=x[0][1],bg='salmon').grid(row=2,column=2)
        Label(root3,text=x[0][2],bg='salmon').grid(row=3,column=2)
        Label(root3,text=x[0][3],bg='salmon').grid(row=4,column=2)
        Label(root3,text=x[0][4],bg='salmon').grid(row=5,column=2)
        Label(root3,text=x[0][5],bg='salmon').grid(row=6,column=2)
        Label(root3,text=x[0][6],bg='salmon').grid(row=7,column=2)
        Label(root3,text=x[0][7],bg='salmon').grid(row=8,column=2)
        Label(root3,text=x[0][8],bg='salmon').grid(row=9,column=2)
        Label(root3,text=x[0][9],bg='salmon').grid(row=10,column=2)
        try:
            Label(root3,text=y[0][1],bg='salmon').grid(row=11,column=2)
        except:
            Label(root3,text='',bg='salmon').grid(row=11,column=2)
        try:
            Label(root3,text=y[0][2],bg='salmon').grid(row=12,column=2)
        except:
            Label(root3,text='',bg='salmon').grid(row=12,column=2)
        try:
            Label(root3,text=z[0][1],bg='salmon').grid(row=13,column=2)
        except:
            Label(root3,text='',bg='salmon').grid(row=13,column=2)
        try:
            Label(root3,text=z[0][2],bg='salmon').grid(row=14,column=2)
        except:
            Label(root3,text='',bg='salmon').grid(row=14,column=2)
        Button(root3,text='Delete',font='times 10 bold',command=delete,bg='salmon').grid(row=15,column=0)
        Button(root3,text='Exit',font='times 10 bold',command=close,bg='salmon').grid(row=15,column=2)

                                                                                     

        root3.mainloop()

        
    def detail():
        svalue = lb1.get(lb1.curselection())
        print (svalue)
        root2.destroy()
        showdetail(svalue)
        
    def search1(e=1):
        
        lb1.delete(0,END)
        a=str(e15.get())
        print (a)
        cur.execute('select Fname,Mname,Lname from contactid_1 where Fname like"%'+str(a)+'%"or Mname like "%'+str(a)+'%"or Lname like "%'+str(a)+'%" order by Fname')
        data=cur.fetchall()
        print (data)
        for i in range(len(data)):
            x=data[i][0]+' '+data[i][1]+' '+data[i][2]
            lb1.insert(i+1,x)
        root2.bind('<Button-1>',detail)

        
    root2=Tk()
    root2.geometry('500x600')
    root2.configure(bg='salmon')
    Label(root2,text='SEARCH CONTACT',font='times 20 bold',bg='salmon').grid(row=0,column=1)
    Label(root2,text='Enter Name: ',font='times 10 bold',bg='salmon').grid(row=3,column=0)
    e15=Entry(root2)
    e15.grid(row=3,column=1)
    lb1=Listbox(root2,height=15,width=35,font='Arial 20 bold',fg='sky blue')
    lb1.grid(row=4,columnspan=3)
    root2.bind('<KeyPress>',search1)
    root2.mainloop()
    
#CLOSE
    
def close():
    x=askyesno('closing','Are you sure to close phonebook')
    if x==True:
        root.destroy()
##EDIT
##        
##def edit():
##    showinfo('info','editing is not allowed')
##    root.after(200,close)
    
root=Tk()
root.geometry('500x600')
root.configure(bg='salmon')
img=PhotoImage(file='phone.gif')


#LABEL

Label(root,image=img).grid(row=0,column=1)
Label(root,text='Phone Book',font='times 15 bold underline',fg='green',bg='salmon').grid(row=1,column=1)
Label(root,text='First Name: ',font='times 10 bold',bg='salmon').grid(row=2,column=0)
Label(root,text='Middle Name: ',font='times 10 bold',bg='salmon').grid(row=3,column=0)
Label(root,text='Last Name: ',font='times 10 bold',bg='salmon').grid(row=4,column=0)
Label(root,text='Company Name: ',font='times 10 bold',bg='salmon').grid(row=5,column=0)
Label(root,text='Address: ',font='times 10 bold',bg='salmon').grid(row=6,column=0)
Label(root,text='City: ',font='times 10 bold',bg='salmon').grid(row=7,column=0)
Label(root,text='Pin Code: ',font='times 10 bold',bg='salmon').grid(row=8,column=0)
Label(root,text='Website URL: ',font='times 10 bold',bg='salmon').grid(row=9,column=0)
Label(root,text='Date of Birth: ',font='times 10 bold',bg='salmon').grid(row=10,column=0)
Label(root,text='DD-MM-YYYY',font='times 8 bold',fg='green',bg='salmon').grid(row=10,column=2)
Label(root,text='Select Phone Type ',font='times 10 bold',bg='sky blue').grid(row=11,column=0)
Label(root,text='Phone Number: ',font='times 10 bold',bg='salmon').grid(row=12,column=0)
Label(root,text='Select Email Type ',font='times 10 bold',bg='sky blue').grid(row=13,column=0)
Label(root,text='Emailid: ',font='times 10 bold',bg='salmon').grid(row=14,column=0)

#ENTRY

e1=Entry(root)
e1.grid(row=2,column=1)
e2=Entry(root)
e2.grid(row=3,column=1)
e3=Entry(root)
e3.grid(row=4,column=1)
e4=Entry(root)
e4.grid(row=5,column=1)
e5=Entry(root)
e5.grid(row=6,column=1)
e6=Entry(root)
e6.grid(row=7,column=1)
e7=Entry(root)
e7.grid(row=8,column=1)
e8=Entry(root)
e8.grid(row=9,column=1)
e9=Entry(root)
e9.grid(row=10,column=1)
e10=Entry(root)
e10.grid(row=12,column=1)
e11=Entry(root)
e11.grid(row=14,column=1)


#BUTTON

v1=IntVar()
v2=IntVar()
Radiobutton(root,text='office',variable=v1,value=1,bg='salmon').grid(row=11,column=1)
Radiobutton(root,text='Home',variable=v1,value=2,bg='salmon').grid(row=11,column=2)
Radiobutton(root,text='Mobile',variable=v1,value=3,bg='salmon').grid(row=11,column=3)

Radiobutton(root,text='office',variable=v2,value=1,bg='salmon').grid(row=13,column=1)
Radiobutton(root,text='personal',variable=v2,value=2,bg='salmon').grid(row=13,column=2)

Button(root,text='Save',font='times 10 bold',command=save,bg='salmon').grid(row=15,column=0)
Button(root,text='Search',font='times 10 bold',command=search,bg='salmon').grid(row=15,column=1)
Button(root,text='Close',font='times 10 bold',command=close,bg='salmon').grid(row=15,column=2)
#Button(root,text='Edit',font='times 10 bold',command=edit,bg='salmon').grid(row=15,column=3)


root.mainloop()



