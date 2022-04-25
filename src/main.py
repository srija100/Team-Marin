import tkinter 
from tkinter import *
from tkinter import ttk 
import csv
from tkinter import simpledialog
from tkinter import filedialog as fd
from PIL import Image,ImageTk
import sqlite3
from sqlite3 import Error
from tkinter import messagebox
import matplotlib.pyplot as plt

headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
labelfont = ('Garamond', 14,'bold')
entryfont = ('Garamond', 12,'bold')

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
            new['bg'] = '#36DAA5'
            Label(new,text='New Account',font=headlabelfont,width=150,bg='Black',fg='SpringGreen').place(relx=.5,anchor= N)
            Label(new,text='Full Name',font=labelfont,width=15,bg='#36DAA5').place(relx=.41,rely=.3)
            Label(new,text='Email',font=labelfont,width=15,bg='#36DAA5').place(relx=.39,rely=.4)
            Label(new,text='New Password',font=labelfont,width=15,bg='#36DAA5').place(relx=.43,rely=.5)
            
            Entry(new,width=25,textvariable=n,font=entryfont).place(relx=.45,rely=.35)#name
            Entry(new,width=25,textvariable=e,font=entryfont).place(relx=.45,rely=.45)#email
            Entry(new,width=25,textvariable=p,show='*',font=entryfont).place(relx=.45,rely=.55)#password
            Button(new,text='Create',font=headlabelfont,command=proceed,bg='#567',width='15',fg='White').place(relx=.45,rely=.63)

        em=StringVar()
        pas=StringVar()
        sign=Toplevel()
        sign.title('SignIn/CreateAccount-IAS')
        sign.geometry('960x720')
        sign['bg'] = '#36DAA5'
        Label(sign,text='Sign In',font=headlabelfont,width=150,bg='Black',fg='SpringGreen').place(relx=.5,anchor= N)
        Button(sign,text='Create Account',font=headlabelfont,command=account,bg='#567',height=2,width=20,fg='White').place(relx=0.1,rely=0.5)
        
        Label(sign,text='Email',font=labelfont,width=10,bg='#36DAA5').place(relx=.47,rely=.4)
        Label(sign,text='Password',font=labelfont,width=13,bg='#36DAA5').place(relx=.47,rely=.5)
        
        Entry(sign,width=25,textvariable=em,font=entryfont).place(relx=.5,rely=.45)
        Entry(sign,width=25,textvariable=pas,show='*',font=entryfont).place(relx=.5,rely=.55)
        
        Button(sign,text='Proceed',font=headlabelfont,command=proceed1,bg='#567',width='15',fg='White').place(relx=.5,rely=.63)
    
    class SubjectProjection:
        def subpro():#subject projection
            sub=Toplevel()
            sub.geometry('960x720')
            sub.title('Subject Projection')
            sub['bg'] = '#36DAA5'
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
               
            Label(sub,text='Subject Projection',font=headlabelfont,width=150,bg='Black',fg='SpringGreen').place(relx=.5,anchor= N)
            Label(sub,text='Enter Graph Title',font=labelfont,width=15,bg='#36DAA5').place(relx=.41,rely=.2)
            Label(sub,text='Percentage',font=labelfont,width=15,bg='#36DAA5').place(relx=.39,rely=.30)
            Label(sub,text='no.of students',font=labelfont,width=15,bg='#36DAA5').place(relx=.55,rely=.30)
            Label(sub,text='90%-100%',font=labelfont,width=15,bg='#36DAA5').place(relx=.39,rely=.35)
            Label(sub,text='75%-90%',font=labelfont,width=15,bg='#36DAA5').place(relx=.39,rely=.40)
            Label(sub,text='60%-75%',font=labelfont,width=15,bg='#36DAA5').place(relx=.39,rely=.45)
            Label(sub,text='45%-60%',font=labelfont,width=15,bg='#36DAA5').place(relx=.39,rely=.50)
            Label(sub,text='35%-40%',font=labelfont,width=15,bg='#36DAA5').place(relx=.39,rely=.55)
            Label(sub,text='below 35%',font=labelfont,width=15,bg='#36DAA5').place(relx=.39,rely=.60)
            Label(sub,text='Type of Graph',font=labelfont,width=15,bg='#36DAA5').place(relx=.4,rely=.65)
            
            Entry(sub,width=30,textvariable=subject,font=entryfont).place(relx=.42,rely=.25)
            Entry(sub,width=5,textvariable=first,font=entryfont).place(relx=.6,rely=.35)
            Entry(sub,width=5,textvariable=second,font=entryfont).place(relx=.6,rely=.40)
            Entry(sub,width=5,textvariable=third,font=entryfont).place(relx=.6,rely=.45)
            Entry(sub,width=5,textvariable=fourth,font=entryfont).place(relx=.6,rely=.50)
            Entry(sub,width=5,textvariable=fifth,font=entryfont).place(relx=.6,rely=.55)
            Entry(sub,width=5,textvariable=sixth,font=entryfont).place(relx=.6,rely=.60)
            
            Radiobutton(sub,text='Bar Graph',variable=ch,value=1,font=entryfont,bg='#36DAA5').place(relx=.42,rely=.70)
            Radiobutton(sub,text='Pie Chart',variable=ch,value=2,font=entryfont,bg='#36DAA5').place(relx=.55,rely=.70)
            Button(sub,text='Plot',font=headlabelfont,command=check,width=15,bg='#567',fg='White').place(relx=.45,rely=.8)
        
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
            calc['bg'] = '#36DAA5'
        
            Label(calc,text='Calculator',font=headlabelfont,width=150,bg='Black',fg='SpringGreen').place(relx=.5,anchor= N)
            Label(calc,text='Marks',font=labelfont,width=10,bg='#36DAA5').place(relx=.35,rely=.4)
            Label(calc,text='/',font=labelfont,width=5,bg='#36DAA5').place(relx=.45,rely=.4)
            Label(calc,text='Total',font=labelfont,width=10,bg='#36DAA5').place(relx=.50,rely=.4)
            
            Entry(calc,width=8,textvariable=main,font=entryfont).place(relx=.38,rely=.45)
            Entry(calc,width=8,textvariable=total,font=entryfont).place(relx=.53,rely=.45)
            
            Button(calc,text='Calculate',font=headlabelfont,command=check,width=15,bg='#567',fg='White').place(relx=.39,rely=.55)
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
            newc['bg'] = '#36DAA5'
            cname=StringVar()
            s1=StringVar()
            s2=StringVar()
            s3=StringVar()
            s4=StringVar()
            s5=StringVar()
            Label(newc,text='New Class',font=headlabelfont,width=150,bg='Black',fg='SpringGreen').place(relx=.5,anchor= N)
            Label(newc,text='Class Name:',font=labelfont,width=20,bg='#36DAA5',fg='Black').place(relx=.335,rely=.3)
            Label(newc,text='Subject Details:',font=labelfont,width=20,bg='#36DAA5',fg='Black').place(relx=.35,rely=.4)
            Label(newc,text='Subject1',font=labelfont,width=10,bg='#36DAA5',fg='Black').place(relx=.4,rely=.45)
            Label(newc,text='Subject2',font=labelfont,width=10,bg='#36DAA5',fg='Black').place(relx=.4,rely=.52)
            Label(newc,text='Subject3',font=labelfont,width=10,bg='#36DAA5',fg='Black').place(relx=.4,rely=.59)
            Label(newc,text='Subject4',font=labelfont,width=10,bg='#36DAA5',fg='Black').place(relx=.4,rely=.66)
            Label(newc,text='Subject5',font=labelfont,width=10,bg='#36DAA5',fg='Black').place(relx=.4,rely=.73)
            
            Entry(newc,width=20,textvariable=cname,font=entryfont).place(relx=.4,rely=.35)
            Entry(newc,width=15,textvariable=s1,font=entryfont).place(relx=.55,rely=.45)
            Entry(newc,width=15,textvariable=s2,font=entryfont).place(relx=.55,rely=.52)
            Entry(newc,width=15,textvariable=s3,font=entryfont).place(relx=.55,rely=.59)
            Entry(newc,width=15,textvariable=s4,font=entryfont).place(relx=.55,rely=.66)
            Entry(newc,width=15,textvariable=s5,font=entryfont).place(relx=.55,rely=.73)
            
            Button(newc,text='Add',command=ok,font=headlabelfont,width=15,bg='#567',fg='White').place(relx=.45,rely=.8)
        def signout():
            dash.destroy()
            messagebox.showinfo('Result','Sign Out Successfully')
        classes=[]
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
        dash['bg'] = '#36DAA5'
        s=StringVar()
        
        Label(dash,text='DashBoard',font=headlabelfont,width=150,bg='Black',fg='SpringGreen').place(relx=.5,anchor= N)
        Label(dash,text='Your Name: '+finaln,font=labelfont,width=20,bg='#36DAA5',fg='Black').place(relx=.4,rely=.35)
        Label(dash,text='Email: '+email,font=labelfont,width=20,bg='#36DAA5').place(relx=.4,rely=.4)
        Label(dash,text='No. of classes:'+co,font=labelfont,width=20,bg='#36DAA5').place(relx=.35,rely=.45)
        Label(dash,text='Select Class -->>>>',font=labelfont,width=20,bg='#36DAA5').place(relx=.37,rely=.5)
        classselect=ttk.Combobox(dash,values=classes,state='readonly',textvariable=s,width=10,font=entryfont)
        classselect.place(relx=.6,rely=.505)
        
        if count!=0:
            classselect.current(0)
       
        Button(dash,text='Refresh',command=accwindow1,font=entryfont,width=5,bg='#567',fg='White').place(relx=.05,rely=.1)
        Button(dash,text='Sign Out',command=signout,font=entryfont,width=6,bg='#567',fg='White').place(relx=.9,rely=.1)
        Button(dash,text='Proceed',command=ClassProfile.classprofile,font=headlabelfont,width=15,bg='#567',fg='White').place(relx=.4,rely=.6)
        Button(dash,text='Create New Class',command=newclass,font=headlabelfont,height=1,width=15,bg='#567',fg='White').place(relx=.05,rely=.43)
