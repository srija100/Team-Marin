data1=data2=data3=data4=data5=""
with open('importtkinter.py') as fp:
    data1=fp.read()
with open('homepage.py') as fp:
    data2=fp.read()
with open('subjectprojection.py') as fp:
    data3=fp.read()        
with open('calculator.py') as fp:
    data4=fp.read()
with open('tkinterhome.py') as fp:
    data5=fp.read()        
data1+="\n"
data1+=data2 
data1+="\n"
data1+=data3
data1+="\n"
data1+=data4
data1+="\n"
data1+=data5
with open ('totalcode.py','w') as fp:
    fp.write(data1)