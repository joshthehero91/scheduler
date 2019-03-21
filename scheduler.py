#!/usr/bin/python3
# Written by joshthehero91
import sys
admins = {}

def mainMenu():
    choice = input("""
           ___________________________________________________________
           | Please select an option:                                |
           |---------------------------------------------------------|
           | add - Add a new admin to scheduler                      |
           | del - Remove an existing admin form the scheduler       |
           | mod - Modify and existing admins schedule or roles      |
           | see - Show all admins, their schedules, and their roles |
           | run - Generate a new schedule based off current admins  |
           |---------------------------------------------------------|
           | Type 'quit' to exit the scheduler.                      |
           |_________________________________________________________|
             
             Select option: """)

    if choice == 'add':
        addAdmin()
    elif choice == 'del':
        deleteAdmin()
    elif choice == 'mod':
        modifyAdmin()
    elif choice == 'see':
        listAdmin()
    elif choice == 'run':
        runScheduler()
    elif choice == 'quit':
        sys.exit()
    else:
        print('The option selected is not avaible. Please try again.')
        mainMenu()

def addAdmin():
    print('')
    adminName = input('Please provide the name of the admin being added: ')
    adminSchedule = input("""
                                """ + adminName + """ will need to have their schedule updated.
                                The days are represented as the following:

                                ___________________________________________
                                | Sun | Mon | Tue | Wed | Thu | Fri | Sat |
                                |-----|-----|-----|-----|-----|-----|-----|
                                | '1' | '2' | '3' | '4' | '5' | '6' | '7' |
                                |_____|_____|_____|_____|_____|_____|_____| 

                                For example, Mon-Fri would be represtend by '23456'. 

Please provide the admins schedule: """)
    adminRoles = input("""
                                """ + adminName + """ will now need their roles defined.
                                The roles are represented as the following:

                                _______________________________________________
                                | New | Ongoing | Handoffs | Chatter | Shadow |
                                |-----|---------|----------|---------|--------|
                                | 'n' |   'o'   |   'h'    |   'c'   |   's'  |
                                |_____|_________|__________|_________|________| 

                                For example, andmin who should be on Shadow, Chatter, and New would be represtend by 'scn'. 

Please provide the admins roles: """)
     
    admins[adminName] = {'shift' : adminSchedule, 'roles': adminRoles}
    mainMenu()

def deleteAdmin():
    print('')
    adminName = input('Please provide the name of the admin being removed or \'back\' to return to the main menu: ')
    if adminName == 'back':
        mainMenu()
    elif adminName not in admins:
        print('Admin is not listed as an avaible admin. Please try again.')
        mainMenu()
    else:
        confirm = input('Are you sure you would like to remove ' + adminName + ' from the scheduler? (Y/n): ')
        if confirm == 'Y':
            print('Removing ' + adminName + ' from scheduler...')
            admins.pop(adminName)
            mainMenu()
        elif confirm == 'y':
            print('Please confirm by using \'Y\'.')
            deleteAdmin()
        elif confirm == 'N' or 'n':
            mainMenu()
        else:
            print('Not a valid choice. Please try again')
            mainMenu()

def listAdmin():
    print('')
    print('{:<8} {:<15} {:<10}'.format('Name','Shift','Roles'))
    for k, v in admins.items():
        shift = v['shift']
        roles = v['roles']
        print('{:<8} {:<15} {:<10}'.format(k, shift, roles))
    print('')
    mainMenu()

mainMenu()
