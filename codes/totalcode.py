from tkinter import *
from PIL import Image,ImageTk
import sqlite3
from sqlite3 import Error
from tkinter import messagebox
import matplotlib.pyplot as plt
conn = sqlite3.connect("main.db")#main database conn.
cursor=conn.cursor()
class Homepage:
    def sign():
        def proceed1():
            global email
            email=em.get()
            passwo=pas.get()
            check=[(email,passwo)]
            pre=conn.cursor()
            pre.execute('select email,password from accdetails;')
            row=pre.fetchall()
            flag=0
            for i in range(len(row)):
                if row[i]==check[0]:
                    flag=1
            if flag==0:
                return messagebox.showerror('Error','Email/Password is Incorrect')
            else:
                accwindow()
                sign.destroy()
        def account():#newaccount
            sign.destroy()
            def proceed():
                name=n.get()
                email=e.get()
                passw=p.get()
                if name=='':
                    return messagebox.showerror('Error','Enter Name')
                elif email=='':
                    return messagebox.showerror('Error','Enter email')
                elif passw=='':
                    return messagebox.showerror('Error','Enter  Password')
                else:
                    nc=conn.cursor()
                    sqlite_insert_with_param = """INSERT INTO accdetails
                              (email,password,Name) 
                              VALUES (?, ?, ?);"""
                    data_tuple = (email,passw,name)
                    nc.execute(sqlite_insert_with_param, data_tuple)
                    conn.commit()
                    messagebox.showinfo('Result','Registered Successfully')
            n=StringVar()
            e=StringVar()
            p=StringVar()
            new=Toplevel()
            new.title('Create Account')
            new.geometry('960x720')
            Label(new,text='Enter Details',font='Helvetica 12 bold').grid(row=1,column=2)
            Label(new,text='Enter Full Name').grid(row=2,column=1)
            Entry(new,width=25,textvariable=n).grid(row=2,column=2)#name
            Label(new,text='Enter Email').grid(row=3,column=1)
            Entry(new,width=25,textvariable=e).grid(row=3,column=2)#email
            Label(new,text='Enter New Password').grid(row=4,column=1)
            Entry(new,width=25,textvariable=p,show='*').grid(row=4,column=2)#password
            Button(new,text='Proceed',command=proceed).grid(row=5,column=3)

        em=StringVar()
        pas=StringVar()
        sign=Toplevel()
        sign.title('SignIn/CreateAccount-IAS')
        sign.geometry('960x720')
        Label(sign,text='Sign In',font='Verdana 12 bold').grid(row=1,column=2)
        Button(sign,text='CreateAccount',command=account,bg='yellow').grid(row=1,column=3)
        Label(sign,text='Enter Email Address:').grid(row=2,column=1)
        Entry(sign,width=25,textvariable=em).grid(row=2,column=2)#email
        Label(sign,text='Enter Passsword').grid(row=3,column=1)
        Entry(sign,width=25,textvariable=pas,show='*').grid(row=3,column=2)#password
        Button(sign,text='Proceed',command=proceed1,bg='yellow').grid(row=4,column=3)
    
