import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="pikto",
  buffered = True
)
mycursor = mydb.cursor()

#METHODS:

def print_main_menu():
    print('>>> Now how do you want to work with this')
    print('    program?')
    print('   >>>  1 - insert data')
    print('   >>>  2 - delete data')
    print('   >>>  3 - show data')
    print('   >>>  4 - add price')
    print('   >>> -1 - exit the program')

#insert functions-----------------------------------------------------------------------------------------------------

def print_add_menu():
    print('      >>>INSERT DATA INTO TABLES')
    print('         CHOOSE ONE OF YOUR TABLES: ')
    print('         >>>  1 - art')
    print('         >>>  2 - artist')
    print('         >>>  3 - auction')
    print('         >>>  4 - buyer')
    print('         >>>  5 - exhibition')
    print('         >>>  6 - factor')
    print('         >>> -1 - cancel')

def insert_to_table(table_number): # 1: art | 2: artist | 3: auction | 4: buyer | 5: exhibition | 6: factor
    try:
        if table_number == 1:
            print('            >>>INSERT DATA INTO ART TABLE')
            #getting data from user
            artTitle = input('               >>> artTitle: ')
            artInfo = input('               >>> artInfo: ')
            artCategory = input('               >>> artCategory(photo/painting/sculpture): ')
            artArtist = input('               >>> artArtist: ')
            artExhibition = input('               >>> artExhibition: ')
            artPrice = input('               >>> artPrice: ')
            #creating insert query from user inputs
            sql = "INSERT INTO art (artTitle, artInfo, artCategory, artArtist, artExhibition, artPrice) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (artTitle, artInfo, artCategory, artArtist, artExhibition, artPrice)
        elif table_number == 2:
            print('            >>>INSERT DATA INTO ARTIST TABLE')
            #getting data from user
            artistFirstName = input('               >>> artistFirstName: ')
            artistLastName = input('               >>> artistLastName: ')
            artistId = input('               >>> artistId: ')
            artistPhone = input('               >>> artistPhone: ')
            artistAge = input('               >>> artistAge: ')
            #creating insert query from user inputs
            sql = "INSERT INTO artist (artistFirstName, artistLastName, artistId, artistPhone, artistAge) VALUES (%s, %s, %s, %s, %s)"
            val = (artistFirstName, artistLastName, artistId, artistPhone, artistAge)
        elif table_number == 3:
            print('            >>>INSERT DATA INTO AUCTION TABLE')
            #getting data from user
            auctionExhibition = input('               >>> auctionExhibition: ')
            auctionDate = input('               >>> auctionDate: ')
            #creating insert query from user inputs
            sql = "INSERT INTO auction (auctionExhibition, auctionDate) VALUES (%s, %s)"
            val = (auctionExhibition, auctionDate)
        elif table_number == 4:
            print('            >>>INSERT DATA INTO BUYER TABLE')
            #getting data from user
            buyerFirstName = input('               >>> buyerFirstName: ')
            buyerLastName = input('               >>> buyerLastName: ')
            buyerPhone = input('               >>> buyerPhone: ')
            #creating insert query from user inputs
            sql = "INSERT INTO buyer (buyerFirstName, buyerLastName, buyerPhone) VALUES (%s, %s, %s)"
            val = (buyerFirstName, buyerLastName, buyerPhone)
        elif table_number == 5:
            print('            >>>INSERT DATA INTO EXHIBITION TABLE')
            #getting data from user
            exhibitionTitle = input('               >>> exhibitionTitle: ')
            exhibitionDateOfStart = input('               >>> exhibitionDateOfStart: ')
            exhibitionDateOfEnd = input('               >>> exhibitionDateOfEnd: ')
            #creating insert query from user inputs
            sql = "INSERT INTO exhibition (exhibitionTitle, exhibitionDateOfStart, exhibitionDateOfEnd) VALUES (%s, %s, %s)"
            val = (exhibitionTitle, exhibitionDateOfStart, exhibitionDateOfEnd)
        elif table_number == 6:
            print('            >>>INSERT DATA INTO FACTOR TABLE')
            #getting data from user
            buyer = input('               >>> buyer: ')
            artist = input('               >>> artist: ')
            exhibition = input('               >>> exhibition: ')
            factorDate = input('               >>> factorDate: ')
            suggestedPrice = input('               >>> suggestedPrice: ')
            #creating insert query from user inputs
            sql = "INSERT INTO factor (buyer, artist, exhibition, factorDate, suggestedPrice) VALUES (%s, %s, %s, %s, %s)"
            val = (buyer, artist, exhibition, factorDate, suggestedPrice)
        #running query
        mycursor.execute(sql, val)
        mydb.commit()
        print('               *** Inserted successfuly!')
    except:
        print('               !!! Try Again')

