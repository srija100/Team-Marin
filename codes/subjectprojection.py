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
        