import tkinter 
from tkinter import *
from tkinter import ttk 
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
                Dashboard.accwindow()
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
            new['bg'] = '#49A'
            Label(new,text='Enter Details',font='Verdana 12 bold',bg='#49A').grid(row=1,column=2)
            Label(new,text='Enter Full Name',bg='#49A').grid(row=2,column=1)
            Entry(new,width=25,textvariable=n).grid(row=2,column=2)#name
            Label(new,text='Enter Email',bg='#49A').grid(row=3,column=1)
            Entry(new,width=25,textvariable=e).grid(row=3,column=2)#email
            Label(new,text='Enter New Password',bg='#49A').grid(row=4,column=1)
            Entry(new,width=25,textvariable=p,show='*').grid(row=4,column=2)#password
            Button(new,text='Proceed',command=proceed,bg='#567',fg='White').grid(row=5,column=3)

        em=StringVar()
        pas=StringVar()
        sign=Toplevel()
        sign.title('SignIn/CreateAccount-IAS')
        sign.geometry('960x720')
        sign['bg'] = '#49A'
        Label(sign,text='Sign In',font='Verdana 12 bold',bg='#49A').grid(row=1,column=2)
        Button(sign,text='CreateAccount',command=account,bg='yellow').grid(row=1,column=3)
        Label(sign,text='Enter Email Address:',bg='#49A').grid(row=2,column=1)
        Entry(sign,width=25,textvariable=em).grid(row=2,column=2)#email
        Label(sign,text='Enter Passsword',bg='#49A').grid(row=3,column=1)
        Entry(sign,width=25,textvariable=pas,show='*').grid(row=3,column=2)#password
        Button(sign,text='Proceed',command=proceed1,bg='yellow').grid(row=4,column=3)
    
    class SubjectProjection:
        def subpro():#subject projection
            sub=Toplevel()
            sub.geometry('960x720')
            sub.title('Subject Projection')
            sub['bg'] = '#49A'
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
               
            Label(sub,text='Enter details',bg='#49A').grid(row=1,column=2)
            Label(sub,text='Enter Graph Title',bg='#49A').grid(row=2,column=1)
            Entry(sub,width=20,textvariable=subject).grid(row=2,column=2)
            Label(sub,text='Percentage',bg='#49A').grid(row=3,column=2)
            Label(sub,text='no. of students',bg='#49A').grid(row=3,column=3)
            Label(sub,text='90%-100%',bg='#49A').grid(row=4,column=2)
            Label(sub,text='75%-90%',bg='#49A').grid(row=5,column=2)
            Label(sub,text='60%-75%',bg='#49A').grid(row=6,column=2)
            Label(sub,text='below 35%',bg='#49A').grid(row=9,column=2)
            Label(sub,text='45%-60%',bg='#49A').grid(row=7,column=2)
            Label(sub,text='35%-40%',bg='#49A').grid(row=8,column=2)
            Entry(sub,width=2,textvariable=first).grid(row=4,column=3)
            Entry(sub,width=2,textvariable=second).grid(row=5,column=3)
            Entry(sub,width=2,textvariable=third).grid(row=6,column=3)
            Entry(sub,width=2,textvariable=fourth).grid(row=7,column=3)
            Entry(sub,width=2,textvariable=fifth).grid(row=8,column=3)
            Entry(sub,width=2,textvariable=sixth).grid(row=9,column=3)
            Label(sub,text='Type of Graph',bg='#49A').grid(row=10,column=2)
            Radiobutton(sub,text='BarGraph',variable=ch,value=1,bg='#49A').grid(row=11,column=2)
            Radiobutton(sub,text='PieChart',variable=ch,value=2,bg='#49A').grid(row=11,column=3)
            Button(sub,text='Plot',command=check,bg='#567',fg='White').grid(row=12,column=4)
        
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
            calc['bg'] = '#49A'
        
            Label(calc,text='Enter marks',font='Helvetica 12 bold',bg='#49A').grid(row=1,column=4)
            Label(calc,text='marks',bg='#49A').grid(row=2,column=2)
            Entry(calc,width=8,textvariable=main).grid(row=3,column=2)
            Label(calc,text='/',bg='#49A').grid(row=2,column=3)
            Label(calc,text='Total',bg='#49A').grid(row=2,column=4)
            Entry(calc,width=8,textvariable=total).grid(row=3,column=4)
            Button(calc,text='Calculate',command=check,bg='#567',fg='White').grid(row=4,column=5)
