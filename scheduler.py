#!/usr/bin/python3
# Written by joshthehero91

# Importing modules:
import os
import sys
import json

# Creating empty dictionary:
admins = {}

# Function to onfirming the existence of 'admins.json' which stores the admin 
# data for persistent list:
def readList():
    if os.path.isfile('admins.json') == True:
        with open('admins.json', 'r') as f:
            admins = json.load(f)
            return admins

# Function to save the list to 'admins.json':
def saveList():
    with open('admins.json', 'w') as f:
        json.dump(admins, f, sort_keys=True, indent=4)

# Function to get admin schedule:
def getSchedule(adminName):
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
    return adminSchedule

# Function to get admin roles:
def getRoles(adminName):
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
    return adminRoles

# Main menu and display:
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

# Function to add new admins to scheduler:
def addAdmin():
    print('')
    adminName = input('Please provide the name of the admin being added: ')
    adminSchedule = getSchedule(adminName)
    adminRoles = getRoles(adminName)
    
    # Adds the new user to the 'admins' dictionary
    admins[adminName] = {'shift' : adminSchedule, 'roles': adminRoles}
    saveList()
    mainMenu()

# Function to remove admin from scheduler with validation:
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
            saveList()
            mainMenu()
        elif confirm == 'y':
            print('Please confirm by using \'Y\'.')
            deleteAdmin()
        elif confirm == 'N' or 'n':
            mainMenu()
        else:
            print('Not a valid choice. Please try again')
            mainMenu()

# Function to modify existing admins with validation:
def modifyAdmin():
    adminName = input('Please provide the name of the admin being modifies or \'back\' to return to the main menu: ')
    if adminName == 'back':
        mainMenu()
    elif adminName not in admins:
        print('Admin is not listed as an avaible admin. Please try again.')
        mainMenu()
    else:
        confirm = input('Are you sure you would like to modify ' + adminName + ' shift and roles? (Y/n): ')
        if confirm == 'Y':
            adminSchedule = getSchedule(adminName)
            adminRoles = getRoles(adminName)
            
            # Updates the 'admins' dictinoary with new values
            admins[adminName] = {'shift' : adminSchedule, 'roles': adminRoles}
            print('Updating ' + str(adminName) + '\'s schedule to ' + str(adminSchedule) + ' and roles to ' + str(adminRoles) + '...')
            saveList()
            mainMenu()
        elif confirm == 'y':
            print('Please confirm by using \'Y\'.')
            modifyAdmin()
        elif confirm == 'N' or 'n':
            mainMenu()
        else:
            print('Not a valid choice. Please try again')
            mainMenu()

# Function to display all admins in scheduler in a table format:
def listAdmin():

    # Rereading the file for data validation:
    admins = readList()
    print('')
    line ='{:<16} {:<30} {:<20}'.format('Name','Shift','Roles')
    print(line)
    print('_' * len(line))
    for k, v in admins.items():
        shift = v['shift']
        roles = v['roles']
        print('{:<16} {:<30} {:<20}'.format(k, shift, roles))
    print('')
    mainMenu()

# The magic!
admins = readList()
mainMenu()
