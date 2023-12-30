'''This project is designed to  list animes by their Anime names, Genre,Date of release, No. of episodes
and Sites available to watch the desired anime by choice
You can enter new data 
Delete some old data and many other funcions all of this is done using SQL database in collaboration with Python'''
import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
import mysql.connector as sq

def create():
    mydb = sq.connect(host="localhost",user="root",password="root")
    mycursor = mydb.cursor()
    sql = "Create database company_database"
    mycursor.execute(sql)
    mycursor.execute("Use company_database")
    mydb.commit()
    mycursor.execute("Create table Employee(Employee_Name VARCHAR(500), Position VARCHAR(100), Date_of_joining DATE, Emp_id INTEGER,Email VARCHAR(500), Phone_no VARCHAR(500))")
    mydb.commit()
def check_database_existence():
    try:
        mydb = sq.connect(host="localhost",user="root",password="root",database="company_database")
    except sq.Error as e:
        if e.errno == 1049:  # MySQL error code for "Unknown database"
            create()
        else:
            print(f"Error: {e}")
check_database_existence()

def recreate_root():
    global root
    # Add any initialization code for the root window here
    root=tk.Tk()
    root.geometry('660x350')
    root.configure(bg='teal')
    root.title('Option Page')
    lab3=tk.Label(root, text="WELCOME TO COMPANY DATABASE",font=('Arial',16,'bold'),bg='teal')
    lab6=tk.Label(root, text="Made By: Drona Srivastava",font=('Arial',16,'bold'),bg='teal')
    lab3.place(x=150,y=20)  
    lab6.place(x=195,y=50)  

    lin1=tk.Label(root,text="1.Insert new data ",font=('Arial',14),bg='teal')
    lin2=tk.Label(root,text="2.Update the table",font=('Arial',14),bg='teal')
    lin3=tk.Label(root,text="3.Delete the record from the table",font=('Arial',14),bg='teal')
    lin4=tk.Label(root,text="4.Search a record from the table",font=('Arial',14),bg='teal')
    lin5=tk.Label(root,text="5.Display the table",font=('Arial',14),bg='teal')
    lin6=tk.Label(root,text="6.Quit",font=('Arial',14),bg='teal')

    lin1.place(x=10,y=80)
    lin2.place(x=10,y=110)
    lin3.place(x=10,y=140)
    lin4.place(x=10,y=170)
    lin5.place(x=10,y=200)
    lin6.place(x=10,y=230)

    ch=StringVar()
    
    lab1=tk.Label(root,text="Which function do you want to apply:",font=('Arial',14),bg='teal')
    lab1.place(x=10,y=260)

    en1=tk.Entry(root, textvariable=ch, font=('Arial',14))
    en1.place(x=325,y=263)

    def on_closing():
            if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
                root.destroy()
            else:
                pass 
    def choicefunc():
        choice=ch.get()
        if choice=='1':  # To insert new data
            insert()        
        #To update
        elif choice=='2':
            update()
        #To delete a record
        elif choice=='3':
            delete()
        #To search a record
        elif choice=='4':
            search()
        #To Display the data
        elif choice=='5':
            display()   
        else:
            on_closing()

    btn1=tk.Button(root,text='Enter',font=('Arial',14),bg='teal',command=choicefunc)
    btn1.place(x=555,y=255)
    root.mainloop()
    #Recreating the option window

