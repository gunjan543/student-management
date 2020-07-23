from tkinter import *
import time
import random
import pymysql
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Treeview


root=Tk()
root.title('Student Management System')
root.config(bg='#ecf8f8')
root.geometry('1174x700+250+150')
root.iconbitmap('icon.ico')
root.resizable(False,False)
#_________________________________functions___________________________________________
colors=['#9db4c0','#5c6b73','#253237']#'#9c89b8','#f0a6ca','#efc3e6','#f0e6ef','#b8bedd'
def IntroColor():
    fg=random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2,IntroColor)

def IntroLabelTick():
    global count,text
    if count>=len(ss):
        count=-1
        text=''
        SliderLabel.config(text=text)
    else:
        text=text+ss[count]
        SliderLabel.config(text=text)
    count+=1
    SliderLabel.after(300,IntroLabelTick)

def tick():
    time_string=time.strftime("%H:%M:%S")
    date_string=time.strftime("%d/%m/%Y")
    clock.config(text="Date: "+date_string+'\nTime: '+time_string)
    clock.after(200,tick)

def ConnectDatabase():
    def submitdb():

        global con, mycursor
        host=hostval.get()
        user=userval.get()
        password=passval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','Data is incorrect,please try again ')
            return

    top=Toplevel()
    top.grab_set()
    top.geometry('470x250+800+300')
    top.iconbitmap('icon.ico')
    top.resizable(False,False)
    top.config(bg='#ecf8f8')

    hostval=StringVar()
    userval=StringVar()
    passval=StringVar()

    idLabel1=Label(top,text='Host Id:',font=('Courier',15,'bold'),width=12,anchor='w',bg='#ecf8f8',fg='#253237')
    idLabel2=Label(top,text='Username: ',font=('Courier',15,'bold'),width=12,anchor='w',bg='#ecf8f8',fg='#253237')
    idLabel3=Label(top,text='Password: ',font=('Courier',15,'bold'),width=12,anchor='w',bg='#ecf8f8',fg='#253237')
    idLabel1.place(x=10,y=10)
    idLabel2.place(x=10,y=60)
    idLabel3.place(x=10,y=110)

    entryLabel1 = Entry(top,font = ('Courier',15,'bold'),width = 28,textvariable=hostval)
    entryLabel2 = Entry(top,font = ('Courier',15,'bold'),width = 28,textvariable=userval)
    entryLabel3 = Entry(top,font = ('Courier',15,'bold'),width = 28,textvariable=passval)

    entryLabel1.place(x=120,y=10)
    entryLabel2.place(x=120,y=60)
    entryLabel3.place(x=120,y=110)

    submit = Button(top,text = "Submit",font = ('Courier',15,'bold'),width = 15, activebackground='#3a506b',activeforeground='#b8f2e6',fg='#253237',command=submitdb)
    submit.place(x = 150,y = 180)

    top.mainloop()

