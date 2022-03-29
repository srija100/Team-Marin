# import subjectprojection
# import caluclator
# import importtkinter
# import tkinterhome
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
                messagebox.showinfo('Result','Sign In Successfully')
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
    