class Dashboard:
    def accwindow():#mainprofile
        global s
        def accwindow1():
            dash.destroy()
            Dashboard.accwindow()
        def newclass():#creating new class
            def ok():
                cursor.execute('select classname from clsaccounts;')
                row=cursor.fetchall()
                clname=cname.get()
                flag=0
                for i in range(len(row)):
                    tp1=''
                    tp=row[i]
                    tp1=tp[0]
                    if tp1==clname:
                        flag=1
                
                sub1=s1.get()
                sub2=s2.get()
                sub3=s3.get()
                sub4=s4.get()
                sub5=s5.get()
                if clname=='':
                    return messagebox.showerror('Error','Enter Class name')
                elif flag==1:
                    return messagebox.showerror('Error','Class name used before')    
                elif sub1=='':
                    return messagebox.showerror('Error','Enter Subject1')
                elif sub2=='':
                    return messagebox.showerror('Error','Enter Subject2')
                elif sub3=='':
                    return messagebox.showerror('Error','Enter Subject3')
                elif sub4=='':
                    return messagebox.showerror('Error','Enter Subject4')
                elif sub5=='':
                    return messagebox.showerror('Error','Enter Subject5')
                else:
                 
                    sql8="""INSERT INTO clsaccounts
                              (email,classname,subject1,subject2,subject3,subject4,subject5) 
                              VALUES (?, ?, ?, ?, ?, ?, ?);"""
                    data = (email,clname,sub1,sub2,sub3,sub4,sub5)
                    cur=conn.cursor()
                    cur.execute(sql8,data)
                    conn.commit()
                    conn.close()
                    nclass= sqlite3.connect(clname+".db")
                    ncursor=nclass.cursor()#cursor for selected class
                    ncursor.execute("""CREATE TABLE stdetails (grno INTEGER,studentname TEXT,PT1 INTEGER,PT2 INTEGER,HFYEARLY INTEGER,PT3 INTEGER,PT4 INTEGER,M1 INTEGER,M2 INTEGER,FINAL INTEGER)""")#table for student details
                    ncursor.execute("""CREATE TABLE subdetails (grno INTEGER,studentname TEXT,subject TEXT,PT1 INTEGER,PT2 INTEGER,HFYEARLY INTEGER,PT3 INTEGER,PT4 INTGER,M1 INTEGER,M2 INTEGER,FINAL INTEGER)""")#table for subject details
                    nclass.close()
                    newc.destroy()
                    
            
            newc=Toplevel()
            newc.geometry('960x720')
            newc.title('create new class')
            newc['bg'] = '#49A'
            cname=StringVar()
            s1=StringVar()
            s2=StringVar()
            s3=StringVar()
            s4=StringVar()
            s5=StringVar()
            Label(newc,text='Enter Details',font='Helvetica 12 bold',bg='#49A').grid(row=1,column=3)
            Label(newc,text='Enter class name:',bg='#49A').grid(row=2,column=1)
            Entry(newc,width=11,textvariable=cname).grid(row=2,column=2)
            Label(newc,text='Enter Subject details:',bg='#49A').grid(row=3,column=1)
            Label(newc,text='Subject1',bg='#49A').grid(row=4,column=1)
            Entry(newc,width=15,textvariable=s1).grid(row=4,column=2)
            Label(newc,text='Subject2',bg='#49A').grid(row=5,column=1)
            Entry(newc,width=15,textvariable=s2).grid(row=5,column=2)
            Label(newc,text='Subject3',bg='#49A').grid(row=6,column=1)
            Entry(newc,width=15,textvariable=s3).grid(row=6,column=2)
            Label(newc,text='Subject4',bg='#49A').grid(row=7,column=1)
            Entry(newc,width=15,textvariable=s4).grid(row=7,column=2)
            Label(newc,text='Subject5',bg='#49A').grid(row=8,column=1)
            Entry(newc,width=15,textvariable=s5).grid(row=8,column=2)
            Button(newc,text='OK',command=ok,bg='#567',fg='White').grid(row=8,column=3)
        def signout():
            dash.destroy()
            messagebox.showinfo('Result','Sign Out Successfully')
        classes=[]
        def check():
            messagebox.showinfo('Result','Selected Successfully')
        conn = sqlite3.connect("main.db")#main database conn.
        cursor=conn.cursor()
        stat='select * from clsaccounts where email=?'
        cursor.execute(stat, (email,))
        c=cursor.fetchall()
        co=len(c)
        co=str(co)#no. of classes
        #########
        sql='select Name from accdetails where email=?'
        cursor.execute(sql, (email,))
        row=cursor.fetchall()
        row1=row[0]
        finaln=row1[0]
        conn.commit()
        ########
        sql3='select classname from clsaccounts where email=?'
        cursor.execute(sql3, (email,))
        row2=cursor.fetchall()
        count=len(row2)
        for i in range(len(row2)):
            tp=row2[i]
            tp1=tp[0]
            classes.append(tp1)
        dash=Toplevel()
        dash.geometry('960x720')
        dash.title('Dashboard-IAS')
        dash['bg'] = '#49A'
        s=StringVar()
        Button(dash,text='SignOut',command=signout,bg='#567',fg='White').grid(row=1,column=3)
        Label(dash,text='Your DashBoard',font='Verdana 12 bold',bg='#49A').grid(row=1,column=2)
        Label(dash,text='Your Name: '+finaln,bg='#49A').grid(row=2,column=1)
        Label(dash,text='Email: '+email,bg='#49A').grid(row=3,column=1)
        Label(dash,text='No. of classes:'+co,bg='#49A').grid(row=4,column=1)
        Button(dash,text='Create New Class',command=newclass,bg='#567',fg='White').grid(row=5,column=1)
        Label(dash,text='Select Class>>>>',bg='#49A').grid(row=6,column=1)
        classselect=ttk.Combobox(dash,values=classes,state='readonly',textvariable=s)
        classselect.grid(row=6,column=2)
        if count!=0:
            classselect.current(0)
        Button(dash,text='Proceed',command=check,bg='#567',fg='White').grid(row=7,column=3)
        Button(dash,text='refresh',command=accwindow1,bg='#567',fg='White').grid(row=1,column=4)

            
home=Tk()
home['bg'] = 'yellow'
home.geometry('1080x720')
home.title('Instructor Aid System')
img=Image.open('IAS3.jpg')
img = ImageTk.PhotoImage(img, master=home)
Label(home,image=img).pack()
Label(home,text='---HOME PAGE---',font='Verdana 15 bold',bg='#673',fg='White').place(relx=.5,anchor= N)
Button(home,text='SignIn/Create Account',font='Verdana 12 bold',command=Homepage.sign,bg='#567',fg='White').place(relx=.5, rely=.4,anchor= CENTER)
Button(home,text='Subject Projection',font='Verdana 12 bold',command=Homepage.SubjectProjection.subpro,bg='#567',fg='White').place(relx=.5, rely=.5,anchor= CENTER)
Button(home,text='Percentage calculator',font='Verdana 12 bold',command=Homepage.Calculator.calculator,bg='#567',fg='White').place(relx=.5, rely=.6,anchor= CENTER)
home.mainloop()
        
        
        
    