def insert():
# This part of code is to insert record
    root.destroy()  # Closing main tk page
    insertk=tk.Tk()  # Opening a tk page for insert option
    insertk.geometry('750x430')
    insertk.configure(bg='teal')
    insertk.title('Insert Record')
    
    # Introducing labels for this option
    lab0=tk.Label(insertk,text='Fill out the below information',bg='teal',font=('Arial',18,'bold'))
    lab1=tk.Label(insertk,text="Name of the Employee :",bg='teal',font=('Arial',14))
    lab2=tk.Label(insertk,text="Position of Employee:",bg='teal',font=('Aral',14))
    lab3=tk.Label(insertk,text="Date of Joining of the Employee (in YYYY-MM-DD format):",bg='teal',font=('Aral',14))
    lab4=tk.Label(insertk,text="Employee Code:",bg='teal',font=('Aral',14))
    lab5=tk.Label(insertk,text="Employee's email:",bg='teal',font=('Aral',14))
    lab6=tk.Label(insertk,text="Employee's phone no:",bg='teal',font=('Aral',14))

    # Placing the labels
    lab0.place(x=250,y=20)
    lab1.place(x=10,y=60)
    lab2.place(x=10,y=100)
    lab3.place(x=10,y=140)
    lab4.place(x=10,y=180)
    lab5.place(x=10,y=220)
    lab6.place(x=10,y=260)

    # initializing variable to read entry box data
    nm=StringVar()
    po=StringVar()
    doj=StringVar()
    code=StringVar()
    em=StringVar()
    ph=StringVar()

    # Producing Entry boxes
    en1=tk.Entry(insertk,textvariable=nm,font=('Arial',14))
    en2=tk.Entry(insertk,textvariable=po,font=('Arial',14))
    en3=tk.Entry(insertk,textvariable=doj,font=('Arial',14))
    en4=tk.Entry(insertk,textvariable=code,font=('Arial',14))
    en5=tk.Entry(insertk,textvariable=em,font=('Arial',14))
    en6=tk.Entry(insertk,textvariable=ph,font=('Arial',14))
    
    # Placing the entry boxes
    en1.place(x=225,y=62)
    en2.place(x=205,y=102)
    en3.place(x=510,y=142)
    en4.place(x=160,y=182)
    en5.place(x=175,y=222)
    en6.place(x=205,y=262)

    # Button functionality [ logic for the insert option ]
    def insertin():
        Name=nm.get()
        Postion=po.get()
        DOJ=doj.get()
        Emp_code=code.get()
        Email=em.get()
        Phone=ph.get()

        mydb = sq.connect(host="localhost",user="root",password="root",database="company_database")
        mycursor = mydb.cursor()
        sql = "INSERT INTO Employee ( Employee_Name, Position, Date_of_joining, Emp_id, Email,Phone_no) VALUES (%s,%s, %s,%s,%s,%s)"
        val = (Name,Postion,DOJ,Emp_code,Email,Phone)
        mycursor.execute(sql, val)
        mydb.commit()
        
        added=tk.Label(insertk,text='Record Inserted',font=('Arial',24),bg='teal')
        added.place(x=300,y=360)
        
        nm.set('')
        po.set('')
        doj.set('')
        code.set('')
        em.set('')
        ph.set('')    

    # Introducing button with command
    btin=tk.Button(insertk,text='Enter',font=('Arial',18),command=insertin,bg='teal')
    btin.place(x=360,y=310)

    def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            insertk.destroy()
            recreate_root()
        else:
            pass 
    insertk.protocol('WM_DELETE_WINDOW',on_closing)
    insertk.mainloop()  # Closing tk page for insert option

