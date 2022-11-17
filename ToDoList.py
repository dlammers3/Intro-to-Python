# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# DLammers, 11.17.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# If there is no previously saved data, the program will indicate such rather than exiting immediately
try:
    oldData = open(objFile,'r')
    for row in oldData:
        lstRow = row.split(',')
        dicRow = {'Task':lstRow[0], 'Priority':lstRow[1].strip()}
        lstTable.append(dicRow)
    oldData.close()
except:
    print('It appears that there is no saved data in your To-Do list')

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for row in lstTable:
            print(row)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        newTask = input('Enter a new task: ')
        newPriority = input('Enter the priority: ')
        dicRow = {'Task':newTask , 'Priority':newPriority}
        lstTable.append(dicRow)
        print(newTask + ' has been added with '+ newPriority + ' priority!')
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        removeTask = input('Enter a task to remove: ')
        for row in lstTable:
            if row['Task'].lower() == removeTask.lower():
                lstTable.remove(row)
                print(removeTask + ' has been removed!\n')
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        newData = open(objFile, 'w')
        for row in lstTable:
            newData.write(row['Task'] + ',' + row['Priority'] + '\n')
            continue
        print('Your To-Do list has been saved!')
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('You have selected to exit the program. Your To-Do list changes will now be saved automatically.')
        newData = open(objFile, 'w')
        for row in lstTable:
            newData.write(row['Task'] + ',' + row['Priority'] + '\n')
        break  # Exit the program
