'''This project is designed to  list animes by their Anime names, Genre,Date of release, No. of episodes
and Sites available to watch the desired anime by choice'''
def create():
    import mysql.connector as sq

    mydb = sq.connect(host="localhost",user="root",password="root")

    mycursor = mydb.cursor()

    sql = "Create database project"

    mycursor.execute(sql)

    mycursor.execute("Use project")
    
    mydb.commit()

    mycursor.execute("Create table Anime(Anime_Name VARCHAR(500), Genre VARCHAR(100), Date_of_release DATE, No_of_episodes INTEGER, Site VARCHAR(700))")

    mydb.commit()

create()
def insert():
    
    import mysql.connector as sq

    mydb = sq.connect(host="localhost",user="root",password="root",database="project")

    mycursor = mydb.cursor()
   
    sql = "INSERT INTO Anime ( Anime_Name, Genre, Date_of_release, No_of_episodes, Site) VALUES (%s, %s,%s,%s,%s)"

    val = (Name, Genre,DOR, Episodes, Site)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def update():
#This code is to update the Anime list
        print('--> Anime_Name for name \n--> Genre for genre \n--> Date_of_release for date of release \n--> No_of_episodes for No. of episodes \n--> Site for site')
        
        up=input("Enter the Anime name whose record you want to update:")

        field= input("Enter the field you want to update:")

        fieldch=input("Enter the record you want the field to change to:")

        import mysql.connector as sq

        mydb= sq.connect(host="localhost",user="root",passwd="root",database="project")

        cursor=mydb.cursor()

        update="UPDATE Anime set {} = {} WHERE Anime_Name like '%{}%'".format(field,fieldch,up)

        cursor.execute(update)

        mydb.commit()

        print("Record Updated")

def delete():
# This code is the delete a record from the anime list

        dele=input("Enter the Anime name whose data you want to delete:")

        import mysql.connector as sq

        c=sq.connect(host="localhost",user="root",passwd="root",database="project")

        cursor=c.cursor()

        sql = "DELETE FROM Anime WHERE Anime_Name like '%{}%'".format(dele)

        cursor.execute(sql)

        c.commit()

        print("Record Deleted")
def search():
#This code is to search an anime from the list
        import mysql.connector as mysql

        try:
            conn=mysql.connect(host='localhost',user='root',password='root',db='project')

            cmd=conn.cursor()
   
            pat=input("Enter Anime Name whose record you want to see:")
   
            q="select * from anime where Anime_Name like '%{}%'".format(pat)

            cmd.execute(q)

            print("Record is available")

        except :

            print("Record is not available")

def display():
#This code is to display thw whole anime list
        import mysql.connector as sq

        mydb = sq.connect(host="localhost",user="root",password="root",database="project")

        cursor = mydb.cursor()

        sql = "SELECT * FROM Anime ORDER BY Anime_Name"

        cursor.execute(sql)
           
        myresult = cursor.fetchall()

        for x in myresult:

            print( x)

print("________#CLASS 12TH CS PROJECT(083)##_______")
print("____________________________________________")
print("|............@@@ WELCOME @@@...............|")
print("|..................TO......................|")
print("|............ANIME LISTING.................|")
print("|.........Made BY: Drona Srivastava........|")
print("|.....Submitted To: Mrs. Shruti Mehta......|")
print("|..........Session : 2022-2023.............|")
print("____________________________________________")



while True:

    print("1. Insert new data ")

    print("2. Update the table")

    print("3.Delete the record from the table")

    print("4.Search a record from the table")

    print("5.Display the table")

    print("6.Quit")

    choice=input("Enter the function you want to apply in the Anime table from this list:")

    
    if choice=='1':# To insert new data

    #This part of the code is to get access to inserting a new record
        user=['Drona','Shruti']
        passwd=['Drona@2005','Shruti@1986']
    
        #This part of the code is to run loop until the password and username is correct
        us=input("Enter your username:")

        pa=input("Enter your password:")

        if us in user:

            ind=user.index(us)
       
            if pa==passwd[ind]:

                print("You can continue to insert a new record")

                Name=input("Enter the name of Anime you want to enter:")

                Genre= input("Enter the genre of the anime you are insert in:")

                DOR=input("Enter the date of release of the anime (in YYYY-MM-DD format):")

                Episodes=int(input("Enter the No. of Epispodes in the Anime:"))

                Site=input("Enter a suggested site to watch the Anime:")
                
                insert()

            else:

                print("Wrong password\n Try again")
              
        else:

            print("Wrong username\n Try again")
        
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
        print("Code Terminated")
        break