def update():
#This code is to update the Anime list
    root.destroy()
    updatetk=tk.Tk()
    updatetk.geometry('700x465')
    updatetk.configure(bg='teal')
    updatetk.title('Update Record')
    
    lab0=tk.Label(updatetk,text='Update Record',font=('Arial',18,'bold'),bg='teal')
    lab1=tk.Label(updatetk,text='--> 1. Employee name ',font=('Arial',14),bg='teal')
    lab2=tk.Label(updatetk,text='--> 2. Position',font=('Arial',14),bg='teal')
    lab3=tk.Label(updatetk,text='--> 3. Date of Joining',font=('Arial',14),bg='teal')
    lab4=tk.Label(updatetk,text='--> 4. Employee Id',font=('Arial',14),bg='teal')
    lab5=tk.Label(updatetk,text='--> 5. Email',font=('Arial',14),bg='teal')
    lab9=tk.Label(updatetk,text='--> 6. Phone Number',font=('Arial',14),bg='teal')
    lab6=tk.Label(updatetk,text="Employee name whose record you want to update:",font=('Arial',14),bg='teal')
    lab7=tk.Label(updatetk,text="Record you want to update:",font=('Arial',14),bg='teal')
    lab8=tk.Label(updatetk,text="Enter the change:",font=('Arial',14),bg='teal')

    lab0.place(x=300,y=20)
    lab6.place(x=10,y=70)
    lab1.place(x=10,y=100)
    lab2.place(x=10,y=130)
    lab3.place(x=10,y=160)
    lab4.place(x=10,y=190)
    lab5.place(x=10,y=220)
    lab9.place(x=10,y=250)
    lab7.place(x=10,y=280)
    lab8.place(x=10,y=310)

    upe=StringVar()
    fi=StringVar()
    fich=StringVar()

    en1=tk.Entry(updatetk,textvariable=upe,font=('Arial',14)) 
    en2=tk.Entry(updatetk,textvariable=fi,font=('Arial',14)) 
    en3=tk.Entry(updatetk,textvariable=fich,font=('Arial',14)) 

    en1.place(x=440,y=72)
    en2.place(x=250,y=282)
    en3.place(x=165,y=312)
    
    def updateit():
        up=upe.get()
        fields=fi.get()
        fieldch=fich.get()
        if fields=='1':
            field='Employee_Name'
        elif fields=='2':
            field='Position'
        elif fields=='3':
            field='Date_of_joining'
        elif fields=='4':
            field='Email'
        elif fields=='5':
            field='Phone_no'
        mydb= sq.connect(host="localhost",user="root",passwd="root",database="company_database")
        cursor=mydb.cursor()
        update="UPDATE employee set {} = '{}' WHERE Employee_Name like '{}'".format(field,fieldch,up)
        cursor.execute(update)
        mydb.commit()
        lab0=tk.Label(updatetk,text="Record Updated",font=('Arial',24),bg='teal')
        lab0.place(x=250,y=410)
        upe.set('')
        fi.set('')
        fich.set('')

    bt1=tk.Button(updatetk,text='Update',font=('Arial',18),bg='teal',command=updateit)
    bt1.place(x=300,y=350)

    def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            updatetk.destroy()
            recreate_root()
        else:
            pass 
    updatetk.protocol('WM_DELETE_WINDOW',on_closing)
    updatetk.mainloop()
def delete():
# This code is the delete a record from the anime list
    root.destroy()
    deletetk=tk.Tk()        
    deletetk.geometry('900x250')
    deletetk.configure(bg='teal')
    deletetk.title('Delete Record')

    lab0=tk.Label(deletetk,text="Delete Record",font=('Arial',18,'bold'),bg='teal')
    lab0.place(x=400,y=20)
    lab1=tk.Label(deletetk,text="Enter the Employee name whose data you want to delete:",font=('Arial',14),bg='teal')
    lab1.place(x=20,y=70)

    de=StringVar()

    en1=tk.Entry(deletetk,textvariable=de,font=('Arial',14))
    en1.place(x=525,y=72)
    
    def deleteit():
        dele=de.get()
        c=sq.connect(host="localhost",user="root",passwd="root",database="company_database")
        cursor=c.cursor()
        sql = "DELETE FROM employee WHERE Employee_Name like '%{}%'".format(dele)
        cursor.execute(sql)
        c.commit()
        lab2=tk.Label(deletetk,text="Record Deleted",font=('Arial',24,'bold'),bg='teal')
        lab2.place(x=360,y=170)
        de.set('')

    btn1=tk.Button(text='Delete',font=('Arial',18),bg='teal',command=deleteit)
    btn1.place(x=430,y=120)
    def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            deletetk.destroy()
            recreate_root()
        else:
            pass 
    deletetk.protocol('WM_DELETE_WINDOW',on_closing)
    deletetk.mainloop()

def search():
#This code is to search an anime from the list
    root.destroy()
    searchtk=tk.Tk()
    searchtk.geometry('425x250')
    searchtk.title('Search Record')
    searchtk.configure(bg='teal')
    
    lab1=tk.Label(searchtk,text="Employee Name:",font=('Arial',14),bg='teal')
    lab1.place(x=10,y=60)
    lab2=tk.Label(searchtk,text="Search Record",font=('Arial',18,'bold'),bg='teal')
    lab2.place(x=120,y=20)

    se=StringVar()

    en1=tk.Entry(searchtk,textvariable=se,font=('Arial',14))
    en1.place(x=170,y=60)

    def searchit():
        try:
            pat = se.get()
            mydb = sq.connect(host='localhost', user='root', password='root', database='company_database')
            cursor = mydb.cursor()
            q = "SELECT * FROM Employee WHERE Employee_Name LIKE '%{}%'".format(pat)
            cursor.execute(q)
            result = cursor.fetchall()

            if result:
                lab2 = tk.Label(searchtk, text='Record is available', font=('Arial', 18), bg='teal')
                lab2.place(x=100, y=150)
            else:
                lab2 = tk.Label(searchtk, text='Record is not available', font=('Arial', 18), bg='teal')
                lab2.place(x=100, y=150)
        except Exception as e:
            print(f"Error: {e}")

            
    btn1=tk.Button(searchtk,text='Search',command=searchit,font=('Arial',14),bg='teal')
    btn1.place(x=180,y=100)

    def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            searchtk.destroy()
            recreate_root()
        else:
            pass 
    searchtk.protocol('WM_DELETE_WINDOW',on_closing)
    searchtk.mainloop()

