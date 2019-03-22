#!/usr/bin/python3
# Written by joshthehero91

# Importing modules:
import os
import sys
import json

# Creating empty dictionary:
admins = {}
week = {
        'sun': {},
        'mon': {},
        'tue': {},
        'wed': {},
        'thu': {},
        'fri': {},
        'sat': {},
       }


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

# The magic!
admins = readList()
listAdmin()

def addKeys():
    for days in week.keys():
        keys = {'new' : set([]), 'ongo' : set([]), 'hand' : set([]), 'chat' : set([]) , 'shad' : set([])}
        week[days]=keys

addKeys()
setRoles = ['n', 'o', 'h', 'c', 's']
setShift = ['1', '2', '3', '4', '5', '6', '7']

#for days in week.keys():
#    keys = {'new' : set([]), 'ongo' : set([]), 'hand' : set([]), 'chat' : set([]) , 'shad' : set([])}
#    week[days]=keys

def addList(adminName, days, key):
    weekdays = week[days][key]
    add =  weekdays.add(adminName)
    if 'n' in roles:
        add
    if 'o' in roles:
        add
    if 'h' in roles:
        add
    if 'c' in roles:
        add
    if 's' in roles:
        add

def setShift(shift, roles, adminName):
    for days, v in week.items():
        for key, v in week[days].items():
            weekdays = week[days][key]
            addAdmin = addList(adminName, days, key)
            if '1' in shift:
                addAdmin
            if '2' in shift:
                addAdmin
            if '3' in shift:
                addAdmin
            if '4' in shift:
                addAdmin
            if '5' in shift:
                addAdmin
            if '6' in shift:
                addAdmin
            if '7' in shift:
                addAdmin

for k, v in admins.items():
    adminName = k
    shift = v['shift']
    roles = v['roles']
    setShift(shift, roles, adminName)


print('')
print('----------------------')
print('Sun')
print(week['sun'])
print('')
print('Mon')
print(week['mon'])
print('')
print('Tue')
print(week['tue'])
print('')
print('Wed')
print(week['wed'])
print('')
print('Thu')
print(week['thu'])
print('')
print('Fri')
print(week['fri'])
print('')
print('Sat')
print(week['sat'])
print('')