class SubjectProjection:
        def subpro():#subject projection
            sub=Toplevel()
            sub.geometry('960x720')
            sub.title('Subject Projection')
            first=IntVar()
            second=IntVar()
            third=IntVar()
            fourth=IntVar()
            fifth=IntVar()
            sixth=IntVar()
            subject=StringVar()
            ch=IntVar()
            def check():
                percentage=['90%-100%','75%-90%','60%-75%','45%-60%','35%-40%','below 35%']
                subname=subject.get()
                aa=first.get()
                bb=second.get()
                cc=third.get()
                dd=fourth.get()
                ee=fifth.get()
                ff=sixth.get()
                choice=ch.get()
                numbers=[aa,bb,cc,dd,ee,ff]
                col=['green','blue','violet','yellow','black','red']
                plt.title(subname)
                if choice==1:#bargraph
                    plt.bar(percentage,numbers)
                elif choice==2:#piechart
                    plt.pie(numbers,labels=percentage,colors=col,shadow=True,startangle=140)
                else:
                    return messagebox.showerror('Error','Enter Type of Graph')
                plt.show()
               
            Label(sub,text='Enter details').grid(row=1,column=2)
            Label(sub,text='Enter Graph Title').grid(row=2,column=1)
            Entry(sub,width=20,textvariable=subject).grid(row=2,column=2)
            Label(sub,text='Percentage').grid(row=3,column=2)
            Label(sub,text='no. of students').grid(row=3,column=3)
            Label(sub,text='90%-100%').grid(row=4,column=2)
            Label(sub,text='75%-90%').grid(row=5,column=2)
            Label(sub,text='60%-75%').grid(row=6,column=2)
            Label(sub,text='below 35%').grid(row=9,column=2)
            Label(sub,text='45%-60%').grid(row=7,column=2)
            Label(sub,text='35%-40%').grid(row=8,column=2)
            Entry(sub,width=2,textvariable=first).grid(row=4,column=3)
            Entry(sub,width=2,textvariable=second).grid(row=5,column=3)
            Entry(sub,width=2,textvariable=third).grid(row=6,column=3)
            Entry(sub,width=2,textvariable=fourth).grid(row=7,column=3)
            Entry(sub,width=2,textvariable=fifth).grid(row=8,column=3)
            Entry(sub,width=2,textvariable=sixth).grid(row=9,column=3)
            Label(sub,text='Type of Graph').grid(row=10,column=2)
            Radiobutton(sub,text='BarGraph',variable=ch,value=1).grid(row=11,column=2)
            Radiobutton(sub,text='PieChart',variable=ch,value=2).grid(row=11,column=3)
            Button(sub,text='Plot',command=check).grid(row=12,column=4)
        
class Calculator:
        def calculator():
            def check():
                rec=main.get()
                tt=total.get()
                if rec<0:
                    return messagebox.showerror('Error','Invalid')
                elif rec==0:
                    return messagebox.showerror('Error','Invalid')
                elif tt<0:
                    return messagebox.showerror('Error','Invalid')
                elif tt==0:
                    return messagebox.showerror('Error','Invalid')
                else:
                    result=(rec/tt)*100
                    last=round(result)
                    messagebox.showinfo('Result',str(last)+'%')
            calc=Toplevel()
            main=IntVar()
            total=IntVar()
            calc.geometry('960x720')
            calc.title('Percentage calculator')
        
            Label(calc,text='enter mark',font='Helvetica 12 bold').grid(row=1,column=4)
            Label(calc,text='marks').grid(row=2,column=2)
            Entry(calc,width=3,textvariable=main).grid(row=3,column=2)
            Label(calc,text='/').grid(row=2,column=3)
            Label(calc,text='Total').grid(row=2,column=4)
            Entry(calc,width=3,textvariable=total).grid(row=3,column=4)
            Button(calc,text='Calculate',command=check).grid(row=4,column=5)
          
home=Tk()
home['bg'] = 'yellow'
home.geometry('1080x720')
home.title('Instructor Aid System')
img=Image.open('IAS3.jpg')
img = ImageTk.PhotoImage(img, master=home)
Label(home,image=img).pack()
Label(home,text='---HOME PAGE---',font='Verdana 15 bold',bg='#673',fg='White').place(relx=.5,anchor= N)
Button(home,text='SignIn/Create Account',font='Verdana 12 bold',command=sign,bg='#567',fg='White').place(relx=.5, rely=.4,anchor= CENTER)
Button(home,text='Subject Projection',font='Verdana 12 bold',command=SubjectProjection.subpro,bg='#567',fg='White').place(relx=.5, rely=.5,anchor= CENTER)
Button(home,text='Percentage calculator',font='Verdana 12 bold',command=Calculator.calculator,bg='#567',fg='White').place(relx=.5, rely=.6,anchor= CENTER)
home.mainloop()