def insert_to_database():
    print('--------------------------------------------------------')
    print_add_menu()
    command = int(input('         please enter your choice:  '))
    while command != -1:
        #add to art table
        if command == 1:
            insert_to_table(command)
            print_add_menu()
            command = int(input('         please enter your choice:  '))
        #add to artist table
        elif command == 2:         
            insert_to_table(command)
            print_add_menu()
            command = int(input('         please enter your choice:  '))
        #add to auction table
        elif command == 3:
            insert_to_table(command)
            print_add_menu()
            command = int(input('         please enter your choice:  '))
        #add to buyer table
        if command == 4:
            insert_to_table(command)
            print_add_menu()
            command = int(input('         please enter your choice:  '))
        #add to exhibition table
        elif command == 5:
            insert_to_table(command)
            print_add_menu()
            command = int(input('         please enter your choice:  '))
        #add to factor table
        elif command == 6:
            insert_to_table(command)
            print_add_menu()
            command = int(input('         please enter your choice:  '))
        else:
            command = int(input('         please enter a valid number:  '))
    print('--------------------------------------------------------')

#delete functions-----------------------------------------------------------------------------------------------------

def print_delete_menu():
    print('      >>>DELETE DATA FROM TABLES')
    print('         CHOOSE ONE OF YOUR TABLES: ')
    print('         >>>  1 - art')
    print('         >>>  2 - artist')
    print('         >>>  3 - auction')
    print('         >>>  4 - buyer')
    print('         >>>  5 - exhibition')
    print('         >>>  6 - factor')
    print('         >>> -1 - cancel')

def delete_from_table(table_number): # 1: art | 2: artist | 3: auction | 4: buyer | 5: exhibition | 6: factor
    try:
        if table_number == 1:
            print('            >>>DELETE DATA FROM ART TABLE')
            #getting data from user
            print('               >>> please enter the primary key of you row: ')
            artTitle = input('               >>> artTitle: ')
            #creating insert query from user inputs
            sql = "DELETE FROM art WHERE artTitle = %s"
            pk = (artTitle, )

        elif table_number == 2:
            print('            >>>DELETE DATA FROM ARTIST TABLE')
            #getting data from user
            print('               >>> please enter the primary key of you row: ')
            artistId = input('               >>> artistId: ')
            #creating insert query from user inputs
            sql = "DELETE FROM artist WHERE artistId = %s"
            pk = (artistId, )

        elif table_number == 3:
            print('            >>>DELETE DATA FROM AUCTION TABLE')
            #getting data from user
            print('               >>> please enter the primary key of you row: ')
            auctionExhibition = input('               >>> auctionExhibition : ')
            auctionDate = input('               >>> auctionDate : ')
            #creating insert query from user inputs
            sql = "DELETE FROM auction WHERE auctionExhibition = %s AND auctionDate = %s"
            pk = (auctionExhibition, auctionDate, )

        elif table_number == 4:
            print('            >>>DELETE DATA FROM BUYER TABLE')
            #getting data from user
            print('               >>> please enter the primary key of you row: ')
            buyerPhone = input('               >>> buyerPhone : ')
            #creating insert query from user inputs
            sql = "DELETE FROM buyer WHERE auctionExhibition = %s"
            pk = (buyerPhone, )
            
        elif table_number == 5:
            print('            >>>DELETE DATA FROM EXHIBITION TABLE')
            #getting data from user
            print('               >>> please enter the primary key of you row: ')
            exhibitionTitle = input('               >>> exhibitionTitle : ')
            #creating insert query from user inputs
            sql = "DELETE FROM exhibition WHERE auctionExhibition = %s"
            pk = (exhibitionTitle, )

        elif table_number == 6:
            print('            >>>DELETE DATA FROM FACTOR TABLE')
            #getting data from user
            print('               >>> please enter the primary key of you row: ')
            buyer = input('               >>> buyer : ')
            artist  = input('               >>> artist  : ')
            #creating insert query from user inputs
            sql = "DELETE FROM factor WHERE buyer = %s AND artist = %s"
            pk = (buyer, artist, )
            
        #running query
        mycursor.execute(sql, pk)
        mydb.commit()
        print('               *** Deleted successfuly!')
    except:
        print('               !!! Try Again')