'''This project is designed to  list animes by their Anime names, Genre,Date of release, No. of episodes
and Sites available to watch the desired anime by choice'''
def create():
    import mysql.connector as sq

    mydb = sq.connect(host="localhost",user="root",password="root")

    mycursor = mydb.cursor()

    sql = "Create database project"

    mycursor.execute(sql)

    mycursor.execute("Use project")
    
    mydb.commit()

    mycursor.execute("Create table Anime(Anime_Name VARCHAR(500), Genre VARCHAR(100), Date_of_release DATE, No_of_episodes INTEGER, Site VARCHAR(700))")

    mydb.commit()

create()
def insert():
    
    import mysql.connector as sq

    mydb = sq.connect(host="localhost",user="root",password="root",database="project")

    mycursor = mydb.cursor()
   
    sql = "INSERT INTO Anime ( Anime_Name, Genre, Date_of_release, No_of_episodes, Site) VALUES (%s, %s,%s,%s,%s)"

    val = (Name, Genre,DOR, Episodes, Site)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def update():
#This code is to update the Anime list
        print('--> Anime_Name for name \n--> Genre for genre \n--> Date_of_release for date of release \n--> No_of_episodes for No. of episodes \n--> Site for site')
        
        up=input("Enter the Anime name whose record you want to update:")

        field= input("Enter the field you want to update:")

        fieldch=input("Enter the record you want the field to change to:")

        import mysql.connector as sq

        mydb= sq.connect(host="localhost",user="root",passwd="root",database="project")

        cursor=mydb.cursor()

        update="UPDATE Anime set {} = {} WHERE Anime_Name like '%{}%'".format(field,fieldch,up)

        cursor.execute(update)

        mydb.commit()

        print("Record Updated")

def delete():
# This code is the delete a record from the anime list

        dele=input("Enter the Anime name whose data you want to delete:")

        import mysql.connector as sq

        c=sq.connect(host="localhost",user="root",passwd="root",database="project")

        cursor=c.cursor()

        sql = "DELETE FROM Anime WHERE Anime_Name like '%{}%'".format(dele)

        cursor.execute(sql)

        c.commit()

        print("Record Deleted")
def search():
#This code is to search an anime from the list
        import mysql.connector as mysql

        try:
            conn=mysql.connect(host='localhost',user='root',password='root',db='project')

            cmd=conn.cursor()
   
            pat=input("Enter Anime Name whose record you want to see:")
   
            q="select * from anime where Anime_Name like '%{}%'".format(pat)

            cmd.execute(q)

            print("Record is available")

        except :

            print("Record is not available")

def display():
#This code is to display thw whole anime list
        import mysql.connector as sq

        mydb = sq.connect(host="localhost",user="root",password="root",database="project")

        cursor = mydb.cursor()

        sql = "SELECT * FROM Anime ORDER BY Anime_Name"

        cursor.execute(sql)
           
        myresult = cursor.fetchall()

        for x in myresult:

            print( x)

print("________#CLASS 12TH CS PROJECT(083)##_______")
print("____________________________________________")
print("|............@@@ WELCOME @@@...............|")
print("|..................TO......................|")
print("|............ANIME LISTING.................|")
print("|.........Made BY: Drona Srivastava........|")
print("|.....Submitted To: Mrs. Shruti Mehta......|")
print("|..........Session : 2022-2023.............|")
print("____________________________________________")



while True:

    print("1. Insert new data ")

    print("2. Update the table")

    print("3.Delete the record from the table")

    print("4.Search a record from the table")

    print("5.Display the table")

    print("6.Quit")

    choice=input("Enter the function you want to apply in the Anime table from this list:")

    
    if choice=='1':# To insert new data

    #This part of the code is to get access to inserting a new record
        user=['Drona','Shruti']
        passwd=['Drona@2005','Shruti@1986']
    
        #This part of the code is to run loop until the password and username is correct
        us=input("Enter your username:")

        pa=input("Enter your password:")

        if us in user:

            ind=user.index(us)
       
            if pa==passwd[ind]:

                print("You can continue to insert a new record")

                Name=input("Enter the name of Anime you want to enter:")

                Genre= input("Enter the genre of the anime you are insert in:")

                DOR=input("Enter the date of release of the anime (in YYYY-MM-DD format):")

                Episodes=int(input("Enter the No. of Epispodes in the Anime:"))

                Site=input("Enter a suggested site to watch the Anime:")
                
                insert()

            else:

                print("Wrong password\n Try again")
              
        else:

            print("Wrong username\n Try again")
        
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
        print("Code Terminated")
        break

