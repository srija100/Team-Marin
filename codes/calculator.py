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
          