def display():
    # This code is to display the whole anime list
    root.destroy()
    displaytk = tk.Tk()
    displaytk.configure(bg='teal')
    displaytk.geometry('1000x600')
    displaytk.title('Display Record')

    mydb= sq.connect(host="localhost", user="root", password="root", database="company_database")
    cursor = mydb.cursor()
    sql = "SELECT * FROM employee ORDER BY Employee_Name"
    cursor.execute(sql)
    myresult = cursor.fetchall()
    lab1=tk.Label(displaytk,text='Displaying Records',font=('Arial',18,'bold'),bg='teal')
    lab1.place(x=415,y=20)
    # Display header labels
    header_labels = ['Employee Name', 'Position', 'Date of Joining', 'Employee Id', 'Email', 'Phone Number']
    for i, header in enumerate(header_labels):
        tk.Label(displaytk, text=f'{i + 1}. {header}', font=('Arial', 16), bg='teal').place(x=10, y=60 + i * 30)

    # Display employee records
    for i, record in enumerate(myresult):
        record_text = ', '.join(map(str, record))
        tk.Label(displaytk, text=record_text, font=('Arial', 16), bg='teal').place(x=10, y=245 + i * 30)
    def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            displaytk.destroy()
            recreate_root()
        else:
            pass 
    displaytk.protocol('WM_DELETE_WINDOW',on_closing)
    displaytk.mainloop()

# Root window
root=tk.Tk()
root.geometry('660x350')
root.configure(bg='teal')
root.title('Option Page')
lab3=tk.Label(root, text="WELCOME TO COMPANY DATABASE",font=('Arial',16,'bold'),bg='teal')
lab6=tk.Label(root, text="Made By: Drona Srivastava",font=('Arial',16,'bold'),bg='teal')
lab3.place(x=150,y=20)  
lab6.place(x=195,y=50)  

lin1=tk.Label(root,text="1.Insert new data ",font=('Arial',14),bg='teal')
lin2=tk.Label(root,text="2.Update the table",font=('Arial',14),bg='teal')
lin3=tk.Label(root,text="3.Delete the record from the table",font=('Arial',14),bg='teal')
lin4=tk.Label(root,text="4.Search a record from the table",font=('Arial',14),bg='teal')
lin5=tk.Label(root,text="5.Display the table",font=('Arial',14),bg='teal')
lin6=tk.Label(root,text="6.Quit",font=('Arial',14),bg='teal')

lin1.place(x=10,y=80)
lin2.place(x=10,y=110)
lin3.place(x=10,y=140)
lin4.place(x=10,y=170)
lin5.place(x=10,y=200)
lin6.place(x=10,y=230)

ch=StringVar()
   
lab1=tk.Label(root,text="Which function do you want to apply:",font=('Arial',14),bg='teal')
lab1.place(x=10,y=260)

en1=tk.Entry(root, textvariable=ch, font=('Arial',14))
en1.place(x=325,y=263)

def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            root.destroy()
        else:
            pass 
def choicefunc():
    choice=ch.get()
    if choice=='1':  # To insert new data
        insert()
            
    #To update
    elif choice=='2':
        update()
        
    #To delete a record
    elif choice=='3':
        delete()
        
    #To search a record
    elif choice=='4':
        search()
    
    #To Display the data
    elif choice=='5':
        display()
        
    else:
        on_closing()

btn1=tk.Button(root,text='Enter',font=('Arial',14),bg='teal',command=choicefunc)
btn1.place(x=555,y=255)
root.mainloop()