def delete_from_database():
    print('--------------------------------------------------------')
    print_delete_menu()
    command = int(input('         please enter your choice:  '))
    while command != -1:
        #add to art table
        if command == 1:
            delete_from_table(command)
            print_delete_menu()
            command = int(input('         please enter your choice:  '))
        #add to artist table
        elif command == 2:         
            delete_from_table(command)
            print_delete_menu()
            command = int(input('         please enter your choice:  '))
        #add to auction table
        elif command == 3:
            delete_from_table(command)
            print_delete_menu()
            command = int(input('         please enter your choice:  '))
        #add to buyer table
        if command == 4:
            delete_from_table(command)
            print_delete_menu()
            command = int(input('         please enter your choice:  '))
        #add to exhibition table
        elif command == 5:
            delete_from_table(command)
            print_delete_menu()
            command = int(input('         please enter your choice:  '))
        #add to factor table
        elif command == 6:
            delete_from_table(command)
            print_delete_menu()
            command = int(input('         please enter your choice:  '))
        else:
            command = int(input('         please enter a valid number:  '))
    print('--------------------------------------------------------')

#showing functions----------------------------------------------------------------------------------------------------

def print_select_menu():
    print('      >>>SHOWING DATAS IN TABLES')
    print('         CHOOSE ONE OF YOUR TABLES: ')
    print('         >>>  1 - art')
    print('         >>>  2 - artist')
    print('         >>>  3 - auction')
    print('         >>>  4 - buyer')
    print('         >>>  5 - exhibition')
    print('         >>>  6 - factor')
    print('         >>> -1 - cancel')

def select_from_table(table_number): # 1: art | 2: artist | 3: auction | 4: buyer | 5: exhibition | 6: factor
    try:
        if table_number == 1:
            print('            >>>SELECT DATA FROM ART TABLE')
            mycursor.execute("SELECT * FROM art")

        elif table_number == 2:
            print('            >>>SELECT DATA FROM ARTIST TABLE')
            mycursor.execute("SELECT * FROM artist")

        elif table_number == 3:
            print('            >>>SELECT DATA FROM AUCTION TABLE')
            mycursor.execute("SELECT * FROM auction")

        elif table_number == 4:
            print('            >>>SELECT DATA FROM BUYER TABLE')
            mycursor.execute("SELECT * FROM buyer")
            
        elif table_number == 5:
            print('            >>>SELECT DATA FROM EXHIBITION TABLE')
            mycursor.execute("SELECT * FROM exhibition")

        elif table_number == 6:
            print('            >>>SELECT DATA FROM FACTOR TABLE')
            mycursor.execute("SELECT * FROM factor")
            
        myresult = mycursor.fetchall()
        # print(myresult[0][0])
        show_table_rows(table_number, myresult)
        print('               *** Selected successfuly!')
    except:
        print('               !!! Try Again')