class ClassProfile:
    def classprofile():#classprofile
        global subjects #subjectlist
        global clname
        global fil
        global filters #filterlist
        global flag
        exams=['-select-','PT1','PT2','HFYEARLY','PT3','PT4','M1','M2','FINAL']
        clname=s.get()
        nclass= sqlite3.connect(clname+".db")
        ncursor=nclass.cursor()
        sql22='SELECT subject1,subject2,subject3,subject4,subject5 FROM clsaccounts WHERE classname=?'
        cursor.execute(sql22, (clname,))
        row=cursor.fetchall()
        data=row[0]
        sub=[]
        subjects=['-select-']
        for i in range(len(data)):
            subjects.append(data[i])#subjectslist
            sub.append(data[i])
        ncursor.execute('select studentname from stdetails')
        st=ncursor.fetchall()
        students=['-select-'] 
        for i in range(len(st)):
            stu=st[i]
            students.append(stu[0]) #studentslist
        def remove():
            def pre():
                name=nm.get()
                ex='delete from stdetails where studentname=?'
                ncursor.execute(ex,(name,))
                nclass.commit()
                ex1='delete from subdetails where studentname=?'
                ncursor.execute(ex1,(name,))
                nclass.commit()
                rem.destroy()
                messagebox.showinfo('Result','Student Removed Successfully')
                cprofile.destroy()
                ClassProfile.classprofile()
            nms=[]#student names
            nm=StringVar()
            ncursor.execute('select studentname from stdetails')
            d=ncursor.fetchall()
            for i in d:
                i=i[0]
                nms.append(i)
            rem=Toplevel()
            rem.geometry('300x300')
            rem.title('Remove Student')
            rem['bg'] = '#36DAA5'
            Label(rem,text='Select Student',font=labelfont,bg='#36DAA5').grid(row=1,column=1)
            stuselect1=ttk.Combobox(rem,values=nms,state='readonly',textvariable=nm)
            stuselect1.grid(row=1,column=2)
            stuselect1.current(0)
            Button(rem,text='Proceed',command=pre,font=entryfont,width=15,bg='#567').place(x=80,y=200)

        def cperformance():
            ncursor.execute('select * from stdetails')
            row=ncursor.fetchall()#data-stdetails
            rows=len(row) #number of students
            def ok():
                def project():
                    ms=[]#marks-list
                    names=[]#names-lists
                    ex='select studentname from stdetails'
                    ex1='select '+exam+' from stdetails'
                    ncursor.execute(ex)
                    d=ncursor.fetchall()
                    for i in d:
                        i=i[0]
                        names.append(i)
                    ncursor.execute(ex1)
                    d=ncursor.fetchall()
                    for i in d:
                        i=i[0]
                        ms.append(i)
                    plt.title(exam+' marks')
                    plt.xlabel('students')
                    plt.ylabel('marks')
                    plt.bar(names,ms,width=0.3)
                    plt.show()

                    
                exam=exm.get()
                if exam=='-select-':
                    return messagebox.showerror('Error','Select Exam')
                else:
                    marks=[]
                    ex='select '+exam+' from stdetails'
                    ncursor.execute(ex)
                    fe=ncursor.fetchall()
                    for i in fe:
                        i=i[0]
                        marks.append(i)
                    mar=sum(marks)/len(marks)
                    cp.destroy()
                    cpf=Toplevel()
                    cpf.geometry('600x400')
                    cpf.title('Class Performance-IAS')
                    cpf['bg'] = '#36DAA5'
                    Label(cpf,text='Class: '+clname,font=labelfont,bg='#36DAA5').grid(row=1,column=1)
                    Label(cpf,text='Number of students: '+str(rows),font=labelfont,bg='#36DAA5').grid(row=2,column=1)
                    Label(cpf,text='Exam Type: '+exam,font=labelfont,bg='#36DAA5').grid(row=3,column=1)
                    Label(cpf,text='Class Average: '+str(round(mar))+'%',font=labelfont,bg='#36DAA5').grid(row=4,column=1)
                    Label(cpf,text='---Individual Marks---',font=headlabelfont,bg='#36DAA5').grid(row=5,column=2)
                    Button(cpf,text=sub[0]+' marks',command=sub1m,font=entryfont,width=15,bg='#567').grid(row=6,column=1)
                    Button(cpf,text=sub[1]+' marks',command=sub2m,font=entryfont,width=15,bg='#567').grid(row=7,column=1)
                    Button(cpf,text=sub[2]+' marks',command=sub3m,font=entryfont,width=15,bg='#567').grid(row=8,column=1)
                    Button(cpf,text=sub[3]+' marks',command=sub4m,font=entryfont,width=15,bg='#567').grid(row=9,column=1)
                    Button(cpf,text=sub[4]+' marks',command=sub5m,font=entryfont,width=15,bg='#567').grid(row=10,column=1)
                    Button(cpf,text='Project Scores',command=project,font=entryfont,width=15,bg='#567').grid(row=10,column=3)


            exm=StringVar()
            cp=Toplevel()
            cp.geometry('300x200')
            cp.title('Class Performance-IAS')
            cp['bg'] = '#36DAA5'
            Label(cp,text='Select exam',font=labelfont,bg='#36DAA5').grid(row=1,column=1)
            stuselect1=ttk.Combobox(cp,values=['-select-','PT1','PT2','HFYEARLY','PT3','PT4','M1','M2','FINAL'],state='readonly',textvariable=exm)
            stuselect1.grid(row=1,column=2)
            stuselect1.current(0)
            Button(cp,text='Proceed',command=ok,font=entryfont,width=15,bg='#567').place(x=80,y=150)
            
        def sreport(): #student report
            def report():
                def project():
                    plt.title(exm+' projection')
                    plt.xlabel('Subjects')
                    plt.ylabel('Marks')
                    plt.bar(sub,ms)
                    plt.show()
                stname=student.get()
                exm=exam.get()
                if stname=='-select-':
                    return messagebox.showerror('Error','Select Student')
                elif exm=='-select-':
                    return messagebox.showerror('Error','Select Exam')
                else:
                    ms=[]#obtained marks
                    ask.destroy()
                    rep=Toplevel()
                    rep.geometry('550x500')
                    rep.title('Student Report')
                    rep['bg'] = '#36DAA5'
                    Label(rep,text='Class:'+clname,font=labelfont,bg='#36DAA5').grid(row=1,column=1)
                    Label(rep,text='Student Name:'+stname,font=labelfont,bg='#36DAA5').grid(row=2,column=1)
                    Label(rep,text='Exam Type:'+exm,font=labelfont,bg='#36DAA5').grid(row=3,column=1)
                    Label(rep,text='----Mark Distribution----',font=labelfont,bg='#36DAA5').grid(row=4,column=2)
                    exec1='select '+exm+' from subdetails where studentname=? and subject=?'
                    det=(stname,sub[0])
                    ncursor.execute(exec1,det)
                    row=ncursor.fetchall()
                    row1=row[0]
                    row2=row1[0]
                    ms.append(row2)
                    Label(rep,text=sub[0]+'marks: '+str(row2),font=labelfont,bg='#36DAA5').grid(row=5,column=2)
                    exec1='select '+exm+' from subdetails where studentname=? and subject=?'
                    det=(stname,sub[1])
                    ncursor.execute(exec1,det)
                    row=ncursor.fetchall()
                    row1=row[0]
                    row2=row1[0]
                    ms.append(row2)
                    Label(rep,text=sub[1]+'marks: '+str(row2),font=labelfont,bg='#36DAA5').grid(row=6,column=2)
                    exec1='select '+exm+' from subdetails where studentname=? and subject=?'
                    det=(stname,sub[2])
                    ncursor.execute(exec1,det)
                    row=ncursor.fetchall()
                    row1=row[0]
                    row2=row1[0]
                    ms.append(row2)
                    Label(rep,text=sub[2]+'marks: '+str(row2),font=labelfont,bg='#36DAA5').grid(row=7,column=2)
                    exec1='select '+exm+' from subdetails where studentname=? and subject=?'
                    det=(stname,sub[3])
                    ncursor.execute(exec1,det)
                    row=ncursor.fetchall()
                    row1=row[0]
                    row2=row1[0]
                    ms.append(row2) 
                    Label(rep,text=sub[3]+'marks: '+str(row2),font=labelfont,bg='#36DAA5').grid(row=8,column=2)
                    exec1='select '+exm+' from subdetails where studentname=? and subject=?'
                    det=(stname,sub[4])
                    ncursor.execute(exec1,det)
                    row=ncursor.fetchall()
                    row1=row[0]
                    row2=row1[0]
                    ms.append(row2)
                    Label(rep,text=sub[4]+'marks: '+str(row2),font=labelfont,bg='#36DAA5').grid(row=9,column=2)
                    exec1='select '+exm+' from stdetails where studentname=?'
                    ncursor.execute(exec1,(stname,))
                    row=ncursor.fetchall()
                    row1=row[0]
                    row2=row1[0]
                    Label(rep,text='Total Percentage: '+str(row2)+'%',font=labelfont,bg='#36DAA5').grid(row=10,column=1)
                    Button(rep,text='Project Scores',command=project,font=entryfont,width=15,bg='#567').grid(row=11,column=2)

            student=StringVar()
            exam=StringVar()
            ncursor.execute('select studentname from stdetails')
            st=ncursor.fetchall()
            students=['-select-'] 
            for i in range(len(st)):
                stu=st[i]
                students.append(stu[0]) #studentslist
            ask=Toplevel()
            ask.geometry('550x500')
            ask['bg'] = '#36DAA5'
            ask.title('Student Report')
            Label(ask,text='Student Name ',font=labelfont,bg='#36DAA5').place(relx=.25,rely=.4)
            stuselect2=ttk.Combobox(ask,values=students,state='readonly',textvariable=student)
            stuselect2.place(relx=.5,rely=.405)
            stuselect2.current(0)
            Label(ask,text='Select exam',font=labelfont,bg='#36DAA5').place(relx=.25,rely=.5)
            stuselect1=ttk.Combobox(ask,values=['-select-','PT1','PT2','HFYEARLY','PT3','PT4','M1','M2','FINAL'],state='readonly',textvariable=exam)
            stuselect1.place(relx=.5,rely=.505)
            stuselect1.current(0)
            Button(ask,text='Proceed',command=report,font=entryfont,width=15,bg='#567').place(relx=.36,rely=0.8)

        def mrksheetupload():#upload marksheet 
            def file1():
                outof=0
                mexe=mex.get() #type of exam
                subj=subu.get()
                outof=mrs.get()
                if subj=='-select-':
                    return messagebox.showerror('Error','Enter Subject')
                if mexe=='-select-':
                    return messagebox.showerror('Error','Enter Name')
                if outof==0:
                    return messagebox.showerror('Error','Select Total Marks')
                ft=[("CSV",".csv"),('All Files',"'*")]
                file=fd.askopenfilename(parent=upload,initialdir='/',title='Select File',filetypes=ft,defaultextension=ft)
                mrdata=[] #main data
                datas=[]#cleaned data
                with open(file,'r') as csvfile:
                    readCSV = csv.reader(csvfile)
                    for row23 in readCSV:
                        mrdata.append(row23)  #appending data             
                    for i in range(len(mrdata)):
                        if i%2==0:
                            datas.append(mrdata[i]) #cleaning data
                    datas.pop(0)
                    print(datas)
                    dat=[]
                    for i in range(len(datas)):
                        dat=datas[i]
                        sq='UPDATE subdetails SET '+mexe+' = ? WHERE studentname = ?  AND subject = ?' #for subdetails
                        data32=(int(dat[1]),dat[0],subj)
                        ncursor.execute(sq,data32)
                        nclass.commit()
                        pers=[]
                        execu='select '+mexe+' from stdetails where studentname=?'
                        ncursor.execute(execu, (dat[0],))
                        tm=ncursor.fetchall()
                        tm=tm[0]
                        tms=tm[0]
                        pers.append(tms)
                        per=(int(dat[1])/outof)*100 #current percentage
                        pers.append(per)
                        avg1=sum(pers)/len(pers) #total precentage
                        avg=round(avg1)
                        sql37='UPDATE stdetails SET '+mexe+' = ? WHERE studentname = ?' #for stdetails
                        data37=(avg,dat[0])
                        ncursor.execute(sql37,data37)
                        nclass.commit()
                    upload.destroy()
                    messagebox.showinfo('Result','Marks Uploaded')
                    cprofile.destroy()
                    ClassProfile.classprofile()
            mex=StringVar()
            subu=StringVar()
            upload=Toplevel()
            mrs=IntVar()
            upload.geometry('400x300')
            upload.title('Marksheet Upload')
            upload['bg'] = '#36DAA5'
            Label(upload,text='Enter Details',font=labelfont,bg='#36DAA5').grid(row=1,column=2)
            Label(upload,text='Select Exam',font=labelfont,bg='#36DAA5').grid(row=2,column=1)
            sel=ttk.Combobox(upload,values=['-select-','PT1','PT2','HFYEARLY','PT3','PT4','M1','M2','FINAL'],state='readonly',textvariable=mex)
            sel.grid(row=2,column=2)
            sel.current(0)
            Label(upload,text='Select Subject',font=labelfont,bg='#36DAA5').grid(row=3,column=1)
            sel1=ttk.Combobox(upload,values=['-select-',sub[0],sub[1],sub[2],sub[3],sub[4]],state='readonly',textvariable=subu)
            sel1.grid(row=3,column=2)
            sel1.current(0)
            Label(upload,text='Marks are out of:',font=labelfont,bg='#36DAA5').grid(row=4,column=1)
            Radiobutton(upload,text='20',variable=mrs,value=20,bg='#36DAA5').place(x=30,y=120)
            Radiobutton(upload,text='30',variable=mrs,value=30,bg='#36DAA5').place(x=70,y=120)
            Radiobutton(upload,text='70',variable=mrs,value=70,bg='#36DAA5').place(x=110,y=120)
            Radiobutton(upload,text='80',variable=mrs,value=80,bg='#36DAA5').place(x=150,y=120)
            Button(upload,text='Select File:',command=file1,font=entryfont,width=15,bg='#567').place(x=80,y=160)
        

        def dmarksheet():#saving marksheet
            ft=[('CSV file','*.csv')]
            file=fd.asksaveasfile(filetypes=ft,mode="w",defaultextension=ft)
            fieldnames=['Student Name','Marks']
            writer=csv.DictWriter(file,fieldnames=fieldnames)
            writer.writeheader() 
            ncursor.execute('select studentname from stdetails;')
            row331=ncursor.fetchall()
            for i in range(len(row331)):
                row33=row331[i]
                nm=row33[0]#name
                writer.writerow({'Student Name':nm,'Marks':0})
            file.close()
            print('Complete')
        def sub1m(): #subject1 marks
            execu='select * from subdetails where subject=?'
            ncursor.execute(execu,(subjects[1],))
            marks=ncursor.fetchall()
            sub1=Toplevel()
            sub1.geometry('730x250')
            sub1['bg'] = '#36DAA5'
            sub1.title(subjects[1]+' marks')
            scroll1=ttk.Scrollbar(sub1)
            scroll1.grid(row=1,column=2)
            tb1=ttk.Treeview(sub1,columns=(1,2,3,4,5,6,7,8,9,10,11),show='headings',selectmode='browse')
            tb1.grid(row=1,column=1)
            tb1.heading(1,text="Grno")
            tb1.column(1,minwidth=0,width=50,stretch=NO)
            tb1.heading(2,text="Studentname")
            tb1.column(2,minwidth=0,width=120,stretch=NO)
            tb1.heading(3,text="Subject")
            tb1.column(3,minwidth=0,width=50,stretch=NO)
            tb1.heading(4,text="PT1")
            tb1.column(4,minwidth=0,width=50,stretch=NO)
            tb1.heading(5,text="PT2")
            tb1.column(5,minwidth=0,width=50,stretch=NO)
            tb1.heading(6,text="HFYEARLY")
            tb1.column(6,minwidth=0,width=80,stretch=NO)
            tb1.heading(7,text="PT3")
            tb1.column(7,minwidth=0,width=50,stretch=NO)
            tb1.heading(8,text="PT4")
            tb1.column(8,minwidth=0,width=50,stretch=NO)
            tb1.heading(9,text="M1")
            tb1.column(9,minwidth=0,width=50,stretch=NO)
            tb1.heading(10,text="M2")
            tb1.column(10,minwidth=0,width=70,stretch=NO)
            tb1.heading(11,text="FINAL")
            tb1.column(11,minwidth=0,width=70,stretch=NO)
            scroll1.config(command=tb1.yview)
            for i in marks: #appending details(subdetails)
                tb1.insert('','end',values=i)
        def sub2m(): #subject 2 marks
            execu='select * from subdetails where subject=?'
            ncursor.execute(execu,(subjects[2],))
            marks=ncursor.fetchall()
            sub2=Toplevel()
            sub2.geometry('730x250')
            sub2['bg'] = '#36DAA5'
            sub2.title(subjects[2]+' marks')
            scroll1=ttk.Scrollbar(sub2)
            scroll1.grid(row=1,column=2)
            tb1=ttk.Treeview(sub2,columns=(1,2,3,4,5,6,7,8,9,10,11),show='headings',selectmode='browse')
            tb1.grid(row=1,column=1)
            tb1.heading(1,text="Grno")
            tb1.column(1,minwidth=0,width=50,stretch=NO)
            tb1.heading(2,text="Studentname")
            tb1.column(2,minwidth=0,width=120,stretch=NO)
            tb1.heading(3,text="Subject")
            tb1.column(3,minwidth=0,width=50,stretch=NO)
            tb1.heading(4,text="PT1")
            tb1.column(4,minwidth=0,width=50,stretch=NO)
            tb1.heading(5,text="PT2")
            tb1.column(5,minwidth=0,width=50,stretch=NO)
            tb1.heading(6,text="HFYEARLY")
            tb1.column(6,minwidth=0,width=80,stretch=NO)
            tb1.heading(7,text="PT3")
            tb1.column(7,minwidth=0,width=50,stretch=NO)
            tb1.heading(8,text="PT4")
            tb1.column(8,minwidth=0,width=50,stretch=NO)
            tb1.heading(9,text="M1")
            tb1.column(9,minwidth=0,width=50,stretch=NO)
            tb1.heading(10,text="M2")
            tb1.column(10,minwidth=0,width=70,stretch=NO)
            tb1.heading(11,text="FINAL")
            tb1.column(11,minwidth=0,width=70,stretch=NO)
            scroll1.config(command=tb1.yview)
            for i in marks: #appending details(subdetails)
                tb1.insert('','end',values=i)
        def sub3m(): #subject3 marks
            execu='select * from subdetails where subject=?'
            ncursor.execute(execu,(subjects[3],))
            marks=ncursor.fetchall()
            sub3=Toplevel()
            sub3.geometry('730x250')
            sub3['bg'] = '#36DAA5'
            sub3.title(subjects[3]+' marks')
            scroll1=ttk.Scrollbar(sub3)
            scroll1.grid(row=1,column=2)
            tb1=ttk.Treeview(sub3,columns=(1,2,3,4,5,6,7,8,9,10,11),show='headings',selectmode='browse')
            tb1.grid(row=1,column=1)
            tb1.heading(1,text="Grno")
            tb1.column(1,minwidth=0,width=50,stretch=NO)
            tb1.heading(2,text="Studentname")
            tb1.column(2,minwidth=0,width=120,stretch=NO)
            tb1.heading(3,text="Subject")
            tb1.column(3,minwidth=0,width=50,stretch=NO)
            tb1.heading(4,text="PT1")
            tb1.column(4,minwidth=0,width=50,stretch=NO)
            tb1.heading(5,text="PT2")
            tb1.column(5,minwidth=0,width=50,stretch=NO)
            tb1.heading(6,text="HFYEARLY")
            tb1.column(6,minwidth=0,width=80,stretch=NO)
            tb1.heading(7,text="PT3")
            tb1.column(7,minwidth=0,width=50,stretch=NO)
            tb1.heading(8,text="PT4")
            tb1.column(8,minwidth=0,width=50,stretch=NO)
            tb1.heading(9,text="M1")
            tb1.column(9,minwidth=0,width=50,stretch=NO)
            tb1.heading(10,text="M2")
            tb1.column(10,minwidth=0,width=70,stretch=NO)
            tb1.heading(11,text="FINAL")
            tb1.column(11,minwidth=0,width=70,stretch=NO)
            scroll1.config(command=tb1.yview)
            for i in marks: #appending details(subdetails)
                tb1.insert('','end',values=i)
        def sub4m(): #subject4marks
            execu='select * from subdetails where subject=?'
            ncursor.execute(execu,(subjects[4],))
            marks=ncursor.fetchall()
            sub4=Toplevel()
            sub4.geometry('730x250')
            sub4['bg'] = '#36DAA5'
            sub4.title(subjects[4]+' marks')
            scroll1=ttk.Scrollbar(sub4)
            scroll1.grid(row=1,column=2)
            tb1=ttk.Treeview(sub4,columns=(1,2,3,4,5,6,7,8,9,10,11),show='headings',selectmode='browse')
            tb1.grid(row=1,column=1)
            tb1.heading(1,text="Grno")
            tb1.column(1,minwidth=0,width=50,stretch=NO)
            tb1.heading(2,text="Studentname")
            tb1.column(2,minwidth=0,width=120,stretch=NO)
            tb1.heading(3,text="Subject")
            tb1.column(3,minwidth=0,width=50,stretch=NO)
            tb1.heading(4,text="PT1")
            tb1.column(4,minwidth=0,width=50,stretch=NO)
            tb1.heading(5,text="PT2")
            tb1.column(5,minwidth=0,width=50,stretch=NO)
            tb1.heading(6,text="HFYEARLY")
            tb1.column(6,minwidth=0,width=80,stretch=NO)
            tb1.heading(7,text="PT3")
            tb1.column(7,minwidth=0,width=50,stretch=NO)
            tb1.heading(8,text="PT4")
            tb1.column(8,minwidth=0,width=50,stretch=NO)
            tb1.heading(9,text="M1")
            tb1.column(9,minwidth=0,width=50,stretch=NO)
            tb1.heading(10,text="M2")
            tb1.column(10,minwidth=0,width=70,stretch=NO)
            tb1.heading(11,text="FINAL")
            tb1.column(11,minwidth=0,width=70,stretch=NO)
            scroll1.config(command=tb1.yview)
            for i in marks: #appending details(subdetails)
                tb1.insert('','end',values=i)
        def sub5m(): #subject5 marks
            execu='select * from subdetails where subject=?'
            ncursor.execute(execu,(subjects[5],))
            marks=ncursor.fetchall()
            sub5=Toplevel()
            sub5.geometry('730x250')
            sub5['bg'] = '#36DAA5'
            sub5.title(subjects[5]+' marks')
            scroll1=ttk.Scrollbar(sub5)
            scroll1.grid(row=1,column=2)
            tb1=ttk.Treeview(sub5,columns=(1,2,3,4,5,6,7,8,9,10,11),show='headings',selectmode='browse')
            tb1.grid(row=1,column=1)
            tb1.heading(1,text="Grno")
            tb1.column(1,minwidth=0,width=50,stretch=NO)
            tb1.heading(2,text="Studentname")
            tb1.column(2,minwidth=0,width=120,stretch=NO)
            tb1.heading(3,text="Subject")
            tb1.column(3,minwidth=0,width=50,stretch=NO)
            tb1.heading(4,text="PT1")
            tb1.column(4,minwidth=0,width=50,stretch=NO)
            tb1.heading(5,text="PT2")
            tb1.column(5,minwidth=0,width=50,stretch=NO)
            tb1.heading(6,text="HFYEARLY")
            tb1.column(6,minwidth=0,width=80,stretch=NO)
            tb1.heading(7,text="PT3")
            tb1.column(7,minwidth=0,width=50,stretch=NO)
            tb1.heading(8,text="PT4")
            tb1.column(8,minwidth=0,width=50,stretch=NO)
            tb1.heading(9,text="M1")
            tb1.column(9,minwidth=0,width=50,stretch=NO)
            tb1.heading(10,text="M2")
            tb1.column(10,minwidth=0,width=70,stretch=NO)
            tb1.heading(11,text="FINAL")
            tb1.column(11,minwidth=0,width=70,stretch=NO)
            scroll1.config(command=tb1.yview)
            for i in marks: #appending details(subdetails)
                tb1.insert('','end',values=i)
        def addmarks():#adding marks
            def mrks():
                sel=0
                sel=mr.get() #totalmarks
                marks=mrs.get()
                student=stname.get()
                subject=subname.get()
                exam=exm.get()
                if marks<0:
                    return messagebox.showerror ('Error','Invalid Marks')
                elif marks>sel:
                    return messagebox.showerror('Error','Invalid Marks')
                elif student=='-select-':
                    return messagebox.showerror ('Error','select student')
                elif subject=='-select-':
                    return messagebox.showerror ('Error','select subject')
                elif exam=='-select-':
                    return messagebox.showerror ('Error','select exam')
                elif sel==0:
                    return messagebox.showerror ('Error','Enter Total Marks')
                else:
                    pers=[]
                    execu='select '+exam+' from stdetails where studentname=?'
                    ncursor.execute(execu, (student,))
                    tm=ncursor.fetchall()
                    tm=tm[0]
                    tms=tm[0]
                    pers.append(tms)
                    per=(marks/sel)*100
                    pers.append(per)
                    avg1=sum(pers)/len(pers) #total precentage
                    avg=round(avg1)
                    sql1='select grno from stdetails where studentname=?'
                    ncursor.execute(sql1, (student,))
                    row2=ncursor.fetchall()
                    row2=row2[0]
                    row2=row2[0]#grno
                    
                    sql3='UPDATE subdetails SET '+exam+' = ? WHERE studentname = ?  AND subject = ?' #for subdetails
                    data44=(marks,student,subject)
                    ncursor.execute(sql3,data44)
                    nclass.commit()
                    sql37='UPDATE stdetails SET '+exam+' = ? WHERE studentname = ?' #for stdetails
                    data37=(avg,student)
                    ncursor.execute(sql37,data37)
                    nclass.commit()
                    messagebox.showinfo('Info','Marks Added Successfully')
                    adm.destroy()
                    cprofile.destroy()
                    ClassProfile.classprofile()
            mr=IntVar()#totalmarks
            mrs=IntVar()
            stname=StringVar()
            subname=StringVar()
            exm=StringVar()
            mr.set(20)
            adm=Toplevel()
            adm.geometry('400x300')
            adm.title('Add marks')
            adm['bg'] = '#36DAA5'
            Label(adm,text='Enter Details',font=labelfont,bg='#36DAA5').grid(row=1,column=2)
            Label(adm,text='Select Student',font=labelfont,bg='#36DAA5').grid(row=2,column=1)
            Label(adm,text='Select subject',font=labelfont,bg='#36DAA5').grid(row=3,column=1)
            Label(adm,text='Select exam',font=labelfont,bg='#36DAA5').grid(row=4,column=1)
            stuselect=ttk.Combobox(adm,values=students,state='readonly',textvariable=stname)
            stuselect.grid(row=2,column=2)
            stuselect.current(0)
            subselect=ttk.Combobox(adm,values=subjects,state='readonly',textvariable=subname)
            subselect.grid(row=3,column=2)
            subselect.current(0)
            exselect=ttk.Combobox(adm,values=exams,state='readonly',textvariable=exm)
            exselect.grid(row=4,column=2)
            exselect.current(0)
            Label(adm,text='Enter Marks:',font=labelfont,bg='#36DAA5').grid(row=5,column=1)
            Entry(adm,width=10,textvariable=mrs,font=entryfont).grid(row=5,column=2)#mark entry
            Label(adm,text='marks are out of:',font=labelfont,bg='#36DAA5').grid(row=6,column=1)
            Radiobutton(adm,text='20',variable=mr,value=20,bg='#36DAA5').place(x=30,y=160)
            Radiobutton(adm,text='30',variable=mr,value=30,bg='#36DAA5').place(x=80,y=160)
            Radiobutton(adm,text='70',variable=mr,value=70,bg='#36DAA5').place(x=130,y=160)
            Radiobutton(adm,text='80',variable=mr,value=80,bg='#36DAA5').place(x=180,y=160)
            Button(adm,text='Proceed',command=mrks,font=entryfont,width=15,bg='#567').place(x=90,y=200)
        def update():#for refresh
            cprofile.destroy()
            ClassProfile.classprofile()
        def addstudent():
            def proceed():
                grno=0
                grno=gr.get()
                name=nm.get()
                if grno==0:
                    return messagebox.showerror('Error','Enter Grno.')
                elif name=='':
                    return messagebox.showerror('Error','Enter Student Name')
                else:
                    sql6="""INSERT INTO stdetails
                            (grno,studentname,PT1,PT2,HFYEARLY,PT3,PT4,M1,M2,FINAL) 
                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
                    data = (grno,name,0,0,0,0,0,0,0,0)
                    ncursor.execute(sql6,data)
                    nclass.commit()
                    add.destroy()
                    for i in range(len(sub)):
                                    sq23="""INSERT INTO subdetails
                                            (grno,studentname,subject,PT1,PT2,HFYEARLY,PT3,PT4,M1,M2,FINAL) 
                                            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
                                    data = (grno,name,sub[i],0,0,0,0,0,0,0,0)
                                    ncursor.execute(sq23,data)
                                    nclass.commit()
            gr=IntVar()
            nm=StringVar()
            add=Toplevel()
            add.title('New Student')
            add.geometry('400x200')
            add['bg'] = '#36DAA5'
            Label(add,text='Student Details',font=labelfont,bg='#36DAA5').grid(row=1,column=2)
            Label(add,text='Enter Grno.',font=labelfont,bg='#36DAA5').grid(row=2,column=1)
            Entry(add,width=10,textvariable=gr,font=entryfont).grid(row=2,column=2)
            Label(add,text='Enter Student Name',font=labelfont,bg='#36DAA5').grid(row=3,column=1)
            Entry(add,width=25,textvariable=nm).grid(row=3,column=2)
            Button(add,text='Proceed',command=proceed,font=entryfont,width=15,bg='#567').place(x=100,y=120)
            ####---

        
        ncursor.execute('select * from stdetails')
        row=ncursor.fetchall()#data-stdetails
        rows=len(row)
        ncursor.execute('select * from subdetails')
        staticrow=ncursor.fetchall()
        cprofile=Toplevel() #class-profile-GUI
        cprofile.geometry('1100x720')
        cprofile['bg'] = '#36DAA5'
        cprofile.title('Classprofile-IAS')
        
        Label(cprofile,text='Class:'+clname,font=headlabelfont,bg='#36DAA5').grid(row=1,column=1)
        Label(cprofile,text='No.of students in class:'+str(rows),font=labelfont,bg='#36DAA5').grid(row=2,column=1)
        Button(cprofile,text='Add Student',command=addstudent,font=entryfont,width=15,bg='#567').place(x=500,y=8)
        Button(cprofile,text='Remove Student',command=remove,font=entryfont,width=15,bg='#567').place(x=500,y=37)
        Button(cprofile,text='Add Marks',command=addmarks,font=entryfont,width=15,bg='#567').place(x=650,y=8)
        Button(cprofile,text='Class Performance',command=cperformance,width=15,font=entryfont,bg='#567').place(x=650,y=37)
        Button(cprofile,text='Student Report',command=sreport,font=entryfont,width=15,bg='#567').place(x=800,y=8)
        Button(cprofile,text='Refresh',command=update,font=entryfont,width=15,bg='#567').place(x=800,y=37)
        Label(cprofile,text='Student Details(marks are in %) >>>>>>>',font=entryfont,bg='#36DAA5').grid(row=3,column=1)
        

        #student details
        scroll=ttk.Scrollbar(cprofile)
        scroll.grid(row=4,column=3)
        tb=ttk.Treeview(cprofile,columns=(1,2,3,4,5,6,7,8,9,10),show='headings',selectmode='browse')
        tb.grid(row=4,column=2)
        
        tb.heading(1,text="Grno")
        tb.column(1,minwidth=0,width=50,stretch=NO)
        tb.heading(2,text="Studentname")
        tb.column(2,minwidth=0,width=120,stretch=NO)
        tb.heading(3,text="PT1(%)")
        tb.column(3,minwidth=0,width=50,stretch=NO)
        tb.heading(4,text="PT2(%)")
        tb.column(4,minwidth=0,width=50,stretch=NO)
        tb.heading(5,text="HFYEARLY(%)")
        tb.column(5,minwidth=0,width=80,stretch=NO)
        tb.heading(6,text="PT3(%)")
        tb.column(6,minwidth=0,width=50,stretch=NO)
        tb.heading(7,text="PT4(%)")
        tb.column(7,minwidth=0,width=50,stretch=NO)
        tb.heading(8,text="M1(%)")
        tb.column(8,minwidth=0,width=50,stretch=NO)
        tb.heading(9,text="M2(%)")
        tb.column(9,minwidth=0,width=50,stretch=NO)
        tb.heading(10,text="FINAL(%)")
        tb.column(10,minwidth=0,width=70,stretch=NO)
        scroll.config(command=tb.yview)
        for i in row: #appending details(stdetails)
            tb.insert('','end',values=i)
        Label(cprofile,text='Student Details with Subjects(Individual Marks) >>>',font=entryfont,bg='#36DAA5').grid(row=5,column=1)
        #student details with subjects-individual
        scroll1=ttk.Scrollbar(cprofile)
        scroll1.grid(row=6,column=3)
        tb1=ttk.Treeview(cprofile,columns=(1,2,3,4,5,6,7,8,9,10,11),show='headings',selectmode='browse')
        tb1.grid(row=6,column=2)
        
        tb1.heading(1,text="Grno")
        tb1.column(1,minwidth=0,width=50,stretch=NO)
        tb1.heading(2,text="Studentname")
        tb1.column(2,minwidth=0,width=120,stretch=NO)
        tb1.heading(3,text="Subject")
        tb1.column(3,minwidth=0,width=50,stretch=NO)
        tb1.heading(4,text="PT1")
        tb1.column(4,minwidth=0,width=50,stretch=NO)
        tb1.heading(5,text="PT2")
        tb1.column(5,minwidth=0,width=50,stretch=NO)
        tb1.heading(6,text="HFYEARLY")
        tb1.column(6,minwidth=0,width=80,stretch=NO)
        tb1.heading(7,text="PT3")
        tb1.column(7,minwidth=0,width=50,stretch=NO)
        tb1.heading(8,text="PT4")
        tb1.column(8,minwidth=0,width=50,stretch=NO)
        tb1.heading(9,text="M1")
        tb1.column(9,minwidth=0,width=50,stretch=NO)
        tb1.heading(10,text="M2")
        tb1.column(10,minwidth=0,width=70,stretch=NO)
        tb1.heading(11,text="FINAL")
        tb1.column(11,minwidth=0,width=70,stretch=NO)
        scroll1.config(command=tb1.yview)
        for i in staticrow: #appending details(subdetails)
            tb1.insert('','end',values=i)
        Button(cprofile,text=subjects[1]+' Marks',command=sub1m,font=entryfont,width=15,bg='#567').place(x=120,y=500)
        Button(cprofile,text=subjects[2]+' Marks',command=sub2m,font=entryfont,width=15,bg='#567').place(x=120,y=530)
        Button(cprofile,text=subjects[3]+' Marks',command=sub3m,font=entryfont,width=15,bg='#567').place(x=120,y=560)
        Button(cprofile,text=subjects[4]+' Marks',command=sub4m,font=entryfont,width=15,bg='#567').place(x=120,y=590)
        Button(cprofile,text=subjects[5]+' Marks',command=sub5m,font=entryfont,width=15,bg='#567').place(x=120,y=620)
        Button(cprofile,text='Download Marksheet',command=dmarksheet,font=entryfont,width=15,bg='#567').place(x=650,y=600)
        Button(cprofile,text='Upload Marks',command=mrksheetupload,font=entryfont,width=15,bg='#567').place(x=650,y=630)
        
            
home=Tk()
home['bg'] = 'yellow'
home.geometry('1080x720')
home.title('Instructor Aid System')
home.resizable(0, 0)
img=Image.open('IAS3.jpeg')
img = ImageTk.PhotoImage(img, master=home)
Label(home,image=img).pack()
Label(home,text='---HOME PAGE---',font='Verdana 15 bold',width=100,bg='Skyblue',fg='Black').place(relx=.5,anchor= N)
Button(home,text='SignIn/Create Account',font='Verdana 13 bold',command=Homepage.sign,width=25,bg='#567',fg='White').place(relx=.5, rely=.4,anchor=CENTER)
Button(home,text='Subject Projection',font='Verdana 13 bold',command=Homepage.SubjectProjection.subpro,width=25,bg='#567',fg='White').place(relx=.5, rely=.5,anchor=CENTER)
Button(home,text='Percentage Calculator',font='Verdana 13 bold',command=Homepage.Calculator.calculator,width=25,bg='#567',fg='White').place(relx=.5, rely=.6,anchor=CENTER)
home.mainloop()
        
        
        
    