def addstudent():
    addroot=Toplevel(main=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+270+300')
    addroot.title('Student Management System')
    addroot.iconbitmap('icon.ico')
    addroot.resizable(False,False)
    addroot.config(bg='#ecf8f8')

    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    Emailval=StringVar()
    Addressval=StringVar()
    Genderval=StringVar()
    DobVal=StringVar()

    stuLab1=Label(addroot,text="Student ID: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab2=Label(addroot,text="Student Name: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab3=Label(addroot,text="Mobile Number: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab4=Label(addroot,text="Email ID: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab5=Label(addroot,text="Address: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab6=Label(addroot,text="Gender: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab7=Label(addroot,text="Date Of Birth: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')

    stuLab1.place(x=10,y=10)
    stuLab2.place(x=10,y=70)
    stuLab3.place(x=10,y=130)
    stuLab4.place(x=10,y=190)
    stuLab5.place(x=10,y=250)
    stuLab6.place(x=10,y=310)
    stuLab7.place(x=10,y=370)

    stuEntry1=Entry(addroot,font = ('Courier',15,'bold'),width = 23,textvariable=idval)
    stuEntry2=Entry(addroot,font = ('Courier',15,'bold'),width = 23,textvariable=nameval)
    stuEntry3=Entry(addroot,font = ('Courier',15,'bold'),width = 23,textvariable=mobileval)
    stuEntry4=Entry(addroot,font = ('Courier',15,'bold'),width = 23,textvariable=Emailval)
    stuEntry5=Entry(addroot,font = ('Courier',15,'bold'),width = 23,textvariable=Addressval)
    stuEntry6=Entry(addroot,font = ('Courier',15,'bold'),width = 23,textvariable=Genderval)
    stuEntry7=Entry(addroot,font = ('Courier',15,'bold'),width = 23,textvariable=DobVal)

    stuEntry1.place(x=152,y=10)
    stuEntry2.place(x=152,y=70)
    stuEntry3.place(x=152,y=130)
    stuEntry4.place(x=152,y=190)
    stuEntry5.place(x=152,y=250)
    stuEntry6.place(x=152,y=310)
    stuEntry7.place(x=152,y=370)

    stuSubmit = Button(addroot,text = "Add Student",font = ('Courier',13,'bold'),width = 15, activebackground='#3a506b',activeforeground='#b8f2e6',fg='#253237',command=submitAdd)
    stuSubmit.place(x = 150,y = 420)

    addroot.mainloop()

def searchstudent():
    searchroot=Toplevel(main=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('540x540+270+300')
    searchroot.title('Student Management System')
    searchroot.iconbitmap('icon.ico')
    searchroot.resizable(False,False)
    searchroot.config(bg='#ecf8f8')

    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    Emailval=StringVar()
    Addressval=StringVar()
    Genderval=StringVar()
    DobVal=StringVar()
    DateVal=StringVar()

    stuLab1=Label(searchroot,text="Student ID: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab2=Label(searchroot,text="Student Name: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab3=Label(searchroot,text="Mobile Number: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab4=Label(searchroot,text="Email ID: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab5=Label(searchroot,text="Address: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab6=Label(searchroot,text="Gender: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab7=Label(searchroot,text="Date Of Birth: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab8=Label(searchroot,text="Date: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')


    stuLab1.place(x=10,y=10)
    stuLab2.place(x=10,y=70)
    stuLab3.place(x=10,y=130)
    stuLab4.place(x=10,y=190)
    stuLab5.place(x=10,y=250)
    stuLab6.place(x=10,y=310)
    stuLab7.place(x=10,y=370)
    stuLab8.place(x=10,y=430)

    stuEntry1=Entry(searchroot,font = ('Courier',15,'bold'),width = 23,textvariable=idval)
    stuEntry2=Entry(searchroot,font = ('Courier',15,'bold'),width = 23,textvariable=nameval)
    stuEntry3=Entry(searchroot,font = ('Courier',15,'bold'),width = 23,textvariable=mobileval)
    stuEntry4=Entry(searchroot,font = ('Courier',15,'bold'),width = 23,textvariable=Emailval)
    stuEntry5=Entry(searchroot,font = ('Courier',15,'bold'),width = 23,textvariable=Addressval)
    stuEntry6=Entry(searchroot,font = ('Courier',15,'bold'),width = 23,textvariable=Genderval)
    stuEntry7=Entry(searchroot,font = ('Courier',15,'bold'),width = 23,textvariable=DobVal)
    stuEntry8=Entry(searchroot,font = ('Courier',15,'bold'),width = 23,textvariable=DateVal)

    stuEntry1.place(x=152,y=10)
    stuEntry2.place(x=152,y=70)
    stuEntry3.place(x=152,y=130)
    stuEntry4.place(x=152,y=190)
    stuEntry5.place(x=152,y=250)
    stuEntry6.place(x=152,y=310)
    stuEntry7.place(x=152,y=370)
    stuEntry8.place(x=152,y=430)


    stuSubmit = Button(searchroot,text = "Search Student",font = ('Courier',13,'bold'),width = 15, activebackground='#3a506b',activeforeground='#b8f2e6',fg='#253237',command=submitAdd)
    stuSubmit.place(x =180,y = 480)

    searchroot.mainloop()
def deletestudent():
    pass
def updatestudent():
    updateroot=Toplevel(main=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('535x590+255+250')
    updateroot.title('Student Management System')
    updateroot.iconbitmap('icon.ico')
    updateroot.resizable(False,False)
    updateroot.config(bg='#ecf8f8')

    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    Emailval=StringVar()
    Addressval=StringVar()
    Genderval=StringVar()
    DobVal=StringVar()
    DateVal=StringVar()
    TimeVal=StringVar()

    stuLab1=Label(updateroot,text="Student ID: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab2=Label(updateroot,text="Student Name: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab3=Label(updateroot,text="Mobile Number: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab4=Label(updateroot,text="Email ID: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab5=Label(updateroot,text="Address: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab6=Label(updateroot,text="Gender: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab7=Label(updateroot,text="Date Of Birth: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab8=Label(updateroot,text="Date: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
    stuLab9=Label(updateroot,text="Time: ",anchor='w',width=25,font = ('Courier',13,'bold'),bg='#ecf8f8',fg='#253237')
     

    stuLab1.place(x=10,y=10)
    stuLab2.place(x=10,y=70)
    stuLab3.place(x=10,y=130)
    stuLab4.place(x=10,y=190)
    stuLab5.place(x=10,y=250)
    stuLab6.place(x=10,y=310)
    stuLab7.place(x=10,y=370)
    stuLab8.place(x=10,y=430)
    stuLab9.place(x=10,y=490)

    stuEntry1=Entry(updateroot,font = ('Courier',15,'bold'),width = 23,textvariable=idval)
    stuEntry2=Entry(updateroot,font = ('Courier',15,'bold'),width = 23,textvariable=nameval)
    stuEntry3=Entry(updateroot,font = ('Courier',15,'bold'),width = 23,textvariable=mobileval)
    stuEntry4=Entry(updateroot,font = ('Courier',15,'bold'),width = 23,textvariable=Emailval)
    stuEntry5=Entry(updateroot,font = ('Courier',15,'bold'),width = 23,textvariable=Addressval)
    stuEntry6=Entry(updateroot,font = ('Courier',15,'bold'),width = 23,textvariable=Genderval)
    stuEntry7=Entry(updateroot,font = ('Courier',15,'bold'),width = 23,textvariable=DobVal)
    stuEntry8=Entry(updateroot,font = ('Courier',15,'bold'),width = 23,textvariable=DateVal)
    stuEntry9=Entry(updateroot,font = ('Courier',15,'bold'),width = 23,textvariable=TimeVal)

    stuEntry1.place(x=152,y=10)
    stuEntry2.place(x=152,y=70)
    stuEntry3.place(x=152,y=130)
    stuEntry4.place(x=152,y=190)
    stuEntry5.place(x=152,y=250)
    stuEntry6.place(x=152,y=310)
    stuEntry7.place(x=152,y=370)
    stuEntry8.place(x=152,y=430)
    stuEntry9.place(x=152,y=490)


    stuSubmit = Button(updateroot,text = "Update Student",font = ('Courier',13,'bold'),width = 15, activebackground='#3a506b',activeforeground='#b8f2e6',fg='#253237',command=submitAdd)
    stuSubmit.place(x =180,y =550)

    updateroot.mainloop()
def showstudent():
    pass
def exportstudent():
    pass
def exitstudent():
    res = messagebox.askyesno('Notification','Do you want to exit')
    if(res==True):
        root.destroy()
def submitAdd():
    pass

#___________________________________#GUI#_____________________________________________

#__________________________________Frames__________________________________________
DataEntryFrame=Frame(root,bg='#ecf8f8',borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)

AddStu=Button(DataEntryFrame,text='Add Student',width=25,font = ('Courier',13,'bold'),bd=3,activebackground='#3a506b',activeforeground='#b8f2e6',bg='#ecf8f8',fg='#253237',command=addstudent)
AddStu.pack(side=TOP,expand=True)
SearchStu=Button(DataEntryFrame,text='Search Student',width=25,font = ('Courier',13,'bold'),bd=3,activebackground='#3a506b',activeforeground='#b8f2e6',bg='#ecf8f8',fg='#253237',command=searchstudent)
SearchStu.pack(side=TOP,expand=True)
DeleteStu=Button(DataEntryFrame,text='Delete Student',width=25,font = ('Courier',13,'bold'),bd=3,activebackground='#3a506b',activeforeground='#b8f2e6',bg='#ecf8f8',fg='#253237',command=deletestudent)
DeleteStu.pack(side=TOP,expand=True)
UpdateStu=Button(DataEntryFrame,text='Update Student',width=25,font = ('Courier',13,'bold'),bd=3,activebackground='#3a506b',activeforeground='#b8f2e6',bg='#ecf8f8',fg='#253237',command=updatestudent)
UpdateStu.pack(side=TOP,expand=True)
ShowAll=Button(DataEntryFrame,text='Show All',width=25,font = ('Courier',13,'bold'),bd=3,activebackground='#3a506b',activeforeground='#b8f2e6',bg='#ecf8f8',fg='#253237',command=showstudent)
ShowAll.pack(side=TOP,expand=True)
ExportData=Button(DataEntryFrame,text='Export Data',width=25,font = ('Courier',13,'bold'),bd=3,activebackground='#3a506b',activeforeground='#b8f2e6',bg='#ecf8f8',fg='#253237',command=exportstudent)
ExportData.pack(side=TOP,expand=True)
Exit=Button(DataEntryFrame,text='Exit',width=25,font = ('Courier',13,'bold'),bd=3,activebackground='#3a506b',activeforeground='#b8f2e6',bg='#ecf8f8',fg='#253237',command=exitstudent)
Exit.pack(side=TOP,expand=True)
#____________________________________________________________________________________
ShowDataFrame=Frame(root,bg='#ecf8f8',borderwidth=5,relief=GROOVE)
ShowDataFrame.place(x=550,y=80,width=615,height=600)

style=ttk.Style()
style.configure('Treeview.Heading',font=('Courier',13,'bold'),foreground='#253237')
style.configure('Treeview',font=('Courier',11,'bold'),foreground='#253237')


scrollx=Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scrolly=Scrollbar(ShowDataFrame,orient=VERTICAL)

studenttable=Treeview(ShowDataFrame,columns=('Id','Name','Mobile No.','Email','Address','Gender','D.O.B','Added Date','Added Time'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)

scrollx.pack(side=BOTTOM,fill=X)
scrolly.pack(side=RIGHT,fill=Y)
scrollx.config(command=studenttable.xview)
scrolly.config(command=studenttable.yview)

studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No.',text='Mobile No.')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')

studenttable['show']='headings'

studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No.',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)

studenttable.pack(fill=BOTH,expand=1)

#___________________________________Slider__________________________________________
ss='Welcome to Student Management System'
count=0
text=''
SliderLabel=Label(root,text=ss,font=('Courier',18,'italic bold'),borderwidth=5,width=40,bg='#ecf8f8',height=2)
SliderLabel.place(x=260,y=10)
IntroLabelTick()
IntroColor()
#__________________________________Clock_____________________________________________
clock=Label(root,font=('Courier',14,'bold'),borderwidth=5,bg='#ecf8f8',fg='#253237',height=2)
clock.place(x=10,y=10)
tick()

#_________________________________Connect to db________________________________________
connectbutton=Button(root,text='Connect to database',width=22,font=('Courier',13,'bold'),bd=5,command = ConnectDatabase, activebackground='#3a506b',activeforeground='#b8f2e6',bg='#ecf8f8',fg='#253237',height=2)
connectbutton.place(x=930,y=10)

root.mainloop()