def select_from_database():
    print('--------------------------------------------------------')
    print_select_menu()
    command = int(input('         please enter your choice:  '))
    while command != -1:
        #add to art table
        if command == 1:
            select_from_table(command)
            print_select_menu()
            command = int(input('         please enter your choice:  '))
        #add to artist table
        elif command == 2:         
            select_from_table(command)
            print_select_menu()
            command = int(input('         please enter your choice:  '))
        #add to auction table
        elif command == 3:
            select_from_table(command)
            print_select_menu()
            command = int(input('         please enter your choice:  '))
        #add to buyer table
        if command == 4:
            select_from_table(command)
            print_select_menu()
            command = int(input('         please enter your choice:  '))
        #add to exhibition table
        elif command == 5:
            select_from_table(command)
            print_select_menu()
            command = int(input('         please enter your choice:  '))
        #add to factor table
        elif command == 6:
            select_from_table(command)
            print_select_menu()
            command = int(input('         please enter your choice:  '))
        else:
            command = int(input('         please enter a valid number:  '))
    print('--------------------------------------------------------')

def show_table_rows(table_number, myresult):# 1: art | 2: artist | 3: auction | 4: buyer | 5: exhibition | 6: factor
    try:
        if table_number == 1:
            print('\t\tartTitle\tartInfo\tartCategory\tartArtist\tartExhibition\tartPrice')
            
        elif table_number == 2:
            print('\t\tartistFirstName\tartistLastName\tartistId\tartistPhone\tartistAge')

        elif table_number == 3:
            print('\t\tauctionExhibition\tauctionDate')

        elif table_number == 4:
            print('\t\tbuyerFirstName\tbuyerLastName\tbuyerPhone')
            
        elif table_number == 5:
            print('\t\texhibitionTitle\texhibitionDateOfStart\texhibitionDateOfEnd')
        elif table_number == 6:
            print('\t\tbuyer\tartist\texhibition\tfactorDate\tsuggestedPrice')
            
        print('\t\t----------------------------------------------------------------------------------------------------------------')
        for row in myresult:
                print('\t\t', end='')
                for col in row:
                    print(col,'\t',end='')
                print()
    except:
        print('               !!! Try Again')

#add price------------------------------------------------------------------------------------------------------------

def add_price():
    try:
        print('      >>>ADD PRICE')
        artTitle = (input('         please enter an artTitle:  '))
        artNewPrice = (input('         please enter a price:  '))
        sql = "SELECT artPrice FROM art WHERE artTitle = \'" + artTitle + "\'"
        mycursor.execute(sql)
        myresult = mycursor.fetchone()
        if int(myresult[0]) <= int(artNewPrice) : #can update
            sql = "UPDATE art SET artPrice = \'" + artNewPrice + "\' WHERE artTitle = \'" + artTitle +"\'"
            mycursor.execute(sql)
            mydb.commit()
            print('      *** Updated Successfully!')
        else:
            print('      !!! New Price is Less than the Old Price')
    except:
        print('      !!! Try Again')
    print('--------------------------------------------------------')

#---------------------------------------------------------------------------------------------------------------------

def executeScriptsFromFile(filename):
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')
    for command in sqlCommands:
        try:
            mycursor.execute(command)
        except:
            print ('',end='')

def start():
    print('*******************************************************')
    print('*********************** DATABASE **********************')
    print('******************** FINAL  PROJECT *******************')
    print('**************** Amirhossein Alibakhshi ***************')
    print('********************** id:9731096 *********************')
    print('*******************************************************\n')
    #creating tables from create.sql file (if needed)
    executeScriptsFromFile('create.sql')
    executeScriptsFromFile('tables.sql')
    #start
    print('>>> Hi! How do you want to work with this ')
    print('    program?')
    print('   >>>  1 - insert data')
    print('   >>>  2 - delete data')
    print('   >>>  3 - show data')
    print('   >>>  4 - add price')
    print('   >>> -1 - exit the program')
    command = int(input('   please enter your choice:  '))
    while command != -1:
        if command == 1:
            insert_to_database()
            print_main_menu()
            command = int(input('   please enter your choice:  '))
        elif command == 2:
            delete_from_database()
            print_main_menu()
            command = int(input('   please enter your choice:  '))
        elif command == 3:
            select_from_database()
            print_main_menu()
            command = int(input('   please enter your choice:  '))
        elif command == 4:
            add_price()
            print_main_menu()
            command = int(input('   please enter your choice:  '))
        else:
            command = int(input('   please enter a valid number:  '))
    print('--------------------------------------------------------')
    print('bye:)')

start()
