import tkinter 
from tkinter import *
from tkinter import ttk 
from PIL import Image,ImageTk
import sqlite3
from sqlite3 import Error
from tkinter import messagebox
import matplotlib.pyplot as plt

from homepage import *

class Dashboard:
     def accwindow():#mainprofile
        global s
        def accwindow1():
            dash.destroy()
            accwindow()
        Class.newclass()
        def signout():
                dash.destroy()
        
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
        Class.selectclass()
        dash=Toplevel()
        dash.geometry('960x720')
        dash.title('HomePage-IAS')
        dash['bg'] = '#49A'
        s=StringVar()
        Button(dash,text='SignOut',command=signout).grid(row=1,column=3)
        Label(dash,text='Your DashBoard',font='Helvetica 12 bold',bg='#49A').grid(row=1,column=2)
        Label(dash,text='Your Name: '+finaln,bg='#49A').grid(row=2,column=1)
        Label(dash,text='Email: '+email,bg='#49A').grid(row=3,column=1)
        Label(dash,text='No. of classes:'+co,bg='#49A').grid(row=4,column=1)
        Button(dash,text='Create New Class',command=Class.newclass).grid(row=5,column=1)
        Label(dash,text='Select Class>>>>',bg='#49A').grid(row=6,column=1)
        classselect=ttk.Combobox(dash,values=classes,state='readonly',textvariable=s)
        classselect.grid(row=6,column=2)
        if count!=0:
            classselect.current(0)
        Button(dash,text='Proceed',command=classprofile).grid(row=7,column=3)
        Button(dash,text='refresh',command=accwindow1).grid(row=1,column=4)
class Class:
        def selectclass():
            sql3='select classname from clsaccounts where email=?'
            cursor.execute(sql3, (email,))
            row2=cursor.fetchall()
            count=len(row2)
            for i in range(len(row2)):
                tp=row2[i]
                tp1=tp[0]
                Dashboard.classes.append(tp1)
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
            newc.geometry('400x400')
            newc.title('create new class')
            cname=StringVar()
            s1=StringVar()
            s2=StringVar()
            s3=StringVar()
            s4=StringVar()
            s5=StringVar()
            Label(newc,text='Enter Details',font='Helvetica 12 bold').grid(row=1,column=3)
            Label(newc,text='Enter class name:').grid(row=2,column=1)
            Entry(newc,width=11,textvariable=cname).grid(row=2,column=2)
            Label(newc,text='Enter Subject details:').grid(row=3,column=1)
            Label(newc,text='Subject1').grid(row=4,column=1)
            Entry(newc,width=15,textvariable=s1).grid(row=4,column=2)
            Label(newc,text='Subject2').grid(row=5,column=1)
            Entry(newc,width=15,textvariable=s2).grid(row=5,column=2)
            Label(newc,text='Subject3').grid(row=6,column=1)
            Entry(newc,width=15,textvariable=s3).grid(row=6,column=2)
            Label(newc,text='Subject4').grid(row=7,column=1)
            Entry(newc,width=15,textvariable=s4).grid(row=7,column=2)
            Label(newc,text='Subject5').grid(row=8,column=1)
            Entry(newc,width=15,textvariable=s5).grid(row=8,column=2)
            Button(newc,text='OK',command=ok).grid(row=8,column=3)
        
        
        