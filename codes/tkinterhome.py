#  import homepage.py
# import subjectprojection.py
# import calculator.py
# import importtkinter.py
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