'''This project is designed to  list animes by their Anime names, Genre,Date of release, No. of episodes
and Sites available to watch the desired anime by choice'''
def create():
    import mysql.connector as sq

    mydb = sq.connect(host="localhost",user="root",password="root")

    mycursor = mydb.cursor()

    sql = "Create database project"

    mycursor.execute(sql)

    mycursor.execute("Use project")
    
    mydb.commit()

    mycursor.execute("Create table Anime(Anime_Name VARCHAR(500), Genre VARCHAR(100), Date_of_release DATE, No_of_episodes INTEGER, Site VARCHAR(700))")

    mydb.commit()

create()
def insert():
    
    import mysql.connector as sq

    mydb = sq.connect(host="localhost",user="root",password="root",database="project")

    mycursor = mydb.cursor()
   
    sql = "INSERT INTO Anime ( Anime_Name, Genre, Date_of_release, No_of_episodes, Site) VALUES (%s, %s,%s,%s,%s)"

    val = (Name, Genre,DOR, Episodes, Site)

    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def update():
#This code is to update the Anime list
        print('--> Anime_Name for name \n--> Genre for genre \n--> Date_of_release for date of release \n--> No_of_episodes for No. of episodes \n--> Site for site')
        
        up=input("Enter the Anime name whose record you want to update:")

        field= input("Enter the field you want to update:")

        fieldch=input("Enter the record you want the field to change to:")

        import mysql.connector as sq

        mydb= sq.connect(host="localhost",user="root",passwd="root",database="project")

        cursor=mydb.cursor()

        update="UPDATE Anime set {} = {} WHERE Anime_Name like '%{}%'".format(field,fieldch,up)

        cursor.execute(update)

        mydb.commit()

        print("Record Updated")

def delete():
# This code is the delete a record from the anime list

        dele=input("Enter the Anime name whose data you want to delete:")

        import mysql.connector as sq

        c=sq.connect(host="localhost",user="root",passwd="root",database="project")

        cursor=c.cursor()

        sql = "DELETE FROM Anime WHERE Anime_Name like '%{}%'".format(dele)

        cursor.execute(sql)

        c.commit()

        print("Record Deleted")
def search():
#This code is to search an anime from the list
        import mysql.connector as mysql

        try:
            conn=mysql.connect(host='localhost',user='root',password='root',db='project')

            cmd=conn.cursor()
   
            pat=input("Enter Anime Name whose record you want to see:")
   
            q="select * from anime where Anime_Name like '%{}%'".format(pat)

            cmd.execute(q)

            print("Record is available")

        except :

            print("Record is not available")

def display():
#This code is to display thw whole anime list
        import mysql.connector as sq

        mydb = sq.connect(host="localhost",user="root",password="root",database="project")

        cursor = mydb.cursor()

        sql = "SELECT * FROM Anime ORDER BY Anime_Name"

        cursor.execute(sql)
           
        myresult = cursor.fetchall()

        for x in myresult:

            print( x)

print("________#CLASS 12TH CS PROJECT(083)##_______")
print("____________________________________________")
print("|............@@@ WELCOME @@@...............|")
print("|..................TO......................|")
print("|............ANIME LISTING.................|")
print("|.........Made BY: Drona Srivastava........|")
print("|.....Submitted To: Mrs. Shruti Mehta......|")
print("|..........Session : 2022-2023.............|")
print("____________________________________________")



while True:

    print("1. Insert new data ")

    print("2. Update the table")

    print("3.Delete the record from the table")

    print("4.Search a record from the table")

    print("5.Display the table")

    print("6.Quit")

    choice=input("Enter the function you want to apply in the Anime table from this list:")

    
    if choice=='1':# To insert new data

    #This part of the code is to get access to inserting a new record
        user=['Drona','Shruti']
        passwd=['Drona@2005','Shruti@1986']
    
        #This part of the code is to run loop until the password and username is correct
        us=input("Enter your username:")

        pa=input("Enter your password:")

        if us in user:

            ind=user.index(us)
       
            if pa==passwd[ind]:

                print("You can continue to insert a new record")

                Name=input("Enter the name of Anime you want to enter:")

                Genre= input("Enter the genre of the anime you are insert in:")

                DOR=input("Enter the date of release of the anime (in YYYY-MM-DD format):")

                Episodes=int(input("Enter the No. of Epispodes in the Anime:"))

                Site=input("Enter a suggested site to watch the Anime:")
                
                insert()

            else:

                print("Wrong password\n Try again")
              
        else:

            print("Wrong username\n Try again")
        
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
        print("Code Terminated")
        break

