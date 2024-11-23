#Line 383, how to display the availabe record?

#Importing required libraries
import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
import mysql.connector as sq

 
#Creating the database Movie_database and a table inside it called Movies
def create():
    mydb = sq.connect(host="localhost",user="root",password="root")
    mycursor = mydb.cursor()
    sql = "Create database Movie_database"
    mycursor.execute(sql)
    mycursor.execute("Use Movie_database")
    mydb.commit()
    mycursor.execute("Create table Movies (Movie_Name VARCHAR(500), Genre VARCHAR(100), date_of_release DATE, IMDB_id INTEGER,Director VARCHAR(500), Rating VARCHAR(500))")
    mydb.commit()

#Checking the existence of the database and creating it if the database does not exist
def check_database_existence():
    try:
        mydb = sq.connect(host="localhost",user="root",password="root",database="Movie_database")
    except sq.Error as e:
        if e.errno == 1049:  #1049 is the MySQL error code for "Unknown database"
            create()
        else:
            print(f"Error: {e}")
check_database_existence()


#Re-opening the menu window whenever the close button is clicked.
def recreate_root():
    global root
    root=tk.Tk()
    root.geometry('690x350')
    root.configure(bg='#42c8f5')
    root.title('Menu')
    lab3=tk.Label(root, text="WELCOME TO BLOCKBUSTER: A Movie Database",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
    lab6=tk.Label(root, text="Made By: Atharava Srivastava",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
    lab3.pack()  
    lab6.pack()    

    lin1=tk.Label(root,text="1.Insert new records",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lin2=tk.Label(root,text="2.Update a record",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lin3=tk.Label(root,text="3.Delete a record",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lin4=tk.Label(root,text="4.Search a record",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lin5=tk.Label(root,text="5.Display the data",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lin6=tk.Label(root,text="6.Quit",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')

    lin1.place(x=10,y=80)
    lin2.place(x=10,y=110)
    lin3.place(x=10,y=140)
    lin4.place(x=10,y=170)
    lin5.place(x=10,y=200)
    lin6.place(x=10,y=230)

    ch=StringVar()
       
    lab1=tk.Label(root,text="Which function do you want to apply?:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab1.place(x=10,y=260)

    en1=tk.Entry(root, textvariable=ch, font=('Cascadia Mono SemiLight',14))
    en1.place(x=420,y=263)

    #Creating a function to ask confirmation from user if quiting
    def on_closing():
            if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
                root.destroy()
            else:
                pass 
    #Creating conditional loop to run each function as called by the user
    def choicefunc(event=None):
        choice=ch.get()
        # To insert new records
        if choice=='1':  
            insert()        
        #To update a record
        elif choice=='2':
            update()
        #To delete a record
        elif choice=='3':
            delete()
        #To search a record
        elif choice=='4':
            search()
        #To display the data
        elif choice=='5':
            display()       
        #To exit the program
        elif choice=='6':
            exit_=tk.Tk()
            exit_.geometry('500x100')
            exit_.config(bg='#42c8f5')
            exit_.title('Exit')
            label_0=tk.Label(exit_, text="Thank You!",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
            label_1=tk.Label(exit_, text="Hope you have a nice day!",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
            label_0.pack()
            label_1.pack()
            root.destroy()
        #Invaild input
        else:
            lab2=tk.Label(root,text="Please Enter Valid Input!",font=('Cascadia Mono SemiLight',15),bg='#42c8f5')
            lab2.place(x=170,y=300)
            ch.set('')
    
    en1.bind ('<Return>',choicefunc)
    
    #Recreating the option window
    root.mainloop()
    

#Function for inserting data
def insert():
    
    #Closing main tk page
    root.destroy()
    
    #Opening a tk page for insert menu item
    insertk=tk.Tk()  
    insertk.geometry('850x380')
    insertk.configure(bg='#42c8f5')
    insertk.title('Insert Record')
    
    #Creating labels 
    lab0=tk.Label(insertk,text='Fill out the below information',bg='#42c8f5',font=('Cascadia Mono SemiLight',18,'bold'))
    lab1=tk.Label(insertk,text="Name of the Movie :",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    lab2=tk.Label(insertk,text="Genre of the Movie:",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    lab3=tk.Label(insertk,text="Date of Releae of the Movie (in YYYY-MM-DD format):",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    lab4=tk.Label(insertk,text="IMDB ID:",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    lab5=tk.Label(insertk,text="Movie Director:",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    lab6=tk.Label(insertk,text="IMDB Rating:",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    
    #Placing the labels
    lab0.pack()
    lab1.place(x=10,y=60)
    lab2.place(x=10,y=100)
    lab3.place(x=10,y=140)
    lab4.place(x=10,y=180)
    lab5.place(x=10,y=220)
    lab6.place(x=10,y=260)

    #Initializing variable to read the entry box data
    nm=StringVar()
    genre=StringVar()
    dor=StringVar()
    code=StringVar()
    dr=StringVar()
    rt=StringVar()

    #Creating the entry boxes
    en1=tk.Entry(insertk,textvariable=nm,font=('Cascadia Mono SemiLight',14))
    en2=tk.Entry(insertk,textvariable=genre,font=('Cascadia Mono SemiLight',14))
    en3=tk.Entry(insertk,textvariable=dor,font=('Cascadia Mono SemiLight',14))
    en4=tk.Entry(insertk,textvariable=code,font=('Cascadia Mono SemiLight',14))
    en5=tk.Entry(insertk,textvariable=dr,font=('Cascadia Mono SemiLight',14))
    en6=tk.Entry(insertk,textvariable=rt,font=('Cascadia Mono SemiLight',14))
    en7=tk.Entry(insertk)
    
    #Placing the entry boxes
    en1.place(x=225,y=62)
    en2.place(x=225,y=102)
    en3.place(x=575,y=142)
    en4.place(x=105,y=182)
    en5.place(x=180,y=222)      
    en6.place(x=145,y=262)
    
    #Quries for entering data in MySQL table)
    def insertin(event=None):
        Name=nm.get()
        Genre=genre.get()
        DOR=dor.get()
        Movie_code=code.get()
        Director=dr.get()
        Rating=rt.get()

        mydb = sq.connect(host="localhost",user="root",password="root",database="movie_database")
        mycursor = mydb.cursor()
        sql = "INSERT INTO Movies (Movie_Name, Genre, Date_of_release, IMDB_id, Director, Rating) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (Name,Genre,DOR,Movie_code,Director,Rating)
        mycursor.execute(sql, val)
        mydb.commit()
        
        added=tk.Label(insertk,text='Record Inserted',font=('Cascadia Mono SemiLight',20),bg='#42c8f5')
        added.place(x=300,y=295)
        
        nm.set('')
        genre.set('')
        dor.set('')
        code.set('')
        dr.set('')
        rt.set('')    
    insertk.bind_all('<Return>', insertin)
    
    
    #Function to ask confirmation from user for quiting
    def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            insertk.destroy() # Closing this window
            recreate_root() # Re-opening root window
        else:
            pass
        
    insertk.protocol('WM_DELETE_WINDOW',on_closing)
    insertk.mainloop()


#Function for updating a record
def update():
    root.destroy()
    updatetk=tk.Tk()
    updatetk.geometry('750x380')
    updatetk.configure(bg='#42c8f5')
    updatetk.title('Update Record')
    
    #Creating labels 
    lab0=tk.Label(updatetk,text='Update Record',font=('Cascadia Mono SemiLight',18,'bold'),bg='#42c8f5')
    lab1=tk.Label(updatetk,text='--> 1. Movie name ',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab2=tk.Label(updatetk,text='--> 2. Genre',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab3=tk.Label(updatetk,text='--> 3. Date of Release',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab4=tk.Label(updatetk,text='--> 4. IMDB Id',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab5=tk.Label(updatetk,text='--> 5. Director',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab9=tk.Label(updatetk,text='--> 6. IMDB Rating',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab6=tk.Label(updatetk,text="Movie name whose record you want to update:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab7=tk.Label(updatetk,text="Record you want to update:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab8=tk.Label(updatetk,text="Enter the change:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')

    #Placing the labels
    lab0.pack()
    lab6.place(x=10,y=50)
    lab1.place(x=10,y=80)
    lab2.place(x=10,y=110)
    lab3.place(x=10,y=140)
    lab4.place(x=10,y=170)
    lab5.place(x=10,y=200)
    lab9.place(x=10,y=230)
    lab7.place(x=10,y=260)
    lab8.place(x=10,y=290)

    #Initialising variable to read entry box
    upe=StringVar()
    fi=StringVar()
    fich=StringVar()

    #Creating the entry boxes
    en1=tk.Entry(updatetk,textvariable=upe,font=('Cascadia Mono SemiLight',14)) 
    en2=tk.Entry(updatetk,textvariable=fi,font=('Cascadia Mono SemiLight',14)) 
    en3=tk.Entry(updatetk,textvariable=fich,font=('Cascadia Mono SemiLight',14)) 

    #Placing the entry boxes
    en1.place(x=490,y=52)
    en2.place(x=300,y=262)
    en3.place(x=200,y=294)
            
    #Quries for updating data in MySQL table)
    def updateit(event=None):
        up=upe.get()
        fields=int(fi.get())
        fieldch=fich.get()
        if fields==1:
            field='Movie_Name'
        elif fields==2:
            field='Genre'
        elif fields==3:
            field='Date_of_release'
        elif fields==4:
            field='IMDB_id'
        elif fields==5:
            field='Director'
        elif fields==6:
            field='Rating'
        mydb= sq.connect(host="localhost",user="root",passwd="root",database="Movie_database")
        cursor=mydb.cursor()
        update="UPDATE Movies set {} = '{}' WHERE Movie_Name like '{}'".format(field,fieldch,up)
        cursor.execute(update)
        mydb.commit()
        lab0=tk.Label(updatetk,text="Record Updated!",font=('Cascadia Mono SemiLight',24),bg='#42c8f5')
        lab0.place(x=240,y=325)
        upe.set('')
        fi.set('')
        fich.set('')

    
    updatetk.bind_all('<Return>', updateit)
   
    #Function to ask confirmation from user for quiting
    def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            updatetk.destroy() # Closing the window
            recreate_root() # Re-opening root window
        else:
            pass
        
    updatetk.protocol('WM_DELETE_WINDOW',on_closing)
    updatetk.mainloop()

#Function for deleting a record 
def delete():
    root.destroy()
    deletetk=tk.Tk()        
    deletetk.geometry('850x120')
    deletetk.configure(bg='#42c8f5')
    deletetk.title('Delete Record')

    #Creating labels 
    lab0=tk.Label(deletetk,text="Delete Record",font=('Cascadia Mono SemiLight',18,'bold'),bg='#42c8f5')
    lab1=tk.Label(deletetk,text="Enter the Movie name whose data you want to delete:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    
    #Placing the labels
    lab0.pack()
    lab1.place(x=20,y=40)

    #Initialising variable to read entry box
    de=StringVar()

    #Creating the entry box
    en1=tk.Entry(deletetk,textvariable=de,font=('Cascadia Mono SemiLight',14))

    #Placing the entry box
    en1.place(x=585,y=40)
    
    #Quries for deleting data in MySQL table)
    def deleteit(event=None):
        dele=de.get()
        c=sq.connect(host="localhost",user="root",passwd="root",database="movie_database")
        cursor=c.cursor()
        sql="DELETE FROM Movies WHERE Movie_Name like '%{}%'".format(dele)
        cursor.execute(sql)
        c.commit()
        lab2=tk.Label(deletetk,text="Record Deleted",font=('Cascadia Mono SemiLight',15,'bold'),bg='#42c8f5')
        lab2.place(x=320,y=80)
        de.set('')

    deletetk.bind_all('<Return>', deleteit)

    #Function to ask confirmation from user for quiting
    def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            deletetk.destroy() # Closing this window
            recreate_root() # Re-opening root window
        else:
            pass
        
    deletetk.protocol('WM_DELETE_WINDOW',on_closing)
    deletetk.mainloop()

#Function for searching a movie from the list
def search():
    root.destroy()
    searchtk=tk.Tk()
    searchtk.geometry('425x150')
    searchtk.title('Search Record')
    searchtk.configure(bg='#42c8f5')

    #Creating label
    lab1=tk.Label(searchtk,text="Search Record",font=('Arial',18,'bold'),bg='#42c8f5')
    lab2=tk.Label(searchtk,text="Movie Name:",font=('Arial',14),bg='#42c8f5')
    #Placing the label
    lab1.pack()
    lab2.place(x=10,y=50)   

    #Initialising a variable to read entry box
    se=StringVar()
    output=StringVar()
    
    #Creating entry box
    en1=tk.Entry(searchtk,textvariable=se,font=('Arial',14))
    en2=tk.Entry(searchtk,textvariable=output,font=('Arial',14),bg='#42c8f5',relief='flat')
    #Placing the entry box
    en1.place(x=130,y=50)
    en2.place(x=100,y=90)
    #Quries for searching data in MySQL table using movie name)
    def searchit(event=None):
        try:
            pat=se.get()
            mydb=sq.connect(host='localhost', user='root', password='root', database='movie_database')
            cursor=mydb.cursor()
            q="SELECT * FROM Movies WHERE Movie_Name LIKE '%{}%'".format(pat)
            cursor.execute(q)
            result=cursor.fetchall()

            if result:
                output.set('Record is available.')
                ############################################################################################################################################
            else:
                output.set('Record is not available.')
        except Exception as e:
            print(f"Error: {e}")
    searchtk.bind_all('<Return>',searchit)
    
    #Function to ask confirmation from user for quiting
    def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            searchtk.destroy()
            recreate_root()
        else:
            pass 
    searchtk.protocol('WM_DELETE_WINDOW',on_closing)
    searchtk.mainloop()

#Function for displaying the data
def display():
    root.destroy()
    displaytk=tk.Tk()
    displaytk.configure(bg='#42c8f5')
    displaytk.geometry('1000x550')
    displaytk.title('Display Record')

    #Queries for displaying the table data in MySQL
    mydb=sq.connect(host="localhost", user="root", password="root", database="movie_database")
    cursor=mydb.cursor()
    sql="SELECT * FROM Movies ORDER BY Movie_Name"
    cursor.execute(sql)
    myresult=cursor.fetchall()

    #Creating a frame
    container=tk.Frame(displaytk, bg='#42c8f5')
    container.pack(fill='both', expand=True)

    #Creating the canvas and the scrollbar
    canvas = tk.Canvas(container, bg='#42c8f5')
    scrollbar = tk.Scrollbar(container, orient='vertical', command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg='#42c8f5')

    #Configuring the scrollable frame
    scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    #Adding the header labels
    header_labels = ['Movie Name', 'Genre', 'Date of Release', 'IMDB Id', 'Director', 'Rating']
    for i, header in enumerate(header_labels):
        tk.Label(scrollable_frame, text=header, font=('Cascadia Mono SemiLight', 16), bg='#42c8f5').grid(row=0, column=i, padx=10, pady=10)

    #Adding movie records in rows
    for i, record in enumerate(myresult):
        for j, value in enumerate(record):
            tk.Label(scrollable_frame, text=value, font=('Cascadia Mono SemiLight', 14), bg='#42c8f5').grid(row=i+1, column=j, padx=10, pady=5)

    #Placing the canvas and the scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    #Function to ask confirmation from user for quitting
    def on_closing():
        if messagebox.askyesno(title='QUIT?', message='Are you sure you want to quit'):
            displaytk.destroy()  # Closing this window
            recreate_root()  # Re-opening root window
        else:
            pass

    displaytk.protocol('WM_DELETE_WINDOW', on_closing)
    displaytk.mainloop()

#Root window
root=tk.Tk()
root.geometry('690x350')
root.configure(bg='#42c8f5')
root.title('Menu')
lab3=tk.Label(root, text="WELCOME TO BLOCKBUSTER: A Movie Database",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
lab6=tk.Label(root, text="Made By: Atharava Srivastava",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
lab3.pack()  
lab6.pack()    

lin1=tk.Label(root,text="1.Insert new data ",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lin2=tk.Label(root,text="2.Update the table",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lin3=tk.Label(root,text="3.Delete the record from the table",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lin4=tk.Label(root,text="4.Search a record from the table",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lin5=tk.Label(root,text="5.Display the table",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lin6=tk.Label(root,text="6.Quit",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')

lin1.place(x=10,y=80)
lin2.place(x=10,y=110)
lin3.place(x=10,y=140)
lin4.place(x=10,y=170)
lin5.place(x=10,y=200)
lin6.place(x=10,y=230)

ch=StringVar()
   
lab1=tk.Label(root,text="Which function do you want to apply?:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lab1.place(x=10,y=260)
en1=tk.Entry(root, textvariable=ch, font=('Cascadia Mono SemiLight',14))
en1.place(x=420,y=263)

#Function to ask confirmation from user for quiting
def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            root.destroy() #closing root window
        else:
            pass

def choicefunc(event=None):
    choice=ch.get()
    #To insert new data
    if choice=='1':  
        insert()
    #To update a record
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
    #To Exit the program
    elif choice=='6':
        exit_=tk.Tk()
        exit_.geometry('500x100')
        exit_.config(bg='#42c8f5')
        exit_.title('Exit')
        label_0=tk.Label(exit_, text="Thank You!",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
        label_1=tk.Label(exit_, text="Hope you have a nice day!",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
        label_0.pack()
        label_1.pack()
        root.destroy()
    #Invaild input
    else:
        lab2=tk.Label(root,text="Please Enter Valid Input!",font=('Cascadia Mono SemiLight',15),bg='#42c8f5')
        lab2.place(x=170,y=300)
        ch.set('')
        
en1.bind('<Return>',choicefunc)#Line 383, how to display the availabe record?

#Importing required libraries
import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox
import mysql.connector as sq

 
#Creating the database Movie_database and a table inside it called Movies
def create():
    mydb = sq.connect(host="localhost",user="root",password="root")
    mycursor = mydb.cursor()
    sql = "Create database Movie_database"
    mycursor.execute(sql)
    mycursor.execute("Use Movie_database")
    mydb.commit()
    mycursor.execute("Create table Movies (Movie_Name VARCHAR(500), Genre VARCHAR(100), date_of_release DATE, IMDB_id INTEGER,Director VARCHAR(500), Rating VARCHAR(500))")
    mydb.commit()

#Checking the existence of the database and creating it if the database does not exist
def check_database_existence():
    try:
        mydb = sq.connect(host="localhost",user="root",password="root",database="Movie_database")
    except sq.Error as e:
        if e.errno == 1049:  #1049 is the MySQL error code for "Unknown database"
            create()
        else:
            print(f"Error: {e}")
check_database_existence()


#Re-opening the menu window whenever the close button is clicked.
def recreate_root():
    global root
    root=tk.Tk()
    root.geometry('690x350')
    root.configure(bg='#42c8f5')
    root.title('Menu')
    lab3=tk.Label(root, text="WELCOME TO BLOCKBUSTER: A Movie Database",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
    lab6=tk.Label(root, text="Made By: Atharava Srivastava",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
    lab3.pack()  
    lab6.pack()    

    lin1=tk.Label(root,text="1.Insert new records",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lin2=tk.Label(root,text="2.Update a record",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lin3=tk.Label(root,text="3.Delete a record",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lin4=tk.Label(root,text="4.Search a record",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lin5=tk.Label(root,text="5.Display the data",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lin6=tk.Label(root,text="6.Quit",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')

    lin1.place(x=10,y=80)
    lin2.place(x=10,y=110)
    lin3.place(x=10,y=140)
    lin4.place(x=10,y=170)
    lin5.place(x=10,y=200)
    lin6.place(x=10,y=230)

    ch=StringVar()
       
    lab1=tk.Label(root,text="Which function do you want to apply?:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab1.place(x=10,y=260)

    en1=tk.Entry(root, textvariable=ch, font=('Cascadia Mono SemiLight',14))
    en1.place(x=420,y=263)

    #Creating a function to ask confirmation from user if quiting
    def on_closing():
            if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
                root.destroy()
            else:
                pass 
    #Creating conditional loop to run each function as called by the user
    def choicefunc(event=None):
        choice=ch.get()
        # To insert new records
        if choice=='1':  
            insert()        
        #To update a record
        elif choice=='2':
            update()
        #To delete a record
        elif choice=='3':
            delete()
        #To search a record
        elif choice=='4':
            search()
        #To display the data
        elif choice=='5':
            display()       
        #To exit the program
        elif choice=='6':
            exit_=tk.Tk()
            exit_.geometry('500x100')
            exit_.config(bg='#42c8f5')
            exit_.title('Exit')
            label_0=tk.Label(exit_, text="Thank You!",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
            label_1=tk.Label(exit_, text="Hope you have a nice day!",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
            label_0.pack()
            label_1.pack()
            root.destroy()
        #Invaild input
        else:
            lab2=tk.Label(root,text="Please Enter Valid Input!",font=('Cascadia Mono SemiLight',15),bg='#42c8f5')
            lab2.place(x=170,y=300)
            ch.set('')
    
    en1.bind ('<Return>',choicefunc)
    
    #Recreating the option window
    root.mainloop()
    

#Function for inserting data
def insert():
    
    #Closing main tk page
    root.destroy()
    
    #Opening a tk page for insert menu item
    insertk=tk.Tk()  
    insertk.geometry('850x380')
    insertk.configure(bg='#42c8f5')
    insertk.title('Insert Record')
    
    #Creating labels 
    lab0=tk.Label(insertk,text='Fill out the below information',bg='#42c8f5',font=('Cascadia Mono SemiLight',18,'bold'))
    lab1=tk.Label(insertk,text="Name of the Movie :",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    lab2=tk.Label(insertk,text="Genre of the Movie:",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    lab3=tk.Label(insertk,text="Date of Releae of the Movie (in YYYY-MM-DD format):",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    lab4=tk.Label(insertk,text="IMDB ID:",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    lab5=tk.Label(insertk,text="Movie Director:",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    lab6=tk.Label(insertk,text="IMDB Rating:",bg='#42c8f5',font=('Cascadia Mono SemiLight',14))
    
    #Placing the labels
    lab0.pack()
    lab1.place(x=10,y=60)
    lab2.place(x=10,y=100)
    lab3.place(x=10,y=140)
    lab4.place(x=10,y=180)
    lab5.place(x=10,y=220)
    lab6.place(x=10,y=260)

    #Initializing variable to read the entry box data
    nm=StringVar()
    genre=StringVar()
    dor=StringVar()
    code=StringVar()
    dr=StringVar()
    rt=StringVar()

    #Creating the entry boxes
    en1=tk.Entry(insertk,textvariable=nm,font=('Cascadia Mono SemiLight',14))
    en2=tk.Entry(insertk,textvariable=genre,font=('Cascadia Mono SemiLight',14))
    en3=tk.Entry(insertk,textvariable=dor,font=('Cascadia Mono SemiLight',14))
    en4=tk.Entry(insertk,textvariable=code,font=('Cascadia Mono SemiLight',14))
    en5=tk.Entry(insertk,textvariable=dr,font=('Cascadia Mono SemiLight',14))
    en6=tk.Entry(insertk,textvariable=rt,font=('Cascadia Mono SemiLight',14))
    en7=tk.Entry(insertk)
    
    #Placing the entry boxes
    en1.place(x=225,y=62)
    en2.place(x=225,y=102)
    en3.place(x=575,y=142)
    en4.place(x=105,y=182)
    en5.place(x=180,y=222)      
    en6.place(x=145,y=262)
    
    #Quries for entering data in MySQL table)
    def insertin(event=None):
        Name=nm.get()
        Genre=genre.get()
        DOR=dor.get()
        Movie_code=code.get()
        Director=dr.get()
        Rating=rt.get()

        mydb = sq.connect(host="localhost",user="root",password="root",database="movie_database")
        mycursor = mydb.cursor()
        sql = "INSERT INTO Movies (Movie_Name, Genre, Date_of_release, IMDB_id, Director, Rating) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (Name,Genre,DOR,Movie_code,Director,Rating)
        mycursor.execute(sql, val)
        mydb.commit()
        
        added=tk.Label(insertk,text='Record Inserted',font=('Cascadia Mono SemiLight',20),bg='#42c8f5')
        added.place(x=300,y=295)
        
        nm.set('')
        genre.set('')
        dor.set('')
        code.set('')
        dr.set('')
        rt.set('')    
    insertk.bind_all('<Return>', insertin)
    
    
    #Function to ask confirmation from user for quiting
    def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            insertk.destroy() # Closing this window
            recreate_root() # Re-opening root window
        else:
            pass
        
    insertk.protocol('WM_DELETE_WINDOW',on_closing)
    insertk.mainloop()


#Function for updating a record
def update():
    root.destroy()
    updatetk=tk.Tk()
    updatetk.geometry('750x380')
    updatetk.configure(bg='#42c8f5')
    updatetk.title('Update Record')
    
    #Creating labels 
    lab0=tk.Label(updatetk,text='Update Record',font=('Cascadia Mono SemiLight',18,'bold'),bg='#42c8f5')
    lab1=tk.Label(updatetk,text='--> 1. Movie name ',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab2=tk.Label(updatetk,text='--> 2. Genre',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab3=tk.Label(updatetk,text='--> 3. Date of Release',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab4=tk.Label(updatetk,text='--> 4. IMDB Id',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab5=tk.Label(updatetk,text='--> 5. Director',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab9=tk.Label(updatetk,text='--> 6. IMDB Rating',font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab6=tk.Label(updatetk,text="Movie name whose record you want to update:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab7=tk.Label(updatetk,text="Record you want to update:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    lab8=tk.Label(updatetk,text="Enter the change:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')

    #Placing the labels
    lab0.pack()
    lab6.place(x=10,y=50)
    lab1.place(x=10,y=80)
    lab2.place(x=10,y=110)
    lab3.place(x=10,y=140)
    lab4.place(x=10,y=170)
    lab5.place(x=10,y=200)
    lab9.place(x=10,y=230)
    lab7.place(x=10,y=260)
    lab8.place(x=10,y=290)

    #Initialising variable to read entry box
    upe=StringVar()
    fi=StringVar()
    fich=StringVar()

    #Creating the entry boxes
    en1=tk.Entry(updatetk,textvariable=upe,font=('Cascadia Mono SemiLight',14)) 
    en2=tk.Entry(updatetk,textvariable=fi,font=('Cascadia Mono SemiLight',14)) 
    en3=tk.Entry(updatetk,textvariable=fich,font=('Cascadia Mono SemiLight',14)) 

    #Placing the entry boxes
    en1.place(x=490,y=52)
    en2.place(x=300,y=262)
    en3.place(x=200,y=294)
            
    #Quries for updating data in MySQL table)
    def updateit(event=None):
        up=upe.get()
        fields=int(fi.get())
        fieldch=fich.get()
        if fields==1:
            field='Movie_Name'
        elif fields==2:
            field='Genre'
        elif fields==3:
            field='Date_of_release'
        elif fields==4:
            field='IMDB_id'
        elif fields==5:
            field='Director'
        elif fields==6:
            field='Rating'
        mydb= sq.connect(host="localhost",user="root",passwd="root",database="Movie_database")
        cursor=mydb.cursor()
        update="UPDATE Movies set {} = '{}' WHERE Movie_Name like '{}'".format(field,fieldch,up)
        cursor.execute(update)
        mydb.commit()
        lab0=tk.Label(updatetk,text="Record Updated!",font=('Cascadia Mono SemiLight',24),bg='#42c8f5')
        lab0.place(x=240,y=325)
        upe.set('')
        fi.set('')
        fich.set('')

    
    updatetk.bind_all('<Return>', updateit)
   
    #Function to ask confirmation from user for quiting
    def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            updatetk.destroy() # Closing the window
            recreate_root() # Re-opening root window
        else:
            pass
        
    updatetk.protocol('WM_DELETE_WINDOW',on_closing)
    updatetk.mainloop()

#Function for deleting a record 
def delete():
    root.destroy()
    deletetk=tk.Tk()        
    deletetk.geometry('850x120')
    deletetk.configure(bg='#42c8f5')
    deletetk.title('Delete Record')

    #Creating labels 
    lab0=tk.Label(deletetk,text="Delete Record",font=('Cascadia Mono SemiLight',18,'bold'),bg='#42c8f5')
    lab1=tk.Label(deletetk,text="Enter the Movie name whose data you want to delete:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
    
    #Placing the labels
    lab0.pack()
    lab1.place(x=20,y=40)

    #Initialising variable to read entry box
    de=StringVar()

    #Creating the entry box
    en1=tk.Entry(deletetk,textvariable=de,font=('Cascadia Mono SemiLight',14))

    #Placing the entry box
    en1.place(x=585,y=40)
    
    #Quries for deleting data in MySQL table)
    def deleteit(event=None):
        dele=de.get()
        c=sq.connect(host="localhost",user="root",passwd="root",database="movie_database")
        cursor=c.cursor()
        sql="DELETE FROM Movies WHERE Movie_Name like '%{}%'".format(dele)
        cursor.execute(sql)
        c.commit()
        lab2=tk.Label(deletetk,text="Record Deleted",font=('Cascadia Mono SemiLight',15,'bold'),bg='#42c8f5')
        lab2.place(x=320,y=80)
        de.set('')

    deletetk.bind_all('<Return>', deleteit)

    #Function to ask confirmation from user for quiting
    def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            deletetk.destroy() # Closing this window
            recreate_root() # Re-opening root window
        else:
            pass
        
    deletetk.protocol('WM_DELETE_WINDOW',on_closing)
    deletetk.mainloop()

#Function for searching a movie from the list
def search():
    root.destroy()
    searchtk=tk.Tk()
    searchtk.geometry('425x150')
    searchtk.title('Search Record')
    searchtk.configure(bg='#42c8f5')

    #Creating label
    lab1=tk.Label(searchtk,text="Search Record",font=('Arial',18,'bold'),bg='#42c8f5')
    lab2=tk.Label(searchtk,text="Movie Name:",font=('Arial',14),bg='#42c8f5')
    #Placing the label
    lab1.pack()
    lab2.place(x=10,y=50)   

    #Initialising a variable to read entry box
    se=StringVar()
    output=StringVar()
    
    #Creating entry box
    en1=tk.Entry(searchtk,textvariable=se,font=('Arial',14))
    en2=tk.Entry(searchtk,textvariable=output,font=('Arial',14),bg='#42c8f5',relief='flat')
    #Placing the entry box
    en1.place(x=130,y=50)
    en2.place(x=100,y=90)
    #Quries for searching data in MySQL table using movie name)
    def searchit(event=None):
        try:
            pat=se.get()
            mydb=sq.connect(host='localhost', user='root', password='root', database='movie_database')
            cursor=mydb.cursor()
            q="SELECT * FROM Movies WHERE Movie_Name LIKE '%{}%'".format(pat)
            cursor.execute(q)
            result=cursor.fetchall()

            if result:
                output.set('Record is available.')
                ############################################################################################################################################
            else:
                output.set('Record is not available.')
        except Exception as e:
            print(f"Error: {e}")
    searchtk.bind_all('<Return>',searchit)
    
    #Function to ask confirmation from user for quiting
    def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            searchtk.destroy()
            recreate_root()
        else:
            pass 
    searchtk.protocol('WM_DELETE_WINDOW',on_closing)
    searchtk.mainloop()

#Function for displaying the data
def display():
    root.destroy()
    displaytk=tk.Tk()
    displaytk.configure(bg='#42c8f5')
    displaytk.geometry('1000x550')
    displaytk.title('Display Record')

    #Queries for displaying the table data in MySQL
    mydb=sq.connect(host="localhost", user="root", password="root", database="movie_database")
    cursor=mydb.cursor()
    sql="SELECT * FROM Movies ORDER BY Movie_Name"
    cursor.execute(sql)
    myresult=cursor.fetchall()

    #Creating a frame
    container=tk.Frame(displaytk, bg='#42c8f5')
    container.pack(fill='both', expand=True)

    #Creating the canvas and the scrollbar
    canvas = tk.Canvas(container, bg='#42c8f5')
    scrollbar = tk.Scrollbar(container, orient='vertical', command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg='#42c8f5')

    #Configuring the scrollable frame
    scrollable_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    #Adding the header labels
    header_labels = ['Movie Name', 'Genre', 'Date of Release', 'IMDB Id', 'Director', 'Rating']
    for i, header in enumerate(header_labels):
        tk.Label(scrollable_frame, text=header, font=('Cascadia Mono SemiLight', 16), bg='#42c8f5').grid(row=0, column=i, padx=10, pady=10)

    #Adding movie records in rows
    for i, record in enumerate(myresult):
        for j, value in enumerate(record):
            tk.Label(scrollable_frame, text=value, font=('Cascadia Mono SemiLight', 14), bg='#42c8f5').grid(row=i+1, column=j, padx=10, pady=5)

    #Placing the canvas and the scrollbar
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    #Function to ask confirmation from user for quitting
    def on_closing():
        if messagebox.askyesno(title='QUIT?', message='Are you sure you want to quit'):
            displaytk.destroy()  # Closing this window
            recreate_root()  # Re-opening root window
        else:
            pass

    displaytk.protocol('WM_DELETE_WINDOW', on_closing)
    displaytk.mainloop()

#Root window
root=tk.Tk()
root.geometry('690x350')
root.configure(bg='#42c8f5')
root.title('Menu')
lab3=tk.Label(root, text="WELCOME TO BLOCKBUSTER: A Movie Database",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
lab6=tk.Label(root, text="Made By: Atharava Srivastava",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
lab3.pack()  
lab6.pack()    

lin1=tk.Label(root,text="1.Insert new data ",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lin2=tk.Label(root,text="2.Update the table",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lin3=tk.Label(root,text="3.Delete the record from the table",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lin4=tk.Label(root,text="4.Search a record from the table",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lin5=tk.Label(root,text="5.Display the table",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lin6=tk.Label(root,text="6.Quit",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')

lin1.place(x=10,y=80)
lin2.place(x=10,y=110)
lin3.place(x=10,y=140)
lin4.place(x=10,y=170)
lin5.place(x=10,y=200)
lin6.place(x=10,y=230)

ch=StringVar()
   
lab1=tk.Label(root,text="Which function do you want to apply?:",font=('Cascadia Mono SemiLight',14),bg='#42c8f5')
lab1.place(x=10,y=260)
en1=tk.Entry(root, textvariable=ch, font=('Cascadia Mono SemiLight',14))
en1.place(x=420,y=263)

#Function to ask confirmation from user for quiting
def on_closing():
        if messagebox.askyesno(title='QUIT?',message='Are you sure you want to quit'):
            root.destroy() #closing root window
        else:
            pass

def choicefunc(event=None):
    choice=ch.get()
    #To insert new data
    if choice=='1':  
        insert()
    #To update a record
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
    #To Exit the program
    elif choice=='6':
        exit_=tk.Tk()
        exit_.geometry('500x100')
        exit_.config(bg='#42c8f5')
        exit_.title('Exit')
        label_0=tk.Label(exit_, text="Thank You!",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
        label_1=tk.Label(exit_, text="Hope you have a nice day!",font=('Cascadia Mono SemiLight',16,'bold'),bg='#42c8f5')
        label_0.pack()
        label_1.pack()
        root.destroy()
    #Invaild input
    else:
        lab2=tk.Label(root,text="Please Enter Valid Input!",font=('Cascadia Mono SemiLight',15),bg='#42c8f5')
        lab2.place(x=170,y=300)
        ch.set('')
        
en1.bind('<Return>',choicefunc)